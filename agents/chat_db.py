
from langchain_openai import ChatOpenAI
# 加载环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_core.runnables.history import RunnableWithMessageHistory
from .chat_manager import ChatAgentManager

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    # 将 seed 参数作为模型参数传递
    model_kwargs={
        "seed": 666
    }
)


class ChatDBAgent:
    @classmethod
    def db_gpt(cls) -> RunnableWithMessageHistory:
        """
         创建一个聊天管理器实例，并执行查询及管理聊天历史。

         这是一个类方法，用于初始化和管理聊天代理，该代理执行必要的语言模型逻辑和聊天历史的管理。

         返回:
             RunnableWithMessageHistory: 一个执行聊天操作并管理历史记录的对象。
         """
        # 执行查询并管理聊天历史
        chat_manager = ChatAgentManager(llm=llm)
        return chat_manager.execute_and_manage()

    @classmethod
    def chat_db(cls, input: str) -> str:
        """
        处理输入字符串，并通过聊天代理生成响应。
        此方法利用 ChatAgentManager 来执行查询并管理聊天历史，然后调用聊天代理
        的 invoke 方法来处理输入，并生成输出。
        Args:
            input (str): 输入到聊天代理的字符串。

        Returns:
            str: 聊天代理处理后的输出结果。
        该方法主要以接口的形式用户调用
        """
        # 执行查询并管理聊天历史
        chat_manager = ChatAgentManager(llm=llm)
        agent_with_chat_history = chat_manager.execute_and_manage()

        reply = agent_with_chat_history.invoke(
            {"input": input},
            config={"configurable": {"session_id": "dbgpt-session"}},
        )
        output = reply['output']
        return output


if __name__ == '__main__':
    output_only = ChatDBAgent.db_gpt("把我们系统的用户信息告诉我")
    # output_only = query_db.nlp_query_db("给我插入一条用户数据")
    print("------------------------")
    print(output_only)
