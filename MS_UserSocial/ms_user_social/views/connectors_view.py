from django.http import JsonResponse
from ms_user_social.models import User
from django.views.decorators.csrf import csrf_exempt
from ms_user_social.sender import send
from neomodel import db
import json

@csrf_exempt
def connectUaU(request):
    if request.method == 'PUT':
        try:
            json_data = json.loads(request.body)
            uid1 = json_data.get('uid1', None)
            userName1 = json_data.get('userName1', None)
            emailAddr1 = json_data.get('emailAddr1', None)
            uid2 = json_data.get('uid2', None)
            userName2 = json_data.get('userName2', None)
            emailAddr2 = json_data.get('emailAddr2', None)
            if (uid1 == uid2 and userName1 == None and emailAddr1 == None and userName2 == None and emailAddr2 == None):
                response = {"error": "You can't follow yourself"}
                return JsonResponse(response, safe=False)
            elif(userName1 == userName2 and uid1 == None and emailAddr1 == None and uid2 == None and emailAddr2 == None):
                response = {"error": "You can't follow yourself"}
                return JsonResponse(response, safe=False)
            elif(emailAddr1 == emailAddr2 and uid1 == None and userName1 == None and uid2 == None and userName2 == None):
                response = {"error": "You can't follow yourself"}
                return JsonResponse(response, safe=False)
        
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
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}
            return JsonResponse(response, safe=False, status=400)
        except person1.DoesNotExist:
            response = {"error": "User 1 does not exist"}
            return JsonResponse(response, safe=False, status=404)
        except person2.DoesNotExist:
            response = {"error": "User 2 does not exist"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)
        
@csrf_exempt
def disconnectUaU(request):
    if request.method == 'PUT':
        try:
            json_data = json.loads(request.body)
            uid1 = json_data.get('uid1', None)
            userName1 = json_data.get('userName1', None)
            emailAddr1 = json_data.get('emailAddr1', None)
            uid2 = json_data.get('uid2', None)
            userName2 = json_data.get('userName2', None)
            emailAddr2 = json_data.get('emailAddr2', None)
            if (uid1 == uid2 and userName1 == None and emailAddr1 == None and userName2 == None and emailAddr2 == None):
                response = {"error": "You can't unfollow yourself"}
                return JsonResponse(response, safe=False)
            elif(userName1 == userName2 and uid1 == None and emailAddr1 == None and uid2 == None and emailAddr2 == None):
                response = {"error": "You can't unfollow yourself"}
                return JsonResponse(response, safe=False)
            elif(emailAddr1 == emailAddr2 and uid1 == None and userName1 == None and uid2 == None and userName2 == None):
                response = {"error": "You can't unfollow yourself"}
                return JsonResponse(response, safe=False)
        
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
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}
            return JsonResponse(response, safe=False, status=400)
        except person1.DoesNotExist:
            response = {"error": "User 1 does not exist"}
            return JsonResponse(response, safe=False, status=404)
        except person2.DoesNotExist:
            response = {"error": "User 2 does not exist"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)

@csrf_exempt
def getFollows(request):
    if request.method == 'GET':
        userName = request.GET.get('userName', None)
        emailAddr = request.GET.get('emailAddr', None)
        uid = request.GET.get('uid', None)

        try:
            if uid:
                user = User.nodes.get(uid=uid)
            elif userName:
                user = User.nodes.get(userName=userName)
            elif emailAddr:
                user = User.nodes.get(email=emailAddr)
            else:
                response = {"error": "No user identifier provided"}
                return JsonResponse(response, safe=False, status=400)

            query = """
            MATCH (u:User)<-[FOLLOW]-(follower)
            WHERE u.uid = $user_id
            RETURN count(follower)
            """
            
            results, meta = db.cypher_query(query, {"user_id": user.uid})
            follower_count = results[0][0]

            response = {"followers": follower_count}
            return JsonResponse(response, safe=False, status=200)

        except User.DoesNotExist:
            response = {"error": "User does not exist"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)

@csrf_exempt
def getFollowers(request):
    if request.method == 'GET':
        userName = request.GET.get('userName', None)
        emailAddr = request.GET.get('emailAddr', None)
        uid = request.GET.get('uid', None)

        try:
            if uid:
                user = User.nodes.get(uid=uid)
            elif userName:
                user = User.nodes.get(userName=userName)
            elif emailAddr:
                user = User.nodes.get(email=emailAddr)
            else:
                response = {"error": "No user identifier provided"}
                return JsonResponse(response, safe=False, status=400)

            query = """
            MATCH (u:User)<-[FOLLOW]-(follower)
            WHERE u.uid = $user_id
            RETURN collect(follower.userName)
            """

            results, meta = db.cypher_query(query, {"user_id": user.uid})
            followers = results[0][0]

            response = {"followers": followers}
            return JsonResponse(response, safe=False, status=200)

        except User.DoesNotExist:
            response = {"error": "User does not exist"}
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response = {"error": str(e)}
            return JsonResponse(response, safe=False, status=500)        
    