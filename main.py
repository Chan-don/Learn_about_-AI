# A lot of data takes a lot of buffers.
# A lot of buffers requires a lot of data, and a lot of data requires a lot of execution time and moeny.
# So, our solution is store 1 to 5 data. And add 6 data(New data). And then delete first data(old data) at the memory.
# We use 'ConversationBufferWindowMeomory' WindowMemory
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    return_messages= True,
    k=4,
)

def add_message(input, output):
    memory.save_context({"input" : input}, {"output" : output})

add_message(1,1)

# -- next code --
add_message(2,2)
add_message(3,3)
add_message(4,4)

# -- next code --

memory.load_memory_variables({})
# what is '({})' ?
# () is do function code. {} is api.

# -- next code --

# Upper conclusion is add_message() 1 to 4
# But, we add new message
add_message(5,5)

# -- next code --

memory.load_memory_variables({})
# So, delete (1,1) at memory(old memory).
# Add, (5,5) at memory(new memory)
# This is a way protect memory from excessive buffering.