import streamlit as st
import zipfile
import io
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Script Lab | Enterprise Site Factory", layout="wide", page_icon="🧪")

# Custom CSS for the Streamlit Admin UI
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stTextArea textarea { font-family: 'Courier New', monospace; color: #1e293b; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4em; 
        background: linear-gradient(135deg, #4285F4 0%, #34A853 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: BRANDING & CUSTOM THEME ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=60)
    st.title("Kaydiem Lab")
    st.markdown("---")
    
    st.header("🎨 Custom Branding")
    primary_color = st.color_picker("Brand Primary Color", "#1A73E8")
    accent_color = st.color_picker("Call-to-Action Color", "#34A853")
    font_family = st.selectbox("Typography", ["Inter", "Poppins", "Montserrat", "Roboto"])
    
    st.header("⚙️ Search Console")
    gsc_tag = st.text_input("GSC Tag (Point 16)", placeholder="google-site-verification=...")
    
    st.info("Lead Lab: www.kaydiemscriptlab.com")

st.title("🏗️ Enterprise Google Site Factory")
st.write("Professional 17-Point Compliant Business Asset Generator")

# --- 2. DATA COLLECTION TABS ---
tab1, tab2, tab3 = st.tabs(["📍 Business Profile", "✍️ SEO Content", "⚖️ Legal (Privacy/Terms)"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        biz_name = st.text_input("Business Name (NAP)", "Gupta Electronics")
        biz_phone = st.text_input("Phone", "+91 98765 43210")
        biz_email = st.text_input("Email", "info@gupta.com")
    with col2:
        biz_category = st.text_input("Category", "Electronics Repair")
        biz_hours = st.text_input("Hours", "Mon-Sat 10:00-20:00")
        website_url = st.text_input("Production URL (Trailing /)", "https://kani201012.github.io/site/")
    biz_address = st.text_area("Full Maps Address")
    biz_services = st.text_area("Services (One per line)", "AC Repair\nTV Service\nLaptop Repair")

with tab2:
    seo_desc = st.text_input("Meta Description (160 Chars)", "Best electronics repair in Bengaluru...")
    about_content = st.text_area("About Us Section (E-E-A-T Content)", height=300, 
                                 placeholder="Write 800-2000 words here for Google ranking...")

with tab3:
    privacy_content = st.text_area("Privacy Policy (Point 17)", height=300, 
                                   placeholder="Enter your full Privacy Policy here...")
    terms_content = st.text_area("Terms & Conditions (Point 17)", height=300, 
                                 placeholder="Enter your full Terms & Conditions here...")

# --- 3. THE GENERATION ENGINE ---

if st.button("🚀 GENERATE 100% COMPLIANT BIZ PACKAGE"):
    
    def get_layout(title, desc, content, is_index=False):
        verification = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_index and gsc_tag) else ""
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {verification}
    <title>{title} | {biz_name}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{website_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={font_family}:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: '{font_family}', sans-serif; }}
        :root {{ --primary: {primary_color}; --accent: {accent_color}; }}
        .text-primary {{ color: var(--primary); }}
        .bg-primary {{ background-color: var(--primary); }}
        .btn-accent {{ background-color: var(--accent); color: white; padding: 1.2rem 2.5rem; border-radius: 99px; font-weight: 900; display: inline-block; transition: all 0.3s; box-shadow: 0 10px 20px -5px var(--accent); }}
        .btn-accent:hover {{ transform: translateY(-3px); box-shadow: 0 20px 25px -5px var(--accent); }}
    </style>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_address}" }},
      "telephone": "{biz_phone}",
      "url": "{website_url}"
    }}
    </script>
