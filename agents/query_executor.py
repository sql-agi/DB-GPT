import os
from langchain_community.agent_toolkits import create_sql_agent
# 从URI创建SQLDatabase实例
# 这里的"../../../../../notebooks/Chinook.db"是数据库文件的相对路径
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from prompts.temple import DBExpert
from langchain.agents.agent import AgentExecutor
from utils import DatabaseUtils
class QueryExecutor:
    def __init__(self, llm):
        self.llm = llm
        self.db = SQLDatabase.from_uri(os.getenv("MYSQL_URL"))
        # self.db = SQLDatabase.from_uri(DatabaseUtils.create_mysql_url())
        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)

    def execute_query(self) -> AgentExecutor:
        """
        构造查询提示并创建 SQL 执行代理。

        此方法首先从 toolkit 获取当前的上下文环境。
        接着，获取数据库专家系统定义的聊天提示，根据当前上下文环境调整这些提示。
        最后，使用提供的语言模型(llm)、toolkit、和定制的提示来创建一个 SQL 查询执行代理。

        返回:
            Agent: 配置好的 SQL 执行代理，具备执行查询的能力并能详细记录操作过程。
        """
        context = self.toolkit.get_context()
        prompt = DBExpert.chat_prompt_message()
        prompt = prompt.partial(**context)
        return create_sql_agent(
            llm=self.llm,
            toolkit=self.toolkit,
            agent_type="openai-tools",
            prompt=prompt,
            verbose=True)
