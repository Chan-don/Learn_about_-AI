from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate

chat = ChatOpenAI(
    temperature=0.1
    #temperature valuse high == creativity is high. 
)

template = PromptTemplate.from_template("What is the distance between {country_a} and {country_b}",)

prompt = template.format(country_a = "Korea", country_b = "USA")

chat.predict(prompt)

template = ChatPromptTemplate.from_messages([
    ("system", "Your are a geograpy expert. And you only reply in {language}."),
    ("ai", "Hi!, My name is {name}!"),
    ("human", "What is the distance between {country_a} and {country_b}. Also, what is your name?"),
])

# -- plus code --

prompt = template.format_messages(
    language = "Korean",
    name = "Chae Eun",
    country_a = "Korea",
    country_b = "USA",
)

chat.predict_messages(prompt)