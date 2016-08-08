from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ext.models import Extension
from ext.serializers import ExtensionSerializer

@api_view(['GET', 'POST'])
def detail(request,name):
	try:
		ex = Extension.objects.get(name=name)
	except Extension.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = ExtensionSerializer(ex)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer=ExtensionSerializer(ex,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
