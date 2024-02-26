from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain.prompts.few_shot import FewShotChatMessagePromptTemplate
#FewShotPromptTemplate provieds specific prompt templates. Like, Just Capital letter or Just small letter, space, comma, etc..
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code

chat = ChatOpenAI(
    temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler(),],
    #temperature valuse high == creativity is high.
    #streaming is live streaming. so, streaming = True means run streaming.
    # and callbacks code is to combine the streaming code
)

examples = [
    {
        "country" : "France",
        "answer" : """
        Here is what I know:
        Capital: Paris
        Language: French
        Food: wine and Cheese
        Currency: Euro
        """,
    },
    {
        "country" : "Italy",
        "answer" : """
        I know this:
        Capital: Rome
        Language: Italian
        Food: pizza and pasta
        Currency: Euro
        """,
    },
    {
        "country" : "Korea",
        "answer" : """
        I know this:
        Capital: Seoul
        Language: Korean
        Food: Kimki and bulgogi
        Currency: Won
        """,
    },
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "what do you know about {country}?"),
    ("ai", "{answer}"),
])
example_prompt = FewShotChatMessagePromptTemplate(
    example_prompt= example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a travel expert."),
    example_prompt,
    ("human", "what do you know about {country}?")
])
# first, AI see the system string.
# Second, AI see the 'example_prompt' and learn about answer template itself
# Third, human speak to AI

chain = final_prompt | chat

chain.invoke({
    "country": "United Kingdom"
})
#Upper code is Run prompt according to 'chat'
