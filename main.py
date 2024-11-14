import streamlit as st
import pandas as pd
from datetime import datetime
import openai

# Set up the page configuration
st.set_page_config(page_title="ThriveConnect", layout="wide")

# Initialize user session state
if "avatar" not in st.session_state:
    st.session_state["avatar"] = "Default Avatar"
if "preferences" not in st.session_state:
    st.session_state["preferences"] = {}
if "hub" not in st.session_state:
    st.session_state["hub"] = "General Wellness"

# Home Page
def home():
    st.title("Welcome to ThriveConnect!")
    st.write("""
        **ThriveConnect** is your personalized well-being and community platform.
        Here, you can connect anonymously, explore resources, and receive tailored support.
    """)
    st.image("welcome_image.png", use_column_width=True)

# User Registration with Personalized Hub Recommendation
def user_registration():
    st.subheader("Create Your Profile")
    st.text("Help us personalize your experience with a few questions.")
    user_name = st.text_input("What's your first name?")
    main_concern = st.selectbox(
        "What is your primary area of concern?",
        ["Managing Stress", "Feeling Depressed", "Experiencing Anxiety", "Chronic Illness (e.g., Diabetes)", "General Well-being"]
    )
    additional_preferences = st.multiselect(
        "Select any additional topics you're interested in:",
        ["Mindfulness", "Peer Support", "Physical Health", "Workshops & Events"]
    )
    st.session_state["preferences"] = {
        "name": user_name,
        "main_concern": main_concern,
        "additional_topics": additional_preferences
    }

    # Determine the appropriate hub based on the main concern
    if main_concern == "Feeling Depressed":
        st.session_state["hub"] = "Depression Support Hub"
    elif main_concern == "Experiencing Anxiety":
        st.session_state["hub"] = "Anxiety Management Hub"
    elif main_concern == "Chronic Illness (e.g., Diabetes)":
        st.session_state["hub"] = "Chronic Illness Hub"
    elif main_concern == "Managing Stress":
        st.session_state["hub"] = "Stress Relief Hub"
    else:
        st.session_state["hub"] = "General Wellness Hub"

    if st.button("Submit"):
        st.success(f"Welcome to ThriveConnect, {user_name}! We've personalized your experience based on your preferences.")
        st.session_state["avatar"] = f"Avatar for {user_name}"

# Daily Check-In with Dynamic Hub Routing
def daily_check_in():
    st.subheader("Daily Check-In")
    st.write("How are you feeling today?")
    user_response = st.text_area("Share your thoughts or describe any challenges you're facing:")
    
    if st.button("Submit"):
        if "depress" in user_response.lower():
            st.session_state["hub"] = "Depression Support Hub"
        elif "anxiety" in user_response.lower():
            st.session_state["hub"] = "Anxiety Management Hub"
        elif "stress" in user_response.lower():
            st.session_state["hub"] = "Stress Relief Hub"
        elif "diabetes" in user_response.lower():
            st.session_state["hub"] = "Chronic Illness Hub"
        else:
            st.session_state["hub"] = "General Wellness Hub"
        
        st.success(f"We've directed you to the {st.session_state['hub']} based on your check-in.")

# Wellness Hubs
def wellness_hub():
    hub = st.session_state["hub"]
    st.header(f"Welcome to the {hub}")
    
    if hub == "Depression Support Hub":
        st.write("This hub offers resources for managing depression, including peer stories, expert advice, and guided workshops.")
        st.write("- **Mindfulness Techniques**")
        st.write("- **Peer Support Forum**")
        st.write("- **Counseling Services**")
    elif hub == "Anxiety Management Hub":
        st.write("Explore strategies for handling anxiety, including breathing exercises, expert talks, and community support.")
        st.write("- **Guided Breathing Sessions**")
        st.write("- **Expert Q&A on Anxiety**")
        st.write("- **Upcoming Workshops**")
    elif hub == "Chronic Illness Hub":
        st.write("This hub provides support for managing chronic illnesses like diabetes, with tips, diet plans, and shared experiences.")
        st.write("- **Diet and Lifestyle Tips for Diabetes**")
        st.write("- **Support Group Meetings**")
        st.write("- **Health Monitoring Resources**")
    elif hub == "Stress Relief Hub":
        st.write("Find relief from stress with resources on mindfulness, relaxation techniques, and community activities.")
        st.write("- **Guided Meditation**")
        st.write("- **Stress Management Workshops**")
        st.write("- **Peer Discussion Groups**")
    else:
        st.write("Explore a variety of wellness topics and discover resources tailored to your needs.")
        st.write("- **General Health Tips**")
        st.write("- **Community Events**")
        st.write("- **Campus Resources**")

# Main Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Registration", "Daily Check-In", "Wellness Hub"])

if page == "Home":
    home()
elif page == "Registration":
    user_registration()
elif page == "Daily Check-In":
    daily_check_in()
elif page == "Wellness Hub":
    wellness_hub()
