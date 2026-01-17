import streamlit as st
import zipfile
import io
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Script Lab | Mobile-First Engine", layout="wide", page_icon="🧪")

st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4em; 
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Kaydiem Lab")
    st.markdown("---")
    st.header("🎨 Visual Theme")
    p_color = st.color_picker("Brand Primary Color", "#001F3F")
    s_color = st.color_picker("Accent Action Color", "#3EB489")
    font_choice = st.selectbox("Typography", ["Inter", "Poppins", "Montserrat", "Outfit"])
    st.header("⚙️ Tech SEO")
    gsc_tag = st.text_input("GSC Verification Tag", placeholder="google-site-verification=...")
    st.info("By www.kaydiemscriptlab.com")

st.title("🏗️ Mobile-First Enterprise Site Factory")

# --- 2. DATA COLLECTION TABS ---
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🌟 Social Proof", "⚖️ Legal Pages"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Urban Prime Dental & Implant Clinic")
        biz_phone = st.text_input("Phone", "+91 98765 43210")
        biz_email = st.text_input("Email", "care@urbanprimedental.com")
    with c2:
        biz_cat = st.text_input("Category", "Dental Clinic")
        biz_hours = st.text_input("Hours", "Mon-Sat: 09:00 - 21:00")
        prod_url = st.text_input("Production URL", "https://username.github.io/repo/")
    biz_addr = st.text_area("Full Address (Exact match to Google Maps)")
    map_iframe = st.text_area("Google Map Embed Link (Paste <iframe> here)")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "Smile with Confidence: World-Class Dental Care")
    seo_d = st.text_input("Meta Description", "Best dental clinic in Bengaluru. Trusted by 5000+ patients.")
    biz_key = st.text_input("Keywords", "Dentist, Root Canal, Implants")
    biz_serv = st.text_area("Services (One per line)")
    about_txt = st.text_area("About Us (Deep E-E-A-T Content)", height=350)

with tabs[2]:
    testi = st.text_area("Testimonials (Name | Comment)")
    faqs = st.text_area("FAQ (Question ? Answer)")

with tabs[3]:
    priv_body = st.text_area("Privacy Policy", height=400)
    terms_body = st.text_area("Terms & Conditions", height=400)

# --- 3. THE RECTIFIED GENERATION ENGINE ---

if st.button("🚀 GENERATE PREMIUM COMPLIANT BIZ PACKAGE"):
    
    theme_css = f"""
    :root {{ --p: {p_color}; --s: {s_color}; --font: '{font_choice}', sans-serif; }}
    body {{ font-family: var(--font); scroll-behavior: smooth; color: #0f172a; line-height: 1.7; letter-spacing: -0.01em; }}
    .bg-brand {{ background-color: var(--p); }}
    .text-brand {{ color: var(--p); }}
    .btn-accent {{ background-color: var(--s); color: white; padding: 1rem 2rem; border-radius: 99px; font-weight: 800; transition: all 0.3s; display: inline-block; }}
    .btn-accent:hover {{ transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
    .legal-text {{ white-space: pre-wrap; }}
    """

    def get_layout(title, desc, content, is_index=False):
        gsc = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_index and gsc_tag) else ""
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
    <link href="https://fonts.googleapis.com/css2?family={font_choice.replace(' ', '+')}:wght@400;700;900&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
</head>
<body class="bg-white flex flex-col min-h-screen">
    <nav class="bg-white sticky top-0 z-50 border-b">
        <div class="max-w-[1400px] mx-auto px-4 py-4 flex flex-wrap justify-between items-center gap-4">
            <a href="index.html" class="text-lg md:text-2xl font-black text-brand tracking-tighter uppercase">{biz_name}</a>
            <div class="flex items-center space-x-4 md:space-x-8 text-[10px] md:text-xs font-black uppercase tracking-widest">
                <a href="index.html" class="hover:text-brand transition">Home</a>
                <a href="about.html" class="hover:text-brand transition">About</a>
                <a href="contact.html" class="hover:text-brand transition">Contact</a>
                <a href="tel:{biz_phone}" class="bg-brand text-white px-4 py-2 md:px-6 md:py-2 rounded-full font-bold shadow-lg">Call</a>
            </div>
        </div>
    </nav>
    <main class="flex-grow">{content}</main>
    <footer class="bg-slate-950 text-slate-400 py-16 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-12">
            <div class="col-span-2">
                <h4 class="text-white font-black text-xl mb-6 tracking-tighter uppercase">{biz_name}</h4>
                <p class="max-w-md mb-8 text-slate-400 leading-relaxed text-sm">{biz_addr}</p>
                <p class="text-[10px]">Build By <a href="https://www.kaydiemscriptlab.com" class="text-white underline font-bold">Kaydiem Script Lab</a></p>
            </div>
            <div class="text-sm">
                <h4 class="text-white font-bold mb-6 uppercase tracking-widest">Legal</h4>
                <ul class="space-y-3">
                    <li><a href="privacy.html" class="hover:text-white transition">Privacy Policy</a></li>
                    <li><a href="terms.html" class="hover:text-white transition">Terms & Conditions</a></li>
                </ul>
            </div>
            <div class="text-sm">
                <h4 class="text-white font-bold mb-6 uppercase tracking-widest">Support</h4>
                <p>{biz_phone}<br>{biz_email}</p>
            </div>
        </div>
    </footer>
