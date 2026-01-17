import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Script Lab | Premium Site Engine", layout="wide", page_icon="💎")

# UI Styling for the Streamlit Dashboard
st.markdown("""
    <style>
    .main { background-color: #f1f5f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #ffffff; border-radius: 8px 8px 0 0; padding: 12px 24px; font-weight: bold; border: 1px solid #e2e8f0; }
    .stTextArea textarea { font-family: 'Inter', sans-serif; font-size: 1rem; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4.5em; 
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.3rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); transition: all 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 25px 30px -5px rgba(0, 0, 0, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: DESIGN STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Kaydiem Lab")
    st.markdown("---")
    
    st.header("🎨 Visual Theme")
    theme_style = st.selectbox("Design Preset", ["Modern Tech (SaaS)", "Royal Elegant (Luxury)", "Clean Minimalist", "Corporate Pro"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        p_color = st.color_picker("Primary Color", "#2563EB")
        bg_color = st.color_picker("Background", "#FFFFFF")
    with col_b:
        s_color = st.color_picker("Accent Color", "#10B981")
        txt_color = st.color_picker("Text Color", "#1E293B")

    font_family = st.selectbox("Font Family", ["Inter", "Playfair Display", "Montserrat", "Poppins", "Outfit"])
    
    st.header("⚙️ SEO Controls")
    gsc_code = st.text_input("GSC Verification Tag", placeholder="google-site-verification=...")
    
    st.markdown("---")
    st.info("Onboarding Tool by Kaydiem Script Lab")

# --- 2. MULTI-TAB DATA ORCHESTRATOR ---
st.title("💎 Premium Google Business Site Factory")
st.write("Generating 100% Certified Search-Engine Optimized Web Assets.")

tabs = st.tabs(["📍 Identity", "🏗️ Layout & Content", "🌟 Social Proof", "⚖️ Legal Pages"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Excel Digital Solutions")
        biz_phone = st.text_input("Verified Phone", "+91 98765 43210")
        biz_email = st.text_input("Business Email", "hello@exceldigital.com")
    with c2:
        biz_cat = st.text_input("Primary Category", "IT Consulting")
        biz_hours = st.text_input("Operating Hours", "Mon-Fri: 09:00 - 18:00")
        prod_url = st.text_input("Production URL", "https://kani201012.github.io/site/")
    biz_addr = st.text_area("Full Address (Exact match to Google Maps)")

with tabs[1]:
    hero_title = st.text_input("Hero Headline", f"Premium {biz_cat} Services in {biz_name}")
    seo_desc = st.text_input("Meta Description (160 Chars)", f"The #1 {biz_cat} in your area. Trusted by 500+ clients.")
    biz_services = st.text_area("Our Services (One per line)", "Web Development\nCloud Solutions\nCyber Security")
    about_text = st.text_area("About Us (Deep E-E-A-T Content)", height=350)

with tabs[2]:
    st.subheader("Building Trust (Point 9 & 14)")
    testimonials = st.text_area("Testimonials (Format: Name | Comment)", "Rahul S. | Best service ever!\nAnjali P. | Highly professional.")
    faqs = st.text_area("FAQ (Format: Question ? Answer)", "Is it 24/7 ? Yes, we operate 24/7.\nDo you offer refunds ? Yes, within 30 days.")

with tabs[3]:
    st.subheader("Mandatory Compliance Pages (Point 17)")
    privacy_body = st.text_area("Full Privacy Policy Text", height=350)
    terms_body = st.text_area("Full Terms & Conditions Text", height=350)

# --- 3. THE MASTER ARCHITECT ENGINE ---

if st.button("🚀 GENERATE PREMIUM COMPLIANT BIZ PACKAGE"):
    
    # CSS Strategy for Themes
    theme_css = f"""
    :root {{
        --p: {p_color}; --s: {s_color}; --bg: {bg_color}; --txt: {txt_color};
        --font: '{font_family}', sans-serif;
    }}
    body {{ font-family: var(--font); background-color: var(--bg); color: var(--txt); scroll-behavior: smooth; }}
    .btn-p {{ background: var(--p); color: white; transition: all 0.3s; }}
    .btn-p:hover {{ transform: translateY(-2px); opacity: 0.9; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
    .text-p {{ color: var(--p); }}
    .bg-light {{ background: #f8fafc; }}
    """

    def get_full_html(title, desc, content, is_index=False):
        gsc = f'<meta name="google-site-verification" content="{gsc_code}">' if (is_index and gsc_code) else ""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {gsc}
    <title>{title} | {biz_name}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{prod_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={font_family.replace(' ', '+')}:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
    <!-- Point 14: LocalBusiness Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "description": "{seo_desc}",
      "url": "{prod_url}",
      "telephone": "{biz_phone}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_addr}" }},
      "openingHours": "{biz_hours}"
    }}
    </script>
</head>
<body class="flex flex-col min-h-screen">
    <nav class="bg-white/90 backdrop-blur-md sticky top-0 z-50 border-b">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="index.html" class="text-2xl font-black tracking-tighter text-p uppercase">{biz_name}</a>
            <div class="hidden md:flex space-x-8 text-xs font-black uppercase tracking-widest">
                <a href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="contact.html">Contact</a>
            </div>
            <a href="tel:{biz_phone}" class="btn-p px-6 py-2 rounded-full text-sm font-bold">Call Now</a>
        </div>
    </nav>
    <main class="flex-grow">{content}</main>
    <footer class="bg-slate-950 text-slate-400 py-20 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-12">
            <div class="col-span-2">
                <h4 class="text-white font-black text-2xl mb-4 tracking-tighter uppercase">{biz_name}</h4>
                <p class="max-w-sm mb-6">{biz_addr}</p>
                <p class="text-sm font-bold">Build By <a href="https://www.kaydiemscriptlab.com" class="text-white underline">Kaydiem Script Lab</a></p>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">LEGAL</h4>
                <ul class="space-y-3 text-sm">
                    <li><a href="privacy.html" class="hover:text-white">Privacy Policy</a></li>
                    <li><a href="terms.html" class="hover:text-white">Terms & Conditions</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">SUPPORT</h4>
                <p class="text-sm">{biz_phone}<br>{biz_email}</p>
            </div>
        </div>
    </footer>
</body></html>"""

    # --- CONTENT BUILDERS ---
    
    # Index Content
    service_cards = "".join([f'<div class="bg-white p-8 rounded-2xl shadow-xl border-t-4 border-p"><h3 class="text-xl font-bold mb-3">{s}</h3><p class="text-slate-500 text-sm">Professional {biz_cat} tailored for your needs.</p></div>' for s in biz_services.splitlines()])
    
    testimonial_cards = "".join([f'<div class="italic border-l-4 border-s p-4 bg-light">"{t.split("|")[1].strip()}"<br><span class="font-bold not-italic text-sm">- {t.split("|")[0].strip()}</span></div>' for t in testimonials.splitlines() if "|" in t])
    
    faq_html = "".join([f'<details class="p-4 bg-white border rounded-lg mb-2 cursor-pointer"><summary class="font-bold">{f.split("?")[0].strip()}?</summary><p class="mt-2 text-slate-600">{f.split("?")[1].strip()}</p></details>' for f in faqs.splitlines() if "?" in f])

    idx_main = f"""
    <section class="py-32 px-6 text-center">
        <h1 class="text-6xl md:text-9xl font-black mb-8 leading-none tracking-tighter">{hero_title}</h1>
        <p class="text-2xl text-slate-500 mb-12 max-w-3xl mx-auto leading-relaxed">{seo_desc}</p>
        <a href="tel:{biz_phone}" class="btn-p px-12 py-5 rounded-full text-lg font-black uppercase tracking-widest shadow-2xl inline-block">Work with Us</a>
    </section>
    
    <section class="max-w-7xl mx-auto py-24 px-6">
        <h2 class="text-4xl font-black mb-12 uppercase tracking-tighter text-center">Our Expertise</h2>
        <div class="grid md:grid-cols-3 gap-10">{service_cards}</div>
    </section>

    <section class="bg-light py-24 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-20">
            <div><h2 class="text-4xl font-black mb-10 uppercase tracking-tighter">What Clients Say</h2><div class="space-y-6">{testimonial_cards}</div></div>
            <div><h2 class="text-4xl font-black mb-10 uppercase tracking-tighter">Common Questions</h2>{faq_html}</div>
        </div>
    </section>
    """

    # --- ZIP ENGINE ---
    zip_buf = io.BytesIO()
    with zipfile.ZipFile(zip_buf, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", get_full_html("Home", seo_desc, idx_main, True))
        zf.writestr("about.html", get_full_html("About Us", "History", f"<section class='max-w-4xl mx-auto py-32 px-6'><h1 class='text-5xl font-black mb-10 uppercase tracking-tighter'>About {biz_name}</h1><div class='prose prose-xl max-w-none'>{about_text.replace('\\n', '<br>')}</div></section>"))
        zf.writestr("contact.html", get_full_html("Contact Us", "Location", f"<section class='max-w-4xl mx-auto py-32 px-6 text-center'><h1 class='text-6xl font-black mb-10 tracking-tighter'>VISIT US</h1><div class='bg-slate-50 p-20 rounded-[3rem] border shadow-2xl'><p class='text-5xl font-black mb-4 text-p'>{biz_phone}</p><p class='text-xl'>{biz_addr}</p><div class='mt-10 h-64 bg-slate-200 rounded-2xl flex items-center justify-center font-bold'>Google Maps Embed Frame</div></div></section>"))
        zf.writestr("privacy.html", get_full_html("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-6'><h1 class='text-4xl font-bold mb-10'>Privacy Policy</h1><div class='leading-relaxed text-slate-600'>{privacy_body.replace('\\n', '<br>')}</div></div>"))
        zf.writestr("terms.html", get_full_html("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-6'><h1 class='text-4xl font-bold mb-10'>Terms & Conditions</h1><div class='leading-relaxed text-slate-600'>{terms_body.replace('\\n', '<br>')}</div></div>"))
        zf.writestr("404.html", get_full_html("404", "Not Found", "<div class='py-64 text-center'><h1 class='text-9xl font-black'>404</h1><p class='text-2xl mt-4 uppercase font-bold'>Page Not Found</p><a href='index.html' class='mt-10 inline-block text-p underline'>Go Home</a></div>"))
        zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        zf.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url><url><loc>{prod_url}about.html</loc></url></urlset>')

    st.success("💎 Premium Verified Package Architecture Finished!")
    st.download_button("📥 DOWNLOAD ENTERPRISE BIZ PACKAGE", zip_buf.getvalue(), f"{biz_name.lower()}_enterprise.zip")
