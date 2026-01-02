# Essay Evaluator — AI-Powered Essay Feedback System

## Overview

The **Essay Evaluator** is an AI-powered web application that leverages the capabilities of **LLaMA 3.1 via the Groq API** to:

* Provide structured feedback across key writing dimensions
* Generate an overall qualitative review
* Assign objective scores out of 10
* Calculate an average score
---

## Key Features

* **AI-powered structured evaluation**
* **Language Quality Feedback + Score**
* **Depth of Analysis Feedback + Score**
* **Clarity of Thought Feedback + Score**
* **Overall Summary Feedback**
* **Average Score Calculation**
---

## Tech Stack

| Layer           | Tools & Libraries              |
| --------------- | ------------------------------ |
| Backend         | Python, Flask                  |
| AI Model        | Groq API (LLaMA 3.1)           |
| Orchestration   | LangGraph                      |
| Model Framework | LangChain                      |
| Validation      | Pydantic                       |
| Config          | python-dotenv                  |
| Frontend UI     | HTML, CSS (minimalist styling) |

---

## Demo Screenshot

<img width="2962" height="1880" alt="Screenshot 2026-01-02 at 18-43-13 Essay Evaluator" src="https://github.com/user-attachments/assets/4e0dace7-83a0-4dcc-b793-47ec5ca94500" />
<img width="2948" height="1684" alt="Screenshot 2026-01-02 at 18-44-09 Essay Evaluator" src="https://github.com/user-attachments/assets/8a062244-91e3-4dcc-9050-20399d9136a8" />

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/BhaveshBhakta/Essay-Evaluator-Using-LangGraph.git
cd Essay-Evaluator-Using-LangGraph
```

---

### Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows
```

Install packages:

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### Run the Application

```bash
python app.py
```

---

## Why This Project?

This project demonstrates:

* Practical application of **Generative AI in education**
* Real-world **LLM integration with Flask**
* Use of **LangGraph for structured multi-step reasoning**
* **Prompt engineering for assessment workflows**
* Clean and user-friendly frontend design

##  Collaboration

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.
