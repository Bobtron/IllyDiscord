import requests # dependency

url = "https://discord.com/api/webhooks/1253865140806484028/O-JG1mIsNXIHu8NdYtzGMvMh6_i2S9rJaRcleRljY7ZpUdoLILXsbn4b4lYXqA5AMCre" # webhook url, from here: https://i.imgur.com/f9XnAew.png

# for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content": "Hello <@298186138206732290>, *link* to google [here](<https://google.com>)",
    # "allowed_mentions": {
    #     "parse": ["users"]
    # }
    # "username" : "custom username"
    # "embeds": [
    #     {
    #         "description": "link to google [here](google.com)",
    #         "url": "htt"
    #     }
    # ]
}

# leave this out if you dont want an embed
# for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
# data["embeds"] = [
#     {
#         "description" : "text in embed",
#         "title" : "embed title"
#     }
# ]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print(f"Payload delivered successfully, code {result.status_code}.")

# result: https://i.imgur.com/DRqXQzA.png