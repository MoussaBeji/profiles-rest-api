from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses http methods as function (post, get, put, patch, delete)',
            'Is similar as traditional Django view',
            'Give more control to your application logic',
            'Is mapped manualy to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})