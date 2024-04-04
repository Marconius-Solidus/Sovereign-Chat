# Sovereign Chat
## FOSS AI chatbot that answers all questions about online privacy & security

### What I used?
[Streamlit](https://github.com/streamlit/streamlit) + [Embedchain](https://github.com/embedchain/embedchain/tree/main) + [HuggingFace](https://huggingface.co/) API

### Data
We imported data in forms of URLs that are ebmbeded into LLM. Right now, while we are testing multiple LLMs, we are only using small [dataset](https://gist.githubusercontent.com/Marconius-Solidus/1364954319a117c654cda37fc6b2f96e/raw/19281dc976e499911d0b94093c3bb3f6c9d18866/gistfile1.csv) with 4 URLs so the embedding doesn't take long.

In the meantime I'm building larger [dataset](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/Data.csv). I would appreciate any contributions to it.

# Problem with AI API and running models localy
Right now, I are facing problems with running models. Only functioning AI API was the one from OpenAI, but I don't want to use that one because of data collecting, censorship and overall OpenAI policy.

## The issue
After running embedding without problems you can ask the question, but you won't get answer and this error will show in Terminal.
```bash
File "/home/marconius/.local/lib/python3.12/site-packages/embedchain/llm/huggingface.py", line 36, in get_llm_model_answer
    return HuggingFaceLlm._get_answer(prompt=prompt, config=self.config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/marconius/.local/lib/python3.12/site-packages/embedchain/llm/huggingface.py", line 48, in _get_answer
    raise ValueError("Either model or endpoint must be set in config")
ValueError: Either model or endpoint must be set in config
```

## How to fix this?
Honestly I have no idea. I tried re-installing all the packages, even different OSs and running in clean VMs but still got the same error. I also tried using Mistral API, but I got no answer from the chatbot, but also no error. Last resort was [GPT4LL](https://docs.embedchain.ai/components/embedding-models#gpt4all), but on main PC I got error that `BaseLlmConfig` couldn't be imported. In the VM no error was reported, but I also got no answer.

I would like you to try out implementing other [LLMs](https://docs.embedchain.ai/components/llms) so I can figure out where the bug is. To change what LLM is used, just change the [config.yaml](https://github.com/Marconius-Solidus/Sovereign-Chat/blob/main/config.yaml) file. You can also comment the API key like this`#os.environ["HUGGINGFACE_ACCESS_TOKEN"]= "hf_xxx"` or change it to different `provider os.environ["MISTRAL_API_KEY"] = "xxx"`.

# How to run it yourself:
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
