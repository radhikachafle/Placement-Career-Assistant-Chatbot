# Placement-Career-Assistant-Chatbot
🏹 AI-powered Placement &amp; Career Assistant Chatbot built with ANN (Scikit-learn) for intent classification and Groq LLaMA 3.3 70B for smart responses — helping engineering students ace campus placements. 
# 🏹 Placement & Career Assistant Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ANN-orange?style=for-the-badge&logo=scikit-learn)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

An intelligent AI-powered chatbot that helps engineering students
prepare for campus placements using ANN + LLM hybrid architecture.

</div>

---

## 📌 Project Overview

The **Placement & Career Assistant Chatbot** is a full-stack AI
application that combines the power of **Artificial Neural Networks**
for intent classification and **Large Language Models** for generating
detailed, contextual career guidance responses.

Built specifically for engineering students preparing for campus
placements in India, the chatbot provides expert advice on resumes,
interviews, aptitude tests, salary negotiation, company processes,
and career roadmaps.

---

## ✨ Features

- 🧠 **ANN Intent Classification** — Scikit-learn MLPClassifier with 98%+ accuracy
- 🤖 **Groq LLM Integration** — LLaMA 3.3 70B for detailed smart responses
- 🎨 **Creative UI** — Dark/light theme with 3D liquid glass animations
- 🗺️ **Career Roadmaps** — Visual roadmaps for AI, Data Science, Placement
- 💬 **Personalized Chat** — Welcomes user by name with custom greeting
- 📥 **Chat History Download** — Save entire conversation as .txt file
- ⚡ **Quick Question Buttons** — One-click access to common topics
- 🌙 **Dark/Light Mode** — Toggle between themes instantly
- 📊 **Session Stats** — Track questions asked and messages sent
- 🔒 **Secure API Management** — API keys stored safely in .env file

---

## 🏗️ Project Architecture 
User Input
↓
Streamlit UI (ui/app.py)
↓
ANN Intent Classifier (core/intent_classifier.py)
↓ intent label
Groq LLM Handler (core/llm_handler.py)
↓ smart response
Display to User 
---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | Streamlit | Chat UI and components |
| ANN Model | Scikit-learn MLPClassifier | Intent classification |
| LLM | Groq LLaMA 3.3 70B | Response generation |
| NLP | NLTK | Tokenization and lemmatization |
| Vectors | NumPy | Bag-of-words processing |
| Config | python-dotenv | Secure API key management |
| Language | Python 3.11 | Core programming |

---

## 📁 Project Structure 
PlacementChatbot/
│
├── data/
│   ├── intents.json          ← ANN training data
│   └── knowledge_base.json   ← Company and career info
│
├── model/                    ← Auto-generated after training
│   ├── chatbot_model.pkl
│   ├── words.pkl
│   └── classes.pkl
│
├── training/
│   ├── init.py
│   ├── preprocess.py         ← Tokenize and vectorize
│   └── train_model.py        ← Train and save ANN
│
├── core/
│   ├── init.py
│   ├── intent_classifier.py  ← Predict intent using ANN
│   ├── llm_handler.py        ← Call Groq LLM API
│   └── chatbot.py            ← Combine ANN + LLM
│
├── ui/
│   └── app.py                ← Streamlit frontend
│
├── .streamlit/
│   └── config.toml           ← Streamlit theme config
│
├── .env                      ← API keys (not uploaded)
├── .gitignore
├── requirements.txt
└── README.md 
---

## 🚀 Getting Started

### Prerequisites
- Python 3.11
- Groq API key (free at https://console.groq.com)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/placement-chatbot.git
cd placement-chatbot
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your Groq API key**

Create a `.env` file in the root folder:
Get your free API key at https://console.groq.com

**5. Train the ANN model**
```bash
python training/train_model.py
```

**6. Launch the chatbot**
```bash
streamlit run ui/app.py
```

Open your browser at `http://localhost:8501`

---

## 💬 Topics Covered

| Topic | Description |
|---|---|
| 📄 Resume Writing | Format, tips, ATS optimization |
| 🎤 Interview Prep | Technical and HR round guidance |
| 🧮 Aptitude Tests | Quant, reasoning, verbal tips |
| 💰 Salary Negotiation | CTC understanding and negotiation |
| 🏢 Company Processes | TCS, Infosys, Wipro, Accenture |
| 💻 Coding Rounds | DSA preparation and platforms |
| 🗺️ Career Roadmaps | AI, Data Science, Placement paths |
| 🎓 Higher Studies | GATE, MBA, MS abroad guidance |

---

## 🧠 How ANN Works in This Project

1. User types a message
2. NLTK tokenizes and lemmatizes the text
3. Bag-of-words vector is created (99 dimensions)
4. MLPClassifier ANN predicts intent with confidence score
5. If confidence > 40% → intent is passed to Groq LLM
6. LLM generates a detailed, focused response
7. Response is displayed in the chat UI

---

## 📸 Screenshots

> Add screenshots of your project here after taking them

---

## 🔧 Requirements
groq==0.9.0
python-dotenv==1.0.0
streamlit==1.32.0
nltk==3.8.1
scikit-learn==1.3.0
numpy==1.24.3
---

## 🤝 Contributing

Pull requests are welcome. For major changes please open an issue first.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Made with ❤️ by **Radhika**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/YOUR_USERNAME)

---

<div align="center">
⭐ Star this repo if you found it helpful!
</div>
