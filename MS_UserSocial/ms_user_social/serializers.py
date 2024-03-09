from rest_framework import serializers
from models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        newUser = User(emailAddr = validated_data.get("email"),
                          userName = validated_data.get("userName"),
                          keyIdAuth = validated_data.get("keyIdAuth"),
                          arrArtists = validated_data.get("arrArtists"),
                          arrTracks = validated_data.get("arrTracks"),
                          arrAlbums = validated_data.get("arrAlbums"))
                          
        newUser.save()
        return newUser
    
    def update(self, instance, validated_data):
        try:
            user = User.nodes.get(uid=instance.uid)
        except User.DoesNotExist:
            return "User not found"
        
        user.emailAddr = validated_data.get("email")
        user.userName = validated_data.get("userName")
        user.keyIdAuth = validated_data.get("keyIdAuth")
        user.arrArtists = validated_data.get("arrArtists")
        user.arrTracks = validated_data.get("arrTracks")
        user.arrAlbums = validated_data.get("arrAlbums")
        user.save()
        return user
    