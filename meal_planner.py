import streamlit as st
import google.generativeai as genai
import os

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configure page
st.set_page_config(page_title="NutriFit App", page_icon=":apple:", initial_sidebar_state="collapsed")

# Page header
st.title("🍎 AI-Powered Meal Plan Generator")
st.markdown("### Get customized nutrition plans powered by Gemini AI")

# User input section (same as previous version)
with st.form("user_inputs"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=12, max_value=100, step=1)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    col3, col4 = st.columns(2)
    with col3:
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, step=0.5)
    with col4:
        height = st.number_input("Height (cm)", min_value=100, max_value=250, step=1)
    
    health_goal = st.selectbox(
        "Primary Health Goal",
        ["Weight Loss", "Muscle Gain", "Maintain Weight", "Improve Fitness", "Manage Medical Condition"]
    )
    
    medical_conditions = st.multiselect(
        "Any Medical Conditions?",
        ["Diabetes", "Hypertension", "PCOS", "Celiac Disease", "Cholesterol", "None"]
    )
    
    st.subheader("Fitness Routine")
    workout_frequency = st.slider("Workout days per week", 0, 7, 3)
    workout_intensity = st.selectbox(
        "Workout Intensity",
        ["Sedentary", "Light", "Moderate", "Intense", "Athlete"]
    )
    
    st.subheader("Dietary Preferences")
    diet_type = st.selectbox(
        "Diet Type",
        ["No Restrictions", "Vegetarian", "Vegan", "Keto", "Low-Carb", "Paleo"]
    )
    disliked_foods = st.text_input("Foods you dislike (comma-separated)")
    preferred_cuisines = st.multiselect(
        "Preferred Cuisines",
        ["Mediterranean", "Asian", "Italian", "Mexican", "American", "Middle Eastern"]
    )
    
    submitted = st.form_submit_button("Generate Meal Plan")

# Generate meal plan with Google AI
def generate_meal_plan(inputs):
    # model = genai.GenerativeModel('gemini-pro')
    model=genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""
    **Act as a professional nutritionist** and generate a personalized 7-day meal plan based on:
    - Age: {inputs['age']}
    - Gender: {inputs['gender']}
    - Weight: {inputs['weight']}kg
    - Height: {inputs['height']}cm
    - Health Goal: {inputs['health_goal']}
    - Medical Conditions: {', '.join(inputs['medical_conditions']) if inputs['medical_conditions'] else 'None'}
    - Workout: {inputs['workout_frequency']} days/week ({inputs['workout_intensity']})
    - Diet: {inputs['diet_type']}
    - Dislikes: {inputs['disliked_foods'] or 'None'}
    - Cuisines: {', '.join(inputs['preferred_cuisines']) if inputs['preferred_cuisines'] else 'Any'}

    **Include:**
    1. Daily meals with recipes and cooking instructions
    2. Nutritional values (calories, macros)
    3. Condition-specific adaptations
    4. Grocery shopping list
    5. Hydration guidelines
    6. Post-workout meals
    7. Metric measurements
    8. Allergy alternatives

    **Format:**
    - Use markdown with emojis
    - Clear daily sections
    - Highlight key nutritional tips
    - Bold important recommendations
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating meal plan: {str(e)}")
        return None

# Display results
def run():
    st.set_page_config(page_title="AI Meal Planner", page_icon="🥗")
    st.title("🍎 AI-Powered Meal Plan Generator")
    st.markdown("### Get customized nutrition plans powered by Gemini AI")

    with st.form("user_inputs"):
        # All input UI components...
        # ...
        submitted = st.form_submit_button("Generate Meal Plan")

    if submitted:
        user_inputs = {
            "age": age, "gender": gender, "weight": weight, "height": height,
            "health_goal": health_goal, "medical_conditions": medical_conditions,
            "workout_frequency": workout_frequency, "workout_intensity": workout_intensity,
            "diet_type": diet_type, "disliked_foods": disliked_foods, "preferred_cuisines": preferred_cuisines
        }

        with st.spinner("🧠 Analyzing your profile with Gemini AI..."):
            meal_plan = generate_meal_plan(user_inputs)

        if meal_plan:
            st.success("🎉 Your AI-Generated Meal Plan")
            st.markdown("---")
            st.markdown(meal_plan)
            st.download_button("Download Meal Plan", data=meal_plan, file_name="personalized_meal_plan.md", mime="text/markdown")
        else:
            st.error("Failed to generate meal plan. Please try again.")

    with st.sidebar:
        st.markdown("## 🚀 How It Works")
        st.markdown("1. Enter your health profile\n2. Specify preferences\n3. Get AI-generated plan\n4. Download & implement!")
        st.markdown("---")
        st.markdown("**Key Features:**")
        st.markdown("- 🧬 DNA-inspired nutrition\n- 🏥 Medical condition support\n- 🛒 Shopping list\n- 📱 Mobile-friendly")
        st.markdown("---")
        st.warning("Disclaimer: Consult a healthcare professional before making dietary changes.")