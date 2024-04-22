# Sovereign Chat
## Open Source AI Chatbot that answers all questions about online Privacy & Security
### Why Online Privacy & Security?

ONLINE PRIVACY & SECURITY IS NO LONGER JUST PREVENTION.

There is a high chance that you've opted for the most convenient way of using the Internet. If you use any Big Tech software you're putting yourself into danger of data loss, surveillance, blackmail and more.

Everyday when you use the Internet without the right tools, you get surveilled and spied on. Your data gets collected by Big Tech Corporations and gets sold to marketing companies and governments.

After the Section 702 has been reauthorized, mass surveillance and spying will only rise.

Protecting privacy is becoming harder to do and simultaneously will become more and more important to do so. Even if you think you're not a criminal and have nothing to hide, this can change overnight.

### What is Sovereign Chat?

As I studied digital privacy and security, I understood how complicated it can become for someone who isn't technical type. And even if you are, there are only few places where you can find all the information together. Usually you have to go trough multiple YouTube videos and some blogs to be sure about something.

That's why I decided to build Sovereign Chat, that will focus on digital Privacy & Security.

This Chatbot will won't be just another ChatGPT wrapper. ChatGPT stores your data and probably checks if you had any suspicious prompts. Because of this Sovereign Chat will be running locally with either GPT4ALL or some Ollama LLM.


### What I used?
[Chainlit](https://docs.chainlit.io/get-started/overview) + [Embedchain](https://github.com/embedchain/embedchain/tree/main) + [Ollama](https://ollama.com/)
### Data
I imported data in forms of URLs that are embedded into LLM. Right now, while I'm testing multiple LLMs and embeddings, I'm only using small [dataset](https://gist.githubusercontent.com/Marconius-Solidus/1364954319a117c654cda37fc6b2f96e/raw/19281dc976e499911d0b94093c3bb3f6c9d18866/gistfile1.csv) with 4 URLs so the embedding doesn't take long.

In the meantime I'm building larger [dataset](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Data.csv), which now includes more than 5000 resources.

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
chainlit run main.py
```

# Preview

![Screenshot](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Screenshot)
