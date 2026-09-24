import streamlit as st

def display_investment_thesis_form():
    st.header("Define Your Investment Thesis")
    
    fund_name = st.text_input("Fund Name")
    preferred_geographies = st.text_input("Preferred Geographies (comma-separated)")
    preferred_sectors = st.text_input("Preferred Industries/Sectors (comma-separated)")
    excluded_sectors = st.text_input("Excluded Sectors (comma-separated)")
    preferred_stage = st.selectbox("Preferred Investment Stage", ["Seed", "Series A", "Series B", "Series C"])
    typical_investment = st.number_input("Typical Investment Amount (in ₹)", min_value=0)
    minimum_revenue = st.number_input("Minimum Revenue (in ₹)", min_value=0)
    preferred_revenue_model = st.text_input("Preferred Revenue Model")
    growth_expectations = st.text_input("Growth Expectations")
    preferred_customer_type = st.text_input("Preferred Customer Type")
    market_characteristics = st.text_input("Market Characteristics")
    business_model_preferences = st.text_input("Business Model Preferences")
    founder_team_preferences = st.text_input("Founder/Team Preferences")
    other_criteria = st.text_input("Other Investment Criteria")

    if st.button("Save Thesis"):
        thesis = {
            "geography": preferred_geographies.split(","),
            "sectors": preferred_sectors.split(","),
            "excluded_sectors": excluded_sectors.split(","),
            "stage": preferred_stage,
            "ticket_size": typical_investment,
            "minimum_revenue": minimum_revenue,
            "revenue_model": preferred_revenue_model,
            "growth_expectations": growth_expectations,
            "customer_type": preferred_customer_type,
            "market_characteristics": market_characteristics,
            "business_model": business_model_preferences.split(","),
            "team_preferences": founder_team_preferences.split(","),
            "other_criteria": other_criteria.split(",")
        }
        st.success("Investment thesis saved successfully!")

def display_startup_data_room():
    st.header("Startup Data Room")
    uploaded_files = st.file_uploader("Upload Startup Documents", accept_multiple_files=True, type=["pdf", "docx", "txt", "xlsx"])
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.write(f"Filename: {uploaded_file.name}")
            st.write(f"Document Type: {uploaded_file.type}")
            st.write("Processing Status: Pending")
            st.write("Number of Pages: N/A")
            st.write("Number of Chunks: N/A")
            st.write("Indexing Status: N/A")
    
    if st.button("Process Documents"):
        st.success("Documents are being processed...")

def main():
    st.title("VENTURELENS")
    st.subheader("AI-Powered Venture Capital Screening & Due-Diligence Assistant")
    
    menu = ["Investment Thesis", "Startup Data Room", "Screening", "Investment Committee", "Founder Interview", "Screening Report", "Evidence Explorer", "System Architecture"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    if choice == "Investment Thesis":
        display_investment_thesis_form()
    elif choice == "Startup Data Room":
        display_startup_data_room()
    # Additional UI components for other options can be added here

if __name__ == "__main__":
    main()