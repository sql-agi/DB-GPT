import os
from langchain_community.agent_toolkits import create_sql_agent
# 从URI创建SQLDatabase实例
# 这里的"../../../../../notebooks/Chinook.db"是数据库文件的相对路径
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from prompts.temple import DBExpert

class QueryExecutor:
    def __init__(self, llm):
        self.llm = llm
        self.db = SQLDatabase.from_uri(os.getenv("MYSQL_URL"))
        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)

    def execute_query(self):
        context = self.toolkit.get_context()
        prompt = DBExpert.chat_prompt_message()
        prompt = prompt.partial(**context)
        return create_sql_agent(
            llm=self.llm,
            toolkit=self.toolkit,
            agent_type="openai-tools",
            prompt=prompt,
            verbose=True)
