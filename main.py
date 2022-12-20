import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1025382145511927849/8fBC6kaVRn0UbtrB-xdhnBnl_9N6pnAEYrf-Kd4-NqjLtMXrMeOFQh37YUeiDuyL4-3Y"

response = requests.get(WEBHOOK_URL)

if response.status_code == 200:
    webhook_info = response.json()

    with open("webhook_info.txt", "w") as f:
        f.write(str(webhook_info))

    delete_response = requests.delete(WEBHOOK_URL)

    if delete_response.status_code == 204:
        print("Webhook deleted successfully")
    else:
        print("Error deleting webhook")
else:
    print("Error getting webhook information")
#(this will fail because the webhook has been deleted)
data = {
    "content": "00O0X"
}
send_response = requests.post(WEBHOOK_URL, json=data)

if send_response.status_code == 404:

    print("Message not sent - webhook does not exist")
else:
    print("Error sending message")
