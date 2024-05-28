import gradio as gr
from agents import ChatDBAgent





def predict(message, history):
    """后续会重构，过渡阶段"""
    print(message)
    response = ChatDBAgent.cli_chat_db(message)
    partial_message = ""
    print(response)
    for chunk in response:
        if chunk is not None:
            partial_message = partial_message + chunk
            yield partial_message


gr.ChatInterface(
    predict,
    title="CHAT_DB",
    description="Ask DB_BOT any question",
    theme="soft"
    ).launch()
