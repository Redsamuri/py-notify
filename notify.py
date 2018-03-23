import subprocess,json

accessToken = input("Access Token: ")

while True:
    msg = input("Message: ")

    msgdat = msg.split("||")

    if len(msgdat) == 1:
        resp = subprocess.getoutput("curl -X POST https://notify-api.line.me/api/notify -H 'Authorization: Bearer %s' -F 'message=%s' --silent" % (accessToken,msgdat[0]))
    else:
        resp = subprocess.getoutput("curl -X POST https://notify-api.line.me/api/notify -H 'Authorization: Bearer %s' -F 'message=%s' -F 'imageFile=@%s' --silent" % (accessToken,msgdat[0],msgdat[1]))

    print(json.loads(resp)["message"])

#L6YRmg8RIIrxraOn2Kpf5egcKCoUv6jCWoOXy3a9T1l