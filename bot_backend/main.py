import requests
url = 'https://consulting-bot-backend.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "hi",
"sender": "user",
}
x = requests.post(url, json = myobj)
print(x.text)