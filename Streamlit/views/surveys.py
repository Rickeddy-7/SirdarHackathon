# streamlit_app/views/home.py

import streamlit as st

# List of enterprise survey questions
enterprise_questions = [
    "There is an up-to-date board charter in place appropriate to the life-stage of the organisation and its current structure.",
    "There is an up-to-date delegation of authority policy in place, which is effectively monitored.",
    "The managing director's report effectively communicates status, identifies issues, and clearly indicates a linkage to the business plan.",
    "Board packs are structured and used effectively to guide the board to make decisions and hold those authorised to make decisions accountable.",
    "The board calendar is up-to-date and relevant for the timing requirements of the enterprise and its strategic focus.",
    "All board meeting dates (and committee dates if applicable) for the year are scheduled in directors' diaries and align with the board calendar.",
    "The organisation has an up-to-date strategy (identifying the company's purpose and medium-term vision) and a business plan (identifying the necessary next steps) that guides its focus and direction.",
    "The board ensures a strategic focus in every board meeting to ensure that board papers relevant to the theme agreed upon for that meeting are prepared and that necessary key strategic issues are addressed proactively.",
    "There is clarity regarding the organisation's culture, values, and beliefs.",
    "The culture and values of the organisation are demonstrated by the board, setting the appropriate tone for the rest of the organisation to follow.",
    "The board's conduct is characterised by trust, respect, candour, professionalism, accountability, diligence and commitment.",
    "The organisation has developed a culture of accountability for performance.",
    "The board committees (where appropriate) have approved terms of reference.",
    "The board committees (where appropriate) have an agreed work plan for the year and are making good progress against that plan."
]

def show():
    # Title
    st.markdown(
        "<h2 style='text-align: center; color: #FFFFFF; padding: 30px;'>Executive Surveys</h2>",
        unsafe_allow_html=True
    )

    # Buttons in the same row
    button_col1, button_col2, button_col3, button_col4 = st.columns(4)

    # Initialize session state if not exists
    if "survey_step" not in st.session_state:
        st.session_state.survey_step = 1

    if button_col1.button("Enterprise Purpose"):
        st.session_state.survey_step = 1

    if button_col2.button("Accountability for Performance"):
        st.session_state.survey_step = 2

    if button_col3.button("Sustainability"):
        st.session_state.survey_step = 3

    if button_col4.button("Conformance"):
        st.session_state.survey_step = 4

    # Survey form based on the selected step
    if st.session_state.survey_step == 1:
        survey_form("Enterprise Purpose", enterprise_questions)


def survey_form(survey_name, questions):
    st.header(f"{survey_name} Questions")

    # Initialize responses dictionary
    responses = {}

    # Survey questions
    with st.form(f"{survey_name.lower()}_form"):
        st.write(f"Welcome to {survey_name}! Please provide your feedback.")

        # Loop through each question and collect responses
        for i, question in enumerate(questions, start=1):
            st.header(f"Question {i}:")
            response = st.slider(question, 0, 4)
            responses[f"Question {i}"] = response

        # Submit button
        submitted = st.form_submit_button("Submit Survey")

    # Process survey responses
    if submitted:
        st.success(f"{survey_name} submitted successfully!")

        # Display responses
        for question, response in responses.items():
            st.write(f"{question}: {response}")
