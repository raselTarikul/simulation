from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from gridsingularity.utils import sim
from gridsingularity.exceptions.exceptions import NotFoundException
from .models import SimulationResult
from .serializers import SimulationResultSerializer


class CreateSimulation(APIView):
    """
    Api view for Create simulation
    """
    def post(self, request):
        """
        Accept request object start simulation

        Parameters: 
        request : request with the payloads
    
        Returns: 
        response: Return a json object

        """
        active, reactive = sim.run_simulation()
        serializer =  SimulationResultSerializer(data={'active': active, 'reactive': reactive})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class GetSimulation(APIView):
    """
    Api view for Get simulation result
    """
    def get(self, request, id):
        """
        Return simulation result
    
        Returns: 
        response: Return a json object

        """
        # Get the last simulation
        try:
            simulation = SimulationResult.objects.get(id=id)
            serializer =  SimulationResultSerializer(simulation)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFoundException('Simulation not found')


class GetSimulationActive(APIView):
    """
    Api view for Get simulation result active only
    """
    def get(self, request, id):
        """
        Return result simulation result active only
    
        Returns: 
        response: Return a json object

        """
        # Get the last simulation
        try:
            simulation = SimulationResult.objects.get(id=id)
            serializer =  SimulationResultSerializer(simulation)
            return Response({'active': serializer.data['active'] })
        except ObjectDoesNotExist:
            raise NotFoundException('Simulation not found')


class GetSimulationReActive(APIView):
    """
    Api view for Get simulation result reactive only
    """
    def get(self, request, id):
        """
        Return result simulation result reactive only
    
        Returns: 
        response: Return a json object

        """
        # Get the last simulation
        try:
            simulation = SimulationResult.objects.get(id=id)
            serializer =  SimulationResultSerializer(simulation)
            return Response({'reactive': serializer.data['reactive'] })
        except ObjectDoesNotExist:
            raise NotFoundException('Simulation not found')

