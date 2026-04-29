# Jebat AI: Local Intelligent Assistant 🗡️

## 🎯 Project Overview
Jebat is a personalized, locally-hosted AI agent designed to bridge the gap between human interaction and system automation. Built with **Python** and **Ollama**, this project focuses on privacy-first AI, running entirely on local hardware (NVIDIA RTX 3060) without relying on external cloud APIs.

This project serves as a practical application of my transition into **AI Development and Technical Operations**, showcasing my ability to integrate LLMs with local system hardware.

## 🚀 Key Features
- **Privacy-First Intelligence:** Utilizes Llama 3.1 via Ollama for offline inference.
- **Hybrid Interaction:** Engineered a dual-input system (Speech-to-Text via `SpeechRecognition` and Keyboard Fallback) to ensure 100% uptime regardless of hardware environment.
- **Custom Persona Logic:** Implemented advanced system prompting to create a culturally resonant "Malay Warrior" persona.
- **Asynchronous Execution:** Optimized for low-latency responses on mid-range GPU hardware.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Frameworks:** Ollama, SpeechRecognition
- **Model:** Llama 3.1 (8B)
- **Development Environment:** VS Code, Git, Windows 11

## 📈 Learning Journey
Building Jebat allowed me to understand several core engineering concepts:
1. **API & Model Integration:** Understanding how to communicate with local LLM endpoints.
2. **Error Handling:** Managing hardware interrupts and microphone sensitivity issues.
3. **Version Control:** Implementing professional Git workflows to track feature development.

## ⚙️ Setup & Installation
1. Install [Ollama](https://ollama.com/).
2. Pull the model: `ollama pull llama3.1`.
3. Clone this repository and install requirements.
4. Run: `python jebat.py`.

---
*Developed as part of a career pivot into Technical Operations and AI Engineering.*
