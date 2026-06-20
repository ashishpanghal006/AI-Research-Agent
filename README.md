# AI Research Agent

A modern multi-agent AI research system built using **LangGraph, FastAPI, React, and Groq LLMs**.

This project simulates a real-world AI research workflow where multiple AI agents collaborate to plan research, gather web information, analyze findings, and generate professional research reports with citations.

---

# Features 

* Multi-Agent AI Workflow using LangGraph
* Parallel Research Agents
* Real-Time Web Research with Tavily
* Structured Research Planning
* Automated Research Summarization
* Research Analysis & Insights
* Professional Markdown Reports
* Source References & Citations
* Modern React + Tailwind Frontend
* FastAPI Backend
* Modular Agent Architecture

---

# Architecture  

```text
User Query
    ↓
Planner Agent
    ↓
Dispatcher
    ↓
Parallel Research Workers
    ↓
Merge Results
    ↓
Analyst Agent
    ↓
Writer Agent
    ↓
Final Research Report
```

---

# Tech Stack

## Frontend

* React
* Tailwind CSS
* Axios
* React Markdown
* Lucide React

## Backend

* FastAPI
* LangGraph
* LangChain
* Groq LLM
* Tavily Search API
* Python

---

# Project Structure

```text
backend/

agents/
├── planner.py
├── dispatcher.py
├── research_worker.py
├── merge.py
├── analyst.py
├── writer.py

graph/
├── workflow.py

tools/
├── search.py

config/
├── llm.py

state.py
api.py
main.py


frontend/

src/

components/
├── Header.jsx
├── SearchBox.jsx
├── ProgressSteps.jsx
├── SectionCard.jsx
├── SourcesList.jsx
├── ReportActions.jsx

pages/
├── Home.jsx

services/
├── api.js
```

---

# How It Works

## 1. Planner Agent

The planner agent generates:

* A concise research strategy
* Multiple research questions

## 2. Dispatcher

The dispatcher distributes research questions to parallel research workers.

## 3. Research Workers

Each worker:

* Searches the web using Tavily
* Collects relevant information
* Summarizes findings
* Extracts source references

## 4. Merge Node

All research summaries and sources are merged into a single research context.

## 5. Analyst Agent

The analyst identifies:

* Key findings
* Trends
* Opportunities
* Risks
* Strategic insights

## 6. Writer Agent

The writer generates a professional research report with:

* Executive Summary
* Market Insights
* Opportunities
* Risks
* References
* Conclusion

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/ashishpanghal006/AI-Research-Agent.git
cd AI-Research-Agent
```

---

# Backend Setup

## 1. Navigate to Backend

```bash
cd backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Create .env File

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 6. Run Backend Server

```bash
uvicorn api:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

## 2. Install Dependencies

```bash
npm install
```

## 3. Run Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# Example Research Topics

* Top AI Coding Assistants in 2026
* Future of Electric Vehicles
* AI in Healthcare
* Benefits of Remote Work
* Future of AI Agents

---

# Learning Outcomes

This project demonstrates:

* Multi-Agent Systems
* AI Workflow Orchestration
* Parallel Agent Execution
* Retrieval-Augmented Generation (RAG)
* LLM Prompt Engineering
* Full Stack AI Application Development
* Modern Frontend Architecture
* FastAPI Backend Development

---

# License

MIT License

---

# Author

Ashish Panghal

Built as a portfolio project to explore modern AI agent architectures and production-style GenAI systems.