#If you want to chain model
from langchain.llms.openai import OpenAI

chat = OpenAI(
    temperature= 0.1,
    max_tokens=450,
    model="gpt-3.5-turbo-0125"
)

chat.save("model.json")
# if you want save model. use upper code
# And then you can see 'model.json' at the left 'file-list'

# or you can also write this code.
# NEW CODE
from langchain.llms.loading import load_llm

chat = load_llm("model.json")

chat