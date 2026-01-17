import streamlit as st

# --- WEBSITE GENERATOR TAB ---
st.header("🌐 Website Builder Engine")
st.write("Fill this out to generate a Google-compliant website code.")

shop_name = st.text_input("Shop Name", key="web_name")
shop_address = st.text_input("Full Address", key="web_addr")
shop_phone = st.text_input("Phone Number", key="web_phone")

# The Template Logic
website_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{shop_name}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: sans-serif; text-align: center; padding: 50px; background: #f4f4f4; }}
        .card {{ background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
        .btn {{ background: #4285F4; color: white; padding: 15px 25px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{shop_name}</h1>
        <p>📍 {shop_address}</p>
        <p>📞 {shop_phone}</p>
        <a href="tel:{shop_phone}" class="btn">Call Now</a>
        <a href="https://www.google.com/maps/search/?api=1&query={shop_name}" class="btn" style="background:#34A853;">Get Directions</a>
    </div>
</body>
</html>
"""

if st.button("Generate Website Code"):
    st.code(website_code, language="html")
    st.success("Copy the code above and create an 'index.html' file in your GitHub repo!")
