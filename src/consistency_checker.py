import re


def check_consistency(financial_data, documents):
    inconsistencies = []
    
    # Example of checking for inconsistencies in revenue data
    revenue_sources = {}
    
    for doc in documents:
        if isinstance(doc, dict) and 'revenue' in doc:
            revenue_sources[doc.get('source', 'unknown')] = doc['revenue']
    
    if len(set(revenue_sources.values())) > 1:
        inconsistencies.append({
            'type': 'Financial Inconsistency',
            'details': 'Different revenue figures found across documents.',
            'sources': revenue_sources
        })
    
    # Additional checks can be added here for other types of inconsistencies
    
    return inconsistencies

def check_document_consistency(documents):
    all_inconsistencies = []
    values_by_label = {}
    for document in documents:
        text = document.page_content if hasattr(document, "page_content") else document.get("text", "")
        metadata = document.metadata if hasattr(document, "metadata") else document.get("metadata", {})
        source = metadata.get("source", "unknown")
        for label in ("revenue", "customers", "arr", "mrr"):
            matches = re.findall(rf"\b{label}\b[^\n:$]*[$₹]?\s*([\d,.]+)", text, flags=re.IGNORECASE)
            for value in matches:
                values_by_label.setdefault(label, {}).setdefault(value.replace(",", ""), []).append(source)
    for label, values in values_by_label.items():
        if len(values) > 1:
            all_inconsistencies.append({"type": "Contradiction", "field": label, "values": values})
    return all_inconsistencies