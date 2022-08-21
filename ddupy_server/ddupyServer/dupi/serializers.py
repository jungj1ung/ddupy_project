

from rest_framework import serializers
from .models import Dupi
from drf_extra_fields.fields import Base64ImageField

#테스트 할때만 Hyperlinked시리얼라이즈랑 dupiImg 시리얼라이즈 하고 실제할때는 두피상태만 하자
class DupiSerializer(serializers.ModelSerializer):
    dupiImg = Base64ImageField()

    class Meta:
        model = Dupi
        fields = ('dupiState', 'dupiImg')

    def create(self, validated_data):
        dupiImg = validated_data.pop('dupiImg')
        dupiState = validated_data.pop('dupiState')
        return Dupi.objects.create(dupiImg=dupiImg, dupiState=dupiState)

