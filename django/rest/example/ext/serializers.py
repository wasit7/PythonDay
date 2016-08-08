from rest_framework import serializers
from ext.models import Extension

class ExtensionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Extension
		fields=('name','number')
