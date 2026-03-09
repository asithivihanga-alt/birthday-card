import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Birthday Surprises for Baby! 💖", page_icon="🎁")

# 2. Enhanced CSS Styling
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
    /* Styling the grid buttons */
    div.stButton > button:first-child {
        background-color: #ff69b4;
        color: white;
        border-radius: 15px;
        border: 2px solid #ff1493;
        font-weight: bold;
        height: 80px;
        width: 100%;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Main Header
st.markdown("""
    <div class="birthday-card">
        <h1>🎈 Happy Birthday, Baby! 🎈</h1>
        <p style='color: #e91e63; font-size: 18px;'>
            I've hidden some surprises for you below.<br>
            Click each button to open your gifts! 🎁
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# 4. The Surprise Buttons Grid
st.subheader("Tap to Open Your Gifts 💌")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎁 Gift #1"):
        st.balloons()
        st.success("A huge hug is waiting for you! 🤗")
        
    if st.button("💖 Gift #3"):
        st.snow()
        st.info("I promise to love you more every single day. ✨")

with col2:
    if st.button("🍰 Gift #2"):
        st.toast("Yum! Virtual cake for my favorite person!", icon='🎂')
        st.warning("We're going to eat so much real cake later! 😋")
        
    if st.button("🌟 Gift #4"):
        st.balloons()
        st.balloons()
        st.error("Surprise! You get 100 extra kisses today! 💋")

st.write("---")

# 5. Interactive "Kiss Counter"
st.subheader("How many kisses do you want? 💋")
kiss_count = st.slider("", 0, 100, 50)
if st.button("Claim Kisses!"):
    st.write(f"### Sending {kiss_count} virtual kisses to you right now! 😘")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    st.write("Done! Check your cheeks! ❤️")

# 6. Final Big Button
if st.button("Tap for the BIGGEST Surprise! 💓"):
    st.balloons()
    st.snow()
    st.markdown("""
        <div style="text-align: center; background-color: white; padding: 20px; border-radius: 15px; border: 5px dashed #ff1493;">
            <h2 style="color: #ff1493;">You are my Forever & Always!</h2>
            <p style="font-size: 20px;">Happy Birthday, Baby. I love you to the moon and back! 🌙✨</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: white; margin-top: 50px;'>Created with ❤️ by Your Girl</p>", unsafe_allow_html=True)
