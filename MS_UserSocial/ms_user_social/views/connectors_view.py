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
        userName1 = json_data['userName1']
        emailAddr1 = json_data['emailAddr1']
        uid2 = json_data['uid2']
        userName2 = json_data['userName2']
        emailAddr2 = json_data['emailAddr2']
        if (uid1 == uid2 or userName1 == userName2 or emailAddr1 == emailAddr2):
            response = {"error": "You can't follow yourself"}
            return JsonResponse(response, safe=False)
        try:
            if(uid1 and uid2):
                person1 = User.nodes.get(uid=uid1)
                person2 = User.nodes.get(uid=uid2)
            elif(userName1 and userName2):
                person1 = User.nodes.get(userName=userName1)
                person2 = User.nodes.get(userName=userName2)
            elif(emailAddr1 and emailAddr2):
                person1 = User.nodes.get(emailAddr=emailAddr1)
                person2 = User.nodes.get(emailAddr=emailAddr2)
            else:
                response = {"error": "You must provide both users with uid, userName or emailAddr"}
                return JsonResponse(response, safe=False)
            res = person1.follow.connect(person2)
            response = {"result": res}
            print(type(uid1))
            print(response)
            send("Follows", f"Now user {person1.userName} follows you", person2.userName)
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
        userName1 = json_data['userName1']
        emailAddr1 = json_data['emailAddr1']
        uid2 = json_data['uid2']
        userName2 = json_data['userName2']
        emailAddr2 = json_data['emailAddr2']
        if (uid1 == uid2 or userName1 == userName2 or emailAddr1 == emailAddr2):
            response = {"error": "You can't unfollow yourself"}
            return JsonResponse(response, safe=False)
        try:
            if(uid1 and uid2):
                person1 = User.nodes.get(uid=uid1)
                person2 = User.nodes.get(uid=uid2)
            elif(userName1 and userName2):
                person1 = User.nodes.get(userName=userName1)
                person2 = User.nodes.get(userName=userName2)
            elif(emailAddr1 and emailAddr2):
                person1 = User.nodes.get(emailAddr=emailAddr1)
                person2 = User.nodes.get(emailAddr=emailAddr2)
            else:
                response = {"error": "You must provide both users with uid, userName or emailAddr"}
                return JsonResponse(response, safe=False)
            # Desconectar los dos usuarios
            res = person1.follow.disconnect(person2)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
        


#Add follow and unfollow with userName and email