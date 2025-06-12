
text = "Hello,, son ,,,, When are yoo coming home,"

def dad_filter(message):
    while ",," in message:
        message = message.replace(",,",",")
    return message.strip(",") #strip чистить зайву кому вкінці

res = dad_filter(text)
print(res)
    