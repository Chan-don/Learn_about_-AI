# This memory 'ConversationKGMemory' is extracts the most important summary.
from langchain.memory import ConversationKGMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature= 0.1,)

memory = ConversationKGMemory(
    llm=llm,
    return_messages=True,
)

def add_message(input, output):
    memory.save_context({"input" : input}, {"output" : output})

add_message("Hi, my name is Chandon, I live in South Korea", "Wow that is nice!!")

# -- next code --

memory.load_memory_variables({"input" : "who is Chandon?"})
# why write {"input" : "who is Chandon?"}, That is a way of asking to the memory what it knows about a specific node on the knowledge graph.

# -- next code --

add_message("Chandon likes jimin", "Wow that is great!")

# -- next code --

memory.load_memory_variables({"input": "Report Chandon."})