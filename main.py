# Connect memory to the chain.
# LLM chain == off-the-shelf chain.
# The off-the-shelf chain refer to general purpose chain. And this chain is very distributed in langchain.
# off-the-shelf chain is quick to use. However, that cannot customize it.

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
#Upper chain 'LLMChain' is off-the-shelf chain.
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(
    temperature=0.1
)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit= 120,
    memory_key="chat_history"
    # Insert the contents of the template into conversation Suammy memory.
    # Insert "chat_history" into memory, LLMChain can now use the memory.
)

template = """
    You are a helpful AI talking to human.

    {chat_history}
    Human: {question}
"""

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=PromptTemplate.from_template(template),
    verbose=True,
    # This Upper code can show chain prompt log
)

chain.predict(question="I'm chandon!")

# -- next code --

chain.predict(question="I live in yeosu!")
# We find new option. Human!
# This is chat_history memory!!
# Now, LLMchat model can remember our chat.

# -- next code --

chain.predict(question = "what is my name?")
# Now, we can find 'Human : I'm chandon!'
# This is chat_history. So, Now LLMChat model remember my name!

# -- next code --

memory.load_memory_variables({})
# Upper Code is Summary my chat memory.