# This time, use SummaryMemory by specifying a limit token. 
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.1)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=150,
    # Upper code 'max_token_limit' means limit message.
    return_messages=True
)

get_history()

# -- next code --

add_message("South korea is pretty!", "I want to visit Seoul!")

# -- next code --

get_history()
#Not reach limit yet.

# -- next code --

add_message("How far Seoul from Salt lake city?!", "I don't know! But, that is too far!!!")

# -- next code --

get_history()
#Not reach limit yet.

# -- next code --

add_message("How many people live Seoul and Salt Lake City?", "I don't know! But, many people are live Seoul and Salt Lake City!")
# Push multiple times until the limit token is reached.

# -- next code --

get_history()
# Reach limit token!
# When consuming tokens up tp the limit tokens.
# Old data is summarized.