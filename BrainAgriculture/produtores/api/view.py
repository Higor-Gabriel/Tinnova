from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum
from produtores.models import Produtor, Cultura
from produtores.api.serializer import ProdutorSerializer, CulturaSerializer


class ProdutorViewesets(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """
    Lista, Cria, Edita e Exclui produtores rurais
    """
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CulturaViewsets(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    """
    Lista, Cria, Edita e Exclui os grãos que podem ser plantdos
    """
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DashboardTotalsViewesets(View):
    def get(self, request, *args, **kwargs):
        total_productores = Produtor.objects.count()
        total_area_cultivable = Produtor.objects.aggregate(total_area=Sum('area_agricultavel_hectares'))['total_area']

        return JsonResponse({
            'total_produtores': total_productores,
            'total_area_cultivada': total_area_cultivable,
        })
