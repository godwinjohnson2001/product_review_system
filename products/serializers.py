from rest_framework import serializers
from .models import User, Product, Review
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)  # ensure password is not exposed

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            data['user'] = user  # include user in validated data
            return data
        raise serializers.ValidationError("Invalid credentials")

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_by']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']
