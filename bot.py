import vk_api
import time
import random

token = "c7a4ca4620c0cc70411f61e66299c0ea5825f0d21420426c40e90c0d318ce21042b2b05ad5825f696c29b"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет, напиши узнать", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "узнать":
                vk.method("messages.send",
                          {"peer_id": id, "message": "ютуб!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "ты дурак":
                vk.method("messages.send",
                          {"peer_id": id, "message": "не обзывайся", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "Я Аня Нефедова":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Ты красотка!", "random_id": random.randint(1, 2147483647)})
             
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
