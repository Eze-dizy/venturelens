# prompts.py

# This file contains predefined prompts for interacting with the language model and generating questions or analyses.

def get_investment_thesis_prompt(thesis):
    return f"Evaluate the startup against the following investment thesis: {thesis}"

def get_business_model_analysis_prompt(startup_data):
    return f"Analyze the business model of the startup based on the following data: {startup_data}"

def get_market_analysis_prompt(market_data):
    return f"Assess the market opportunity using the following data: {market_data}"

def get_financial_analysis_prompt(financial_data):
    return f"Calculate and analyze the financial metrics based on the following data: {financial_data}"

def get_risk_analysis_prompt(risk_factors):
    return f"Identify and analyze potential risks associated with the startup considering these factors: {risk_factors}"

def get_due_diligence_questions_prompt(information_gaps):
    return f"Generate due diligence questions based on the following information gaps: {information_gaps}"

def get_consistency_check_prompt(financial_data):
    return f"Check for consistency in the following financial data: {financial_data}"

def get_screening_report_prompt(analysis_results):
    return f"Generate a screening report based on the following analysis results: {analysis_results}"