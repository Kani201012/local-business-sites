import streamlit as st
import zipfile
import io
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Enterprise Google Site Factory", layout="wide")

# --- CSS FOR PROFESSIONAL UI ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4285F4; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏗️ 17-Point Google Compliant Website Factory")
st.write("Generate a '1st Class' professional business site that meets all Google search requirements.")

# --- STEP 1: DATA COLLECTION (The 17 Points) ---
with st.form("business_info"):
    st.header("📋 Mandatory Business Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        biz_name = st.text_input("Business Name (Exact match to Google Maps)", "Gupta Electronics")
        biz_phone = st.text_input("Phone Number (with +91)", "+91 98765 43210")
        biz_email = st.text_input("Business Email", "contact@guptaelectronics.com")
        biz_city = st.text_input("City/Locality", "Indiranagar, Bengaluru")
        biz_hours = st.text_input("Opening Hours", "Mon-Sat: 10:00 AM - 08:30 PM")
        website_url = st.text_input("Final Website URL (Your GitHub Link)", "https://username.github.io/repo-name/")
    
    with col2:
        biz_category = st.text_input("Business Category", "Consumer Electronics Store")
        biz_address = st.text_area("Full Physical Address", "Shop No. 42, 10th Main Rd, Indiranagar, Bengaluru, KA 560038")
        seo_desc = st.text_area("SEO Meta Description (Max 160 chars)", "Best electronics store in Indiranagar. Authorized dealer for Sony, Samsung, and LG. Quality service and genuine parts.")
        biz_services = st.text_area("List of Services (One per line)", "AC Repair\nOven Service\nLaptop Repair\nHome Delivery")

    long_about = st.text_area("Detailed About Us (E-E-A-T Content - Min 500 words recommended)", 
                              "Gupta Electronics has been a pillar of the Bengaluru community for over 20 years. Our expertise in consumer electronics is unmatched...")

    submitted = st.form_submit_button("🚀 GENERATE COMPLIANT WEBSITE PACKAGE")

# --- STEP 2: THE WEBSITE ENGINE ---
if submitted:
    # --- SHARED COMPONENTS (Tailwind, Schema, Navbar) ---
    def get_header(title, desc):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {biz_name}</title>
    <meta name="description" content="{desc}">
    <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "description": "{seo_desc}",
      "url": "{website_url}",
      "telephone": "{biz_phone}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_address}", "addressLocality": "{biz_city}", "addressCountry": "IN" }},
      "openingHours": "{biz_hours}"
    }}
    </script>
    <style> body {{ font-family: 'Inter', sans-serif; }} </style>
</head>
<body class="bg-gray-50 text-gray-900">
    <nav class="bg-white border-b sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="index.html" class="text-2xl font-bold text-blue-600">{biz_name}</a>
            <div class="hidden md:flex space-x-6 font-medium">
                <a href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="contact.html">Contact</a>
            </div>
            <a href="tel:{biz_phone}" class="bg-blue-600 text-white px-5 py-2 rounded-full text-sm">Call Now</a>
        </div>
    </nav>"""

    footer = f"""
    <footer class="bg-gray-900 text-white py-12 px-4 mt-20">
        <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
            <div><h3 class="font-bold mb-4">{biz_name}</h3><p class="text-gray-400 text-sm">{biz_address}</p></div>
            <div><h3 class="font-bold mb-4">Quick Links</h3>
                <ul class="text-gray-400 text-sm space-y-2">
                    <li><a href="privacy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms & Conditions</a></li>
                </ul>
            </div>
            <div><h3 class="font-bold mb-4">Hours</h3><p class="text-gray-400 text-sm">{biz_hours}</p></div>
        </div>
        <div class="text-center mt-10 pt-8 border-t border-gray-800 text-gray-500 text-xs">
            &copy; {datetime.now().year} {biz_name}. Google Compliant & Mobile Optimized.
        </div>
    </footer>
</body></html>"""

    # 1. INDEX PAGE
    index_html = get_header(biz_category, seo_desc) + f"""
    <header class="py-20 bg-white border-b">
        <div class="max-w-4xl mx-auto text-center px-4">
            <h1 class="text-5xl font-extrabold mb-6 leading-tight">{biz_name}</h1>
            <p class="text-xl text-gray-600 mb-8">{seo_desc}</p>
            <div class="flex justify-center gap-4">
                <a href="tel:{biz_phone}" class="bg-blue-600 text-white px-8 py-4 rounded-lg font-bold shadow-lg">Call Operator</a>
                <a href="https://wa.me/{biz_phone.replace(' ', '')}" class="bg-green-500 text-white px-8 py-4 rounded-lg font-bold shadow-lg">WhatsApp Us</a>
            </div>
        </div>
    </header>
    <section class="py-16 max-w-6xl mx-auto px-4">
        <h2 class="text-3xl font-bold mb-10 text-center">Our Specialized Services</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {"".join([f'<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:border-blue-500 transition"><h3 class="font-bold mb-2">{s}</h3><p class="text-gray-500 text-sm">Expert {s} solutions in {biz_city}.</p></div>' for s in biz_services.splitlines()])}
        </div>
    </section>""" + footer

    # 2. ABOUT PAGE
    about_html = get_header("About Us", f"Learn more about {biz_name}") + f"""
    <main class="max-w-3xl mx-auto py-20 px-4">
        <h1 class="text-4xl font-bold mb-8">About {biz_name}</h1>
        <div class="prose prose-lg text-gray-700 leading-relaxed">
            {long_about.replace('\\n', '<br>')}
        </div>
    </main>""" + footer

    # 3. LEGAL PAGES
    privacy_html = get_header("Privacy Policy", "Legal") + f"<main class='p-20'><h1>Privacy Policy</h1><p>We value your privacy at {biz_name}...</p></main>" + footer
    terms_html = get_header("Terms & Conditions", "Legal") + f"<main class='p-20'><h1>Terms & Conditions</h1><p>By using this site, you agree to...</p></main>" + footer

    # 4. TECHNICAL FILES
    robots_txt = f"User-agent: *\nAllow: /\nSitemap: {website_url}sitemap.xml"
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>{website_url}index.html</loc></url>
    <url><loc>{website_url}about.html</loc></url>
</urlset>"""

    # --- STEP 3: ZIP PACKAGING ---
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        zip_file.writestr("index.html", index_html)
        zip_file.writestr("about.html", about_html)
        zip_file.writestr("privacy.html", privacy_html)
        zip_file.writestr("terms.html", terms_html)
        zip_file.writestr("robots.txt", robots_txt)
        zip_file.writestr("sitemap.xml", sitemap_xml)
    
    st.success("✅ Website Engine Finished! Your 17-point compliant package is ready.")
    st.download_button(
        label="📥 DOWNLOAD WEBSITE ZIP PACKAGE",
        data=zip_buffer.getvalue(),
        file_name=f"{biz_name.lower().replace(' ', '_')}_website.zip",
        mime="application/zip"
    )
