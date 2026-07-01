# Roccia Marketing — Website Source

This folder contains the *editable* source for the site. The finished HTML files
one level up (in the main folder) are what you actually upload/host — you only
need this folder if you want to change content later.

## How it works
- `_partials/header.html` and `_partials/footer.html` — the nav and footer that
  appear on every page. Edit once here instead of in 10 different files.
- `_pages/*.html` — the actual content for each page (just the middle part,
  no `<head>`, no nav, no footer).
- `build.py` — stitches `_partials` + `_pages` together into the final,
  complete HTML files (adds `<head>`, meta tags, SEO schema, etc).

## To make a content change
1. Edit the relevant file in `_pages/` (or `_partials/` for nav/footer changes).
2. Run: `python3 build.py`
3. This regenerates all the `.html` files in the parent folder — copy those
   into your hosting (GitHub Pages, Netlify, etc).

Titles, meta descriptions, and social-share images for each page are set in
`build.py` under `PAGE_META` — update them there if you rename a page or want
different SEO copy.

## Things you'll want to swap in before launch
- **Contact form**: currently shows a "message received" confirmation but
  doesn't actually send anywhere. Wire it up to Formspree, a Google Form, or
  your own backend (see `js/main.js`, the `contactForm` handler).
- **Email address**: `hello@rocciamarketing.com` is a placeholder — replace
  with your real inbox everywhere it appears.
- **Team photos**: the team page currently uses initials on a brand-colored
  card instead of real headshots. Swap in real photos when you have them.
- **Testimonials**: the Track Record page has 3 placeholder testimonial
  cards — replace with real client quotes as soon as you have them.
- **Blog**: 3 starter posts are live. Add more by copying one of the
  `blog-*.html` files in `_pages/`, then registering it in `PAGE_META` in
  `build.py` so it gets a proper `<head>` and shows up if you rebuild.
- **Sitemap**: `sitemap.xml` has today's date hardcoded — regenerate or
  update `lastmod` values when you publish real changes.
