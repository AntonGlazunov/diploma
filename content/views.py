import networkx as nx
import json
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from config.settings import GRAPH
from content.models import Movie
from users.models import User


class ContentListView(ListView):
    model = Movie


class ContentDetailView(DetailView):
    model = Movie

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        user.views.add(self.object)
        GRAPH.add_edge(user.pk, self.object.name)
        json_graph = nx.node_link_data(GRAPH, edges='edges')
        with open('graph.json', 'w', encoding='utf-8') as f:
            json.dump(json_graph, f, ensure_ascii = False)
        self.object.rank = GRAPH.in_degree(self.object.name)
        self.object.save()
        user.save()
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
        users = User.objects.all()
        user = self.request.user
        dict_neighbors = {}
        recommended_views_dict = {}
        recommended_views_list = []
        context_list = []
        movies = Movie.objects.all()
        neighbors = nx.average_neighbor_degree(GRAPH, source='out', target='in', nodes=[i for i in range(0, len(users)+1)])
        for key, item in neighbors.items():
            if item > 1.3:
                neighbors_preferences = users.get(pk=key).preferences.all()
                for preference in neighbors_preferences:
                    if preference in user.preferences.all():
                        dict_neighbors[key] = item
                        break
        if len(dict_neighbors) > 5:
            sort_list_neighbors = list(dict(sorted(dict_neighbors.items(), key=lambda item: item[1], reverse=True)).keys())[:5]
        else:
            sort_list_neighbors = list(dict_neighbors.keys())
        user_views_list = list(dict(GRAPH[user.pk]).keys())
        for neighbor in sort_list_neighbors:
            for view in list(dict(GRAPH[neighbor]).keys()):
                if view not in user_views_list:
                    recommended_views_list.append(view)
        for recommended in recommended_views_list:
            recommended_views_dict[recommended] = GRAPH.in_degree(recommended)
        sort_recommended_views_list = list(dict(sorted(recommended_views_dict.items(), key=lambda item: item[1], reverse=True)).keys())
        for i in sort_recommended_views_list:
            context_list.append(Movie.objects.get(name=i))
        for movie in movies:
            for preference in user.preferences.all():
                if preference in movie.category.all():
                    context_list.append(movie)
                    break
        context_data['objects'] = context_list
        return context_data

