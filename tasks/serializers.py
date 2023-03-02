from rest_framework import serializers
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['sub_category'] = CategorySerializer(instance.sub_category).data
        return rep


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = "__all__"

    def to_representation(self, instance):
        try:
            rep = super().to_representation(instance)
            rep['category'] = CategorySerializer(instance.category).data
            return rep
        except AttributeError:
            return