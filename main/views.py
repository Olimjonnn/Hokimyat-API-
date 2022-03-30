from cgitb import text
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


    http_method_names = ['get']

class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

    http_method_names = ['get']

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

   
class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def create(self, request):
        try:
            News.objects.create(
                category_id = request.data['category'],
                image = request.FILES.get("image"),
                title = request.data['title'],
                text = request.data['text'],
                is_new = request.data['is_new']
            )
            return Response({"Created"})

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


    def create(self, request):
        try:
            Malumotlar.objects.create(
                category_id = request.POST.get("category"),
                image = request.FILES.get("image"),
                title = request.data['title'],
                text = request.POST.get['text'],
            )
            return Response({"Created"})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    http_method_names = ['get']
    def list(self, request):
        video = Video.objects.last()
        vid = VideoSerializer(video)
        return Response(vid.data)

class VideoNewsView(viewsets.ModelViewSet):
    queryset = VideoNews.objects.all()
    serializer_class = VideoNewsSerializer

    def create(self, request):
        try:
            VideoNews.objects.create(
                video_id = request.POST.get("video"),
                title = request.data['title'],
                text = request.data['text']
            )
            return Response({"Created"})
        
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class XabarlarView(viewsets.ModelViewSet):
    queryset = Xabarlar.objects.all()
    serializer_class = XabarlarSerializer

    def create(self, request):
        try:
            Xabarlar.objects.create(
                category_id = request.POST.get("category"),
                image = request.FILES.get("image"),
                title = request.data['title'],
                text = request.POST.get['text'],
            )
            return Response({"Created"})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class ReklamaView(viewsets.ModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer

    http_method_names = ['get']

class FoydaliSaytlarView(viewsets.ModelViewSet):
    queryset = FoydaliSaytlar.objects.all()
    serializer_class = FoydaliSaytlarSerializer

    http_method_names = ['get']


class AndOrganingView(viewsets.ModelViewSet):
    queryset = AndOrganing.objects.all()
    serializer_class = AndOrganingSerializer

    http_method_names = ['get']


class Malumotlar2View(viewsets.ModelViewSet):
    queryset = Malumotlar2.objects.all()
    serializer_class = Malumotlar2Serializer

    def create(self, request):
        try:
            Malumotlar2.objects.create(
                category_id = request.POST.get("category"),
                image = request.FILES.get("image"),
                title = request.data['title'],
                text = request.POST.get['text'],
            )
            return Response({"Created"})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)
    

class TavsiyaVideoView(viewsets.ModelViewSet):
    queryset = TavsiyaVideo.objects.all()
    serializer_class = TavsiyaVideoSerializer
    
    def create(self, request):
        try:
            TavsiyaVideo.objects.create(
                title = request.data["title"],
                video = request.FILES.get("video")
            )
            return Response({"Created"})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

class KerakView(viewsets.ModelViewSet):
    queryset = Kerak.objects.all()
    serializer_class = KerakSerializer
    
    http_method_names = ['get']


class Loyiha1View(viewsets.ModelViewSet):
    queryset = Loyiha1.objects.all()
    serializer_class = Loyiha1Serializer
    
    http_method_names = ['get']


class XizmatlarView(viewsets.ModelViewSet):
    queryset = Xizmatlar.objects.all()
    serializer_class = XizmatlarSerializer
    
    http_method_names = ['get']


class AndijonView(viewsets.ModelViewSet):
    queryset = Andijon.objects.all()
    serializer_class = AndijonSerializer

    http_method_names = ['get']


class Loyiha2View(viewsets.ModelViewSet):
    queryset = Loyiha2.objects.all()
    serializer_class = Loyiha2Serializer

    http_method_names = ['get']


class InvsTarmoqlarView(viewsets.ModelViewSet):
    queryset = InvsTarmoqlar.objects.all()
    serializer_class = InvsTarmoqlarSerializer

    def create(self, request):
        try:
            InvsTarmoqlar.objects.create(
                category_id = request.POST.get("category"),
                image = request.FILES['image'],
                text = request.data['text']
            )
            return Response({"Created"})
        except Exception as ar:
            data = {
                "error":f"{ar}"
            }
            return Response(data)
            

class HujjatView(viewsets.ModelViewSet):
    queryset = Hujjat.objects.all()
    serializer_class = HujjatSerializer

    http_method_names = ['get']

class QoshimchaXizmatView(viewsets.ModelViewSet):
    queryset = QoshimchaXizmat.objects.all()
    serializer_class = QoshimchaXizmatSerializer

    http_method_names = ['get']


class SavolView(viewsets.ModelViewSet):
    queryset = Savol.objects.all()
    serializer_class = SavolSerializer


class JavobView(viewsets.ModelViewSet):
    queryset = Javob.objects.all()
    serializer_class = JavobSerializer

    def create(self, request):
        try:
            savol_id = request.data['savol']
            javob = request.data['javob']
            tick = request.data['tick']
            Javob.objects.create(tick=tick, savol_id=savol_id, javob=javob)
            return Response({"Added"})
        except Exception as ar:
            data = {
                "error": f"{ar}"
            }
            return Response(data)
        
    @action(['GET'], detail=False)
    def answer(self, request):
        savol = request.GET.get("savol")
        javob = Javob.objects.filter(savol_id=savol, tick=True)
        java = JavobSerializer(javob, many=True)
        return Response(java.data)
    
    @action(['GET'], detail=False)
    def sss(self, request):
        st_id = request.GET.get("st_id")
        end_id = request.GET.get("end_id")
        jab = Javob.objects.filter(id__gte=st_id, id__lte=end_id)
        jaav = JavobSerializer(jab, many=True)
        return Response(jaav.data) 

class Loyiha3View(viewsets.ModelViewSet):
    queryset = Loyiha3.objects.all()
    serializer_class = Loyiha3Serializer

    http_method_names = ['get']


class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    http_method_names = ['get']
