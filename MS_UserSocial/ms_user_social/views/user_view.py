from django.http import JsonResponse
from ms_user_social.models import User
from django.views.decorators.csrf import csrf_exempt
import json


def getAllUsers(request):
    if request.method == 'GET':
        try:
            users = User.nodes.all()
            response = []
            for user in users :
                obj = {
                    "uid": user.uid,
                    "emailAddr": user.emailAddr,
                    "userName": user.userName,
                    "nickname": user.nickname,
                    "keyIdAuth": user.keyIdAuth,
                    "description": user.description,
                    "arrArtists": user.arrArtists,
                    "arrTracks": user.arrTracks,
                    "arrAlbums": user.arrAlbums,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
        
@csrf_exempt
def userDetails(request):
    if request.method == 'GET':
        userName = request.GET.get('userName', '')
        emailAddr = request.GET.get('emailAddr', '')
        uid = request.GET.get('uid', '')
        try:
            if (uid):
                user = User.nodes.get(uid=uid)
            elif (userName):
                user = User.nodes.get(userName=userName)
            elif (emailAddr):
                user = User.nodes.get(emailAddr=emailAddr)
            response = {
                "uid": user.uid,
                "emailAddr": user.emailAddr,
                "userName": user.userName,
                "nickname": user.nickname,
                "keyIdAuth": user.keyIdAuth,
                "description": user.description,
                "arrArtists": user.arrArtists,
                "arrTracks": user.arrTracks,
                "arrAlbums": user.arrAlbums,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one person
        json_data = json.loads(request.body)
        emailAddr = json_data['emailAddr']
        userName = json_data['userName']
        nickname = json_data['nickname']
        keyIdAuth = json_data['keyIdAuth']
        description = json_data['description']
        try:
            user = User(emailAddr = emailAddr,
                            userName=userName, 
                            nickname=nickname, 
                            keyIdAuth = keyIdAuth, 
                            description=description)
            user.save()
            response = {
                "uid": user.uid,
                "emailAddr": user.emailAddr,
                "userName": user.userName,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        userName = request.GET.get('userName', '')
        emailAddr = request.GET.get('emailAddr', '')
        uid = request.GET.get('uid', '')
        # update one person
        json_data = json.loads(request.body)
        nickname = json_data['nickname']
        description = json_data['description']
        arrArtists = json_data['arrArtists']
        arrTracks = json_data['arrTracks']
        arrAlbums = json_data['arrAlbums']
        try:
            if (uid):
                user = User.nodes.get(uid=uid)
            elif (userName):
                user = User.nodes.get(userName=userName)
            elif (emailAddr):
                user = User.nodes.get(emailAddr=emailAddr)
            user.nickname = nickname
            user.description = description
            user.arrArtists = arrArtists
            user.arrTracks = arrTracks
            user.arrAlbums = arrAlbums
            user.save()
            response = {
                "uid": user.uid,
                "emailAddr": user.emailAddr,
                "userName": user.userName,
                "nickname": user.nickname,
                "keyIdAuth": user.keyIdAuth,
                "description": user.description,
                "arrArtists": user.arrArtists,
                "arrTracks": user.arrTracks,
                "arrAlbums": user.arrAlbums,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one person
        json_data = json.loads(request.body)
        userName = json_data['userName']
        try:
            person = User.nodes.get(userName=userName)
            person.delete()
            response = {"success": "User deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)