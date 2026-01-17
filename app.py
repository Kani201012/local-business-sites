import streamlit as st
import zipfile
import io
from datetime import datetime

# --- 1. APP CONFIGURATION & UI ---
st.set_page_config(page_title="Kaydiem Script Lab | Site Factory", layout="wide", page_icon="🧪")

# Custom CSS for the Streamlit Interface
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #ffffff; border-radius: 5px 5px 0 0; padding: 10px 20px; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background: linear-gradient(90deg, #4285F4, #34A853); color: white; font-weight: bold; border: none; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Branding
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=80)
    st.title("Admin Panel")
    st.info("By www.kaydiemscriptlab.com")
    
    st.header("🎨 Theme Customization")
    primary_color = st.color_picker("Brand Primary Color", "#4285F4")
    accent_color = st.color_picker("Accent Color (Buttons/Links)", "#34A853")
    font_choice = st.selectbox("Typography Style", ["Inter", "Poppins", "Roboto", "Oswald"])

# Main Header
st.title("🏗️ Enterprise Google Site Factory")
st.write("Generate high-performance, 17-point compliant business assets for local SEO dominance.")

# --- 2. DATA COLLECTION TABS ---
tab1, tab2, tab3 = st.tabs(["📍 Business Profile", "📝 Content & SEO", "⚖️ Legal Pages"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        biz_name = st.text_input("Business Name (NAP Match)", "Gupta Electronics")
        biz_phone = st.text_input("Verified Phone", "+91 98765 43210")
        biz_email = st.text_input("Business Email", "contact@gupta.com")
    with col2:
        biz_category = st.text_input("Business Category", "Electronics Repair")
        biz_hours = st.text_input("Working Hours (Google Format)", "Mon-Sat: 10:00-20:00")
        website_url = st.text_input("Target URL (Include trailing /)", "https://username.github.io/repo/")
    
    biz_address = st.text_area("Full Physical Address (Must match Google Maps exactly)")
    biz_services = st.text_area("Services (One per line for Semantic HTML listing)", "AC Repair\nTV Service\nLaptop Care")

with tab2:
    st.header("SEO Configuration")
    seo_title = st.text_input("Meta Title (50-65 chars)", f"Best {biz_category} in {biz_name}")
    seo_desc = st.text_input("Meta Description (150-160 chars)", f"Looking for {biz_category}? Visit {biz_name}. Expert service in {biz_address[:30]}.")
    hero_alt = st.text_input("Hero Image Alt Text", f"{biz_name} storefront interior")
    
    about_content = st.text_area("About Us (800 - 2000 words for E-E-A-T Compliance)", 
                                 "Established in 2004, Gupta Electronics has been the leading service provider...", height=300)

with tab3:
    st.header("Mandatory Legal Content")
    privacy_content = st.text_area("Privacy Policy Text", "We value your privacy. Your data is never sold...", height=200)
    terms_content = st.text_area("Terms & Conditions Text", "By using this site, you agree to our service terms...", height=200)

# --- 3. GENERATION ENGINE ---

if st.button("🚀 BUILD & PACKAGE COMPLIANT WEBSITE"):
    
    # 17-Point Compliance Layout Helper
    def get_layout(page_title, page_desc, content):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Point 11: Unique Title & Meta -->
    <title>{page_title} | {biz_name}</title>
    <meta name="description" content="{page_desc}">
    <!-- Point 6 & 7: Speed & HTTPS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={font_choice}:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: '{font_choice}', sans-serif; }}
        :root {{ --brand: {primary_color}; --accent: {accent_color}; }}
        .bg-brand {{ background-color: var(--brand); }}
        .text-accent {{ color: var(--accent); }}
        .border-accent {{ border-color: var(--accent); }}
    </style>
    <!-- Point 14: Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_address}" }},
      "telephone": "{biz_phone}",
      "openingHours": "{biz_hours}",
      "url": "{website_url}"
    }}
    </script>
</head>
<body class="bg-gray-50 flex flex-col min-h-screen">
    <!-- Point 8: Crawlable Internal Links -->
    <nav class="bg-white border-b sticky top-0 z-50 p-4">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <a href="index.html" class="text-xl font-bold" style="color: {primary_color}">{biz_name}</a>
            <div class="space-x-6 text-sm font-bold uppercase">
                <a href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="contact.html">Contact</a>
            </div>
        </div>
    </nav>
    <main class="flex-grow">{content}</main>
    <footer class="bg-gray-900 text-white p-12">
        <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
            <div><h3 class="font-bold mb-4">{biz_name}</h3><p class="text-gray-400">{biz_address}</p></div>
            <div><h4 class="font-bold mb-4">Legal</h4>
                <ul class="text-gray-400 space-y-2 text-sm">
                    <li><a href="privacy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms & Conditions</a></li>
                </ul>
            </div>
            <div><h4 class="font-bold mb-4">Lead Lab</h4>
                <p class="text-xs text-gray-500">This site build by <br>
                <a href="https://www.kaydiemscriptlab.com" class="text-white underline">www.kaydiemscriptlab.com</a></p>
            </div>
        </div>
    </footer>
