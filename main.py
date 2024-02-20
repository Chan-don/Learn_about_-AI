from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    temperature=0.1
    #temperature valuse high == creativity is high. 
)

from langchain.schema import HumanMessage, AIMessage, SystemMessage
#HumanMessage == we know things.
#AIMessage == we sent to AI
#SystemMessage == provide to setting

messages = [
    SystemMessage(content="Your are a geograpy expert. And you only reply in Korean."),
    AIMessage(content="안녕!, 나는 미래야!"),
    HumanMessage(content="What is the distance between seoul and New york city. Also, what is your name?"),
]

chat.predict_messages(messages)