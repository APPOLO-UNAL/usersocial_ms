from django.http import JsonResponse
from ms_user_social.models import User
from django.views.decorators.csrf import csrf_exempt
from ms_user_social.sender import send
import json

@csrf_exempt
def connectUaU(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        uid1 = json_data['uid1']
        uid2 = json_data['uid2']
        try:
            person1 = User.nodes.get(uid=uid1)
            person2 = User.nodes.get(uid=uid2)
            res = person1.follow.connect(person2)
            response = {"result": res}
            print(type(uid1))
            print(response)
            send("Follows", f"Now user {uid1} follows you", uid2)
            #send("Title", "Body", "1")
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
        
@csrf_exempt
def disconnectUaU(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        uid1 = json_data['uid1']
        uid2 = json_data['uid2']
        try:
            person1 = User.nodes.get(uid=uid1)
            person2 = User.nodes.get(uid=uid2)
            # Desconectar los dos usuarios
            res = person1.follow.disconnect(person2)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
        


#Add follow and unfollow with userName and email