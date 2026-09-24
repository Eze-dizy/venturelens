from datetime import datetime

def generate_screening_report(startup_data, thesis_alignment, analyses, evidence_sources):
    report = {
        "executive_summary": generate_executive_summary(startup_data, thesis_alignment),
        "company_overview": startup_data.get("company_overview", ""),
        "investment_thesis": startup_data.get("investment_thesis", ""),
        "thesis_alignment": thesis_alignment,
        "business_model": analyses.get("business_model_analysis", ""),
        "market_opportunity": analyses.get("market_analysis", ""),
        "traction": analyses.get("traction_analysis", ""),
        "financial_analysis": analyses.get("financial_analysis", ""),
        "founder_team": analyses.get("founder_analysis", ""),
        "competitive_landscape": analyses.get("competitive_analysis", ""),
        "key_strengths": analyses.get("key_strengths", ""),
        "potential_risks": analyses.get("risks", ""),
        "document_inconsistencies": analyses.get("inconsistencies", ""),
        "missing_information": analyses.get("missing_information", ""),
        "due_diligence_questions": analyses.get("due_diligence_questions", ""),
        "scenario_analysis": analyses.get("scenario_analysis", ""),
        "screening_outcome": analyses.get("screening_outcome", ""),
        "evidence_sources": evidence_sources,
        "timestamp": datetime.now().isoformat(),
    }
    
    return report


def generate_report(analysis_results):
    return generate_screening_report(
        analysis_results.get("startup_data", {}),
        analysis_results.get("thesis_alignment", {}),
        analysis_results.get("analyses", {}),
        analysis_results.get("evidence_sources", []),
    )

def generate_executive_summary(startup_data, thesis_alignment):
    summary = f"Executive Summary for {startup_data.get('company_name', 'Unknown Company')}\n"
    summary += f"Investment Thesis Alignment: {thesis_alignment}\n"
    summary += f"Overview: {startup_data.get('company_overview', 'No overview provided.')}\n"
    return summary

def format_report(report):
    formatted_report = ""
    for section, content in report.items():
        formatted_report += f"{section.replace('_', ' ').title()}:\n{content}\n\n"
    return formatted_report

def save_report_to_file(report, filename):
    with open(filename, 'w') as file:
        file.write(format_report(report))