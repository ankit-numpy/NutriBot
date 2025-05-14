import streamlit as st

# Page configuration
st.set_page_config(page_title="AI Health Hub", page_icon="🌿", layout="centered")

# App title
st.title("🌿 AI Health Hub")
st.markdown("### Your personalized wellness assistant")

# Sidebar menu with styled options
st.sidebar.markdown("## 🧭 Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["🥗 Meal Plan Generator", "🧘‍♂️ Meal Analyzer"],
    label_visibility="collapsed"  # hides the radio label for cleaner look
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Tips")
st.sidebar.info("Use the sidebar to switch between apps.")

st.sidebar.markdown("---")
st.sidebar.markdown("🔒 *Your data stays on your device*")

# Page routing logic
if page == "🥗 Meal Plan Generator":
   import meal_planner as mp
   mp.plan()
elif page == "🧘‍♂️ Meal Analyzer":
    import app as app
    app.run()
