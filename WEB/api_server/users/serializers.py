from .models import User, rank_lists
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    #오버라이딩, userserializer는 create 시에 입력 데이터에 대한 검증이 필수이다. 
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            army_num = validated_data['army_num'],
            army_rank = validated_data['army_rank'],
            name = validated_data['name'],
            password = validated_data['password']
        )   
        return user

    class Meta:
        model = User
        fields = ['email', 'army_num', 'army_rank', 'name', 'password']


class UserRegisterSerializer(RegisterSerializer):
    
    army_num = serializers.CharField(max_length=100, help_text='**-********')
    army_rank = serializers.ChoiceField(choices=rank_lists)
    name = serializers.CharField(max_length=100, help_text='본명')

    def save(self, request):
        user = super().save(request)
        user.army_num = self.data.get('army_num')
        user.army_rank = self.data.get('army_rank')
        user.name = self.data.get('name')
        user.save()
        return user
