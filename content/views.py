import networkx as nx
import json
from django.views.generic import ListView, DetailView

from config.settings import GRAPH
from content.models import Movie
from content.services import recommended_movies


class ContentListView(ListView):
    model = Movie


class ContentDetailView(DetailView):
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


class RecommendedMoviesListView(ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = recommended_movies(self.request.user)
        return context_data

