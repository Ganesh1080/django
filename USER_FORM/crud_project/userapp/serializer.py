from rest_framework import serializers
from .models import UserForm


class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = "__all__"

    def validate_name(self, value):
        if len(value) > 30:
            raise serializers.ValidationError("name cnnot excced 30 characters")
        return value

    def validate_email(self, value):
        if len(value) > 20:
            raise serializers.ValidationError("Emial cannot exceed 20 characters")
        return value
