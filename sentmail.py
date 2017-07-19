import string
import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxe684f8cb7f724476ab6bada89016c684.mailgun.org/messages",
        auth=("api", "key-ba814f3b76b7b575a24c8d69f1918851"),
        data={"from": "Excited User <mailgun@sandboxe684f8cb7f724476ab6bada89016c684.mailgun.org>",
              "to": ["poorimcstp@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
sentmail = send_simple_message();
