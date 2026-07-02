# SHL Assessment Recommendation Agent

## Overview

This project is a conversational AI agent that helps hiring managers identify the most suitable SHL Individual Test Solutions through natural language conversations.

The agent clarifies vague hiring requests, recommends relevant assessments, supports refinement, compares assessments, and only recommends assessments available in the official SHL catalog.

---

## Features

- Conversational hiring assistant
- Clarifies ambiguous hiring requirements
- Recommends SHL Individual Test Solutions
- Supports refinement during conversation
- Supports assessment comparison
- Uses Hybrid Retrieval (BM25 + Semantic Search)
- Gemini-powered natural language responses
- Stateless FastAPI API
- Grounded recommendations from the SHL catalog only

---

## Architecture

```
User Request
      │
      ▼
Conversation Parser
      │
      ▼
Decision Engine
      │
      ▼
Hybrid Retrieval
(BM25 + Sentence Transformers)
      │
      ▼
SHL Catalog
      │
      ▼
Gemini Response Generation
      │
      ▼
JSON API Response
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

---

### Chat

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java developer"
    }
  ]
}
```

---

## Tech Stack

- FastAPI
- Python
- BM25
- Sentence Transformers
- FAISS
- Google Gemini
- Pydantic

---

## Running Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Deployment

Designed to deploy on Render.

Environment Variable:

```
GEMINI_API_KEY=YOUR_API_KEY
```
