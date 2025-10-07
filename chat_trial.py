import requests
import streamlit as st
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(
    page_title="Gabriel Bouferguene | Portfolio",
    page_icon="💼",
    layout="centered"
)
# --- Asset loading ---

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_skills = load_lottieurl("https://lottie.host/a64474df-fa75-4bd3-b569-dd33d94fd380/50a4lT2dow.json")
lottie_contact = load_lottieurl("https://lottie.host/3f5184ee-9d2c-4662-9dc4-7b781791f251/YXQnt26XUs.json")
lottie_wave = load_lottieurl("https://lottie.host/3ccb7dcb-5cef-4b2a-9426-ab83f6c93c1c/Sq615NKdFm.json")



# --- Header ---
st.title("Hello! I'm Gabriel Bouferguene :wave:")
st.subheader("Business Student | Finance | Programmer | Photographer")

st.write("---")

# --- About Me ---
st.header("About Me")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    Hi, I’m **Gabriel Bouferguene**, a business student at the **University of Alberta** specializing in **Finance**.  
    I’m working toward becoming a **financial advisor**, combining analytical precision with an ability to communicate clearly and connect with people.  
    I’m a quick learner who can understand concepts within days of training, and I take pride in delivering work that exceeds expectations.
    """)
with col2:
    st.image("A25A0184_01.png", caption="Gabriel Bouferguene", width=250)  # replace None with your Lottie variable

st.write("---")

# --- Experience & Skills ---
st.header("Experience & Skills")
col3, col4 = st.columns([2, 1])
with col3:
    st.markdown("""
    I’ve had the opportunity to work with the **Faculty of Engineering** under university professors while still in high school, 
    where I provided great results that earned me an open invitation to return.

    Beyond finance, I’ve developed hands-on experience in:
    - **Excel** for data organization and analysis  
    - **Python** for automation and problem-solving  
    - **3D Modeling** for design and visualization  
    - **Photography**, which has become both a creative outlet and a professional service  

    I’m comfortable presenting, working with new teams, and adapting to unfamiliar challenges.  
    I aim to bring that mix of curiosity, professionalism, and reliability to everything I do.  
    
    **If you are interested in hiring me or learning more about my skills, please reach out using the contact information below or fill out the inquiry form.**
    """)
with col4:
    st_lottie(lottie_skills, height=250, key="skills")  # replace None with your Lottie variable

st.write("---")

# --- Contact Information ---
st.header("Contact Me")
col5, col6 = st.columns([2, 1])
with col5:
    st.markdown("""
    Feel free to reach out through any of the following channels:  
    📧 **Email:** [gbouferg@ualberta.ca](mailto:gbouferg@ualberta.ca)  
    📸 **Instagram:** [@skwaka_jr](https://www.instagram.com/skwaka_jr)  
    💼 **LinkedIn:** [Gabriel Bouferguene](https://www.linkedin.com/in/gabriel-bouferguene-779835367)
    """)
with col6:
    st_lottie(lottie_contact, height=220, key="contact")  # replace None with your Lottie variable

st.write("---")

# --- Inquiries Form ---
st.header("Inquiries for Me")

st.markdown("""
If you'd like to reach out directly for anything (resume, interview, photography booking, etc.), please fill out the form below.
""")

contact_form = """
<form action="https://formsubmit.co/gbouferg@ualberta.ca" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width:100%;padding:8px;margin:5px 0;">
     <input type="email" name="email" placeholder="Your Email" required style="width:100%;padding:8px;margin:5px 0;">
     <textarea name="message" placeholder="Your Message" required style="width:100%;padding:8px;margin:5px 0;"></textarea>
     <button type="submit" style="background-color:#0E1117;color:white;padding:10px 20px;border:none;border-radius:5px;">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)