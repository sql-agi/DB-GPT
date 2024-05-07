from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents.agent import AgentExecutor


class MemoryChatMessageHistory:

    @classmethod
    def manage_chat_history(cls, agent_executor: AgentExecutor) -> RunnableWithMessageHistory:
        """
            创建并返回一个关联了聊天历史管理的执行代理。
            此类方法首先创建一个聊天消息历史实例，随后将此历史与提供的执行代理关联起来，形成一个能够同时管理聊天历史的执行代理。
            所创建的代理适用于需要追踪会话历史的场景，例如在对话系统中保存会话内容。
            参数:
                agent_executor (AgentExecutor): 已有的代理执行器，负责执行具体的聊天任务。
            返回:
                RunnableWithMessageHistory: 一个结合了聊天历史管理的执行代理，可以在执行聊天操作时维护历史记录。
            注解:
                在实际应用中，通常需要会话ID来跟踪和管理不同用户的聊天历史。这里虽然使用了简单的内存中聊天历史，
                但结构设计上保留了使用会话ID的可能性，以便在更复杂的实现中使用。
            """
        history = ChatMessageHistory(session_id="dbgpt-session")
        agent_with_chat_history = RunnableWithMessageHistory(
            agent_executor,
            # This is needed because in most real world scenarios, a session id is needed
            # It isn't really used here because we are using a simple in memory ChatMessageHistory
            lambda session_id: history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return agent_with_chat_history
