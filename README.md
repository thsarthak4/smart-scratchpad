# 🚀 Smart Scratchpad Engine

A lightweight, real-time text analysis platform that intelligently classifies and processes unstructured input streams into structured, interactive insights.

### 🌐 Live Demo

**Production Deployment:** https://smart-scratchpad-22oz.vercel.app

---

## 📖 Overview

Smart Scratchpad is a context-aware parsing engine designed to analyze raw text inputs and automatically route them through specialized processing modules.

Instead of manually switching between multiple tools to inspect JSON, debug stack traces, extract URLs, or analyze plain text, users can paste any payload and receive structured results instantly.

The application uses deterministic pattern classification powered by regular expressions to identify content types and trigger the appropriate processing pipeline.

---

## ✨ Key Features

### 📦 JSON Parser

* Detects JSON payloads automatically
* Validates structure and syntax
* Displays formatted key-value hierarchies
* Highlights malformed JSON errors

### 🚨 Error & Stack Trace Analyzer

* Parses Python exception logs
* Extracts file names and line numbers
* Identifies failure locations
* Improves debugging workflow

### 🌐 URL Extractor

* Detects hyperlinks from unstructured text
* Extracts and lists URLs
* Provides direct clickable access

### 📊 Text Analytics Engine

* Word count
* Character count
* Reading time estimation
* Basic linguistic statistics

---

## ⚡ Processing Pipeline

```text
Raw Unstructured Input
           │
           ▼
   Deterministic Router
           │
 ┌─────────┼─────────┬─────────┐
 ▼         ▼         ▼         ▼
JSON     Error     Links     Text
Parser   Parser   Extractor Analytics
 │          │         │         │
 └──────────┴─────────┴─────────┘
                │
                ▼
      Interactive Result Cards
```

---

## 🏗 System Architecture

```text
SMART-SCRATCHPAD
│
├── api
│   └── index.py
│       ├── Request Handling
│       ├── Context Classification
│       ├── Regex Routing Logic
│       └── Result Generation
│
├── templates
│   └── index.html
│       ├── Responsive UI
│       ├── Dark Theme
│       └── Interactive Cards
│
├── requirements.txt
│
└── vercel.json
```

---

## 🛠 Tech Stack

| Category        | Technology                  |
| --------------- | --------------------------- |
| Language        | Python 3.10+                |
| Backend         | Flask                       |
| Parsing Engine  | Regular Expressions (Regex) |
| Frontend        | HTML, CSS, JavaScript       |
| Deployment      | Vercel Serverless Functions |
| Version Control | Git & GitHub                |

---

## 🔍 How It Works

1. User submits raw text input.
2. Classification engine evaluates patterns.
3. Router determines content type.
4. Appropriate parser processes the payload.
5. Structured results are displayed as interactive UI cards.

Supported input types:

* JSON Objects
* Exception Logs
* Stack Traces
* Hyperlinks
* General Text

---

## 🚀 Local Development Setup

### Prerequisites

* Python 3.10+
* Git

### Clone Repository

```bash
git clone https://github.com/thsarthak4/smart-scratchpad.git
cd smart-scratchpad
```

### Create Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python api/index.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deployment Workflow

The project uses an automated CI/CD deployment pipeline through Vercel.

```text
GitHub Push
      │
      ▼
Vercel Build Trigger
      │
      ▼
Serverless Function Build
      │
      ▼
Global Edge Deployment
```

Every push to the main branch automatically triggers a production deployment.

```bash
git push origin main
```

---

## 🎯 Why This Project?

Smart Scratchpad demonstrates:

* Text Processing
* Pattern Recognition
* Backend Engineering
* Serverless Deployment
* Flask Development
* Regular Expression Design
* User Experience Design

It serves as a practical productivity tool while showcasing software engineering fundamentals.

---

## 📄 License

Distributed under the MIT License.

Feel free to fork, modify, and build upon this project.

---

## 👨‍💻 Author

**Sarthak Singh Chaudhary**

Computer Science Engineering Student
AI/ML Enthusiast | Software Developer | Problem Solver

⭐ If you found this project useful, consider giving it a star.
