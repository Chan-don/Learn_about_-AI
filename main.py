from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
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
        "question" : "What do you know about France?",
        "answer" : """
        Here is what I know :
        Capital: Paris
        Language: French
        Food: wine and Cheese
        Currency: Euro
        """,
    },
    {
        "question" : "What do you know about Italy?",
        "answer" : """
        Here is what I know :
        Capital: Rome
        Language: Italian
        Food: pizza and pasta
        Currency: Euro
        """,
    },
    {
        "question" : "What do you know about Korea?",
        "answer" : """
        Here is what I know :
        Capital: Seoul
        Language: Korean
        Food: Kimki and bulgogi
        Currency: Won
        """,
    },
]

# chat.predict("What do you know about Korea")
#Upper code is not use the FewShotPromptTemplate

example_prompt = PromptTemplate.from_template("Human: {question}\nAI:{answer}")
prompt = FewShotPromptTemplate(
    example_prompt= example_prompt,
    examples=examples,
    suffix="Human: What do you know about {country}?",
    input_variables={"country"}
)

# prompt.format(country="Germany")
#Upper code is use FewShotPromptTemplate. And see a prompt that AI will see.
#So, FewShotPromptTemplate is Form. It determines the format in which AI will speak.

chain = prompt | chat

chain.invoke({
    "country": "United States America"
})
#Upper code is Run prompt according to 'chat'
