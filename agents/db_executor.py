import os
from langchain_community.agent_toolkits import create_sql_agent
# 从URI创建SQLDatabase实例
# 这里的"../../../../../notebooks/Chinook.db"是数据库文件的相对路径
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from prompts.temple import DBExpert
from langchain.agents.agent import AgentExecutor
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ConversationSummaryBufferMemory
from langchain.agents import create_openai_tools_agent, create_tool_calling_agent

history = ChatMessageHistory(session_id="db-session")


class DBExecutor:
    def __init__(self, llm, db_uri=None):
        """
        初始化 DBExecutor 实例。
        参数:
            llm: 语言模型实例
            db_uri: 数据库 URI，如果未提供，则从环境变量 MYSQL_URL 中获取
        """
        self.llm = llm
        self.db = SQLDatabase.from_uri(db_uri or os.getenv("MYSQL_URL"))
        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)

    def create_sql_executor(self, is_change: bool) -> AgentExecutor:
        """
        构造查询提示并创建 SQL 执行代理。

        此方法首先从 toolkit 获取当前的上下文环境。
        接着，获取数据库专家系统定义的聊天提示，根据当前上下文环境调整这些提示。
        最后，使用提供的语言模型(llm)、toolkit、和定制的提示来创建一个 SQL 查询执行代理。

        返回:
            Agent: 配置好的 SQL 执行代理，具备执行查询的能力并能详细记录操作过程。
        """
        context = self.toolkit.get_context()
        prompt = DBExpert.chat_db_message()
        prompt = prompt.partial(**context)
        tools = self.toolkit.get_tools()
        if is_change:
            history.clear()
        memory = ConversationSummaryBufferMemory(
            llm=self.llm, memory_key="history", chat_memory=history, return_messages=True, max_token_limit=600
        )
        agent = create_openai_tools_agent(
            self.llm, tools, prompt)
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True,
            memory=memory
        )
        return agent_executor