</body></html>"""

    # --- PAGE 1: INDEX ---
    index_html = get_layout(seo_title, seo_desc, f"""
    <header class="bg-white py-24 text-center px-4">
        <!-- Point 12: Proper Heading Structure -->
        <h1 class="text-5xl font-black mb-6">{biz_name}</h1>
        <p class="text-xl text-gray-600 mb-10 max-w-2xl mx-auto">{seo_desc}</p>
        <div class="flex justify-center gap-4">
            <a href="tel:{biz_phone}" class="px-8 py-4 rounded-lg text-white font-bold" style="background:{accent_color}">Call {biz_phone}</a>
        </div>
    </header>
    <section class="max-w-6xl mx-auto py-20 px-4">
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div>
                <h2 class="text-3xl font-bold mb-6">Expert {biz_category} Services</h2>
                <ul class="space-y-4">
                    {"".join([f'<li class="flex items-center gap-2"><span class="text-accent">✔</span> {s}</li>' for s in biz_services.splitlines()])}
                </ul>
            </div>
            <!-- Point 13: Alt Text for Images -->
            <img src="https://images.unsplash.com/photo-1556740734-7f9a2b7a0f42" alt="{hero_alt}" class="rounded-2xl shadow-2xl">
        </div>
    </section>
    """)

    # --- PAGE 2: ABOUT ---
    about_html = get_layout("About Us", f"Learn about {biz_name}", f"""
    <section class="max-w-4xl mx-auto py-20 px-4">
        <h1 class="text-4xl font-bold mb-8">About {biz_name}</h1>
        <!-- Point 9: Unique & Helpful Content -->
        <div class="prose prose-lg text-gray-700 leading-relaxed">
            {about_content.replace('\\n', '<br>')}
        </div>
    </section>
    """)

    # --- PAGE 3: CONTACT ---
    contact_html = get_layout("Contact Us", "Get in touch", f"""
    <section class="max-w-4xl mx-auto py-20 px-4 text-center">
        <h1 class="text-4xl font-bold mb-10">Contact Details</h1>
        <div class="bg-white p-12 rounded-3xl shadow-xl border-t-8 border-accent">
            <p class="text-3xl font-bold mb-4" style="color: {primary_color}">{biz_phone}</p>
            <p class="text-xl mb-2">{biz_address}</p>
            <p class="text-gray-500 mb-10">{biz_email}</p>
            <a href="https://www.google.com/maps/search/?api=1&query={biz_name}" class="px-10 py-4 rounded-full text-white font-bold" style="background:{primary_color}">Open Google Maps</a>
        </div>
    </section>
    """)

    # --- PAGE 4 & 5: LEGAL (Point 17) ---
    privacy_html = get_layout("Privacy Policy", "Legal", f"<div class='max-w-4xl mx-auto py-20 px-4'><h1>Privacy Policy</h1><div class='mt-10'>{privacy_content}</div></div>")
    terms_html = get_layout("Terms & Conditions", "Legal", f"<div class='max-w-4xl mx-auto py-20 px-4'><h1>Terms & Conditions</h1><div class='mt-10'>{terms_content}</div></div>")

    # --- TECHNICAL FILES (Points 3 & 15) ---
    robots_txt = f"User-agent: *\nAllow: /\nSitemap: {website_url}sitemap.xml"
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>{website_url}index.html</loc></url>
    <url><loc>{website_url}about.html</loc></url>
    <url><loc>{website_url}contact.html</loc></url>
    <url><loc>{website_url}privacy.html</loc></url>
    <url><loc>{website_url}terms.html</loc></url>
</urlset>"""

    # --- ZIP PACKAGING ---
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        zip_file.writestr("index.html", index_html)
        zip_file.writestr("about.html", about_html)
        zip_file.writestr("contact.html", contact_html)
        zip_file.writestr("privacy.html", privacy_html)
        zip_file.writestr("terms.html", terms_html)
        zip_file.writestr("robots.txt", robots_txt)
        zip_file.writestr("sitemap.xml", sitemap_xml)

    st.success("✅ Enterprise Package Built Successfully!")
    st.download_button(
        label="📥 DOWNLOAD ZIP PACKAGE",
        data=zip_buffer.getvalue(),
        file_name=f"{biz_name.lower().replace(' ', '_')}_verified_site.zip",
        mime="application/zip"
    )
