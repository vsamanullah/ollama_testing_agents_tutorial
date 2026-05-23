# Video 2: Python + LangChain Integration with Ollama

This folder contains all the code from Video 2 of the "AI in Testing" series.

## 📁 Files Overview

1. **ollama__generate__simple.py** - Basic Ollama API calls using requests library for Generate functionality
2. **ollama__chat__simple.py** - Basic Ollama API calls using requests library for Chat functionality
3. **ollama__test__with__env.py** - Using environment variables with .env file
3. **ollama__langchain.py** - Basic LangChain + Ollama integration
4. **streamlit__llm__app.py** - Interactive web UI for LLM testing assistant

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.10 or higher installed
- Ollama installed and running (from Video 1)
- A code editor (VS Code or PyCharm recommended)

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```powershell
# Create file by name  .env 
```

Your `.env` file should contain:
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
API_TIMEOUT=30
STREAM_RESPONSE=false
MAX_RETRIES=3
```

### 5. Verify Ollama is Running

Open browser and go to: http://localhost:11434

You should see: "Ollama is running"

## 🎯 Running the Scripts

### Script 1: Basic API Call
```powershell
python ollama_generate_simple.py
python ollama_chat_simple.py
```
This demonstrates direct API calls to Ollama without any frameworks.

### Script 2: Environment Variables
```powershell
python ollama_test_with_env.py
```
Shows how to use .env file for configuration management.

### Script 3: LangChain Basics
```powershell
python ollama_langchain.py
```
### Script 4: Streamlit Interactive App
```powershell
streamlit run streamlit_llm_app.py
```
Interactive web interface for your LLM testing assistant. Opens automatically in your browser at http://localhost:8501

**Features:**
- User-friendly web interface
- Text input for queries
- Beautiful formatted responses
- Loading indicators
- No coding required for end-users

## What Each Script Does

| Script | Purpose | Key Concepts |
|--------|---------|--------------|
| `ollama_generate_simple.py` | Direct Generate API calls | requests library, JSON handling |
| `ollama_chat_simple.py` | Direct Chat API calls | requests library, JSON handling |
| `ollama_test_with_env.py` | Configuration management | python-dotenv, environment variables |
| `streamlit_llm_app.py` | Interactive web UI | Streamlit, web interface, user interaction |

## Running the scripts

| Script | Running |
|--------|---------|
| `ollama_generate_simple.py` | python ollama_generate_simple.py | 
| `ollama_chat_simple.py` | python ollama_chat_simple.py  | 
| `ollama_test_with_env.py` | python  ollama_test_with_env.py | 
| `streamlit_llm_app.py` |  streamlit run streamlit_llm_app.py | 

## Tips

- **Experiment:** Modify the prompts to see different outputs
- **Try Different Models:** Change `OLLAMA_MODEL` in .env to try other models
- **Adjust Temperature:** Lower = more focused, Higher = more creative
- **Add Features:** Extend the TestingGenerator class with your own methods

## Resources

- **LangChain Documentation:** https://python.langchain.com
- **Ollama API Docs:** https://github.com/ollama/ollama/blob/main/docs/api.md
- **Python dotenv:** https://pypi.org/project/python-dotenv/
- **Streamlit Documentation:** https://docs.streamlit.io

## Contributing

Found an issue or want to improve the code? Feel free to submit a pull request!

---

**Happy Testing! 🚀**
