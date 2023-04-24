from rest_framework import serializers

from myapp.models import Blog
from user.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'image',
            'password',
            'password2',
        ]
        extra_kwargs = {
            "email": {'required': True},
            "first_name": {'required': True},
        }

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({'password': 'Password fields did not match'})
        return validated_data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image=validated_data['image'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'image',
            'birth_date',
            'address',
        ]


class UserOfBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'created', 'view']


class UserProfileSerializer(serializers.ModelSerializer):
    blog = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'image',
            'birth_date',
            'address',
            'blog',
        ]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['blog_count'] = instance.my_blogs.count()
        return context

    def get_blog(self, obj):
        blog = obj.my_blogs.all()
        serializers = UserOfBlogSerializer(blog, many=True)
        return serializers.data

