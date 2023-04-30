import openai
openai.api_key='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'

model_engine="text-davinci-003"
def openai_prompt(prompt):

    completion=openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response=completion.choices[0].text
    return response