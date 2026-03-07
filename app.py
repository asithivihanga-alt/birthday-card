import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="HBD Dilenth! 💖", page_icon="🏎️")

# 2. Advanced CSS Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
    }
    .birthday-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 25px;
        border: 3px solid #ff69b4;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    h1 {
        color: #d02090 !important;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
    .stButton > button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b) !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        height: 60px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Main Header
st.markdown(f"""
    <div class="birthday-card">
        <h1>🎉 Happy Birthday, Dilenth! 🎉</h1>
        <p style='color: #e91e63; font-size: 20px; font-weight: bold;'>
            My favorite Automotive Engineer 🛠️ & My World 🌎
        </p>
    </div>
    """, unsafe_allow_html=True)

st.balloons()

# 4. Interactive "Unlock My Heart" Quiz
st.subheader("🔐 Dilenth's Special Challenge")
st.write("Answer this correctly to unlock your birthday wish!")

answer = st.radio("What is my favorite thing about you?", 
                 ["Your smile", "Your love for bikes", "Everything about you!"])

if st.button("Unlock Secret Message"):
    if answer == "Everything about you!":
        st.snow()
        st.success("Correct! You know me so well, Dilenth! ❤️")
        st.markdown("""
            <div style="background-color: white; padding: 20px; border-radius: 15px; border: 2px solid #ff1493; text-align: center;">
                <p style="font-size: 18px; color: #8b0000;">
                "Dilenth, you are the most hardworking and amazing person I know. 
                Whether you're working on engines or making me laugh, you're perfect 
                exactly as you are. I love you so much!"
                </p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Close... but you know the real answer is EVERYTHING! Try again. 😘")

st.write("---")

# 5. The Surprise Grid
st.subheader("Tap Your Birthday Gifts 🎁")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎁 Gift #1"):
        st.balloons()
        st.info("A coupon for a long ride on a CT 100! 🏍️💨")
        
    if st.button("💖 Gift #3"):
        st.toast("You're the best boyfriend ever!")
        st.write("### Sending 1000% Love to Dilenth... Done! ✅")

with col2:
    if st.button("🍰 Gift #2"):
        st.warning("Virtual treat: A sour mango/amberella snack! 🥭😋")
        
    if st.button("🌟 Gift #4"):
        st.snow()
        st.error("Surprise! You get a 'Get Out of Trouble Free' card today! 🃏")

st.write("---")

# 6. The Kiss Meter
st.subheader("💋 Dilenth's Kiss Meter")
kisses = st.select_slider("How many kisses do you deserve today?", options=["A few", "Many", "A Million", "Infinite"])
if st.button("Claim Kisses"):
    st.write(f"### Result: {kisses} kisses are coming your way! 😘")
    st.balloons()

# Footer
st.markdown("<p style='text-align: center; color: white; margin-top: 50px;'>Made with ❤️ by Your Favorite Girl</p>", unsafe_allow_html=True)
