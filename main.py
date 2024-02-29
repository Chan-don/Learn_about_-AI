from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

chat = ChatOpenAI(
    temperature=0.1,
)

with get_openai_callback() as usage:
    a = chat.predict("what is the recipe for soju")
    b = chat.predict("what is the recipe for beer")
    print(a, b, "\n")
    print(usage)
# if you want to show prise to use.
# You must use. 'with' 'get_openai_callback()' 'as' usage:
    # ~~
    # print(usage)
# You must use this! for show prise