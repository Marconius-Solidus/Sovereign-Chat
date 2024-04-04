# Sovereign Chat
## FOSS AI chatbot that answers all questions about online privacy & security

### What we used?
[Streamlit](https://github.com/streamlit/streamlit) + [Embedchain](https://github.com/embedchain/embedchain/tree/main) + [HuggingFace](https://huggingface.co/) API

### Data
We imported data in forms of URLs that are ebmbeded into LLM. Right now, while we are testing multiple LLMs, we are only using small [dataset](https://gist.githubusercontent.com/Marconius-Solidus/1364954319a117c654cda37fc6b2f96e/raw/19281dc976e499911d0b94093c3bb3f6c9d18866/gistfile1.csv) with 4 URLs so the embedding doesn't take long.

In the meantime we are building larger dataset. Right now, we have over 1200 URLs in the dataset that is not public yet.

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
2. Open main.py and add your HuggingFace code to line 16 in the `"hf_xxx"`. You can get one [here](https://huggingface.co/settings/tokens).

```bash
16 os.environ["HUGGINGFACE_ACCESS_TOKEN"]= "hf_xxx"
```
3. Install required packages
```bash
pip install -r requirements.txt
```
4. Start `streamlit`:
```bash
streamlit run main.py
```

# Preview

![Screenshot](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Screenshot)
