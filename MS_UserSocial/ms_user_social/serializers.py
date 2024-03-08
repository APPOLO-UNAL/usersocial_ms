from rest_framework import serializers
from models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        newUser = User(emailAddr = validated_data.get("email"),
                          userName = validated_data.get("userName"),
                          keyIdAuth = validated_data.get("keyIdAuth"),
                          idArtist = validated_data.get("idArtist"),
                          idTracks = validated_data.get("idTracks"),
                          idAlbums = validated_data.get("idAlbums"))
                          
        newUser.save()
        return newUser
    
    def update(self, instance, validated_data):
        try:
            user = User.nodes.get(uid=instance.uid)
        except User.DoesNotExist:
            return "User not found"
        
        user.emailAddr = validated_data.get("email")
        user.userName = validated_data.get("name")
        user.description = validated_data.get("description")
        user.quantity = validated_data.get("quantity")
        user.category = validated_data.get("category")
        user.save()
        return user