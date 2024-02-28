from langchain.chat_models import ChatOpenAI
#FewShotPromptTemplate provieds specific prompt templates. Like, Just Capital letter or Just small letter, space, comma, etc..
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code
from langchain.prompts import PromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate
# pipeline can combine many prompts together.

chat = ChatOpenAI(
    temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler(),],
    #temperature valuse high == creativity is high.
    #streaming is live streaming. so, streaming = True means run streaming.
    # and callbacks code is to combine the streaming code
)

intro = PromptTemplate.from_template(
    """
    You are a role playing assistant
    And you are impersonating a {character}
"""
)

example = PromptTemplate.from_template(
    """
    This is an example of how you talk:
    Human: {example_question}
    You: {example_answer}
"""
)

start = PromptTemplate.from_template(
    """
    Start now!

    Human: {question}
    You:
"""
)

final = PromptTemplate.from_template(
    """
    {intro}

    {example}

    {start}
"""
)

prompts = [
    ("intro", intro),
    ("example", example),
    ("start", start),
]
# ("intro") == value key, intro == just name. You can change name what you want.



full_prompt = PipelinePromptTemplate(final_prompt=final, pipeline_prompts= prompts,)


chain = full_prompt | chat

chain.invoke({
    "character": "Pirate",
    "example_question" : "What is your location?",
    "example_answer" : "Arrrg!! That is a secret!! Arrrg",
    "question" : "What is your fav food?",
})