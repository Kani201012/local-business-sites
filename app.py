import streamlit as st

st.header("🏆 Ultimate Google SEO Website Generator")

# 1. Inputs for 100% Business Info
col1, col2 = st.columns(2)
with col1:
    biz_name = st.text_input("Business Name")
    biz_phone = st.text_input("Phone (with +91)")
    biz_city = st.text_input("City/Area")
    biz_category = st.text_input("Category (e.g. Pharmacy, Cafe)")
with col2:
    biz_address = st.text_area("Full Address (from Google Maps)")
    biz_hours = st.text_input("Opening Hours (e.g. Mon-Sat 9AM-9PM)")
    biz_services = st.text_area("Services (Comma separated: Home Delivery, Consultation, etc.)")

# 2. The Advanced Template
seo_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{biz_name} - {biz_category} in {biz_city}</title>
    <meta name="description" content="Visit {biz_name} in {biz_city}. Specializing in {biz_services}. Call {biz_phone} for details.">
    
    <!-- GOOGLE SCHEMA (JSON-LD) - THIS IS WHAT MAKES IT RANK -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{biz_name}",
      "image": "https://www.google.com/maps/vt/pb=!1m4!1m3!1i17!2i77545!3i50343!2m3!1e0!2sm!3i385055030!3m8!2sen!3sin!5e1105!12m4!1e68!2m2!1sset!2sRoadmap!4e0!5m1!1e0",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "{biz_address}",
        "addressLocality": "{biz_city}",
        "addressRegion": "IN"
      }},
      "telephone": "{biz_phone}",
      "openingHours": "{biz_hours}",
      "priceRange": "$$"
    }}
    </script>

    <style>
        :root {{ --google-blue: #4285F4; --google-green: #34A853; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; color: #333; }}
        header {{ background: var(--google-blue); color: white; padding: 40px 20px; text-align: center; }}
        .container {{ max-width: 800px; margin: auto; padding: 20px; }}
        .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-top: -30px; background: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .btn {{ display: block; text-align: center; padding: 15px; margin: 10px 0; border-radius: 5px; text-decoration: none; font-weight: bold; }}
        .call-btn {{ background: var(--google-green); color: white; }}
        .map-btn {{ border: 1px solid var(--google-blue); color: var(--google-blue); }}
        .services {{ background: #f9f9f9; padding: 15px; border-radius: 5px; margin-top: 20px; }}
    </style>
</head>
<body>

<header>
    <h1>{biz_name}</h1>
    <p>{biz_category} in {biz_city}</p>
</header>

<div class="container">
    <div class="card">
        <p><strong>📍 Address:</strong> {biz_address}</p>
        <p><strong>⏰ Hours:</strong> {biz_hours}</p>
        
        <a href="tel:{biz_phone}" class="call-btn btn">📞 Call Now: {biz_phone}</a>
        <a href="https://www.google.com/maps/search/?api=1&query={biz_name} {biz_address}" class="map-btn btn">🗺️ Get Directions</a>

        <div class="services">
            <h3>Our Services</h3>
            <p>{biz_services}</p>
        </div>
    </div>
    
    <div style="margin-top:20px; text-align:center;">
        <p><small>Proudly serving {biz_city} | Mobile Optimized Business Site</small></p>
    </div>
</div>

</body>
</html>
"""

if st.button("🚀 Build Optimized Website"):
    if biz_name and biz_phone:
        st.subheader("Your SEO-Ready Code")
        st.code(seo_html, language="html")
        st.success("Website generated with Google JSON-LD Schema!")
    else:
        st.error("Please fill in Business Name and Phone.")
