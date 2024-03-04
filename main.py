# If you store memory at llm model
# You use 'ConversationSummaryMemory' SummaryMemory 
# ConverstionSummaryMemory is not just storage.
# That is to give a summary of the conversations.
# Initially, SummaryMemory take more token and space more than other conversation.
# However, as time passes and conversations accumulate, SummaryMemory can be helpful in anwsering.
from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature= 0.1)

memory = ConversationSummaryMemory(llm=llm)
#llm = llm means this code will be needs money

def add_message(input, output):
    memory.save_context({"input": input}, {"output": output})

def get_histroy():
    return memory.load_memory_variables({})

add_message("Hi I'm Chandon, I live in South Korea", "Wow that is so nice!")

# -- next code --

add_message("South Korea is so nice country!", "I want to travel South Korea!")

# -- next code --

get_histroy()
# This conclusion is a summary of the data I wrote down in memory.
