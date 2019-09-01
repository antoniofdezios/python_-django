
from Foods.models import Food
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        qs = self.queryset
        return qs

    def perform_create(self, serializer):
        serializer.save()

    class Meta:
        model = Food
        fields = "__all__"
