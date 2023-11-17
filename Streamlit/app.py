# streamlit_app/app.py

import streamlit as st
from views import surveys, dashboard, reports  # Import your different views

def main():
    st.markdown(
        "<h1 style='text-align: center; color: #FFFFFF; padding: 10px;'>Sirdar Governance Diagnostic</h1>",
        unsafe_allow_html=True
    )

    # Create a sidebar navigation menu
    selected_page = st.sidebar.selectbox("Navigator", ["Executive Surevy", "Board Composition Dashboard", "Governace Diagnostic Report"])


    # Display the selected page
    if selected_page == "Executive Surevy":
        surveys.show()
    elif selected_page == "Board Composition Dashboard":
        dashboard.show()
    elif selected_page == "Governace Diagnostic Report":
        reports.show()

if __name__ == "__main__":
    main()