</body></html>"""

    # Grid Fix and Responsive Spacing Fix
    serv_cards = "".join([f'<div class="bg-slate-50 p-8 rounded-[2rem] border border-slate-100"><h3 class="text-xl font-black mb-3 text-brand uppercase tracking-tight">{s.strip()}</h3><p class="text-slate-500 text-sm leading-relaxed">Expert dental care solution.</p></div>' for s in biz_serv.splitlines() if s.strip()])
    testi_cards = "".join([f'<div class="p-8 bg-white border-l-4 border-brand shadow-sm italic mb-6 text-lg">"{t.split("|")[1].strip()}"<br><span class="font-bold not-italic text-brand text-xs block mt-4 uppercase">— {t.split("|")[0].strip()}</span></div>' for t in testi.splitlines() if "|" in t])
    faq_html = "".join([f'<details class="mb-4 bg-slate-50 p-5 rounded-xl cursor-pointer shadow-sm"><summary class="font-bold">{f.split("?")[0].strip()}?</summary><p class="mt-4 text-slate-600 text-sm">{f.split("?")[1].strip()}</p></details>' for f in faqs.splitlines() if "?" in f])

    idx_main = f"""
    <header class="bg-white py-16 md:py-40 px-4 text-center">
        <div class="max-w-screen-2xl mx-auto">
            <h1 class="text-4xl md:text-[120px] font-black text-slate-900 mb-8 tracking-tighter leading-[1] uppercase">{hero_h.strip()}</h1>
            <p class="text-lg md:text-2xl text-slate-500 mb-12 max-w-4xl mx-auto px-4 leading-relaxed">{seo_d.strip()}</p>
            <a href="tel:{biz_phone}" class="btn-accent uppercase tracking-widest text-xs shadow-2xl">Book Appointment</a>
        </div>
    </header>
    <section class="max-w-7xl mx-auto py-12 md:py-24 px-6">
        <h2 class="text-3xl md:text-5xl font-black mb-12 md:mb-20 text-center uppercase tracking-tighter text-brand">Our Specialties</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-10">{serv_cards}</div>
    </section>
    <section class="bg-slate-50 py-16 md:py-32 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-16 md:gap-24">
            <div><h2 class="text-3xl md:text-5xl font-black mb-10 md:mb-16 uppercase tracking-tighter text-brand">Reviews</h2>{testi_cards}</div>
            <div><h2 class="text-3xl md:text-5xl font-black mb-10 md:mb-16 uppercase tracking-tighter text-brand">FAQ</h2>{faq_html}</div>
        </div>
    </section>
    """

    zip_buf = io.BytesIO()
    with zipfile.ZipFile(zip_buf, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", get_layout("Home", seo_d, idx_main, True))
        zf.writestr("about.html", get_layout("About", "Our History", f"<section class='max-w-5xl mx-auto py-16 md:py-32 px-6'><h1 class='text-4xl md:text-7xl font-black mb-12 text-brand uppercase tracking-tighter leading-none'>About Us</h1><div class='text-lg md:text-xl leading-relaxed text-slate-700 legal-text'>{about_txt.strip()}</div></section>"))
        zf.writestr("contact.html", get_layout("Contact", "Locate Us", f"<section class='max-w-6xl mx-auto py-16 md:py-32 px-6 text-center'><h1 class='text-4xl md:text-8xl font-black mb-12 text-brand tracking-tighter uppercase'>Visit Us</h1><div class='bg-white p-8 md:p-24 rounded-[3rem] shadow-2xl border'><p class='text-3xl md:text-6xl font-black mb-6 text-brand tracking-tight'>{biz_phone}</p><p class='text-lg md:text-2xl mb-12 text-slate-500'>{biz_addr}</p><div class='rounded-[2rem] overflow-hidden shadow-2xl'>{map_iframe}</div></div></section>"))
        zf.writestr("privacy.html", get_layout("Privacy", "Legal", f"<section class='max-w-5xl mx-auto py-16 md:py-32 px-6'><h1 class='text-4xl md:text-6xl font-black mb-12 text-brand uppercase tracking-tighter'>Privacy Policy</h1><div class='text-sm md:text-lg leading-relaxed text-slate-700 legal-text'>{priv_body.strip()}</div></section>"))
        zf.writestr("terms.html", get_layout("Terms", "Legal", f"<section class='max-w-5xl mx-auto py-16 md:py-32 px-6'><h1 class='text-4xl md:text-6xl font-black mb-12 text-brand uppercase tracking-tighter'>Terms & Conditions</h1><div class='text-sm md:text-lg leading-relaxed text-slate-700 legal-text'>{terms_body.strip()}</div></section>"))
        zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        zf.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url></urlset>')

    st.success("💎 Mobile-First Enterprise Package Ready!")
    st.download_button("📥 DOWNLOAD UPDATED PACKAGE", zip_buf.getvalue(), f"{biz_name.lower()}_enterprise.zip")
