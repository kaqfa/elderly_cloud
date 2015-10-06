from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth.models import Group

from member.models import Elder, CareGiver, CareGiving


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'groups')


class ElderSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Elder


class CareGiverSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = CareGiver


class SignupSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=(('e', 'Elder'), ('c', 'Caregiver')))
    address = serializers.CharField()
    birthday = serializers.DateField()
    gender = serializers.ChoiceField(choices=(('l', 'laki-laki'), ('p', 'perempuan')))
    phone = serializers.DecimalField(max_digits=12, decimal_places=0)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(required=False)
    email = serializers.EmailField()
    cared_by = serializers.PrimaryKeyRelatedField(queryset=CareGiver.objects.all(), many=True, required=False)

    def validate(self, data):
        if data['type'] == 'e' and (data.get('cared_by') is None or len(data['cared_by']) == 0):
            raise serializers.ValidationError("Elder harus mempunyai CareGiver")
        elif data['type'] == 'c' and (data.get('password') is None or data['password'] == ""):
            raise serializers.ValidationError("Password kosong")
        return data

    def create(self, validated_data):
        type = validated_data.get('type')
        username = validated_data.get('username')
        if type == 'e' and len(validated_data.get('cared_by')) > 0:
            user = User.objects.create_user(username=username, email=validated_data.get('email'), password='asdfg4321')
            user.first_name = validated_data.get('first_name')
            user.last_name = validated_data.get('last_name')
            user.save()
            code = get_random_string(length=8)
            while Elder.objects.filter(code=code):
                code = get_random_string(length=8)
            signupData = {
            'user': user,
            'address': validated_data.get('address'),
            'birthday': validated_data.get('birthday'),
            'gender': validated_data.get('gender'),
            'phone': validated_data.get('phone'),
            'code': code,
            }
            elder = Elder.objects.create(**signupData)
            for caregiver in validated_data.get('cared_by'):
                CareGiving.objects.create(caregiver=caregiver, elder=elder)
            g = Group.objects.get(name='Elder')
            g.user_set.add(user)
            return elder
        else:
            user = User.objects.create_user(username=username, email=validated_data.get('email'),
                                            password=validated_data.get('password'))
            user.first_name = validated_data.get('first_name')
            user.last_name = validated_data.get('last_name')
            user.save()
            signupData = {
            'user': user,
            'address': validated_data.get('address'),
            'birthday': validated_data.get('birthday'),
            'gender': validated_data.get('gender'),
            'phone': validated_data.get('phone'),
            }
            caregiver = CareGiver.objects.create(**signupData)
            g = Group.objects.get(name='CareGiver')
            g.user_set.add(user)
            return caregiver

    def update(self, instance, validated_data):
        pass