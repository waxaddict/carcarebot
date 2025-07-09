
import streamlit as st
from utils import load_common_searches, get_placeholder_response

st.set_page_config(page_title="CarCleanBot", layout="centered")

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>🧽 CarCleanBot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload a photo or ask a detailing question.</p>", unsafe_allow_html=True)

# --- SEARCH INPUT ---
query = st.text_input("🔍 What do you need help with?", "")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("📎 Upload an image or video", type=["jpg", "png", "jpeg", "mp4", "mov"])

# --- COMMON SEARCHES ---
st.markdown("#### 🔥 Common Searches:")
common_searches = load_common_searches()
for item in common_searches:
    st.markdown(f"- {item}")

# --- RESPONSE PANEL ---
if query or uploaded_file:
    st.markdown("### 🧠 Analyzing...")
    st.divider()
    response = get_placeholder_response(query)

st.markdown(f"### 🛠 Issue Detected:\n{response['issue']}")
{response['fix']}")
    st.markdown(f"### ⭐️ Top Tip:
{response['tip']}")
    st.markdown("### 🎥 Video Tutorial:")
    st.video(response['video_url'])
    st.markdown("### 🛒 Product Comparison:")
    for product in response['products']:
        st.image(product['image'], width=100)
        st.markdown(f"**{product['name']}** — £{product['price']}")
        st.markdown(f"[Buy Now]({product['buy_url']})")
