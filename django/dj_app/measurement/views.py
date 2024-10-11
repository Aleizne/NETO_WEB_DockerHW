# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
# from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorListSerializer, MeasurementListSerializer


class APISensorsView(ListCreateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class APISensorDetailView(RetrieveUpdateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class APIMeasurementView(CreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementListSerializer