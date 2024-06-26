import gradio as gr
from agents import ChatDBAgent





def predict(message, history):
    """后续会重构，过渡阶段"""
    print(message)
    response = ChatDBAgent.db_gpt(message)
    partial_message = ""
    print(response)
    for chunk in response:
        if chunk is not None:
            partial_message = partial_message + chunk
            yield partial_message


gr.ChatInterface(
    predict,
    title="校园智能管理助手",
    description="Ask Campus Intelligent Management Assistant any question",
    theme="soft"
    ).launch(server_name="0.0.0.0", server_port=7860)
