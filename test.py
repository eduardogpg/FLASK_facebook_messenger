import json
import requests

from PIL import Image
#https://www.microsoft.com/cognitive-services/en-US/subscriptions
#https://dev.projectoxford.ai/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236
#https://www.microsoft.com/cognitive-services/en-us/face-api/documentation/overview

#https://emojiisland.com/pages/free-download-emoji-icons-png

#30,000 transactions per month, 20 per minute.	

def add_emoji(left, top, width, height):

	background = Image.open("00000001.jpg")
	foreground = Image.open("emoji.png")
	foreground = foreground.resize( (width, height) )

	background.paste(foreground, (left, top), foreground)
	background.show()


def face():
	uri = {'url' : "https://scontent.xx.fbcdn.net/v/t35.0-12/15502853_196089334187097_1763083346_o.png?_nc_ad=z-m&oh=a78e7416bf2cfa7aa166e815780f3874&oe=5852B613"}
	res = requests.post('https://api.projectoxford.ai/face/v1.0/detect',
									params={'returnFaceId' : 'false', 'returnFaceLandmarks': 'true'},
	                data = json.dumps( uri ),
	                headers={'Content-type': 'application/json', 'Host': 'api.projectoxford.ai', 'Ocp-Apim-Subscription-Key': 'a6d271ac0aa14281835d70a538538aba'})

	if res.status_code == 200:
		response = json.loads(res.text)
		print(response)
		image = response[0]
		print(image['faceId'])
		faceRectangle = image['faceRectangle']

		width = faceRectangle['width'] #324
		height = faceRectangle['height'] #324

		top = faceRectangle['top'] #514
		left = faceRectangle['left'] # 234

		add_emoji(left, top)

	else:
		print(json.loads(res.text))


print "Ginal"
face()

#add_emoji(234, 514, 324, 324)
#print("Fin")

