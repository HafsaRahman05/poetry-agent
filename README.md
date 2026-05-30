# 📝 Poetry Multi-Agent Analyzer

An AI-powered **multi-agent poetry analysis system** that classifies and interprets poetry using specialized agents.  
Built using **OpenAI Agents SDK + Gemini API + Python async architecture**.

---

## 🌐 Project Overview

This system analyzes poetry and automatically routes it to the most appropriate AI agent:

- ✍️ Poet Identification Agent
- 🎭 Dramatic Analysis Agent
- 📖 Narrative Structure Agent
- 🧠 Main Routing Agent (Dispatcher)

Each agent has a specialized role to analyze poetry from different linguistic and emotional perspectives.

---

## ⚙️ Tech Stack

- Python 3.12+
- OpenAI Agents SDK
- Google Gemini API (OpenAI-compatible endpoint)
- AsyncIO (asynchronous execution)
- Rich (terminal formatting)
- dotenv (environment variables)

---

## 🧠 System Architecture

```
User Input (Poetry)
        ↓
MainAgent (Router)
        ↓
 ┌───────────────┬────────────────┬────────────────┐
 ↓               ↓                ↓
PoetAgent   DramaticAgent   NarrativeAgent
 ↓               ↓                ↓
Final Analysis Output Aggregation
```

---

## 🤖 Agents Description

### ✍️ PoetIdentifierAgent
- Identifies possible poet style influence
- Detects literary patterns
- Matches writing style to known poets

---

### 🎭 DramaticAgent
- Detects emotional intensity
- Analyzes psychological conflict
- Identifies dramatic language usage

---

### 📖 NarrativeAgent
- Detects story structure
- Identifies characters
- Finds chronological progression

---

### 🧠 MainAgent (Router)
- Receives poetry input
- Classifies content type
- Delegates task to correct agent
- Prioritizes:
  1. Poet style (short/metaphorical poetry)
  2. Narrative structure
  3. Dramatic content

---

## 🚀 How It Works

1. User enters a poem (or default sample is used)
2. MainAgent analyzes the text
3. System routes to best matching sub-agent
4. Sub-agent performs specialized analysis
5. Final response is returned with agent tracking

---

## ▶️ Installation

### 1️⃣ Clone repository
```bash
git clone https://github.com/HafsaRahman05/poetry-agent.git
cd poetry-agent
```

---

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

or (if using uv)
```bash
uv sync
```

---

### 3️⃣ Add environment variables
Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run project
```bash
python main.py
```

---

## 📌 Example Input

```
In the battlefield of my heart,
I fought memories like enemies.
Then she smiled,
and my war was over.
```

---

## 📤 Example Output

```
Final Output:
This poem is classified as Dramatic Poetry due to emotional conflict and resolution.

Last Agent Used:
DramaticAgent
```

---

## 🧩 Key Features

- 🧠 Multi-agent AI architecture
- 🔄 Intelligent routing system
- 🎭 Emotion-based classification
- ✍️ Literary style detection
- ⚡ Async execution
- 🤖 Gemini-powered LLM integration

---

## 📚 Learning Outcomes

This project demonstrates:

- Multi-agent AI systems
- Prompt-based routing logic
- Context switching between agents
- Async Python programming
- LLM integration architecture
- NLP-based text classification

---

## 🚀 Future Improvements

- Add web UI (Streamlit / Next.js)
- Store analysis history in database
- Add more literary agents (Metaphor, Sentiment, Grammar)
- Export analysis reports (PDF)
- Support multiple languages poetry

---

## 👩‍💻 Author

**Hafsa Rahman**  
Software Engineering Student  
Interested in AI, NLP, and Multi-Agent Systems

---

## ⭐ License

This project is for educational purposes only.
