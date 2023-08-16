from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        # read_only_fields = ('userinfo',)


    # def perform_create(self, serializer):
    #     serializer.save(myuser=self.request.user)