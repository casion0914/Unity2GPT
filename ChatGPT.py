import os
import openai


class ChatGPT:
    def __init__(self, api_key):
        self.api_key = api_key


    def send_message(self, prompt, model,Message, max_tokens=1024, temperature=0.5 , n=1, stop=None):
        openai.api_key = self.api_key
        print(openai.api_key)
        completion = openai.ChatCompletion.create(
            model=model,
            sendmsg=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": Message}
            ]
        )
        return (completion.choices[0].message)