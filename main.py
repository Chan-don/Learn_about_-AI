# Connect memory to the chain.
# LLM chain == off-the-shelf chain.
# The off-the-shelf chain refer to general purpose chain. And this chain is very distributed in langchain.
# off-the-shelf chain is quick to use. However, that cannot customize it.

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
#Upper chain 'LLMChain' is off-the-shelf chain.
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

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True,
    # This Upper code can show chain prompt log
)

chain.predict(question="I'm chandon!")

# -- next code --

chain.predict(question="I live in yeosu!")
# Now, we can show System, Human, AI.
# This is MessagesPlaceholder power.
# That code makes the prompt look neat!

# -- next code --

chain.predict(question = "what is my name?")
# Now, we can find 'Human : I'm chandon!'
# This is chat_history. So, Now LLMChat model remember my name!

