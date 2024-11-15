import streamlit as st
import random

# Initialize session state
if "username" not in st.session_state:
    st.session_state["username"] = None
if "avatar" not in st.session_state:
    st.session_state["avatar"] = "Default Avatar"
if "preferences" not in st.session_state:
    st.session_state["preferences"] = {}
if "recommendations" not in st.session_state:
    st.session_state["recommendations"] = []

# Generate anonymous username
def generate_username():
    adjectives = ["Calm", "Bright", "Brave", "Gentle", "Mighty"]
    nouns = ["Star", "Wave", "Leaf", "Wind", "Echo"]
    return f"{random.choice(adjectives)}{random.choice(nouns)}"

# Home Page
def home():
    st.title("Welcome to Bondary")
    st.write("Your sanctuary for connection, well-being, and support. Explore resources, connect anonymously, and find your path to well-being.")

# Registration Page
def registration():
    st.subheader("Create Your Anonymous Profile")
    if st.session_state["username"] is None:
        st.session_state["username"] = generate_username()
    st.write(f"Your anonymous username: **{st.session_state['username']}**")
    st.session_state["avatar"] = st.selectbox("Choose your avatar:", ["Default Avatar", "Leaf Avatar", "Star Avatar"])
    if st.button("Complete Registration"):
        st.success("Profile created! Welcome to Bondary.")

# Personalized Form (Mental Health Assessment)
def personalized_form():
    st.subheader("Tell Us About Yourself")
    main_concern = st.selectbox("What is your primary area of focus?", ["General Well-being", "Stress", "Anxiety", "Depression", "Chronic Illness"])
    coping_mechanisms = st.multiselect("How do you typically cope with stress?", ["Exercise", "Talking to friends", "Mindfulness", "Distractions", "Struggle to cope"])
    sleep_quality = st.selectbox("How would you rate your sleep quality?", ["Good", "Average", "Poor"])
    social_connection = st.selectbox("How connected do you feel to others?", ["Very connected", "Somewhat connected", "Not connected"])
    
    st.session_state["preferences"] = {
        "main_concern": main_concern,
        "coping_mechanisms": coping_mechanisms,
        "sleep_quality": sleep_quality,
        "social_connection": social_connection
    }

    if st.button("Get Recommendations"):
        st.session_state["recommendations"] = get_recommendations()
        st.success("Recommendations are ready! Check the Wellness Hub.")

# Generate recommendations based on user input
def get_recommendations():
    preferences = st.session_state["preferences"]
    recommendations = []

    if preferences["main_concern"] == "Depression":
        recommendations.append("Consider scheduling a session with BetterMynd for teletherapy.")
        recommendations.append("Join a mindfulness workshop through the Counseling Center Services.")
    elif preferences["main_concern"] == "Anxiety":
        recommendations.append("Explore guided breathing exercises in the Wellness Hub.")
        recommendations.append("Connect with a peer support group through the Let’s Talk program.")
    elif preferences["main_concern"] == "Chronic Illness":
        recommendations.append("Access resources for managing chronic conditions via ThrivingCampus.")
    elif preferences["main_concern"] == "Stress":
        recommendations.append("Try Kognito’s online training for stress recognition and management.")
    else:
        recommendations.append("Explore general well-being tips and workshops available in the Wellness Hub.")

    return recommendations

# Daily Check-In
def daily_check_in():
    st.subheader("Daily Check-In at Bondary")
    st.write("How are you feeling today? Let us guide you to the right resources.")
    user_response = st.text_area("Share your thoughts or any challenges you're facing:")
    if st.button("Submit"):
        st.success("Thank you for sharing! Your feedback will help tailor your experience.")

# Social Space (Reddit-style chat)
def social_space():
    st.subheader("Social Space")
    st.write("Join anonymous discussions and connect with others.")
    topic = st.text_input("Start a new discussion or ask a question:")
    if st.button("Post"):
        st.write(f"**Anonymous User:** {topic}")

# Wellness Hub
def wellness_hub():
    st.subheader("Your Personalized Wellness Hub")
    for recommendation in st.session_state["recommendations"]:
        st.write(f"- {recommendation}")

# Counseling Center & Resources
def counseling_resources():
    st.subheader("Counseling Center & Mental Health Resources")
    st.write("- **Kognito:** [Interactive training for recognizing distress](bentley.kognito.com)")
    st.write("- **BetterMynd:** [Free online therapy sessions](https://login.bettermynd.com/)")
    st.write("- **Let’s Talk Program:** [Drop-in consultations](https://bentleydownloads.s3.amazonaws.com/about/Let's+Talk+Website+Document.pdf)")
    st.write("- **ThrivingCampus:** [Find off-campus providers](https://bentley.thrivingcampus.com/)")

# Explore Section
def explore():
    st.subheader("Explore Bentley and Beyond")
    st.write("- **Student Organizations:** Join clubs and meet new people")
    st.write("- **Campus Events:** Stay updated on upcoming activities")
    st.write("- **Testimonies:** Read stories from fellow students")
    st.write("- **Restaurants:** Discover the best places to eat near campus")
    st.write("- **Local Shops:** Explore popular shops in Waltham")
    st.write("- **Waltham Map:** Navigate the local area with ease")

# Profile Page
def profile():
    st.subheader("Modify Your Profile")
    st.write(f"Username: {st.session_state['username']}")
    st.session_state["avatar"] = st.selectbox("Change your avatar:", ["Default Avatar", "Leaf Avatar", "Star Avatar"])

# Help Page
def help_page():
    st.subheader("Help & Emergency Contacts")
    st.write("- **911:** For immediate emergencies")
    st.write("- **Bentley University Protocol:** Contact campus safety for urgent support")

# Main Navigation
st.sidebar.title("Bondary Navigation")
page = st.sidebar.radio("Navigate to", ["Home", "Registration", "Personalized Form", "Daily Check-In", "Social Space", "Wellness Hub", "Counseling Resources", "Explore", "Profile", "Help"])

# Page Navigation
if page == "Home":
    home()
elif page == "Registration":
    registration()
elif page == "Personalized Form":
    personalized_form()
elif page == "Daily Check-In":
    daily_check_in()
elif page == "Social Space":
    social_space()
elif page == "Wellness Hub":
    wellness_hub()
elif page == "Counseling Resources":
    counseling_resources()
elif page == "Explore":
    explore()
elif page == "Profile":
    profile()
elif page == "Help":
    help_page()
