import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="For My Dilenth 💖", page_icon="🏍️")

# 2. Romantic Aesthetic CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    .romantic-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #d02090;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .wish-text {
        font-family: 'Georgia', serif;
        color: #8b0000;
        font-size: 20px;
        font-style: italic;
        line-height: 1.6;
    }
    h1 {
        color: #d02090 !important;
        font-family: 'Brush Script MT', cursive;
        font-size: 45px;
    }
    .stButton > button {
        background: #d02090 !important;
        color: white !important;
        border-radius: 25px !important;
        width: 100%;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Main Birthday Message
st.markdown(f"""
    <div class="romantic-box">
        <h1>Happy Birthday, Dilenth...</h1>
        <p class="wish-text">
            To the man who drives my heart crazy. <br>
            You aren't just my boyfriend; you are my home. <br>
            Today is all about you, my love.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.balloons()

# 4. The "Bike Wish" Feature (The Deeply Personal Part)
st.markdown("### 🕊️ My Special Prayer for You")
with st.container():
    st.write("Dilenth, I know how much you love the road and the feel of a machine...")
    
    if st.button("Open My Heart's Wish for You 💌"):
        st.snow()
        st.markdown(f"""
            <div style="background: white; padding: 25px; border-radius: 15px; border-left: 5px solid #ff1493;">
                <h3 style="color: #ff1493;">My Birthday Wish... 🏍️✨</h3>
                <p style="color: #444; font-size: 18px;">
                    "Dilenth, I see how hard you work and how much passion you have for engineering. 
                    My biggest wish for you this year is that <b>you get your own bike very soon!</b> <br><br>
                    I can't wait to see the look on your face when you finally hold those keys. 
                    I'll be right there behind you, holding on tight, as we ride into our future together. 🥹💖"
                </p>
            </div>
            """, unsafe_allow_html=True)

st.write("---")

# 5. The "Our Future" Journey Map
st.subheader("🗺️ Our Journey Together")
st.write("Click the milestones to see our path!")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("The Past 🕰️"):
        st.info("Every memory we've made is a treasure I keep in my heart.")
with col2:
    if st.button("The Present 💝"):
        st.success("Celebrating YOU today is the best gift I could ever have.")
with col3:
    if st.button("The Future 🏍️"):
        st.warning("Soon, it will be just you, me, and your new bike on the open road.")

# 6. Romantic "Touch My Heart" Interaction
st.write("---")
st.markdown("<p style='text-align: center;'>Hold this button to send a thousand 'I Love You's</p>", unsafe_allow_html=True)
if st.button("❤️ Click
