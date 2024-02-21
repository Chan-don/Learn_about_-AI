from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(
    temperature=0.1
    #temperature valuse high == creativity is high. 
)

#-- plus code --

from langchain.schema import BaseOutputParser

class CommaOutputParser(BaseOutputParser):

    def parse(self, text):
        items = text.strip().split(",")
        return list(map(str.strip,items))

# this code is how to run the OutputParser.
#-- plus code --

template1 = ChatPromptTemplate.from_messages([
    ("system", "You are a list generating machine. Every thing you are asked will be answered with a comma, list of max {max_items} in lowercase. DO NOT reply with anything else."),
    ("human", "{question}"),
])

# this code is how to use the OutputParser at Ai chat.
#-- plus code --

Chain1 = template1|chat|CommaOutputParser()
Chain1.invoke({
    "max_items": 5,
    "question": "What are the sports car model name?"
})

# | is best code in here, that can divide code each other.
# So, first you write the each part. and collect to using by '|'code.