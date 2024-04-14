import csv
import queue
import threading
from io import StringIO

import os
import requests
import streamlit as st

from embedchain import App
from embedchain.config import BaseLlmConfig
from embedchain.helpers.callbacks import (StreamingStdOutCallbackHandlerYield,
                                          generate)

# Load LLM from
@st.cache_resource
def sovereign_ai():
    app = App.from_config(config_path="config.yaml")
    return app

# Function to read the CSV file row by row
def read_csv_row_by_row(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row

# Function to add the data
@st.cache_resource
def add_data_to_app():
    app = sovereign_ai()
    url = "https://gist.githubusercontent.com/Marconius-Solidus/1364954319a117c654cda37fc6b2f96e/raw/19281dc976e499911d0b94093c3bb3f6c9d18866/gistfile1.csv"  # noqa:E501
    response = requests.get(url)
    csv_file = StringIO(response.text)
    for row in csv.reader(csv_file):
        if row and row[0] != "url":
            app.add(row[0], data_type="web_page")


app = sovereign_ai()
add_data_to_app()

# AI avatara img
assistant_avatar_url = "https://avatars.githubusercontent.com/u/165185399?s=96&v=4"

# Heading
st.title("Sovereign Chat")

# Caption
styled_caption = '<p style="font-size: 17px; color: #aaa;">An <a href="https://sovereignoutcomes.com/">Sovereign Outcomes</a> FOSS app!</p>'  # noqa: E501
st.markdown(styled_caption, unsafe_allow_html=True) 

# Opening message from asisstant
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
                Hi, I'm Sovereign AI. I can answer all the questions about digital Privacy & Security.
            """, 
        }
    ]

# Magic, do not change
for message in st.session_state.messages:
    role = message["role"]
    with st.chat_message(role, avatar=assistant_avatar_url if role == "assistant" else None):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about digital Privacy & Security.!"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar=assistant_avatar_url):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("Thinking...")
        full_response = ""

        q = queue.Queue()

        def app_response(result):
            config = BaseLlmConfig(stream=True, callbacks=[StreamingStdOutCallbackHandlerYield(q)])
            answer, citations = app.chat(prompt, config=config, citations=True)
            result["answer"] = answer
            result["citations"] = citations

        results = {}
        thread = threading.Thread(target=app_response, args=(results,))
        thread.start()

        for answer_chunk in generate(q):
            full_response += answer_chunk
            msg_placeholder.markdown(full_response)

        thread.join()
        answer, citations = results["answer"], results["citations"]
        if citations:
            full_response += "\n\n**Sources**:\n"
            sources = list(set(map(lambda x: x[1]["url"], citations)))
            for i, source in enumerate(sources):
                full_response += f"{i+1}. {source}\n"

        msg_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
