import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Happy Birthday, Baby!", page_icon="💖")

# 2. The "Magic" CSS Styling
st.markdown("""
    <style>
    /* Full page background */
    .stApp {
        background: linear-gradient(180deg, #ffafbd 0%, #ffc3a0 100%);
    }

    /* The Birthday Card Container */
    .birthday-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 25px;
        border: 3px solid #ff69b4;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    /* Floating Heart Animation */
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }

    .heart-icon {
        font-size: 50px;
        animation: floating 3s ease-in-out infinite;
        display: inline-block;
    }

    h1 {
        color: #d02090 !important;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        font-size: 35px;
    }

    .love-text {
        color: #e91e63 !important;
        font-size: 20px;
        font-family: 'Georgia', serif;
        line-height: 1.6;
    }

    /* Styling the button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%);
        color: white;
        border-radius: 50px;
        border: none;
        font-weight: bold;
        padding: 10px 25px;
        box-shadow: 0px 4px 15px rgba(255, 65, 108, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Floating Hearts & Title
st.markdown('<div style="text-align: center;"><span class="heart-icon">💖</span></div>', unsafe_allow_html=True)

# Wrap everything in a card
st.markdown("""
    <div class="birthday-card">
        <h1>🎈 Happy Birthday, Baby! 🎈</h1>
        <p class="love-text">
            To the one who holds my heart... <br>
            You are my favorite adventure and my greatest love. <br>
            I'm so lucky to have you in my life! <br><br>
            <b>I LOVE YOU! 💗✨</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Spacer

# 4. Interactive Elements
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button('Click for a Birthday Surprise! 🎁'):
        st.balloons()
        st.snow()
        st.markdown("""
            <div style="text-align: center; color: #ff1493; font-weight: bold; font-size: 18px;">
                Sending you 1,000,000 kisses! 💋<br>
                🎂🍰🧁🍭🌷
            </div>
            """, unsafe_allow_html=True)

# 5. Little Footer
st.markdown("<p style='text-align: center; color: white; font-size: 12px; margin-top: 50px;'>Made with ❤️ by Your Girl</p>", unsafe_allow_html=True)
