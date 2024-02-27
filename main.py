from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
#FewShotPromptTemplate provieds specific prompt templates. Like, Just Capital letter or Just small letter, space, comma, etc..
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code
from langchain.prompts import PromptTemplate
from langchain.prompts.example_selector.base import BaseExampleSelector

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

class RandomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples

    def add_example(self, example):
        self.examples.append(example)

    def select_examples(self, input_varialbes):
        from random import choice

        return [choice(self.examples)]
    # Upper Code is get random Examples at 'Example Template'


example_prompt = PromptTemplate.from_template("Human: {country}\nAI: {answer}")

example_selector= RandomExampleSelector(
    examples=examples,
)

prompt = FewShotPromptTemplate(
    example_prompt= example_prompt,
    example_selector=example_selector,
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)

prompt.format(country = "Brazil")
