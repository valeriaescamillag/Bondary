import streamlit as st
import pandas as pd
from datetime import datetime
import openai

# Set up the page configuration
st.set_page_config(page_title="Bondary", layout="wide")

# Initialize user session state
if "avatar" not in st.session_state:
    st.session_state["avatar"] = "Default Avatar"
if "preferences" not in st.session_state:
    st.session_state["preferences"] = {}
if "hub" not in st.session_state:
    st.session_state["hub"] = "General Wellness"

# Home Page
def home():
    st.title("Welcome to Bondary!")
    st.write("""
        **Bondary** is your sanctuary for connection and well-being. Here, you can interact anonymously, explore resources, and receive personalized support.
    """)
    st.image("bondary_welcome.png", use_column_width=True)

# User Registration with Personalized Hub Recommendation
def user_registration():
    st.subheader("Create Your Bondary Profile")
    st.text("Help us personalize your experience with a few quick questions.")
    user_name = st.text_input("What's your first name?")
    main_concern = st.selectbox(
        "What is your primary area of focus?",
        ["Managing Stress", "Feeling Depressed", "Experiencing Anxiety", "Living with a Chronic Illness (e.g., Diabetes)", "General Well-being"]
    )
    additional_preferences = st.multiselect(
        "Select additional topics you're interested in:",
        ["Mindfulness", "Community Support", "Physical Health", "Workshops & Events"]
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
    elif main_concern == "Living with a Chronic Illness (e.g., Diabetes)":
        st.session_state["hub"] = "Chronic Illness Hub"
    elif main_concern == "Managing Stress":
        st.session_state["hub"] = "Stress Relief Hub"
    else:
        st.session_state["hub"] = "General Wellness Hub"

    if st.button("Submit"):
        st.success(f"Welcome to Bondary, {user_name}! Your experience has been personalized based on your preferences.")
        st.session_state["avatar"] = f"Avatar for {user_name}"

# Daily Check-In with Dynamic Hub Routing
def daily_check_in():
    st.subheader("Daily Check-In at Bondary")
    st.write("How are you feeling today? Let us guide you to the right resources.")
    user_response = st.text_area("Share your thoughts or any challenges you're facing:")
    
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
        
        st.success(f"You've been directed to the {st.session_state['hub']} based on your check-in.")

# Wellness Hubs
def wellness_hub():
    hub = st.session_state["hub"]
    st.header(f"Welcome to the {hub}")
    
    if hub == "Depression Support Hub":
        st.write("This hub offers resources for managing depression, including peer stories, expert advice, and guided workshops.")
        st.write("- **Mindfulness Techniques**")
        st.write("- **Peer Support Forum**")
        st.write("- **Access to Counseling Services**")
    elif hub == "Anxiety Management Hub":
        st.write("Explore strategies for handling anxiety, including breathing exercises, expert talks, and supportive community interactions.")
        st.write("- **Guided Breathing Sessions**")
        st.write("- **Expert Q&A on Anxiety**")
        st.write("- **Upcoming Anxiety Workshops**")
    elif hub == "Chronic Illness Hub":
        st.write("This hub provides support for managing chronic conditions like diabetes, with tips, diet plans, and shared experiences.")
        st.write("- **Diet and Lifestyle Tips**")
        st.write("- **Support Group Meetings**")
        st.write("- **Health Monitoring Resources**")
    elif hub == "Stress Relief Hub":
        st.write("Find relief from stress with resources on mindfulness, relaxation techniques, and community activities.")
        st.write("- **Guided Meditation Sessions**")
        st.write("- **Stress Management Workshops**")
        st.write("- **Peer Discussion Groups**")
    else:
        st.write("Explore a variety of wellness topics and discover resources tailored to your needs.")
        st.write("- **General Health Tips**")
        st.write("- **Community Events**")
        st.write("- **Campus Resources and Services**")

# Explore Section
def explore_section():
    st.subheader("Explore Bentley and Beyond with Bondary")
    st.write("Discover the best spots for dining, shopping, and activities near campus.")
    recommendations = ["Top Restaurants", "Local Shops", "Upcoming Campus Events"]
    selected_recommendation = st.selectbox("What would you like to explore?", recommendations)
    
    if selected_recommendation == "Top Restaurants":
        st.write("Student favorites near campus:")
        st.write("- **The Friendly Toast**")
        st.write("- **Pressed Café**")
        st.write("- **True North Café**")
    elif selected_recommendation == "Local Shops":
        st.write("Popular shops nearby:")
        st.write("- **Barnes & Noble**")
        st.write("- **The Mall at Chestnut Hill**")
    else:
        st.write("Upcoming events on campus include the Wellness Fair and Student Market Day.")

# User Profile
def user_profile():
    st.subheader("Your Bondary Profile")
    st.write(f"Avatar: {st.session_state['avatar']}")
    st.write("Your Preferences:")
    st.write(st.session_state["preferences"])

# Main Navigation
st.sidebar.title("Bondary Navigation")
page = st.sidebar.radio("Navigate to", ["Home", "Registration", "Daily Check-In", "Wellness Hub", "Explore", "Profile"])

if page == "Home":
    home()
elif page == "Registration":
    user_registration()
elif page == "Daily Check-In":
    daily_check_in()
elif page == "Wellness Hub":
    wellness_hub()
elif page == "Explore":
    explore_section()
elif page == "Profile":
    user_profile()
