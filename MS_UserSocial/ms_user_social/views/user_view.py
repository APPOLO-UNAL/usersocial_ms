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
                    "picture": user.picture,
                    "favArtists": user.favArtists,
                    "favAlbums": user.favAlbums,
                    "favSongs": user.favSongs,
                    "favPlaylists": user.favPlaylists,
                    "pinnedComm": user.pinnedComm,
                }
                response.append(obj)
            return JsonResponse(response, safe=False, status=200)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)
        
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
            else:
                response = {"error": "You must provide either userName, uid or emailAddr"}
                return JsonResponse(response, safe=False, status=400)
            response = {
                "uid": user.uid,
                "emailAddr": user.emailAddr,
                "userName": user.userName,
                "nickname": user.nickname,
                "keyIdAuth": user.keyIdAuth,
                "description": user.description,
                "picture": user.picture,
                "favArtists": user.favArtists,
                "favAlbums": user.favAlbums,
                "favSongs": user.favSongs,
                "favPlaylists": user.favPlaylists,
                "pinnedComm": user.pinnedComm,
            }
            return JsonResponse(response, safe=False)
        except User.DoesNotExist:
            response = {"error": "User not found"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        try:    
            # create one person
            json_data = json.loads(request.body)
            emailAddr = json_data['emailAddr']
            userName = json_data['userName']
            nickname = json_data['nickname']
            keyIdAuth = json_data['keyIdAuth']
            description = json_data['description']
            picture = json_data.get('picture', None)
        
            user = User(emailAddr = emailAddr,
                            userName=userName, 
                            nickname=nickname, 
                            keyIdAuth = keyIdAuth, 
                            description=description,
                            picture=picture)
            user.save()
            response = {
                "uid": user.uid,
                "emailAddr": user.emailAddr,
                "userName": user.userName,
            }
            return JsonResponse(response)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}
            return JsonResponse(response, safe=False, status=400)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)

    if request.method == 'PUT':
        userName = request.GET.get('userName', '')
        emailAddr = request.GET.get('emailAddr', '')
        uid = request.GET.get('uid', '')
        try:
            # update one person
            json_data = json.loads(request.body)
            nickname = json_data['nickname']
            description = json_data['description']
            picture = json_data['picture']
            favArtists = json_data['favArtists']
            favAlbums = json_data['favAlbums']
            favSongs = json_data['favSongs']
            favPlaylists = json_data['favPlaylists']
            pinnedComm = json_data['pinnedComm']
        
            if (uid):
                user = User.nodes.get(uid=uid)
            elif (userName):
                user = User.nodes.get(userName=userName)
            elif (emailAddr):
                user = User.nodes.get(emailAddr=emailAddr)
            else:
                response = {"error": "You must provide either userName, uid or emailAddr"}
                return JsonResponse(response, safe=False, status=400)
            user.nickname = nickname
            user.description = description
            user.picture = picture
            user.favArtists = favArtists
            user.favAlbums = favAlbums
            user.favSongs = favSongs
            user.favPlaylists = favPlaylists
            user.pinnedComm = pinnedComm
            user.save()
            response = {
                "uid": user.uid,
                "emailAddr": user.emailAddr,
                "userName": user.userName,
                "nickname": user.nickname,
                "keyIdAuth": user.keyIdAuth,
                "description": user.description,
                "picture": user.picture,
                "favArtists": user.favArtists,
                "favAlbums": user.favAlbums,
                "favSongs": user.favSongs,
                "favPlaylists": user.favPlaylists,
                "pinnedComm": user.pinnedComm,
            }
            return JsonResponse(response, safe=False)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}
            return JsonResponse(response, safe=False, status=400)
        except User.DoesNotExist:
            response = {"error": "User not found"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)

    if request.method == 'DELETE':
        try:
            # delete one person
            json_data = json.loads(request.body)
            userName = json_data.get('userName', None)
            emailAddr = json_data.get('emailAddr', None)
        
            if(emailAddr):
                person = User.nodes.get(emailAddr=emailAddr)
            elif(userName):
                person = User.nodes.get(userName=userName)
            else:
                response = {"error": "You must provide either userName or emailAddr"}
                return JsonResponse(response, safe=False)
            person.delete()
            response = {"success": "User deleted"}
            return JsonResponse(response, safe=False)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}
            return JsonResponse(response, safe=False, status=400)
        except User.DoesNotExist:
            response = {"error": "User not found"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)