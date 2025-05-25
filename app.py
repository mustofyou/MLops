from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Hugging Face endpoint bilgileri
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HUGGINGFACE_API_TOKEN = "hf_...senin_api_key..."

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def query_huggingface(prompt):
    response = requests.post(
        HUGGINGFACE_API_URL,
        headers=headers,
        json={"inputs": prompt}
    )
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    uploaded_file_path = ""
    if request.method == "POST":
        user_input = request.form.get("message")
        file = request.files.get("file")

        if file and file.filename != "":
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            uploaded_file_path = file_path

        if user_input:
            result = query_huggingface(user_input)
            response = result[0]["generated_text"] if isinstance(result, list) else result.get("error", "Model cevap veremedi.")

    return render_template("index.html", response=response, uploaded_file=uploaded_file_path)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
