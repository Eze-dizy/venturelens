# VentureLens

## Overview
VentureLens is an AI-powered venture capital screening and due-diligence assistant designed to help venture capitalists efficiently evaluate startup investment opportunities. The application leverages Retrieval-Augmented Generation (RAG) and agentic AI to provide structured, evidence-based insights that support human decision-making in the investment process.

## Business Problem
Venture capital firms face challenges in processing large volumes of unstructured and inconsistent information during the initial screening of startups. VentureLens addresses these challenges by providing a systematic approach to analyze startup documents against user-defined investment theses.

## Installation & Setup

### Prerequisites
- Python 3.11 or newer
- Git
- An OpenAI API key belonging to you

### Clone the repository
```powershell
git clone <repository-url>
cd venturelens
```

### Create and activate a virtual environment
Run these commands in Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, review your local PowerShell execution-policy settings or activate the environment using another supported shell. Do not bypass security controls by copying credentials into scripts.

### Install dependencies
```powershell
pip install -r requirements.txt
```

### Configure the OpenAI API key
Create your own `.env` file in the project root. Add your personal key in this format:
```dotenv
OPENAI_API_KEY=your_api_key_here
```

Do not use or request the author's API key. Each person running VentureLens must create and use their own OpenAI account and API key.

### Run the application
From the project root, with the virtual environment activated:
```powershell
streamlit run app.py
```

Open the local URL in your browser:

<http://localhost:8501>

### How VentureLens works
1. Upload startup documents such as pitch decks, financial models, founder profiles, market reports, and business plans.
2. Define the investment thesis, including preferred and excluded sectors and the target investment stage.
3. Index the uploaded documents into ChromaDB.
4. Retrieve relevant evidence from the indexed documents using Retrieval-Augmented Generation (RAG).
5. Run analytical agents covering business, market, traction, financial, team, competition, risk, consistency, and thesis alignment topics.
6. Generate a structured screening report and due-diligence questions for human review.

## Usage
To run the application, execute the following command:
```
python -m streamlit run app.py
```

Once the application is running, you can define your investment thesis, upload startup documents, and initiate the screening process to receive structured insights and reports.

## Features
- Define and customize investment theses.
- Upload and process various startup documents (PDF, DOCX, TXT, XLSX).
- Analyze business models, financial health, market opportunities, and risks.
- Generate targeted due-diligence questions based on identified information gaps.
- Produce comprehensive screening reports that support investment decisions.

## Security
- Keep the local `.env` file excluded through `.gitignore`.
- Never commit API keys, passwords, tokens, credentials, or other secrets to GitHub.
- Every user must use their own OpenAI API key. Do not share or request another user's key.
- If a secret is accidentally committed, revoke it immediately and remove it from the repository history before continuing to use the project.

## Project Architecture

The main application flow is implemented across these files in `src/`:

- `config.py` loads the root `.env` file and provides project paths and configuration.
- `document_processor.py` extracts and cleans text from PDF, DOCX, TXT, and XLSX uploads.
- `vector_store.py` creates the persistent ChromaDB store and manages embeddings and indexed documents.
- `retrieval.py` chunks documents and retrieves relevant evidence with source metadata.
- `thesis.py` represents the user's investment thesis and its criteria.
- `agents.py` coordinates evidence-based analytical tasks, information-gap detection, risk review, and due-diligence questions.
- `financial_analysis.py` provides financial metric calculations.
- `consistency_checker.py` identifies contradictory values across documents.
- `risk_analysis.py` records risks, supporting evidence, implications, and missing information.
- `report_generator.py` assembles the structured screening report.
- `prompts.py` contains reusable analysis prompt templates.
- `utilities.py` contains shared validation, text, metadata, and environment helpers.
- `ui.py` contains reusable Streamlit interface components.

The system is a decision-support tool: its evidence, analysis, risks, contradictions, and information gaps are intended to support human VC judgment rather than make an autonomous investment decision.

## Future Improvements
- Enhance the user interface for better usability.
- Integrate additional data sources for more comprehensive analyses.
- Implement advanced machine learning models for improved predictions and insights.

## Acknowledgments
This project is developed as part of an academic initiative to explore the applications of AI in venture capital and investment decision-making.