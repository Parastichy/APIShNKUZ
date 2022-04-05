from rest_framework import serializers
from .models import Standard, ResourceRequirement, Resources, Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name']


class ResourcesSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=False)

    class Meta:
        model = Resources
        fields = ['code', 'resourceName', 'unit']


class ResourceRequirementSerializer(serializers.ModelSerializer):
    expenditure = ResourcesSerializer(many=False)

    class Meta:
        model = ResourceRequirement
        fields = ['expenditure', 'consumptionRate', ]


class StandardSerializer(serializers.ModelSerializer):
    must = ResourceRequirementSerializer(many=True)


    class Meta:
        model = Standard
        fields = ['id', 'searchCode', 'originalCipherFromDocument', 'name', 'unit', 'must']

class StandardMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = ['id', 'searchCode']


