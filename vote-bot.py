import requests
import random
import time


#### Preffix zeroes
def prefix(data, count):
    while len(data) < (count+1):
        data = '0'+data
    return data

count = 2

while 1==1 :

    ## Create new User
    try:
        newuser = requests.get('https://uinames.com/api/?region=india')
        user_name = newuser.json()['name']
    except ConnectionError:
        print("Network Error! Can't connect to Names API!")
        time.sleep(10)
        continue

    ## Generate new IP
    new_ip = prefix(str(random.randint(1,256)),2)+'.'+prefix(str(random.randint(1,256)),2)+'.'+prefix(str(random.randint(1,256)),2)+'.'+prefix(str(random.randint(1,256)),2)

    ## Create new Vote Data
    new_vote = {
        'user_id': 1108,
        'user_session': '',
        'ip': new_ip,
        'voter_name': user_name
    }

    ## Generate new cookies
    try:
        cookies_page = requests.get('https://faceofdigital.com/new_contestpage.php?n=ca5cbed9682beb8ff6a8c3c087d0973b')
        new_cookies = {"__cfduid":cookies_page.cookies["__cfduid"], "PHPSESSID":cookies_page.cookies["PHPSESSID"], "customip":new_ip }
    except ConnectionError:
        print("Network Error! Can't connect to Candidate's Page!")
        time.sleep(10)
        continue

    ## Make a Vote
    try:
        response = requests.post('https://faceofdigital.com/ajax/user-vote.php', new_vote, cookies=new_cookies)

        local_time = time.localtime(time.time())
        cur_time = prefix(str(local_time.tm_hour),1) + '-' + prefix(str(local_time.tm_min),1) + '-' + prefix(str(local_time.tm_sec),1)
        count += 1
        status = "Done!" if(response.text.find('Thank You For Vote') != -1) else "Failed!"
        print('<'+ user_name +'>  '+ str(count) +'  |  '+ status)
    except ConnectionError:
        print("Network Error! Can't Vote!")
        time.sleep(10)
        continue

    time.sleep(random.randint(250,500))