</head>
<body class="bg-white flex flex-col min-h-screen text-slate-900">
    <nav class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50 p-5">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <a href="index.html" class="text-2xl font-black text-primary tracking-tighter uppercase">{biz_name}</a>
            <div class="hidden md:flex space-x-10 text-xs font-black uppercase tracking-widest">
                <a href="index.html" class="hover:text-primary transition">Home</a>
                <a href="about.html" class="hover:text-primary transition">About</a>
                <a href="contact.html" class="hover:text-primary transition">Contact</a>
            </div>
        </div>
    </nav>
    <main class="flex-grow">{content}</main>
    <footer class="bg-slate-950 text-slate-400 p-16">
        <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-16">
            <div class="col-span-2">
                <h4 class="text-white font-black mb-6 uppercase tracking-widest">{biz_name}</h4>
                <p class="max-w-sm text-lg leading-relaxed">{biz_address}</p>
            </div>
            <div>
                <h4 class="text-white font-bold mb-6">COMPLIANCE</h4>
                <ul class="space-y-4 text-sm font-medium">
                    <li><a href="privacy.html" class="hover:text-white transition">Privacy Policy</a></li>
                    <li><a href="terms.html" class="hover:text-white transition">Terms & Conditions</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold mb-6">LEAD LAB</h4>
                <p class="text-sm">This site build by</p>
                <a href="https://www.kaydiemscriptlab.com" class="text-white font-black text-lg underline">www.kaydiemscriptlab.com</a>
            </div>
        </div>
    </footer>
</body></html>"""

    # --- PAGE LOGIC ---
    index_html = get_layout(biz_category, seo_desc, f"""
    <header class="py-32 px-6 text-center">
        <h1 class="text-7xl md:text-9xl font-black mb-8 tracking-tighter leading-none" style="color: {primary_color}">{biz_name}</h1>
        <p class="text-2xl text-slate-500 mb-12 max-w-3xl mx-auto font-medium">{seo_desc}</p>
        <a href="tel:{biz_phone}" class="btn-accent uppercase tracking-widest">Connect Now</a>
    </header>
    <section class="max-w-7xl mx-auto py-24 px-6">
        <div class="grid md:grid-cols-3 gap-10">
            {"".join([f'<div class="bg-slate-50 p-10 rounded-3xl border border-slate-100"><h3 class="text-2xl font-black mb-4 uppercase">{s}</h3><p class="text-slate-500">Premium {biz_category} solution verified by {biz_name}.</p></div>' for s in biz_services.splitlines()])}
        </div>
    </section>
    """, is_index=True)

    # ZIP Creation
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        zip_file.writestr("index.html", index_html)
        zip_file.writestr("about.html", get_layout("About Us", "History", f"<section class='max-w-4xl mx-auto py-24 px-6'><article class='prose prose-2xl leading-relaxed'>{about_content.replace('\\n', '<br>')}</article></section>"))
        zip_file.writestr("privacy.html", get_layout("Privacy", "Legal", f"<section class='max-w-4xl mx-auto py-24 px-6'><h1 class='text-5xl font-black mb-10'>Privacy Policy</h1><div>{privacy_content.replace('\\n', '<br>')}</div></section>"))
        zip_file.writestr("terms.html", get_layout("Terms", "Legal", f"<section class='max-w-4xl mx-auto py-24 px-6'><h1 class='text-5xl font-black mb-10'>Terms & Conditions</h1><div>{terms_content.replace('\\n', '<br>')}</div></section>"))
        zip_file.writestr("contact.html", get_layout("Contact", "Location", f"<section class='max-w-4xl mx-auto py-32 px-6 text-center'><h1 class='text-6xl font-black mb-10'>Visit Us</h1><div class='bg-slate-50 p-20 rounded-[3rem]'><p class='text-4xl font-black mb-4'>{biz_phone}</p><p class='text-xl'>{biz_address}</p></div></section>"))
        zip_file.writestr("404.html", get_layout("404", "Not Found", "<div class='py-40 text-center'><h1 class='text-9xl font-black'>404</h1></div>"))
        zip_file.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {website_url}sitemap.xml")
        zip_file.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{website_url}index.html</loc></url></urlset>')

    st.success("✅ Enterprise Verified Package Ready for Download!")
    st.download_button("📥 DOWNLOAD CERTIFIED BIZ PACKAGE", zip_buffer.getvalue(), f"{biz_name.lower()}_site.zip")
