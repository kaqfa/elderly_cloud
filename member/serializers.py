from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
# from django.utils.crypto import get_random_string
# from django.contrib.auth.models import Group

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
    GENDER_CHOICES = (('l', 'laki-laki'), ('p', 'perempuan'))
    unique_val = [UniqueValidator(queryset=User.objects.all())]

    type = serializers.ChoiceField(choices=(('e', 'Elder'),
                                            ('c', 'Caregiver')))
    address = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES,
                                     default='1')
    phone = serializers.DecimalField(max_digits=12, decimal_places=0,
                                    validators=[UniqueValidator(queryset=Elder.objects.all())])
    username = serializers.CharField(validators=unique_val,
                                     required=False)
    fullname = serializers.CharField()
    # last_name = serializers.CharField()
    password = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    cared_by = serializers.PrimaryKeyRelatedField(
                        queryset=CareGiver.objects.all(),
                        many=True, required=False)

    def validate(self, data):
        user = self.context['request'].user
        if data['type'] == 'e':
            if user.is_authenticated():
                caregiver = CareGiver.objects.get(user=user)
                data['cared_by']=[caregiver.id]
            else:
                raise serializers.ValidationError("Harus Login Dulu")
        elif (data['type'] == 'e' and
              (data.get('cared_by') is None or len(data['cared_by']) == 0)):
            raise serializers.ValidationError("Elder harus mempunyai CareGiver")
        elif data['type'] == 'c':
            validator = ""
            if (data.get('password') is None or data['password'] == ""):
                validator += "Password kosong"
            if (data.get('username') is None or data['username'] == ""):
                if validator != "":
                    validator += ", "
                validator += "Username harus diisi"
            if (data.get('email') is None or data['email'] == ""):
                if validator != "":
                    validator += ", "
                validator += "Email harus diisi"
            if validator != "":
                raise serializers.ValidationError(validator)
        return data

    def create(self, validated_data):
        type = validated_data.get('type')
        user = self.context['request'].user
        if user.is_authenticated():
            try:
                caregiver = CareGiver.objects.get(user=user)
                cared_by=[caregiver]
            except:
                cared_by=validated_data.get('cared_by')
        if type == 'e' and len(validated_data.get('cared_by')) > 0:
            # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            # code = get_random_string(length=8, allowed_chars=alphabet)
            # while Elder.objects.filter(code=code):
            #     code = get_random_string(length=8)
            phone = validated_data.get('phone')
            email = validated_data.get('email')
            user = User.objects.create_user(username=phone, email=email,
                                            password='asdfg4321')
            fullname = validated_data.get('fullname')
            names = fullname.split(' ', 1)
            user.first_name = names[0]
            if len(names)>1:
                user.last_name = names[1]
            user.save()
            signupData = {
                'user': user,
                'address': validated_data.get('address'),
                'birthday': validated_data.get('birthday'),
                'gender': validated_data.get('gender'),
                'phone': phone,
                'code': phone,
            }
            elder = Elder.objects.create(**signupData)
            for caregiver in cared_by:
                CareGiving.objects.create(caregiver=caregiver, elder=elder)
            # g = Group.objects.get(name='Elder')
            # g.user_set.add(user)
            return elder
        else:
            username = validated_data.get('username')
            email = validated_data.get('email')
            password = validated_data.get('password')
            user = User.objects.create_user(username=username, email=email,
                                            password=password)
            fullname = validated_data.get('fullname')
            names = fullname.split(" ")
            user.first_name = names[0]
            if len(names)>1:
                user.last_name = names[1]
            user.save()
            signupData = {
                'user': user,
                'address': validated_data.get('address'),
                'birthday': validated_data.get('birthday'),
                'gender': validated_data.get('gender'),
                'phone': validated_data.get('phone'),
            }
            caregiver = CareGiver.objects.create(**signupData)
            # g = Group.objects.get(name='CareGiver')
            # g.user_set.add(user)
            return caregiver
