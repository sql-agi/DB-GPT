from .query_executor import QueryExecutor
from memory.memory_chat_message_history import MemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


class ChatAgentManager:
    def __init__(self, llm, db_uri=None):
        """
        初始化 ChatAgentManager 实例。
        参数:
            llm: 语言模型实例
            db_uri: 数据库 URI，可选。如果未提供，则从环境变量 MYSQL_URL 中获取
        """
        self.query_executor = QueryExecutor(llm=llm, db_uri=db_uri)

    def execute_and_manage(self) -> RunnableWithMessageHistory:
        """
        执行查询并对返回的代理进行聊天历史管理。

        此方法首先通过 `query_executor` 执行查询，获取一个代理执行器。
        然后，将该代理执行器传递给 `MemoryChatMessageHistory` 类的 `manage_chat_history` 方法，
        以便管理聊天历史并返回一个能够持续执行和记录聊天历史的对象。

        返回:
            RunnableWithMessageHistory: 一个能执行聊天操作并维护聊天历史的对象。
        """
        # 执行查询并管理聊天历史
        agent_executor = self.query_executor.execute_query()
        agent_with_chat_history = MemoryChatMessageHistory.manage_chat_history(agent_executor)
        return agent_with_chat_history
