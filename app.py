# Import relevant packages
import streamlit as st
from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import re
from myPrompts import *
import pandas as pd
import  json


# create an instance of the model
def instanModel(temp=0.1):
    """
    This function returns an instance of the model with the specified temperature
    args:
        temp: Float (Model Temperature)
    returns:
        Model
    """
    model = OllamaLLM(
        model='llama3.2:latest',
        temperature=0.1
    )
    return model

#================= Using Zero SHot Template===================================
# template = zero_shot_template
# prompt = ChatPromptTemplate.from_template(template)

# #get the chain
# chain = prompt | instanModel(temp=0.1)

# # since the data is in a dataframe, lets get the texts one-by-one
# def getData(path):
#     """
#     returns the data
#     """
#     return pd.read_csv(path)

# df = getData("data/Support_ticket_text_data.csv")

# text = df['support_ticket_text'][0]

# # invoke the chain
# response = chain.invoke({"ticket_text": text})

# print(json.loads(response))


#================= Using Few Shots Template===================================
template = few_shots_template
prompt = ChatPromptTemplate.from_template(template)

#get the chain
chain = prompt | instanModel(temp=0.1)

# since the data is in a dataframe, lets get the texts one-by-one
def getData(path):
    """
    returns the data
    """
    return pd.read_csv(path)

df = getData("data/Support_ticket_text_data.csv")

output = {
'support_tick_id': [],
'support_ticket_text' : [],
'category': [],
'tags': [],
'priority': [],
'suggested ETA' :[],
'first_response': []
}

for index in range(df.shape[0]):
    print("**"*20)
    print(index)
    output['support_tick_id'].append(df['support_tick_id'][index])
    output['support_ticket_text'].append(df['support_ticket_text'][index])

    text = df['support_ticket_text'][index]
    print(text)

    response = chain.invoke({"ticket_text": text})
    if "response: " in response:
        response.replace("response: ", "")
    response = json.loads(response)

    print("--"*20)
    print(response)
    print("**"*20)
    output['category'].append(response['category'])
    output['tags'].append(response['tags'])
    output['priority'].append(response['priority'])
    output['suggested ETA'].append(response['suggested ETA'])
    output['first_response'].append(response['first_response'])



# create a dataframe with the data
new_df = pd.DataFrame(output)
print(new_df)
print("**"*10)
print('Done')
print("**"*10)

save_path = "data/output_support_ticket_data.csv"
new_df.to_csv(save_path)
