import streamlit as st

st.set_page_config(layout="wide")
st.title("💎 Enterprise Google Site Generator")

# --- PROFESSIONAL INPUTS ---
with st.expander("Step 1: Core Business Data (NAP Consistency)", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Business Name", "Sharma Premium Electronics")
        phone = st.text_input("Verified Phone", "+91 98765 43210")
        email = st.text_input("Business Email", "contact@sharma.com")
    with col2:
        category = st.text_input("Business Category", "Consumer Electronics Store")
        address = st.text_area("Full Address (Must match Google Maps exactly)")
        map_link = st.text_input("Google Maps Embed Link (from Share -> Embed Map)")

with st.expander("Step 2: SEO & Trust Signals"):
    services = st.text_area("Services (One per line)", "AC Repair\nOven Service\nGenuine Parts")
    hours = st.text_input("Working Hours", "Mon - Sat: 10:00 AM - 08:00 PM")
    description = st.text_area("SEO Description", "Leading electronics provider in South Delhi for 20+ years.")

# --- THE HIGH-END HTML GENERATOR ---
# This uses Tailwind CSS for a professional "SaaS" look
enterprise_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | {category} in {address[:20]}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    
    <!-- ADVANCED SCHEMA FOR GOOGLE RANKING -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{name}",
      "description": "{description}",
      "address": {{ "@type": "PostalAddress", "streetAddress": "{address}" }},
      "telephone": "{phone}",
      "openingHours": "{hours}"
    }}
    </script>
</head>
<body class="bg-gray-50 font-['Inter']">

    <!-- NAVBAR -->
    <nav class="bg-white shadow-sm p-4 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <span class="text-xl font-bold text-blue-600">{name}</span>
            <a href="tel:{phone}" class="bg-blue-600 text-white px-5 py-2 rounded-full font-semibold">Call Now</a>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <header class="bg-white py-16 px-4">
        <div class="max-w-4xl mx-auto text-center">
            <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">{name}</h1>
            <p class="text-xl text-gray-600 mb-8">{description}</p>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="https://wa.me/{phone.replace(' ', '')}" class="bg-green-500 text-white px-8 py-3 rounded-lg font-bold">Order on WhatsApp</a>
                <a href="#map" class="bg-gray-800 text-white px-8 py-3 rounded-lg font-bold">Visit Store</a>
            </div>
        </div>
    </header>

    <!-- SERVICES -->
    <section class="py-12 bg-gray-50">
        <div class="max-w-6xl mx-auto px-4">
            <h2 class="text-2xl font-bold mb-8">Specialized Services</h2>
            <div class="grid md:grid-cols-3 gap-6">
                {"".join([f'<div class="bg-white p-6 rounded-xl shadow-sm border-b-4 border-blue-500"><h3 class="font-bold text-lg">{s}</h3><p class="text-gray-500 mt-2">Professional service in {address.split(",")[-1]}</p></div>' for s in services.splitlines()])}
            </div>
        </div>
    </section>

    <!-- MAP & CONTACT -->
    <section id="map" class="py-12 bg-white">
        <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12">
            <div>
                <h2 class="text-2xl font-bold mb-4">Contact & Location</h2>
                <p class="text-gray-600 mb-2">📍 {address}</p>
                <p class="text-gray-600 mb-2">📞 {phone}</p>
                <p class="text-gray-600 mb-6">⏰ {hours}</p>
                <div class="rounded-lg overflow-hidden border">
                    {map_link}
                </div>
            </div>
            <div class="bg-blue-50 p-8 rounded-2xl">
                <h3 class="text-xl font-bold mb-4">Send a Query</h3>
                <input type="text" placeholder="Your Name" class="w-full p-3 mb-4 rounded-lg border">
                <textarea placeholder="How can we help you?" class="w-full p-3 mb-4 rounded-lg border h-32"></textarea>
                <button class="w-full bg-blue-600 text-white py-3 rounded-lg font-bold">Request a Callback</button>
            </div>
        </div>
    </section>

</body>
</html>
"""

if st.button("🚀 Generate 1st Class Business Website"):
    st.subheader("Professional Website Code")
    st.code(enterprise_html, language="html")
    st.write("---")
    st.subheader("Live Preview (Simulated)")
    st.components.v1.html(enterprise_html, height=600, scrolling=True)
