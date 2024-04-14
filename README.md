# Sovereign Chat
## FOSS AI chatbot that answers all questions about online privacy & security

### What I used?
[Streamlit](https://github.com/streamlit/streamlit) + [Embedchain](https://github.com/embedchain/embedchain/tree/main) + [GPT4ALL](https://gpt4all.io/index.html)
### Data
I imported data in forms of URLs that are ebmbeded into LLM. Right now, while I'm testing multiple LLMs, I'm only using small [dataset](https://gist.githubusercontent.com/Marconius-Solidus/1364954319a117c654cda37fc6b2f96e/raw/19281dc976e499911d0b94093c3bb3f6c9d18866/gistfile1.csv) with 4 URLs so the embedding doesn't take long.

In the meantime I'm building larger [dataset](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Data.csv). I would appreciate any contributions to it.

# Problem with AI API and running models locally
Right now, I'm facing problems with running models. Only functioning AI API was the one from OpenAI, but I don't want to use that one because of data collecting, censorship and overall OpenAI policy. I also tried to use GPT4ALL, but I only got the response in Terminal. The response looked like this - pretty wierd.

# How to run it yourself:
## Step by Step instructions

The setup assumes you have `python` already installed.

1. Download the code or clone the repository.
```bash
git clone https://github.com/Marconius-Solidus/Sovereign-Chat.git
```

2. Install required packages
```bash
pip install -r requirements.txt
```
3. Start `streamlit`:
```bash
streamlit run main.py
```

# Preview

![Screenshot](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Screenshot)
