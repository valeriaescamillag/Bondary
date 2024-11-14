import streamlit as st

# App Title
st.title("HealthUniverse - Bentley's Holistic Mental Health App")

# Sidebar for Navigation
menu = ["Home", "Daily Assessment", "Anonymous Community", "Recommendations", "Events & Resources"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Section
if choice == "Home":
    st.subheader("Welcome to HealthUniverse!")
    st.write("Your personalized wellness companion at Bentley. Take a quick assessment to see resources tailored to your needs.")

# Daily Assessment Section
elif choice == "Daily Assessment":
    st.subheader("Daily Mental Health Assessment")
    st.write("Answer these quick questions to get personalized wellness resources.")
    
    stress = st.radio("Do you feel stressed today?", ("Yes", "No"))
    anxiety = st.radio("Are you experiencing anxiety or feeling overwhelmed?", ("Yes", "No"))
    isolation = st.radio("Do you feel isolated or disconnected?", ("Yes", "No"))
    low_energy = st.radio("Do you feel low energy or trouble focusing?", ("Yes", "No"))
    need_sharing = st.radio("Do you want to share experiences or seek advice from peers?", ("Yes", "No"))
    personal_support = st.radio("Do you need confidential support?", ("Yes", "No"))
    events_interest = st.radio("Would you like to learn about upcoming events for wellness?", ("Yes", "No"))

    # Based on responses, provide a summary
    if st.button("Get Recommendations"):
        st.subheader("Your Recommendations")
        if stress == "Yes":
            st.write("Visit Bentley’s Counseling Services for stress management resources.")
        if anxiety == "Yes":
            st.write("Explore upcoming talks and support groups focusing on anxiety relief.")
        if isolation == "Yes":
            st.write("Join a social wellness activity or peer support circle.")
        # More recommendations based on other answers...

# Anonymous Community Section (always accessible)
elif choice == "Anonymous Community":
    st.subheader("Community Support")
    st.write("Share experiences, ask questions, and support each other in an anonymous environment.")
    # Placeholder for community input feature (would need a database integration for full functionality)

# Recommendations Section
elif choice == "Recommendations":
    st.subheader("Personalized Recommendations")
    st.write("Based on your assessment, here are today’s resources.")
    # Display recommendations from the assessment if they took it

# Events & Resources Section
elif choice == "Events & Resources":
    st.subheader("Events & Resources")
    st.write("Explore Bentley’s counseling services, upcoming talks, yoga classes, and more.")
    # Static list or dynamically generated list of events

# Footer
st.write("Developed for the CHB Case Competition at Bentley University")
