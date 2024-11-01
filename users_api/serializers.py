from rest_framework import serializers

from config.settings import GRAPH
from content.services import recommended_movies, knn
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'avatar', 'phone', 'country', 'pk']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['preferences']


class MovieStatisticSerializer(serializers.ModelSerializer):
    count_views = serializers.SerializerMethodField()
    most_popular = serializers.SerializerMethodField()
    count_recommended_movie = serializers.SerializerMethodField()
    neighbor = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['count_views', 'most_popular', 'count_recommended_movie', 'neighbor']

    def get_count_views(self, instance):
        user = self.context['request'].user
        return len(list(GRAPH[user.pk]))

    def get_most_popular(self, instance):
        user = self.context['request'].user
        user_views = list(GRAPH[user.pk])
        most_popular = ''
        count_view = 0
        for view in user_views:
            if int(GRAPH.in_degree(view)) > count_view:
                count_view = int(GRAPH.in_degree(view))
                most_popular = view
        return most_popular

    def get_count_recommended_movie(self, instance):
        user = self.context['request'].user
        return len(recommended_movies(user))

    def get_neighbor(self, instance):
        user = self.context['request'].user
        neighbor = User.objects.get(pk=list(knn(user.pk))[0]).email
        return neighbor
