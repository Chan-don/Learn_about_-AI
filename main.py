# 'Conversation Buffer Memory'
# We must use memory!
# Why memory? Because, memory can store personal data.
# Langchain model and model doesn't have memory. So, we must store data using memory.
# Provides vivid conversation as if a person were speaking.
# This memory is simple. But, this memory unsuitable big data.

from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)

memory.save_context({"input" : "Hi!"}, {"output" : "Hi! How are you?"})

memory.load_memory_variables({})
# '\n' means change line.

# -- next code --
memory.save_context({"input" : "Hi!"}, {"output" : "Hi! How are you?"})

memory.load_memory_variables({})
# store

# -- next code --

memory.save_context({"input" : "Hi!"}, {"output" : "Hi! How are you?"})

memory.load_memory_variables({})
# store
# So, this situation shows that data is being store in memory