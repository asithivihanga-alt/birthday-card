import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="For My Dilenth 💖", page_icon="🎈")

# 2. Romantic Pink & White Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffd1dc 100%);
    }
    .main-card {
        background: white;
        padding: 25px;
        border-radius: 25px;
        border: 3px solid #ff69b4;
        text-align: center;
        box-shadow: 0px 8px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stButton > button {
        background-color: #ff69b4 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
        height: 50px;
    }
    h1, h2, h3 {
        color: #d02090 !important;
        font-family: 'Comic Sans MS', cursive;
    }
    .message-text {
        color: #8b0000;
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sweet Short Birthday Message
st.markdown(f"""
    <div class="main-card">
        <h1>Happy Birthday, Patiyoo! 🎉</h1>
        <p class="message-text">
            To the man who makes my heart feeling loved everytime... <br>
            I hope your day is as wonderful and handsome as you are! I love u soo much Babee ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

st.balloons()

# 4. The 4 Surprise Gifts
st.subheader("🎁 Open Your 4 Surprises, Dilenth!")
col1, col2 = st.columns(2)

with col1:
    if st.button("Surprise 1 ✨"):
        st.toast("Gift Unlocked!")
        st.info("A coupon for a 'No-Arguments' day! You win every debate today. 😉")
    
    if st.button("Surprise 3 🏍️"):
        st.snow()
        st.success("My biggest wish: That you get your own bike very soon!  🥹")

with col2:
    if st.button("Surprise 2 🍫"):
        st.warning("A virtual box of your favorite treats  (and some sour mangoes!) 🥭")
    
    if st.button("Surprise 4 🎫"):
        st.error("1000 Virtual hugs from mee! ")

st.write("---")

# 5. The Kisses Thing
st.subheader("💋 Send Yourself Kisses")
kiss_type = st.radio("Pick a kiss style:", ["Sweet Forehead Kiss", "Romantic Long Kiss", "Cute Cheek Kiss"])
if st.button("Claim My Kiss! 😘"):
    st.balloons()
    if kiss_type == "Romantic Long Kiss":
        st.write("### 💋💋💋 Sending a deep, long kiss to my favorite guy!")
    else:
        st.write(f"### 💋 A {kiss_type} sent with all my love!")

st.write("---")

# 6. NEW QUESTION STYLE: The Love Slider
st.subheader("❓ A Secret Question for my duduu...")
st.write("Slide the heart to 100% to unlock my answer!")

# The interactive slider
love_percent = st.select_slider(
    "How much do I love you?",
    options=[0, 20, 40, 60, 80, 100],
    value=0
)

if love_percent < 100:
    st.write(f"### Current Love Level: {love_percent}% 💓")
    st.write("Keep sliding... it's much higher than that! 😉")
else:
    st.snow()
    st.markdown("""
        <div style='background: #ffebf0; padding: 15px; border-radius: 15px; border: 2px solid #ff1493; text-align: center;'>
            <h3 style='color: #ff1493; margin: 0;'>🏆 YOU UNLOCKED THE TRUTH!</h3>
            <p style='color: #8b0000; font-size: 18px; margin-top: 10px;'>
                The truth is... I love you to the moon & the back 
                and more than every bike on the road ! 🌌🏍️
            </p>
        </div>
    """, unsafe_allow_html=True)



# 7. Short Love U Ending Message
st.write("---")
st.markdown("""
    <div style='text-align: center; background: white; padding: 20px; border-radius: 15px; border: 2px dashed #ff1493;'>
        <h2 style='color: #ff1493;'>I Love You, Dilenth!</h2>
        <p style='color: #8b0000; font-size: 18px;'>
            Forever & Always, <br>
            <b>Your Favorite Girl (KKK) , Asiii
            XOXO❤️</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.caption("Coded with love in Python 🐍")
