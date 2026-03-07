import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Kisses for Dilenth 💋", page_icon="😘")

# 2. Romantic & Kiss-Themed CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffc1cc 0%, #ff99aa 100%);
    }
    .main-card {
        background: white;
        padding: 25px;
        border-radius: 30px;
        border: 3px solid #ff4d6d;
        text-align: center;
        box-shadow: 0px 10px 25px rgba(255, 77, 109, 0.4);
        margin-bottom: 20px;
    }
    .stButton > button {
        background: #ff4d6d !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 18px !important;
        height: 50px;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background: #ff0033 !important;
        transform: scale(1.1);
    }
    h1, h2, h3 {
        color: #c9184a !important;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Main Header
st.markdown(f"""
    <div class="main-card">
        <h1>Happy Birthday, Dilenth! 🎂</h1>
        <p style='font-size: 18px; color: #ff4d6d;'>Sending you a million virtual kisses today! 💋💋💋</p>
    </div>
    """, unsafe_allow_html=True)

st.balloons()

# 4. NEW FEATURE: The Kiss Counter
st.markdown("### 💋 The Birthday Kiss Meter")
st.write("How many kisses do you want right now, Dilenth?")
kiss_num = st.select_slider("", options=[10, 50, 100, "Infinite"])

if st.button(f"Claim {kiss_num} Kisses! 😘"):
    st.snow() # This creates the falling heart/star effect
    if kiss_num == "Infinite":
        st.write("### ♾️ Sending you endless kisses forever and ever!")
    else:
        st.write(f"### 💋 {kiss_num} Kisses sent to your cheeks!")
    st.balloons()

st.write("---")

# 5. The "Bike Wish" (Keep this romantic part!)
st.markdown("### 🏍️ My Heart's Wish")
with st.expander("Click to see your gift..."):
    st.markdown("""
        <div style='text-align: center; font-style: italic; color: #8b0000;'>
            "Dilenth, I wish for you to get your dream bike very soon. 
            I can't wait for our first ride together! I'll be holding you tight the whole way." 🥹💖
        </div>
    """, unsafe_allow_html=True)

# 6. Surprise: The "Kiss Button" Grid
st.markdown("### 🎁 Tap for a Surprise Kiss")
col1, col2 = st.columns(2)
with col1:
    if st.button("Forehead Kiss 😚"):
        st.info("A kiss for my hardworking Engineer. I'm so proud of you!")
    if st.button("Hand Kiss 🤝"):
        st.success("A kiss for the gentleman who treats me like a queen.")
with col2:
    if st.button("Cheek Kiss 😊"):
        st.warning("A cute kiss just because you make me smile, Dilenth!")
    if st.button("The BIG One 💋"):
        st.error("A long, romantic birthday kiss! I love you!")

st.write("---")

# 7. Final Secret Surprise
if st.button("Final Birthday Surprise! ✨"):
    st.balloons()
    st.snow()
    st.markdown("""
        <div style='text-align: center;'>
            <h2 style='color: #ff4d6d;'>I Love You, Dilenth!</h2>
            <p style='font-size: 20px;'>You + Me + Your New Bike = My Perfect Dream. 🏍️👩‍❤️‍👨</p>
            <p style='font-size: 40px;'>💋💋💋💋💋</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #ff4d6d; font-size: 14px; margin-top: 50px;'>Made with all my kisses ❤️ for Dilenth</p>", unsafe_allow_html=True)
