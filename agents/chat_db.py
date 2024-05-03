from langchain_community.agent_toolkits import create_sql_agent
# 从URI创建SQLDatabase实例
# 这里的"../../../../../notebooks/Chinook.db"是数据库文件的相对路径
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
# 加载环境变量
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

from prompts.temple import DBExpert
from memory.memory_chat_message_history import MemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os
from .query_executor import QueryExecutor

llm = ChatOpenAI(model="gpt-4")


class ChatDBAgent:
    @classmethod
    def chat_db(cls) -> RunnableWithMessageHistory:
        query_executor = QueryExecutor(llm=llm)
        # 调用 execute_query 方法
        agent_executor = query_executor.execute_query()
        # 增加记忆
        agent_with_chat_history = MemoryChatMessageHistory.manage_chat_history(agent_executor)
        return agent_with_chat_history

    @classmethod
    def db_gpt(cls, input: str) -> RunnableWithMessageHistory:
        query_executor = QueryExecutor(llm=llm)
        # 调用 execute_query 方法
        agent_executor = query_executor.execute_query()
        # 增加记忆
        agent_with_chat_history = MemoryChatMessageHistory.manage_chat_history(agent_executor)

        reply = agent_with_chat_history.invoke(
            {"input": input},
            config={"configurable": {"session_id": "nlp2sql-session"}},
        )
        output = reply['output']
        return output


if __name__ == '__main__':
    output_only = ChatDBAgent.db_gpt("把我们系统的用户信息告诉我")
    # output_only = query_db.nlp_query_db("给我插入一条用户数据")
    print("------------------------")
    print(output_only)
