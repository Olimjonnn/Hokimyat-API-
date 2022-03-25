from django.shortcuts import render
from rest_framework.decorators import permission_classes, authentication_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from main.models import *
from main.serializer import *


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                name = request.data['name']
                Category.objects.create(name=name)
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                News.objects.create(
                    category_id = request.data['category'],
                    image = request.FILES.get("image"),
                    title = request.data['title'],
                    text = request.data['text'],
                    is_new = request.data['is_new']
                )
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

    @action(["GET"], detail=False)
    def find(self, request):
        try:
            category = request.GET.get("category")
            news = News.objects.filter(category_id=category)
            new = NewsSerializer(news, many=True)
            return Response(new.data)
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)
        

class MalumotlarView(viewsets.ModelViewSet):
    queryset = Malumotlar.objects.all()
    serializer_class = MalumotlarSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                Malumotlar.objects.create(
                    category_id = request.POST.get("category"),
                    image = request.FILES.get("image"),
                    title = request.data['title'],
                    text = request.POST.get['text'],
                )
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']
    def list(self, request):
        video = Video.objects.last()
        vid = VideoSerializer(video)
        return Response(vid.data)

class VideoNewsView(viewsets.ModelViewSet):
    queryset = VideoNews.objects.all()
    serializer_class = VideoNewsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                VideoNews.objects.create(
                    video_id = request.POST.get("video"),
                    title = request.data['title'],
                    text = request.data['text']
               )
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class XabarlarView(viewsets.ModelViewSet):
    queryset = Xabarlar.objects.all()
    serializer_class = XabarlarSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            user = request.user
            if user.type == 1:
                Xabarlar.objects.create(
                    category_id = request.POST.get("category"),
                    image = request.FILES.get("image"),
                    title = request.data['title'],
                    text = request.POST.get['text'],
                )
                return Response({"Created"})
            else:
                return Response({"Sorry :("})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)