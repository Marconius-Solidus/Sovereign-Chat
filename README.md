
# Streamlit + Langchain + LLama.cpp w/ Mistral fine-tuned LLM

# How to run locally
## Step by Step instructions

The setup assumes you have `python` already installed and `venv` module available.

1. Download the code or clone the repository.
```bash
git clone https://github.com/Marconius-Solidus/Chatbot.git
```
3. Inside the root folder of the repository, initialize a python virtual environment:
```bash
python -m venv venv
```
3. Activate the python environment:
```bash
source venv/bin/activate
```
4. Install required packages (`langchain`, `llama.cpp`, and `streamlit`):
```bash
pip install -r requirements.txt
```
5. Start `streamlit`:
```bash
streamlit run main.py
```
6. The `Mistral7b` quantized model from `huggingface` will be downloaded and cached locally from the following link:
[mistral-7b-instruct-v0.1.Q4_0.gguf](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf)

# Screenshot

![Screenshot from 2023-10-23 20-00-09](https://github.com/lalanikarim/ai-chatbot/assets/1296705/65ceac4a-f3c0-41db-8519-182076afb215)
