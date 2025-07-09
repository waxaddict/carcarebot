
import streamlit as st
from utils import load_common_searches, get_placeholder_response
import time

# --- Page Setup ---
st.set_page_config(page_title="CarCleanBot", layout="centered")

# --- Init State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- ROUTING ---
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center;'>🧽 CarCleanBot</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Upload a photo or ask a detailing question.</p>", unsafe_allow_html=True)

    query = st.text_input("🔍 What do you need help with?", "")
    uploaded_file = st.file_uploader("📎 Upload an image or video", type=["jpg", "png", "jpeg", "mp4", "mov"])

    st.markdown("#### 🔥 Common Searches:")
    for item in load_common_searches():
        st.markdown(f"- {item}")

   if query or uploaded_file:
    if st.button("🔍 Analyze"):
        st.session_state.query = query
        st.session_state.uploaded_file = uploaded_file
        st.session_state.page = "loading"
        st.experimental_rerun()
        
elif st.session_state.page == "loading":
    st.markdown("<h1 style='text-align: center;'>🔄 Analyzing...</h1>", unsafe_allow_html=True)
    with st.spinner("Thinking..."):
        time.sleep(2)
    st.session_state.page = "results"
    st.experimental_rerun()

elif st.session_state.page == "results":
    response = get_placeholder_response(st.session_state.query)

    st.markdown(f"### 🛠 Issue Detected:\n{response['issue']}")
    st.markdown(f"### 🧼 Fix:\n{response['fix']}")
    st.markdown(f"### ⭐️ Top Tip:\n{response['tip']}")

    st.markdown("### 🎥 Video Tutorial:")
    st.video(response['video_url'])

    st.markdown("### 🛒 Product Comparison:")
    for product in response['products']:
        st.image(product['image'], width=100)
        st.markdown(f"**{product['name']}** — £{product['price']}")
        st.markdown(f"[Buy Now]({product['buy_url']})")
