import requests

Data = [x for x in input().split()] # Создание списка логинов

URL = "https://codeforces.com/api/"
for login in Data:
    u_info_URL = URL+"user.status?handle="+login+"&from=1"
    response = requests.get(u_info_URL)
    jfile = response.json()
    orig = []

    for i in jfile["result"]:
        orig.append([i["problem"]["contestId"],i["problem"]["index"]])

    temp = []
    for x in orig:
        if x not in temp:

            temp.append(x)

    orig = temp

    print(login +": ", len(orig))