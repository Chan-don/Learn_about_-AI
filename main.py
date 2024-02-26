from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
#prompts.few_shot is shortcut to prompts. 
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code

chat = ChatOpenAI(
    temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler()]
    #temperature valuse high == creativity is high.
    #streaming is live streaming. so, streaming = True means run streaming.
    # and callbacks code is to combine the streaming code
)

t = PromptTemplate.from_template("what is the capital of {country}")

t.format(country="france")
# Upper code is shortcode to show prompts

t = PromptTemplate(
    template= "what is the capital of {country}",
    input_variables=["country"],
)
t.format(country="Seoul")
# Upper code is principled to show prompts.