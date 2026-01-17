import streamlit as st
import zipfile
import io
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Certified Google Site Factory", layout="wide", page_icon="🏗️")

# --- UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #4285F4; color: white; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #357abd; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏗️ 17-Point Google Compliant Website Factory")
st.info("This engine generates a complete multi-page business site with Schema.org, Sitemap, and Robots.txt.")

# --- STEP 1: DATA COLLECTION ---
with st.form("business_data_form"):
    st.header("📋 Business Details (NAP Consistency)")
    
    col1, col2 = st.columns(2)
    with col1:
        biz_name = st.text_input("Business Name", "Gupta Electronics")
        biz_phone = st.text_input("Phone Number", "+91 98765 43210")
        biz_email = st.text_input("Business Email", "info@guptaelectronics.com")
        biz_city = st.text_input("City/Area", "Indiranagar, Bengaluru")
        website_url = st.text_input("Final Website URL", "https://kani201012.github.io/local-business-sites/")
    
    with col2:
        biz_category = st.text_input("Business Category", "Electronics Repair Shop")
        biz_hours = st.text_input("Working Hours", "Mon-Sat: 10 AM - 8 PM")
        biz_address = st.text_area("Full Physical Address (Exact match to Google Maps)")
        biz_services = st.text_area("Services (One per line)", "AC Repair\nOven Service\nRefrigerator Repair")

    st.header("✍️ Content & SEO")
    seo_desc = st.text_input("SEO Meta Description", "Best electronics repair in Bengaluru. 20+ years of experience.")
    long_about = st.text_area("Detailed About Us (E-E-A-T content for ranking)", "Established in 2004, Gupta Electronics has served over 10,000 customers...")
    
    submit_btn = st.form_submit_button("🚀 GENERATE FULL COMPLIANT PACKAGE")

# --- STEP 2: GENERATION ENGINE ---
if submit_btn:
    # --- INTERNAL HELPER: HTML COMPONENTS ---
    def get_layout(title, content):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {biz_name}</title>
    <meta name="description" content="{seo_desc}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_address}", "addressLocality": "{biz_city}" }},
      "telephone": "{biz_phone}",
      "openingHours": "{biz_hours}"
    }}
    </script>
</head>
<body class="flex flex-col min-h-screen bg-gray-50 text-gray-800">
    <nav class="bg-white border-b p-4 shadow-sm">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <a href="index.html" class="text-2xl font-bold text-blue-600">{biz_name}</a>
            <div class="space-x-6 font-semibold">
                <a href="index.html" class="hover:text-blue-600">Home</a>
                <a href="about.html" class="hover:text-blue-600">About</a>
                <a href="contact.html" class="hover:text-blue-600">Contact</a>
            </div>
        </div>
    </nav>
    <main class="flex-grow">{content}</main>
    <footer class="bg-gray-900 text-white p-10 mt-10">
        <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
            <div><h3 class="font-bold text-lg mb-4">{biz_name}</h3><p>{biz_address}</p></div>
            <div><h4 class="font-bold mb-4">Quick Links</h4>
                <ul class="text-gray-400 space-y-2">
                    <li><a href="privacy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms & Conditions</a></li>
                </ul>
            </div>
            <div><h4 class="font-bold mb-4">Contact</h4><p>{biz_phone}<br>{biz_email}</p></div>
        </div>
        <div class="text-center text-gray-500 text-xs mt-10 border-t border-gray-800 pt-5">
            © {datetime.now().year} {biz_name} | Built for Google Compliance
        </div>
    </footer>
</body></html>"""

    # --- INDIVIDUAL PAGES ---
    # 1. Index (Home)
    index_content = f"""
    <header class="bg-white py-20 px-4 text-center">
        <h1 class="text-5xl font-extrabold text-gray-900 mb-6">{biz_name}</h1>
        <p class="text-xl text-gray-600 mb-10">{seo_desc}</p>
        <a href="tel:{biz_phone}" class="bg-blue-600 text-white px-10 py-4 rounded-full font-bold text-lg">Call Now</a>
    </header>
    <section class="max-w-6xl mx-auto py-16 px-4">
        <h2 class="text-3xl font-bold text-center mb-12">Expert {biz_category} Services</h2>
        <div class="grid md:grid-cols-3 gap-8">
            {"".join([f'<div class="bg-white p-8 rounded-2xl shadow-sm border-t-4 border-blue-600"><h3>{s}</h3></div>' for s in biz_services.splitlines()])}
        </div>
    </section>"""
    
    # 2. About
    about_content = f"""<div class="max-w-4xl mx-auto py-20 px-4">
        <h1 class="text-4xl font-bold mb-6">About Our Business</h1>
        <p class="text-lg leading-relaxed">{long_about}</p>
    </div>"""

    # 3. Contact (The missing file!)
    contact_content = f"""<div class="max-w-4xl mx-auto py-20 px-4 text-center">
        <h1 class="text-4xl font-bold mb-6">Contact Us</h1>
        <div class="bg-white p-10 rounded-xl shadow-lg">
            <p class="text-2xl font-bold text-blue-600 mb-4">{biz_phone}</p>
            <p class="mb-4">{biz_address}</p>
            <p class="mb-8">{biz_email}</p>
            <a href="https://www.google.com/maps/search/?api=1&query={biz_name} {biz_city}" class="bg-green-600 text-white px-8 py-3 rounded-lg">Open in Google Maps</a>
        </div>
    </div>"""

    # 4. Legal Pages
    privacy_content = f"<div class='p-20'><h1>Privacy Policy</h1><p>Legal information for {biz_name}...</p></div>"
    terms_content = f"<div class='p-20'><h1>Terms & Conditions</h1><p>Terms of service for {biz_name}...</p></div>"

    # --- TECHNICAL SEO FILES ---
    robots_txt = f"User-agent: *\nAllow: /\nSitemap: {website_url}sitemap.xml"
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>{website_url}index.html</loc></url>
    <url><loc>{website_url}about.html</loc></url>
    <url><loc>{website_url}contact.html</loc></url>
</urlset>"""

    # --- ZIP PACKAGING ---
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        zip_file.writestr("index.html", get_layout("Home", index_content))
        zip_file.writestr("about.html", get_layout("About Us", about_content))
        zip_file.writestr("contact.html", get_layout("Contact Us", contact_content))
        zip_file.writestr("privacy.html", get_layout("Privacy Policy", privacy_content))
        zip_file.writestr("terms.html", get_layout("Terms", terms_content))
        zip_file.writestr("robots.txt", robots_txt)
        zip_file.writestr("sitemap.xml", sitemap_xml)

    st.success("✅ Package Generated Successfully!")
    st.download_button(
        label="📥 DOWNLOAD GOOGLE COMPLIANT ZIP",
        data=zip_buffer.getvalue(),
        file_name="google_compliant_site.zip",
        mime="application/zip"
    )
