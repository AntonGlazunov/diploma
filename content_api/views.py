from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from content.models import Movie
from content.services import recommended_movies
from content_api.serializers import MovieSerializer
from users_api.paginators import MoviesPaginator


class MovieListAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MoviesPaginator

    def get_queryset(self):
        recommended_list = recommended_movies(self.request.user)
        recommended_name_list = []
        for recommended_movie in recommended_list:
            recommended_name_list.append(recommended_movie.name)
        queryset = Movie.objects.filter(name__in=recommended_name_list)
        return queryset
