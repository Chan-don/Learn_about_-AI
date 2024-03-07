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
)

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=PromptTemplate.from_template("{question}"),
    verbose=True,
    # This Upper code can show chain prompt log
)

chain.predict(question="I'm chandon!")

# -- next code --

chain.predict(question="I live in yeosu!")

# -- next code --

chain.predict(question = "what is my name?")
# Why LLMChain say "I'm Sorry I don't know your name."
# Because, we didn't update memory!

# -- next code --

memory.load_memory_variables({})
# Upper Code is Summary my chat memory.