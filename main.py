# Connect memory to the chain.
# LLM chain == off-the-shelf chain.
# The off-the-shelf chain refer to general purpose chain. And this chain is very distributed in langchain.
# off-the-shelf chain is quick to use. However, that cannot customize it.

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
# Upper Code is make llm model more specific.
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# last time we just write prompt text. So, This time we send message 'text' at Chat
# 'MessagesPlaceholder' is show organize messages. Like, AI : ~~~~, Human : ~~~~.

llm = ChatOpenAI(
    temperature=0.1
)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit= 120,
    memory_key="chat_history",
    # Insert the contents of the template into conversation Suammy memory.
    # Insert "chat_history" into memory, LLMChain can now use the memory.
    return_messages=True,
    # Upper code mean do not change 'string'. Just use 'text'
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI talking to a human"),
    MessagesPlaceholder(variable_name="chat_history"),
    # 'ConversationSummaryBufferMemory' give message -> 'AI' -> 'Human' -> 'System'
    # The MessagesPlaceholder intercept message and make many class.
    ("human", "{question}"),
])

def load_memory(_):
    # '_' mean omit input code.
    return memory.load_memory_variables({})["chat_history"]
# Upper code is def for get memory variable
# 'RunnablePassthrought.assign()' must take at least one argument. So, we need to enter input.
# So, we give input in function, and print(input)

chain = RunnablePassthrough.assign(chat_history = load_memory) | prompt | llm
# Upper code is make chain yourself.
# When starting a chain. RunnablePassthrought.assign starts load_memory first, then prompts and then llm.
# 'RunnablePassthrought' function allows you to use a function before the prompt is format.
# And also, we can assign any value we want to that function 'chat_history = load_memory'
# And that variable is given to the prompt.
# 'RunnablePassthrought.assign()' must take at least one argument. So, we need to enter input.

chain.invoke({"question" : "My name is chandon"})
# Upper Code == dictionary, the first input item provided in the chain.