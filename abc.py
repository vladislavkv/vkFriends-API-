import requests

userId = 'vladislavk'
apiURL = 'https://api.vk.com/method/'

def getUser(name):
    data = requests.get(apiURL+'users.get',{'user_ids':name,'v':'5.74'})
    return data.json()

def getFriends(name):
    data = requests.get(apiURL+'friends.get',{'user_id':name,'v':'5.74'})
    return data.json()

#user = getUser('vladislavk')
#urlImage = user['response'][0]['photo_max_orig']

friends1 = set(getFriends('247348873')['response']['items'])
friends2 = set(getFriends('238354785')['response']['items'])

#image = requests.get(urlImage)
#imageFile = open('image.png','wb')
#imageFile.write(image.content)
#imageFile.close()


user = friends1 & friends2

print(friends1)
print(friends2)
print('Общие друзья: ',friends1 & friends2)

mutualFriend = list(user)[0]
mutualFriendName = getUser(mutualFriend)

print(mutualFriendName)

#print(user)
