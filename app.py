import streamlit as st

# Set page title and icon
st.set_page_config(page_title="For My Special One", page_icon="💖")

# 1. Background styling and heart pattern
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;  /* Soft Pink Background */
        text-align: center;
    }
    h1 {
        color: #ff1493;  /* Deep Pink Color for Birthday Title */
        font-family: 'Comic Sans MS', cursive;
        font-size: 3em;
        text-shadow: 2px 2px 4px #ffb6c1;
    }
    p {
        color: #8b0000;  /* Dark Red color for message */
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        font-weight: bold;
    }
    /* Heart Pattern Overlay */
    body {
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/ea/Love-heart-emoji-pink.svg');
        background-repeat: repeat;
        background-size: 50px;
        opacity: 0.1;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Main Title and Animation
# This triggers balloons automatically when the page loads!
st.balloons() 

st.markdown("<h1>🎉 HAPPY BIRTHDAY, BABY! 💗</h1>", unsafe_allow_html=True)

st.write("---")  # Add a dividing line

# 3. Personalized Message and More Hearts
st.markdown("""
    <p> To the love of my life,</p>
    
    <p> Wishing you the most incredible birthday ever. You make every day brighter and my heart full.</p>
    
    <p> I love you more than words can say. 💕</p>
    """, unsafe_allow_html=True)

# Add some large pink heart emojis explicitly
st.header("💗💖💝💓")

# 4. A sweet, interactive 'surprise' button
if st.button('Click for my biggest birthday wish for you!'):
    st.write("### 🎁 My wish is...")
    st.write("...that all of your dreams come true, and that I get to be by your side for all of them. I can't wait to celebrate you properly! 🥰")
    st.snow()  # Another cute "snowing" animation

# 5. Optional image section (If you want to add a photo of you two)
# Upload a photo to your GitHub repo and uncomment (remove #) the next line
# st.image("our_photo.jpg", caption="Us ❤️")

st.write("---")
st.write("Coded with all my love ❤️")
