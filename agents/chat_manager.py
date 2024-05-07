from .query_executor import QueryExecutor
from memory.memory_chat_message_history import MemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


class ChatAgentManager:
    def __init__(self, llm):
        self.query_executor = QueryExecutor(llm=llm)

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
