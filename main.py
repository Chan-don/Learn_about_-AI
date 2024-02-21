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
    
p = CommaOutputParser()

p.parse("Hello, how, are , you")

# this code is how to run the OutputParser.
#-- plus code --

template = ChatPromptTemplate.from_messages([
    ("system", "You are a list generating machine. Every thing you are asked will be answered with a comma, list of max {max_items} in lowercase. DO NOT reply with anything else."),
    ("human", "{question}"),
])

prompt = template.format_messages(
    max_items = "5",
    question = "What are the color"
)

result = chat.predict_messages(prompt)

p = CommaOutputParser()

p.parse(result.content)

# this code is how to use the OutputParser at Ai chat.