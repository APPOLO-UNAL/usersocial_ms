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
                    "userName": user.userName,
                    "nickname": user.nickname,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
        
@csrf_exempt
def userDetails(request):
    if request.method == 'GET':
        # get one person by name
        name = request.GET.get('userName', ' ')
        try:
            user = User.nodes.get(userName=name)
            response = {
                "uid": user.uid,
                "userName": user.userName,
                "nickname": user.nickname,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one person
        json_data = json.loads(request.body)
        name = json_data['name']
        email = json_data['email']
        age = int(json_data['age'])
        try:
            person = User(emailAddr = email,userName=name, age=age)
            person.save()
            response = {
                "uid": person.uid,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    # if request.method == 'PUT':
    #     # update one person
    #     json_data = json.loads(request.body)
    #     name = json_data['name']
    #     age = int(json_data['age'])
    #     uid = json_data['uid']
    #     try:
    #         person = Person.nodes.get(uid=uid)
    #         person.name = name
    #         person.age = age
    #         person.save()
    #         response = {
    #             "uid": person.uid,
    #             "name": person.name,
    #             "age": person.age,
    #         }
    #         return JsonResponse(response, safe=False)
    #     except:
    #         response = {"error": "Error occurred"}
    #         return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one person
        json_data = json.loads(request.body)
        userName = json_data['userName']
        try:
            person = User.nodes.get(userName=userName)
            person.delete()
            response = {"success": "Person deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)