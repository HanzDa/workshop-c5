from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Models
from .models import Paloma

# Serializadores
from .serializers import PalomaSerializer


# # FUNCTION BASE VIEWS
# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({"message": "Chao mundo!"})
    
#     elif request.method == 'POST':
#         pass

#     else:
#         Response({'msg': 'Método no permitido'})

# # Create your views here.


# GENERIC VIEWS
class Aves(APIView):
    serializer_class = PalomaSerializer

    def get(self, request): # Son obligatorios
        palomas = Paloma.objects.all()
        
        paloma_serializada = self.serializer_class(palomas, many=True).data    

        # mensaje = <paloma -1>  [] {int, str, []}
        return Response({"animal": paloma_serializada}) # Json {} 

    def post(self, request):
        edad = request.data.get('edad')
        color = request.data.get('color')
        habitad = request.data.get('habitad')

        otra_paloma = Paloma.objects.create(edad=edad, color=color, habitad=habitad)

        return Response({'msg': 'Se creo una paloma yay!'})

    def put(self, request):
        pass

    def delete(self, request):
        pass
