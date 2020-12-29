from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from . import serializers

class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		"""Returns a list of APIView features"""

		an_apiview = [
			'Uses HTTP methods as functions (get, post, patch, put, delete)',
			'Is similar to a traditional Django View',
			'Gives you the most control over your logic',
			'Is mapped manually to URLs',
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})

	def post(self, request):
		serializer = self.serializer_class(data = request.data)

		if(serializer.is_valid()):
			name = serializer.validated_data['name']
			message = f'Hello {name}'
			return Response({'message' : message})

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk = None):
		""" Handle updating an object """
		return Response({"message" : "PUT"})

	def patch(self, request, pk = None):
		""" Handle a partial update of an object """
		return Response({"message" : "PATCH"})

	def delete(self, request, pk = None):
		return Response({"message" : "DELETE"})


class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet"""
	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a hello message."""
		...

	def create(self, request):
		"""Create a new hello message."""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}!'
			return Response({'message': message})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

	def retrieve(self, request, pk=None):
		"""Handle getting an object by its ID"""

		return Response({'http_method': 'GET'})

	def update(self, request, pk=None):
		"""Handle updating an object"""

		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):
		"""Handle updating part of an object"""

		return Response({'http_method': 'PATCH'})

	def destroy(self, request, pk=None):
		"""Handle removing an object"""

		return Response({'http_method': 'DELETE'})