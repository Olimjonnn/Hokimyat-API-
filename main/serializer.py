from rest_framework import serializers
from main.models import *

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = News
        fields = "__all__"

class MalumotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malumotlar
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class VideoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNews
        fields = "__all__"

class XabarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xabarlar
        fields = "__all__"

class ReklamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = "__all__"

class FoydaliSaytlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoydaliSaytlar
        fields = "__all__"

class AndOrganingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndOrganing
        fields = "__all__"

class Malumotlar2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Malumotlar2
        fields = "__all__"

class KerakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kerak
        fields = "__all__"

class TavsiyaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TavsiyaVideo
        fields = "__all__"

class Loyiha1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loyiha1
        fields = "__all__"

class XizmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = "__all__"

class AndijonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andijon
        fields = "__all__"

class Loyiha2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loyiha2
        fields = "__all__"

class InvsTarmoqlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvsTarmoqlar
        fields = "__all__"

class HujjatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hujjat
        fields = "__all__"

class QoshimchaXizmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = QoshimchaXizmat
        fields = "__all__"

class SavolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savol
        fields = "__all__"

class JavobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javob
        fields = "__all__"

class Savol_JavobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savol_Javob
        fields = "__all__"

class Loyiha3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loyiha3
        fields = "__all__"

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"