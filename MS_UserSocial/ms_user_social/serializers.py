from rest_framework import serializers
from models import *

class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(name = validated_data.get("name"),
                          description = validated_data.get("description"),
                          quantity = validated_data.get("quantity"))
                          
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = User.nodes.get(instance.username)
        if (user):
            instance.name = validated_data.get("name")
            instance.description = validated_data.get("description")
            instance.quantity = validated_data.get("quantity")
            instance.category = validated_data.get("category")
            instance.save()
            return instance
        else:
            return "User not found"