from parse_data import *
import openai

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = "37635d8c1d7349fe8698c3d77f855d2e"
openai.api_base = "https://literacylab.openai.azure.com/"


def use_gpt(role: str, prompt: str):
    '''the general version of the model where the user gives personal prompts and the
        model responds as instructed(specified by role)'''
    
    response = openai.ChatCompletion.create(
        engine="literacylab",
        messages=[
            {"role": "system", "content": f"{role}"},
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']


def get_recommendation():
    '''one of the features under the literacy lab'''

    role = """you are a expert financial advisor tasked with making recommendations based on a users financial statements"""
    
    recommendations = []
    data_to_read = function_call()

    prompt = "look at the following records and provide insghtful recommendations thereafter."
    # for i in range(3):
    prompt += """These are the top five categories with the number of respective transactions
                where the bulk of their money is used: give one top tip"""
    prompt += f'{data_to_read}'
    recommendations.append(use_gpt(role, prompt))

    # for rec in recommendations:
    print(recommendations[0])


get_recommendation()