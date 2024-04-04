# Sovereign Chat
## FOSS AI chatbot that answers all questions about online privacy & security

### What we used?
Streamlit + Embedchain + HuggingFace API

# Problem with AI API and running models localy
Right now, we are facing problems with running models. Only functioning AI API was the one from OpenAI, but we don't want to use that one because of data collecting, censorship and overall OpenAI policy.

We would like you to try out implementing other [LLMs](https://docs.embedchain.ai/components/llms#hugging-face-inference-endpoint) so we can figure out where the bug is. 

# How to it yourself:
## Step by Step instructions

The setup assumes you have `python` already installed.

1. Download the code or clone the repository.
```bash
git clone https://github.com/Marconius-Solidus/Sovereign-Chat.git
```
2. Open main.py and add your HuggingFace code to line 16 in the `""`. You can get one [here](https://huggingface.co/settings/tokens).

```bash
os.environ["HUGGINGFACE_ACCESS_TOKEN"]= ""
```
3. Install required packages
```bash
pip install -r requirements.txt
```
4. Start `streamlit`:
```bash
streamlit run main.py
```

# Screenshot

![Screenshot](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Screenshot)
