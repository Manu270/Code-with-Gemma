# Code-with-Gemma

AI-Driven Code Compilation and Optimization


This project introduces an AI-powered code compiler that provides real-time code compilation, error detection, and optimization recommendations. Developed using Python, Flask, HTML, and CSS, this compiler supports four major programming languages—Python, Java, C, and C++. It employs both online and offline AI models, Gemini and Ollama, for code analysis and suggestions.

## Features

- **Multi-Language Support**: Compile and optimize code in Python, Java, C, and C++.
- **AI-Driven Optimization**: Leverages Gemini (cloud-based) and Ollama (offline) models to provide optimization suggestions.
- **Error Detection**: Provides real-time feedback on syntax and runtime errors.
- **Performance Metrics**: Tracks execution time and time taken to generate optimization suggestions.

## Technology Stack

- **Frontend**: HTML, CSS, Ace Editor (for code syntax highlighting and autocompletion).
- **Backend**: Python, Flask
- **AI Models**:
  - **Gemini**: Online model with real-time suggestions.
  - **Ollama**: Offline model for environments without internet access.

## Installation

### Prerequisites

- Python 3.x
- Flask
- C, C++, Java compilers (e.g., `gcc`, `g++`, and Java JDK)
- Google Generative AI API Key (for Gemini model)
- Necessary libraries:
  ```bash
  pip install flask
  ```

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd CodeCompiler
   ```
3. Set up your API key for the Gemini model in the backend code where indicated.
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open a web browser and go to `http://localhost:5000`.

## Usage

1. **Select Language**: Choose the programming language (Python, Java, C, C++).
2. **Choose Model**: Select between Gemini (online) or Ollama (offline).
3. **Enter Code**: Write or paste code in the editor.
4. **Run Code**: Press the "Run" button to compile and execute code.
5. **View Results**: See output, errors, and optimization suggestions with execution metrics.

## Architecture

- **Gemini Model**: Cloud-based real-time optimization via API.
- **Ollama Model**: Offline model powered by Llama 3.2 for local optimization.

## Example Outputs

- **Error Detection**: Indicates syntax and runtime issues with line numbers.
- **Optimization Suggestions**: Recommendations for improving performance and efficiency.
- **Performance Metrics**: Tracks execution time and memory usage.

## Screenshots

### User Interface Overview
<img width="1470" alt="Screenshot 2024-10-25 at 5 23 37 PM" src="https://github.com/user-attachments/assets/cbf4e948-3a39-43b9-8e2c-2ec691bf0cee">


### Error Detection and Optimization
<img width="1470" alt="Screenshot 2024-10-25 at 5 25 08 PM" src="https://github.com/user-attachments/assets/786a9f44-d4a6-4ba4-b9e9-128a2ff4b257">


## Future Enhancements

- Add support for additional programming languages.
- Expand the user interface with more customization options.
- Improve AI model capabilities with future updates.



