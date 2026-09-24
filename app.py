import streamlit as st
from src.config import load_config
from src.document_processor import process_documents
from src.vector_store import initialize_vector_store
from src.retrieval import retrieve_evidence
from src.thesis import InvestmentThesis
from src.agents import run_analysis
from src.report_generator import generate_report


def collect_thesis():
    st.sidebar.header("Investment Thesis")
    fund_name = st.sidebar.text_input("Fund name")
    sectors = st.sidebar.text_input("Preferred sectors (comma-separated)")
    excluded = st.sidebar.text_input("Excluded sectors (comma-separated)")
    stage = st.sidebar.selectbox("Preferred stage", ["", "Pre-seed", "Seed", "Series A", "Series B"])
    return InvestmentThesis(
        fund_name=fund_name,
        preferred_geographies=[],
        preferred_sectors=[value.strip() for value in sectors.split(",") if value.strip()],
        excluded_sectors=[value.strip() for value in excluded.split(",") if value.strip()],
        preferred_stage=stage,
        typical_investment=0,
        minimum_revenue=0,
        preferred_revenue_model="",
        growth_expectations="",
        preferred_customer_type="",
        market_characteristics="",
        business_model_preferences=[],
        team_preferences=[],
        other_criteria=[],
    )


def main():
    st.title("VENTURELENS")
    st.subheader("AI-Powered Venture Capital Screening & Due-Diligence Assistant")

    # Load configuration
    config = load_config()

    thesis = collect_thesis()

    # Document Upload
    st.sidebar.header("Upload Startup Documents")
    uploaded_files = st.sidebar.file_uploader("Choose files", accept_multiple_files=True)

    if uploaded_files and st.sidebar.button("Index uploaded documents"):
        try:
            documents = process_documents(uploaded_files)
            vector_store = initialize_vector_store(config)
            vector_store.add_documents(documents)
            st.session_state["vector_store"] = vector_store
            st.session_state["documents_indexed"] = len(documents)
            st.sidebar.success(f"Indexed {len(documents)} document(s).")
        except (ValueError, RuntimeError) as error:
            st.sidebar.error(str(error))

    # Run Screening
    if st.sidebar.button("Run VentureLens Screening"):
        vector_store = st.session_state.get("vector_store")
        if vector_store is None:
            st.warning("Index at least one startup document before screening.")
        else:
            evidence = retrieve_evidence("startup business market financial team risks", vector_store=vector_store)
            analysis_results = run_analysis(evidence, thesis)
            report = generate_report(analysis_results)
            st.json(report)

if __name__ == "__main__":
    main()