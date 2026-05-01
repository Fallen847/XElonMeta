import requests
import time

TOKEN = "8616106742:AAFGFodfmY-McsdTPi7uXzwK_orESCZ176o"
URL = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = None

def send_message(chat_id, text):
    requests.post(URL + "/sendMessage", data={
        "chat_id": chat_id,
        "text": text
    })

def get_updates():
    global last_update_id

    url = URL + "/getUpdates"

    if last_update_id:
        url += f"?offset={last_update_id + 1}"

    r = requests.get(url)
    return r.json()

print("Bot çalışıyor...")

while True:
    data = get_updates()

    if "result" in data:
        for update in data["result"]:
            last_update_id = update["update_id"]

            if "message" in update:
                message = update["message"]
                chat_id = message["chat"]["id"]
                text = message.get("text", "")

                if text == "/start":
                    send_message(chat_id, "Merhaba 👋 Ben çalışan gerçek botum!")

                elif text == "/help":
                    send_message(chat_id, "Komutlar: /start /help")

                else:
                    send_message(chat_id, "Bilinmeyen komut 🤖")

    time.sleep(1)