from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import RecruitSerializer, PlanetSerializer, SithSerializer
from mainapp.models import Recruit, Planet, Sith

# Статистика по планетам
class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class  SithViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class SithViewSet(ModelViewSet):
    queryset = Sith.objects.all()
    serializer_class = SithSerializer


class RecruitViewSet(ModelViewSet):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer


# def planet_list(request):
#     query = get_list_or_404(Planet)
#     data = map(lambda itm: {
#         'id': itm.id,
#         'name': itm.name
#
#     }, query)
#     return JsonResponse({'results': list(data), 'count': len(query)})