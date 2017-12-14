from urllib.request import urlopen
import json
import pprint

print('vk.com id :')
id = input()

request = "https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site&v=5.69".format(id = id)
print('Generated request :', request)

try:
	answer_json = urlopen(request)
	obj = json.loads(answer_json.read())
except:
	print('Server connection error. Check your connection')

if obj.get('response') != None:
	print('Server answer:')
	pprint.pprint(obj)
