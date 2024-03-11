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
    return_messages=True,
    # Upper code mean do not change 'string'. Just use 'text'
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI talking to a human"),
    MessagesPlaceholder(variable_name="history"),
    # 'ConversationSummaryBufferMemory' give message -> 'AI' -> 'Human' -> 'System'
    # The MessagesPlaceholder intercept message and make many class.
    # "chat_history" is no longer needed because the default memory key is "History"
    # So, we can replace "chat_history" to "history"
    ("human", "{question}"),
])

def load_memory(_):
    # '_' mean omit input code.
    return memory.load_memory_variables({})["history"]
# Upper code is def for get memory variable
# 'RunnablePassthrought.assign()' must take at least one argument. So, we need to enter input.
# So, we give input in function, and print(input)

chain = RunnablePassthrough.assign(history = load_memory) | prompt | llm
# Upper code is make chain yourself.
# When starting a chain. RunnablePassthrought.assign starts load_memory first, then prompts and then llm.
# 'RunnablePassthrought' function allows you to use a function before the prompt is format.
# And also, we can assign any value we want to that function 'history = load_memory'
# And that variable is given to the prompt.
# 'RunnablePassthrought.assign()' must take at least one argument. So, we need to enter input.

def invoke_chain(question):
    result = chain.invoke({"question" : question})
    # Last Code is passive management memory. So, we need management memory by automatic.
    # So, we make def invoke_Chain function. JUST 'chain.invoke({"question" : ~~~})' is passive management memory. 
    memory.save_context({"input" : question}, {"outputs" : result.content})
    # result.content mean 'AI' result.
    print(result)

# Add
# The 'load_memory_varialbes' == load memory.
# The 'save_context' == Save 'Human', 'AI' input, output context at memory.
    

# -- next code -- 
    
invoke_chain("Hello~! My name is Chandon!")
# This format is the value entered into the 'question' in the Upper code 'def invoke_chain(question).' 

# -- next code -- 

invoke_chain("And what is my name??")