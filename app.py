import configparser

import openai
from fastapi import FastAPI, HTTPException
from flask import jsonify
from pydantic import BaseModel

from ChatGPT import ChatGPT


class InputData(BaseModel):
    user_id: str
    speaker_id: str
    user_question: str


config = configparser.ConfigParser()
config.read('config.ini')
OPENAI_API_KEY = config.get('openai', 'api_key')
OPENAI_Model = config.get('openai', 'model')
OPENAI_MaxTokens = config.get('openai', 'max_tokens')
OPENAI_Promt = config.get('openai', 'promt')
app = FastAPI()


@app.post("/chat")
async def chat(data: InputData):
    try:
        user_question = data.user_question
        # message_str =message.decode("utf-8")
        # 将消息发送给 ChatGPT
        # 这里省略具体实现
        print(f"Received message: {user_question}")
        # chatbot = ChatGPT(OPENAI_API_KEY)
        # message = chatbot.send_message(prompt=OPENAI_Promt, model=OPENAI_Model, Message=data,
        #                                max_tokens=OPENAI_MaxTokens)

        user_conversations = {}
        # conversation_history = ({"role": "system", "content": "请你扮演游戏《阴阳师》里的不知火，按照不知火的说话习惯回答使用中文回答"})
        conversation_history = ({"role": "user", "content": user_question})
        print(conversation_history)

        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=conversation_history,
        #     temperature=1,  # 可调节输出随机性的参数
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0,
        #     max_tokens=512,  # 限制生成回答的最大长度
        # )
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "请你扮演游戏《阴阳师》里的不知火，按照不知火的说话习惯回答使用中文回答"},
                {"role": "user", "content": user_question}
            ]
            #        temperature=0.8, # 可调节输出随机性的参数
            #        top_p=1,
            #        frequency_penalty=0,
            #        presence_penalty=0,
            #        max_tokens=2048, # 限制生成回答的最大长度
        )
        return response.choices[0].message

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))