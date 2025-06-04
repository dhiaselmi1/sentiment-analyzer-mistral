# Sentiment Analyzer (Mistral)

A lightweight AI-powered sentiment analysis app that leverages the **Mistral language model** hosted via **Ollama** to classify the sentiment of user-input text quickly and accurately.

## Features

- **FastAPI** backend providing a REST API for sentiment classification  
- **Streamlit** frontend offering an interactive UI for users  
- Integration with **Ollama-hosted Mistral model** for state-of-the-art sentiment analysis  
- Easy setup and local deployment  

## Prerequisites

- Python 3.8 or higher  
- [Ollama CLI](https://ollama.com/docs/installation) installed and configured  
- `pip` for Python package installation  

## Setup and Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sentiment-analyzer-mistral.git
cd sentiment-analyzer-mistral

 ```

2.  **Create and activate a Python virtual environment**:
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows (PowerShell):
    .\venv\Scripts\Activate.ps1
    # Or Windows (CMD):
    .\venv\Scripts/activate.bat
    ```

  ## ▶️ Running the Application

1.  **Start the FastAPI backend server**:
    ```bash
    uvicorn backend.main:app --reload
    ```

2.  **In a new terminal, start the Streamlit frontend**:
    ```bash
    streamlit run frontend/app.py
    ```
    Open your browser to `http://localhost:8501`.

---

## 📝 Usage

- Use the frontend interface to input any text.
- The app will send the text to the backend, which classifies the sentiment using the Mistral model.
- The predicted sentiment (e.g., positive, negative, neutral) will be displayed immediately on the frontend.
---

