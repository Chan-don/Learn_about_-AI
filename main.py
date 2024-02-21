from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
#callbacks is the live streaming the chat answer while run code

chat = ChatOpenAI(
    temperature=0.1, streaming=True, callbacks=[StreamingStdOutCallbackHandler()]
    #temperature valuse high == creativity is high.
    #streaming is live streaming. so, streaming = True means run streaming.
    # and callbacks code is to combine the streaming code
)

sportsCar_prompt = sports_car_template = ChatPromptTemplate.from_messages([
    ("system", "You are a best car dealer. You create recommend which sports car is best to me."),
    ("human", "I want to {car_type} car."),
])

sports_car_chain = sportsCar_prompt | chat 
#-- plus code --

bestSportsCar_prompt = ChatPromptTemplate.from_messages([
    ("system", "You work at a used sports car dealership. So, we have a vehicle that we can recommend to our customers. However, customers don't need detailed information about the car, they just want to know the make and model of the car. You need to sort them into categories and show them to your guests. You should also tell the customer if there is a type of car they want."),
    ("human", "{car}"),
])

best_sports_car_chain = bestSportsCar_prompt | chat

final_chain = {"car" : sports_car_chain} | best_sports_car_chain

final_chain.invoke({
    "car_type": "convertible",
})