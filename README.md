# VentureLens

## Overview
VentureLens is an AI-powered venture capital screening and due-diligence assistant designed to help venture capitalists efficiently evaluate startup investment opportunities. The application leverages Retrieval-Augmented Generation (RAG) and agentic AI to provide structured, evidence-based insights that support human decision-making in the investment process.

## Business Problem
Venture capital firms face challenges in processing large volumes of unstructured and inconsistent information during the initial screening of startups. VentureLens addresses these challenges by providing a systematic approach to analyze startup documents against user-defined investment theses.

## Installation
To set up the VentureLens application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd venturelens
   ```

2. Create a virtual environment (if not already created):
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```
   python -m pip install -r requirements.txt
   ```

5. Set up environment variables by creating a `.env` file based on the `.env.example` template.

## Usage
To run the application, execute the following command:
```
python -m streamlit run app.py
```

Once the application is running, you can define your investment thesis, upload startup documents, and initiate the screening process to receive structured insights and reports.

## Features
- Define and customize investment theses.
- Upload and process various startup documents (PDF, DOCX, TXT).
- Analyze business models, financial health, market opportunities, and risks.
- Generate targeted due-diligence questions based on identified information gaps.
- Produce comprehensive screening reports that support investment decisions.

## Future Improvements
- Enhance the user interface for better usability.
- Integrate additional data sources for more comprehensive analyses.
- Implement advanced machine learning models for improved predictions and insights.

## Acknowledgments
This project is developed as part of an academic initiative to explore the applications of AI in venture capital and investment decision-making.