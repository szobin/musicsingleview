from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Single
from .serializers import SingleViewSerializer, SV_API_Serializer


class SingleViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Single.objects.all().order_by('title')
        serializer = SingleViewSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Single.objects.all()
        s = get_object_or_404(queryset, pk=pk)
        serializer = SingleViewSerializer(s, context={'request': request})
        return Response(serializer.data)


class SingleView(views.APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, pk):
        try:
            s = Single.objects.get(pk=pk)
            return Response(SV_API_Serializer(s, context={'request': request}).data)
        except Single.DoesNotExist:
            data = dict(error="Single with iswc: {} was not found".format(pk))
            return Response(data)

        except Exception as exc:
            data = dict(error=repr(exc))
            return Response(data)
