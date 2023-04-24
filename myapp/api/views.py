from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from myapp.api.serializers import CategorySerializer, BlogSerializer, CommentSerializer
from myapp.models import Category, Blog, Comment
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication


## Category Read, Create, Update and Delete


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        request_body=CategorySerializer,
        operation_description='Category create uchun',
        responses={201: CategorySerializer()}
    )
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryCreateAPIView2(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs.get('pk'))
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs.get('pk'))
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs.get('pk'))
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryUpdateAPIView2(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


## Category end



## Blog Read, Create, Update and Delete

class BlogListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogListWithCategoryAPIView(ListAPIView):
    queryset = Blog.objects.all()

    def list(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs.get('pk'))
        blog = Blog.objects.filter(category=category)
        serializer = BlogSerializer(blog, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BlogRetrievAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

## Blog end


## Comment Read, Create, Update and Delete

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrievAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListWithBlogAPIView(ListAPIView):
    queryset = Comment.objects.all()

    def list(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs.get('pk'))
        blog = Comment.objects.filter(blog=blog)
        serializer = CommentSerializer(blog, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDeleteUpdteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


