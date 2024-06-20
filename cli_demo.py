from agents.chat_db import ChatDBAgent
# 日志配置
# from configs import log_config
# logger = log_config.logger

def chat_db_agent():
    human_icon = "\U0001F468"
    ai_icon = "\U0001F916"

    agent_with_chat_history = ChatDBAgent.cli_chat_db()
    while True:
        # text_input = input("User: ")
        task = input(f"{ai_icon}：有什么可以帮您？\n{human_icon}：")
        if task.strip().lower() == "quit":
            break
        reply = agent_with_chat_history.invoke(
            {"input": task},
            config={"configurable": {"session_id": "test-session1"}},
        )
        print(reply)
        output_only = reply['output']

        print(f"{ai_icon}：{output_only}\n")


def chat_db_by_db_executor():
    human_icon = "\U0001F468"
    ai_icon = "\U0001F916"
    db_executor = ChatDBAgent.create_sql_executor()
    while True:
        # text_input = input("User: ")
        task = input(f"{ai_icon}：有什么可以帮您？\n{human_icon}：")
        if task.strip().lower() == "quit":
            break
        reply = db_executor.invoke(
            {"input": task}
        )
        print(reply)
        output_only = reply['output']

        print(f"{ai_icon}：{output_only}\n")


if __name__ == '__main__':
    chat_db_agent()
    # chat_db_by_db_executor()
