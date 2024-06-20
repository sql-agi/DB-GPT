from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from prompts.messages import SYSTEM_QUERY_MESSAGE, SYSTEM_DB_MESSAGE, AI_MESSAGE
from langchain_core.messages import AIMessage

class DBExpert:

    @classmethod
    def chat_prompt_message(cls) -> ChatPromptTemplate:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_QUERY_MESSAGE),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )
        return prompt

    @classmethod
    def chat_db_message(cls) -> ChatPromptTemplate:
        prompt = ChatPromptTemplate.from_messages(
            messages=[
                ("system", SYSTEM_DB_MESSAGE),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
                AIMessage(content=AI_MESSAGE),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        return prompt

