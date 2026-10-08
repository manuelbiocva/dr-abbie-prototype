<?php
/**
 * Plugin Name: Dr. Abbie Clinics - blog
 * Description: Renders the blog in the approved design. [dr_post_body] prints a post's own content inside the article styles, so posts stay editable in WordPress. [dr_blog_grid] lists published posts as cards, so the hub stays current as posts are added instead of being a fixed list.
 * Version: 1.0.0
 */

if (!defined('ABSPATH')) { exit; }

/**
 * The post's body, straight from the editor.
 */
function dra_post_body_shortcode($atts = array()) {
    $id = get_the_ID();
    if (!$id) { return ''; }
    $post = get_post($id);
    if (!$post) { return ''; }
    $content = apply_filters('the_content', $post->post_content);
    return str_replace(']]>', ']]&gt;', $content);
}
add_shortcode('dr_post_body', 'dra_post_body_shortcode');

/**
 * One post card, in the same shape the design uses everywhere else.
 */
function dra_blog_card($post) {
    $id    = $post->ID;
    $cats  = get_the_category($id);
    $cat   = $cats ? $cats[0]->name : '';
    // the inherited posts were never categorised; "Uncategorized" is not a
    // label worth showing a patient
    if ($cat === '' || strtolower($cat) === 'uncategorized' || strtolower($cat) === 'uncategorised') {
        $cat = 'Articles';
    }
    $thumb = get_post_thumbnail_id($id);

    // every card carries a picture, so a row of cards lines up. Posts without
    // a featured image get the brand's hexagon texture rather than a gap.
    if ($thumb) {
        $src = wp_get_attachment_image_url($thumb, 'large');
        $alt = get_post_meta($thumb, '_wp_attachment_image_alt', true);
        $img = '<div class="post-card__img"><img src="' . esc_url($src) . '" alt="' . esc_attr($alt) . '" loading="lazy" decoding="async"></div>';
    } else {
        $img = '<div class="post-card__img post-card__img--placeholder" aria-hidden="true"></div>';
    }

    $excerpt = has_excerpt($id)
        ? get_the_excerpt($id)
        : wp_trim_words(wp_strip_all_tags(strip_shortcodes($post->post_content)), 20, '');
    $excerpt = wp_trim_words($excerpt, 20, '');

    $arrow = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
           . '<path d="M3 7h8M7.5 3.5L11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.7" '
           . 'stroke-linecap="round" stroke-linejoin="round"/></svg>';

    $out  = '<a class="card post-card reveal" href="' . esc_url(get_permalink($id)) . '">';
    $out .= $img;
    $out .= '<div class="post-card__body">';
    if ($cat !== '') { $out .= '<span class="post-card__cat">' . esc_html($cat) . '</span>'; }
    $out .= '<h3>' . esc_html(get_the_title($id)) . '</h3>';
    if ($excerpt !== '') { $out .= '<p>' . esc_html($excerpt) . '</p>'; }
    $out .= '<span class="card__more">Read article ' . $arrow . '</span>';
    $out .= '</div></a>';
    return $out;
}

/**
 * Every published post as a grid of cards.
 *
 * exclude  comma separated post IDs to leave out (the featured one)
 * limit    how many to show, -1 for all
 */
function dra_blog_grid_shortcode($atts = array()) {
    $atts = shortcode_atts(array('exclude' => '', 'per_page' => 8), $atts, 'dr_blog_grid');
    $per  = (int) $atts['per_page'];
    $page = isset($_GET['bp']) ? max(1, (int) $_GET['bp']) : 1;

    $args = array(
        'post_type'           => 'post',
        'post_status'         => 'publish',
        'posts_per_page'      => $per > 0 ? $per : -1,
        'paged'               => $page,
        'orderby'             => 'date',
        'order'               => 'DESC',
        'ignore_sticky_posts' => true,
    );
    if ($atts['exclude'] !== '') {
        $args['post__not_in'] = array_filter(array_map('intval', explode(',', $atts['exclude'])));
    }
    $query = new WP_Query($args);
    if (!$query->have_posts()) { return ''; }

    $out = '';
    foreach ($query->posts as $p) { $out .= dra_blog_card($p); }
    $out .= dra_blog_pager($page, (int) $query->max_num_pages);
    wp_reset_postdata();
    return $out;
}

/**
 * Page links under the grid. The hub is a static page, so the page number
 * travels in its own query argument rather than WordPress's /page/2/.
 */
function dra_blog_pager($current, $total) {
    if ($total < 2) { return ''; }
    $base = strtok($_SERVER['REQUEST_URI'], '?');
    $link = function ($n) use ($base) {
        return esc_url($n <= 1 ? $base : add_query_arg('bp', $n, $base));
    };

    $out = '<nav class="blog-pager" aria-label="Blog pages">';
    if ($current > 1) {
        $out .= '<a class="blog-pager__step" href="' . $link($current - 1) . '" rel="prev">Previous</a>';
    }
    $out .= '<span class="blog-pager__pages">';
    for ($n = 1; $n <= $total; $n++) {
        if ($n === $current) {
            $out .= '<span class="blog-pager__page is-current" aria-current="page">' . $n . '</span>';
        } else {
            $out .= '<a class="blog-pager__page" href="' . $link($n) . '">' . $n . '</a>';
        }
    }
    $out .= '</span>';
    if ($current < $total) {
        $out .= '<a class="blog-pager__step" href="' . $link($current + 1) . '" rel="next">Next</a>';
    }
    $out .= '</nav>';
    return $out;
}

add_shortcode('dr_blog_grid', 'dra_blog_grid_shortcode');

/**
 * The newest post, for the featured slot at the top of the hub.
 */
function dra_blog_latest_id() {
    $latest = get_posts(array('post_type' => 'post', 'post_status' => 'publish', 'posts_per_page' => 1));
    return $latest ? $latest[0]->ID : 0;
}
