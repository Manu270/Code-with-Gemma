from flask import Flask, request, jsonify, render_template
import subprocess
import os
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyCWJ-hXKmlCaUIFFuEYK8EfljjpyeDAclc")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def execute_code(language, code,modelr):
    filename = f"temp_code.{language}"
    output = ""
    error = ""

    with open(filename, 'w') as file:
        file.write(code)
    
    try:
        if language == 'c':
            subprocess.run(['gcc', filename, '-o', 'temp_code'], check=True)
            output = subprocess.check_output('./temp_code', stderr=subprocess.STDOUT, text=True)
        elif language == 'cpp':
            subprocess.run(['g++', filename, '-o', 'temp_code'], check=True)
            output = subprocess.check_output('./temp_code', stderr=subprocess.STDOUT, text=True)
        elif language == 'java':
            subprocess.run(['javac', filename], check=True)
            output = subprocess.check_output(['java', 'temp_code'], stderr=subprocess.STDOUT, text=True)
        elif language == 'python':
            output = subprocess.check_output(['python3', filename], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        error = e.output

    os.remove(filename)
    if language == 'java':
        os.remove('temp_code.class')

    error = error_code(code,modelr)
    return output, error

def call_ollama(prompt):
    # Use subprocess to communicate with Ollama locally
    result = subprocess.run(['ollama', 'run', 'llama3.1'], input=prompt, capture_output=True, text=True)
    return result.stdout.strip()

def optimize_code(code,modelr):
    if modelr=='llama':
        prompt = f"Provide suggestions to optimize the following code in 2-3 lines:\n\n{code}"
        print("Running Ollama...")
        response = call_ollama(prompt)
        return response
    else:
        chat_session = model.start_chat(history=[])
        print("Running Gemini...")
        response = chat_session.send_message(f"just provide suggestion to optimise the code in 2-3 lines:\n\n{code}")
        return response.text

def error_code(code,modelr):
    if modelr=='llama':
        prompt = f"Detect error in this code. Specify the line number, how to fix it briefly, or if no error is present, say 'No Error!':\n\n{code}"
        response = call_ollama(prompt)
        return response
    else:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"Detect error in this code. Specify the line number, how to fix it briefly, or if no error is present, say 'No Error!':\n\n{code}")
        return response.text

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.json
    language = data.get('language')
    modelr=data.get('modelr')
    code = data.get('code')

    if language not in ['c', 'cpp', 'java', 'python']:
        return jsonify({'error': 'Unsupported language'}), 400
    output, error = execute_code(language,code,modelr)
    suggestions = optimize_code(code,modelr)
    
    return jsonify({'output': output, 'error': error, 'suggestions': suggestions})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
