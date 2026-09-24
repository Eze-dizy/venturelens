from src.consistency_checker import check_document_consistency
from src.financial_analysis import calculate_revenue_growth
from src.risk_analysis import RiskAnalysis


def _text(document):
    return document.page_content if hasattr(document, "page_content") else document.get("text", "")


def _source(document):
    metadata = document.metadata if hasattr(document, "metadata") else document.get("metadata", {})
    return metadata.get("source", "unknown")


class VentureLensAgent:
    """Coordinate analysis tools while leaving the investment decision to a human."""

    def __init__(self, tools=None):
        self.tools = tools or {
            "search_documents": search_documents,
            "calculate_financial_metric": calculate_financial_metric,
            "check_consistency": check_consistency,
            "analyze_thesis_alignment": analyze_thesis_alignment,
            "identify_information_gaps": identify_information_gaps,
            "generate_due_diligence_questions": generate_due_diligence_questions,
        }

    def run(self, input_text, evidence=None):
        return self.tools["search_documents"](input_text, evidence)


def search_documents(query, evidence=None):
    return [document for document in (evidence or []) if query.lower() in _text(document).lower()]


def retrieve_evidence(query, evidence=None):
    return search_documents(query, evidence)


def calculate_financial_metric(current_revenue=None, previous_revenue=None):
    if current_revenue is None or previous_revenue is None:
        return {"value": None, "status": "missing_evidence"}
    return {"value": calculate_revenue_growth(current_revenue, previous_revenue), "status": "calculated"}


def compare_documents(documents):
    return check_document_consistency(documents)


def check_consistency(documents):
    return compare_documents(documents)


def analyze_thesis_alignment(evidence, thesis):
    text = " ".join(_text(document) for document in evidence).lower()
    sectors = [sector for sector in thesis.preferred_sectors if sector]
    matched = [sector for sector in sectors if sector.lower() in text]
    excluded = [sector for sector in thesis.excluded_sectors if sector and sector.lower() in text]
    return {"matched_criteria": matched, "excluded_criteria": excluded, "status": "evidence_limited" if not sectors else "assessed"}


def identify_information_gaps(evidence):
    text = " ".join(_text(document) for document in evidence).lower()
    expected = {"financials": "revenue", "market": "market", "traction": "customer", "team": "founder", "competition": "competitor"}
    return [{"area": area, "status": "missing_evidence", "needed": keyword} for area, keyword in expected.items() if keyword not in text]


def generate_due_diligence_questions(gaps):
    return [f"What evidence supports the {gap['area']} assessment, including {gap['needed']} data?" for gap in gaps]


def generate_screening_report(analysis_results):
    return analysis_results


def run_analysis(evidence, thesis):
    evidence_sources = [{"source": _source(document), "excerpt": _text(document)[:500]} for document in evidence]
    gaps = identify_information_gaps(evidence)
    risks = RiskAnalysis()
    for gap in gaps:
        risks.add_risk(gap["area"], "No supporting evidence found in retrieved documents.", "retrieval", "Requires human follow-up.", "low", gap["needed"])
    return {
        "startup_data": {"company_name": "Uploaded startup", "company_overview": "Evidence-based screening from uploaded documents."},
        "thesis_alignment": analyze_thesis_alignment(evidence, thesis),
        "analyses": {
            "business_model_analysis": "Evidence retrieved for business model review.",
            "market_analysis": "Evidence retrieved for market review.",
            "traction_analysis": "Evidence retrieved for traction review.",
            "financial_analysis": calculate_financial_metric(),
            "founder_analysis": "Evidence retrieved for team review.",
            "competitive_analysis": "Evidence retrieved for competition review.",
            "risks": risks.analyze_risks(),
            "inconsistencies": compare_documents(evidence),
            "missing_information": gaps,
            "due_diligence_questions": generate_due_diligence_questions(gaps),
            "screening_outcome": "Human review required; no autonomous investment decision was made.",
        },
        "evidence_sources": evidence_sources,
    }