import networkx as nx
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from config.settings import GRAPH
from content.models import Movie
from content.services import recommended_movies, statistics_for_user


class ContentListView(LoginRequiredMixin, ListView):
    model = Movie


class ContentDetailView(LoginRequiredMixin, DetailView):
    model = Movie

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        GRAPH.add_edge(user.pk, self.object.name)
        json_graph = nx.node_link_data(GRAPH, edges='edges')
        with open('graph.json', 'w', encoding='utf-8') as f:
            json.dump(json_graph, f, ensure_ascii = False)
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['graph'] = GRAPH
        context_data['categories'] = self.object.category.all()
        return context_data


class RecommendedMoviesListView(LoginRequiredMixin, ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = recommended_movies(self.request.user)
        return context_data

@login_required
def statistics(request):
    count_user_views, most_popular, count_recommended_movie, neighbor = statistics_for_user(request.user)
    context = {
        'count_user_views': count_user_views,
        'most_popular': most_popular,
        'count_recommended_movie': count_recommended_movie,
        'neighbor': neighbor.email
    }
    return render(request, 'content/statistics.html', context)
