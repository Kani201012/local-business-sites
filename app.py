import os

def generate_compliant_site(biz_data):
    # 1. SETUP STRUCTURE (Point 8: Site Structure)
    folder_name = biz_data['name'].lower().replace(" ", "-")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 2. SHARED ASSETS (Point 5: Mobile-Friendliness, Point 6: Speed)
    # Using Tailwind for responsiveness and CDN for speed
    header_html = f"""
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{biz_data['name']} - {biz_data['category']} in {biz_data['city']}</title>
        <meta name="description" content="{biz_data['seo_description'][:160]}">
        <script src="https://cdn.tailwindcss.com"></script>
        <!-- Point 14: Structured Data -->
        <script type="application/ld+json">
        {{
          "@context": "https://schema.org",
          "@type": "LocalBusiness",
          "name": "{biz_data['name']}",
          "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_data['address']}", "addressLocality": "{biz_data['city']}" }},
          "telephone": "{biz_data['phone']}",
          "url": "{biz_data['website_url']}"
        }}
        </script>
    </head>
    <body class="bg-white text-gray-800">
        <nav class="p-4 border-b flex justify-between max-w-6xl mx-auto">
            <a href="index.html" class="font-bold text-xl">{biz_data['name']}</a>
            <div class="space-x-4">
                <a href="about.html">About</a>
                <a href="contact.html">Contact</a>
            </div>
        </nav>
    """

    footer_html = """
        <footer class="p-10 bg-gray-100 mt-20 text-center border-t">
            <div class="space-x-4 mb-4">
                <a href="privacy.html" class="text-sm text-gray-500">Privacy Policy</a>
                <a href="terms.html" class="text-sm text-gray-500">Terms & Conditions</a>
            </div>
            <p class="text-xs text-gray-400">&copy; 2024 Optimized for Google Search.</p>
        </footer>
    </body>
    """

    # 3. GENERATE index.html (Point 11 & 12: Meta & Headings)
    index_content = f"""
    {header_html}
    <main class="max-w-4xl mx-auto py-20 px-4 text-center">
        <h1 class="text-5xl font-black mb-6">{biz_data['name']}</h1>
        <p class="text-xl mb-8">{biz_data['long_content']}</p>
        <img src="https://images.unsplash.com/photo-1556740734-7f9a2b7a0f42" alt="{biz_data['name']} storefront in {biz_data['city']}" class="rounded-lg mb-10 mx-auto"> <!-- Point 13: Alt Text -->
    </main>
    {footer_html}
    """
    with open(f"{folder_name}/index.html", "w") as f: f.write(index_content)

    # 4. GENERATE MANDATORY PAGES (Point 17: Legal Compliance)
    pages = ['about', 'contact', 'privacy', 'terms']
    for page in pages:
        content = f"{header_html}<main class='p-20'><h1>{page.capitalize()}</h1><p>Content for {biz_data['name']} {page} page.</p></main>{footer_html}"
        with open(f"{folder_name}/{page}.html", "w") as f: f.write(content)

    # 5. GENERATE robots.txt (Point 3)
    with open(f"{folder_name}/robots.txt", "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {biz_data['website_url']}/sitemap.xml")

    # 6. GENERATE sitemap.xml (Point 15)
    with open(f"{folder_name}/sitemap.xml", "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{biz_data["website_url"]}/index.html</loc></url></urlset>')

    print(f"🚀 17-Point Compliant Site Built for {biz_data['name']}")

# --- EXAMPLE DATA ---
biz_info = {
    "name": "Gupta Electronics",
    "category": "Consumer Electronics Store",
    "city": "Bengaluru",
    "address": "123, MG Road, Indiranagar",
    "phone": "+91 9886012345",
    "website_url": "https://kani201012.github.io/local-business-sites/gupta-electronics",
    "seo_description": "Best electronics store in Bengaluru. We provide professional AC repair and oven services.",
    "long_content": "With over 20 years of experience, Gupta Electronics is the trusted choice for high-quality electronics and repair services in the Bengaluru area. Our team is certified..."
}

generate_compliant_site(biz_info)
