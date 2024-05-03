from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents.agent import AgentExecutor


class MemoryChatMessageHistory:

    @classmethod
    def manage_chat_history(cls, agent_executor: AgentExecutor) -> RunnableWithMessageHistory:
        history = ChatMessageHistory(session_id="test-session")
        agent_with_chat_history = RunnableWithMessageHistory(
            agent_executor,
            # This is needed because in most real world scenarios, a session id is needed
            # It isn't really used here because we are using a simple in memory ChatMessageHistory
            lambda session_id: history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return agent_with_chat_history
