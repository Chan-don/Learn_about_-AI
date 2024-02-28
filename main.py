from langchain.chat_models import ChatOpenAI
#FewShotPromptTemplate provieds specific prompt templates. Like, Just Capital letter or Just small letter, space, comma, etc..
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code
from langchain.prompts import load_prompt
#load prompt at the prompt.json or prompt.yaml

#prompt = load_prompt("./prompt.json")
# Upper code is Get prompt at the "prompt.json"

prompt = load_prompt("./prompt.yaml")
# Upper code is Get prompt at the "prompt.yaml"
# What is different at the json and yaml?
# yaml is easier to use then json.

chat = ChatOpenAI(
    temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler(),],
    #temperature valuse high == creativity is high.
    #streaming is live streaming. so, streaming = True means run streaming.
    # and callbacks code is to combine the streaming code
)

prompt.format(country = "xxx")