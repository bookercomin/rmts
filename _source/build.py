import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
PARTIALS = os.path.join(ROOT, '_partials')
PAGES = os.path.join(ROOT, '_pages')

with open(os.path.join(PARTIALS, 'header.html'), encoding='utf-8') as f:
    HEADER = f.read()
with open(os.path.join(PARTIALS, 'footer.html'), encoding='utf-8') as f:
    FOOTER = f.read()

SITE_URL = "https://www.rocciamarketing.com"

PAGE_META = {
  "index": {
    "title": "Roccia Marketing | Make Your Brand Impossible to Ignore",
    "description": "Roccia Marketing is a digital marketing agency delivering agency-quality social media, paid ads, SEO and brand strategy at a fraction of typical agency cost. Book a free discovery call.",
    "og_image": "images/og-home.jpg",
  },
  "services": {
    "title": "Services & Pricing | Roccia Marketing",
    "description": "Social media management, paid advertising, SEO and marketing coaching — transparent pricing, no bloated retainers. See Roccia Marketing's full service menu.",
    "og_image": "images/og-services.jpg",
  },
  "about": {
    "title": "About Us | Roccia Marketing",
    "description": "Roccia means rock in Italian — built to be the solid, reliable base your brand grows from. Learn the story behind Roccia Marketing.",
    "og_image": "images/og-about.jpg",
  },
  "track-record": {
    "title": "Track Record | Who We Work With | Roccia Marketing",
    "description": "See the industries, businesses and results Roccia Marketing has delivered for. Real work, real growth, real proof.",
    "og_image": "images/og-track-record.jpg",
  },
  "team": {
    "title": "Meet the Team | Roccia Marketing",
    "description": "Meet the founders and team behind Roccia Marketing — the people building your brand's strategy, content and growth.",
    "og_image": "images/og-team.jpg",
  },
  "blog": {
    "title": "Blog | Marketing Insights from Roccia Marketing",
    "description": "Practical marketing insights, growth tactics and behind-the-scenes strategy from the Roccia Marketing team.",
    "og_image": "images/og-blog.jpg",
  },
  "contact": {
    "title": "Contact Us | Roccia Marketing",
    "description": "Get in touch with Roccia Marketing or book a free 30-minute discovery call to talk through your brand's growth.",
    "og_image": "images/og-contact.jpg",
  },
  "blog-post-more-is-bad-advice": {
    "title": "Why \u201cPost More\u201d Is Bad Advice | Roccia Marketing Blog",
    "description": "Posting more without a strategy just buries your best content. Here's what to fix before you increase volume.",
    "og_image": "images/og-blog.jpg",
  },
  "blog-cost-of-cheap-ad-manager": {
    "title": "The Real Cost of a \u201cCheap\u201d Ad Manager | Roccia Marketing Blog",
    "description": "A low management fee can hide a much bigger cost in wasted ad spend. Here's what to check before you hire.",
    "og_image": "images/og-blog.jpg",
  },
  "blog-seo-foundation-not-sprint": {
    "title": "SEO Is a Foundation, Not a Sprint | Roccia Marketing Blog",
    "description": "Why bedrock SEO work compounds long after a campaign ends, and how to think about SEO timelines.",
    "og_image": "images/og-blog.jpg",
  },
}

HEAD_TMPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Roccia Marketing">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site_url}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{site_url}/{og_image}">

<link rel="icon" href="images/favicon-32.png" sizes="32x32">
<link rel="icon" href="images/favicon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="images/favicon-180.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Work+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="css/style.css">
{schema}
</head>
<body>
"""

def load_page(slug):
    with open(os.path.join(PAGES, slug + '.html'), encoding='utf-8') as f:
        return f.read()

def load_schema(slug):
    path = os.path.join(PAGES, slug + '.schema.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            data = f.read().strip()
        return f'<script type="application/ld+json">\n{data}\n</script>'
    return ""

def build():
    for slug, meta in PAGE_META.items():
        content = load_page(slug)
        canonical = f"{SITE_URL}/{slug}.html"
        schema = load_schema(slug)
        head = HEAD_TMPL.format(
            title=meta['title'],
            description=meta['description'],
            canonical=canonical,
            site_url=SITE_URL,
            og_image=meta['og_image'],
            schema=schema,
        )
        html = head + HEADER + "\n<main id=\"main\">\n" + content + "\n</main>\n" + FOOTER + "\n</body>\n</html>\n"
        out_path = os.path.join(ROOT, slug + '.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("built", out_path)

if __name__ == '__main__':
    build()
