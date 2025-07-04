# 🧠 AI Text Generation Web App using Flask & Hugging Face Inference API

This is a simple Flask web application that allows users to enter a text prompt and optionally upload a file. The application sends the text prompt to the **Hugging Face Inference API**, which responds using the **Mistral-7B-Instruct-v0.1** large language model. The response is rendered on a dynamic HTML page using Jinja templates.

---

## 🚀 Features

- Accepts user input through a web form  
- Optional file upload functionality (e.g., image or document)  
- Sends prompts to Hugging Face Inference API  
- Utilizes **Mistral-7B**, a state-of-the-art open-source language model  
- Displays the generated response directly on the page  
- All files are saved to a local static directory (`/static/uploads`)  

---

## 🛠️ Technologies Used

### 🔹 Flask (Python Web Framework)
- Lightweight WSGI web application framework  
- Handles routing, form processing, and rendering HTML templates via Jinja2  

### 🔹 Hugging Face Inference API
- RESTful API for interacting with hosted machine learning models  
- Enables quick prototyping without needing to host your own GPU or model  
- Usage of `requests` library to send HTTP POST requests  

### 🔹 Mistral-7B-Instruct-v0.1
- Developed by [Mistral AI](https://mistral.ai)  
- 7 billion parameter transformer model  
- Fine-tuned for instruction-following use cases  
- Open-weight model known for efficiency and strong NLP performance  

### 🔹 Jinja2 Template Engine
- Embedded in Flask  
- Renders dynamic content into HTML (`index.html`)  
- Allows integration of Python-like expressions within HTML  

---

## 🧠 What is Mistral-7B-Instruct?

`Mistral-7B-Instruct-v0.1` is an **instruction-tuned** version of the base Mistral-7B model. It is designed for:

- Natural language understanding  
- Text completion and question answering  
- Reasoning, summarization, and translation  

It is based on the **Transformer architecture**, which uses self-attention mechanisms and dense neural layers to understand context and generate coherent outputs.

### ✅ Why Use Hugging Face's Hosted API?

- No need to provision GPU instances  
- Easy to scale  
- Access to hundreds of state-of-the-art models  
- Authentication and rate limiting via `hf_xxx` tokens  

---

## 📁 Project Structure
project/
│

├── app.py # Flask server application

├── templates/

│ └── index.html # Frontend HTML template

├── static/

│ └── uploads/ # Folder for uploaded files

└── README.md # This file


---

## 🧪 How It Works

1. User enters a prompt and optionally uploads a file  
2. The prompt is sent to the Hugging Face Inference API using a `POST` request  
3. The response (generated text) is parsed and displayed in the frontend  
4. If a file is uploaded, it's stored in `/static/uploads` and optionally shown or linked on the page  

---

## 🧰 Prerequisites

- Python 3.7+  
- Install dependencies:  
  ```bash
  pip install flask requests
  ```
  
## ⚙️ How to Run

### 1. Set up your environment:

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install flask requests
  ```

### 2. Replace your API key:
In app.py, replace:
  HUGGINGFACE_API_TOKEN = "hf_...YOUR_api_key..."

### 3. Run the server
  ```bash
  python app.py
  ```
###4. Open your browser:
  Navigate to:
  http://127.0.0.1:5000

🔐 Security Note
❗ Never expose your hf_... token in public repositories!
✅ Consider using environment variables or a .env file with python-dotenv for production use.



