# Complaint-Ticket-Managemant-Using-AI

## Project Overview
- In today's fast-paced business environment, customer feedback is a vital asset for shaping product and service strategies. Organizations must process and respond to support tickets swiftly and effectively to enhance customer satisfaction, drive growth, and build long-term loyalty. This project leverages Generative AI to automate support ticket categorization, prioritization, and response generation, enabling businesses to address customer concerns efficiently and with precision.

## Key Features
- Automated Categorization: Predict ticket categories using a Large Language Model (LLM).
- Priority Assignment: Assign appropriate priorities to support tickets for effective resolution planning.
- ETA Prediction: Estimate resolution times based on ticket content.
- Response Generation: Create personalized, sentiment-driven responses to customer issues.
- Structured Data Output: Store processed ticket data, including predictions and responses, in a structured format (e.g., a DataFrame).

## Technical Details
The application utilizes the Ollama LLM to process support ticket text data and generate actionable outputs. The workflow integrates Zero-shot and Few-shot prompting techniques for enhanced accuracy in classification and response generation.

## Core Technologies
- LangChain: To manage prompts and chain LLM workflows.
- Ollama LLM: A Large Language Model used for generative tasks.
- Pandas: For data handling and transformation.
- Python: The core programming language for implementation.

## Code Highlights
- Zero-shot Prompting: Quickly predicts ticket properties without prior context.
- Few-shot Prompting: Leverages examples to improve prediction accuracy.
- JSON Parsing: Processes the LLM response to extract meaningful information.
- Data Pipeline: Reads raw ticket data from CSV, processes it with the model, and stores the structured results in a new CSV file.

## Usage
Clone the repository:
Copy code
- git clone https://github.com/james-tabansi/Complaint-Ticket-Managemant-Using-AI.git
- cd Complaint-Ticket-Managemant-Using-AI

- Install dependencies:
 - pip install -r requirements.txt
 - Place your support ticket data CSV file in the data/ directory.
 - Run the script to process support tickets and generate outputs:
 - python main.py


## Project Structure
- data/: Folder containing input and output CSV files.
- myPrompts.py: Contains Zero-shot and Few-shot prompt templates.
- app.py: Core script for processing support tickets.
- requirements.txt: List of Python dependencies.

## Future Enhancements
- Add multi-language support for ticket processing.
- Integrate with real-time ticketing systems (e.g., Zendesk, Freshdesk).
- Deploy as a web application for broader accessibility.
