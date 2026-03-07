import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Dilenth's Magical Day", page_icon="✨")

# 2. Cute Custom Styling
st.markdown("""
    <style>
    .stApp {
        background: #fff5f7;
    }
    .gift-box {
        background: white;
        padding: 25px;
        border-radius: 30px;
        border: 2px dashed #ffb6c1;
        text-align: center;
        box-shadow: 10px 10px 0px #ffb6c1;
        margin-bottom: 25px;
    }
    .stButton > button {
        background-color: #ff85a2 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-family: 'Comic Sans MS', cursive;
    }
    h1, h2, h3 {
        color: #ff4d6d !important;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The "Love Battery" Feature
st.markdown("<h1 style='text-align: center;'>🔋 Dilenth's Love Battery</h1>", unsafe_allow_html=True)
st.write("Click the button to charge your heart for the day!")

if 'charge' not in st.session_state:
    st.session_state.charge = 0

if st.button("Tap to Charge ❤️"):
    if st.session_state.charge < 100:
        st.session_state.charge += 20
    else:
        st.balloons()
        st.success("Battery Full! You are 100% Loved by Me!")

st.progress(st.session_state.charge / 100)
st.write(f"Current Charge: {st.session_state.charge}%")

st.write("---")

# 4. Gift #1: The Virtual Star
st.markdown("""
    <div class="gift-box">
        <h3>⭐ A Star for Dilenth</h3>
        <p>I went to the digital sky and named a star after you.</p>
        <p style="font-size: 40px;">✨ <b>Dilenth-2026</b> ✨</p>
        <p>It will shine as long as I love you (which is forever!)</p>
    </div>
    """, unsafe_allow_html=True)

# 5. Gift #2: The "Mood Matcher"
st.markdown("### 🌈 How are you feeling, Dilenth?")
mood = st.selectbox("Pick your current mood:", ["Tired", "Happy", "Hungry", "Missing You"])

if st.button("Get your Birthday Prescription"):
    if mood == "Tired":
        st.write("🛋️ **Prescription:** 1-hour nap + a forehead kiss from me later.")
    elif mood == "Happy":
        st.write("💃 **Prescription:** Keep that smile on! Let's go for a ride on the CT 100.")
    elif mood == "Hungry":
        st.write("🥭 **Prescription:** I'm bringing you some sour amberella with chili and salt!")
    elif mood == "Missing You":
        st.write("📞 **Prescription:** Call me right now for a 10-minute 'I love you' session.")

st.write("---")

# 6. Gift #3: The "Future Adventure" Scratch Card
st.markdown("### 🎫 Virtual Scratch Card")
st.write("Click below to 'scratch' and see your surprise prize!")

if st.button("Scratch Here! ✨"):
    prizes = [
        "A 5-minute back rub 💆‍♂️",
        "A handwritten love letter 📝",
        "Your favorite dessert tonight 🍰",
        "I'll wash your bike for you! 🏍️",
        "A big tight hug for 60 seconds 🫂"
    ]
    prize = random.choice(prizes)
    st.snow()
    st.markdown(f"""
        <div style="background: #ff4d6d; color: white; padding: 20px; border-radius: 15px;">
            <h2 style="color: white !important;">YOU WON:</h2>
            <p style="font-size: 24px;">{prize}</p>
        </div>
    """, unsafe_allow_html=True)

# 7. Final Birthday Wish
st.write("---")
st.markdown(f"""
    <div style='text-align: center;'>
        <p>Happy Birthday, my favorite Engineer. <br> 
        I hope these little digital gifts made you smile today, Dilenth!</p>
        <p style='font-size: 30px;'>🎂🎈🍰</p>
    </div>
""", unsafe_allow_html=True)
