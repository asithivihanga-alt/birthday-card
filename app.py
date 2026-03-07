import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Dilenth's Birthday Magic", page_icon="✨")

# 2. Romantic & Cute CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
    }
    .main-card {
        background: white;
        padding: 25px;
        border-radius: 30px;
        border: 2px solid #f06292;
        text-align: center;
        box-shadow: 0px 10px 25px rgba(240, 98, 146, 0.3);
        margin-bottom: 20px;
    }
    .stButton > button {
        background: #f06292 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: bold !important;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background: #e91e63 !important;
        transform: scale(1.05);
    }
    h1, h2, h3 {
        color: #ad1457 !important;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Main Header
st.markdown(f"""
    <div class="main-card">
        <h1>Happy Birthday, Dilenth! 🎉</h1>
        <p style='font-size: 18px; color: #ad1457;'>My favorite person, my best friend, and my future rider. 🏍️</p>
    </div>
    """, unsafe_allow_html=True)

st.balloons()

# 4. Surprise #1: The "Wish for the Bike" (Romantic Feature)
st.markdown("### 🕊️ My Deepest Wish for You")
with st.expander("Click to read my heart's wish..."):
    st.write("Dilenth, I see how your eyes light up when you see a beautiful machine. 🛠️")
    st.write("My biggest birthday wish for you is that **you get your own bike very, very soon.**")
    st.write("I can already imagine us riding together, feeling the wind, with me holding you tight. I believe in you and your dreams! 🥹💖")
    if st.button("Send a Virtual Prayer for the Bike 🏍️"):
        st.snow()
        st.success("Prayer sent to the universe! It’s coming soon, Dilenth! ✨")

st.write("---")

# 5. Surprise #2: Digital Flower Bouquet (Cute Feature)
st.markdown("### 🌷 Pick a Flower for a Surprise")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🌹"):
        st.write("I love you more than words can say.")
with col2:
    if st.button("🌻"):
        st.write("You are the sunshine in my life.")
with col3:
    if st.button("🌸"):
        st.write("You are so handsome and kind.")

# 6. Surprise #3: The "Love Note" Generator
st.markdown("### 💌 Random Love Note")
notes = [
    "Dilenth, you're the best thing that ever happened to me. ❤️",
    "I'm so proud of the man you are becoming. 👨‍🔬",
    "Every day with you feels like a beautiful dream. ✨",
    "I can't wait to see you on your new bike! 🏍️💨",
    "You have the most beautiful soul I've ever known. 💎"
]
if st.button("Generate a Love Note"):
    note = random.choice(notes)
    st.markdown(f"<div style='background:
