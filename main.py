from langchain.chat_models import ChatOpenAI
#FewShotPromptTemplate provieds specific prompt templates. Like, Just Capital letter or Just small letter, space, comma, etc..
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code
from langchain.globals import set_llm_cache, set_debug
#If you use 'cache'. you can save LM(Langauge Model) answer.
#'debug' is show the log answer. and also show the model name
from langchain.cache import InMemoryCache, SQLiteCache
# if you want cache save at the Memory, You use 'SQLiteCache'

#set_llm_cache(InMemoryCache())
# this is simpe Cache

#set_debug(True)
# this is debug 

set_llm_cache(SQLiteCache("cache.db"))
# this is cache save at the Memory. (SQLiteCache("[name]"))
# if you use this code. 'cache.db' will appear in the 'file list' next to it.

chat = ChatOpenAI(
    temperature=0.1,
)

chat.predict("How do you make italian pasta")

# --- next code ---

chat.predict("How do you make italian pasta")
#This answer is didn't say LLM, Just Loaded at save LM(Langauge Model). We called this 'cache'
#Why use cache? == Save LLM is Save time is Save Money.