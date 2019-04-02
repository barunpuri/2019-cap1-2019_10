from django.shortcuts import render
from my_mood_music.models import Emotion, Music

from django.http.response import HttpResponse
import cognitive_face as CF

# Create your views here.

'''
# MS Face api 사용
def requestFaceAPI(request):

	emotion_list = Emotion.objects.all()
	return HttpResponse('Hello\n' + emotion_list[0].emotion)

	KEY = 'd0b59c05aee14136af3d8dc739689e4a'  # Replace with a valid subscription key (keeping the quotes in place).
	CF.Key.set(KEY)

	BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
	CF.BaseUrl.set(BASE_URL)

	# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
	img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
	faces = CF.face.detect(img_url)
	print(faces)
'''



# 실질적으로 Queryset을 컨트롤하고 데이터를 조작해 Serializer을 통해 매핑시켜주는 View를 작성
# CBV를 이용해 여러개의 뷰를 작성하지 않고, Viewset을 이용해 Model 하나를 컨트롤하는 CRUD를 1개의 View로 구현

from rest_framework import viewsets
from .serializers import MMMSerializer
from rest_framework import permissions


class MyMoodMusicView(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = MMMSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
	

'''

import http.client, urllib.request, urllib.parse, urllib.error, base64

	headers = {
		# Request headers
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': 'd0b59c05aee14136af3d8dc739689e4a',
	}

	params = urllib.parse.urlencode({
		# Request parameters
		'returnFaceId': 'true',
		'returnFaceLandmarks': 'false',
		'returnFaceAttributes': 'age, emotion',
	})

	try:
		conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
		response = conn.getresponse()
		data = response.read()
		print(data)
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
'''



'''
API Key
d0b59c05aee14136af3d8dc739689e4a
0f45d74f60c14ebeae161adb16fb5bd1
'''
