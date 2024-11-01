import networkx as nx
from config.settings import GRAPH
import random

from content.models import Movie

nodes = len(GRAPH.nodes())


dict_graph_index = {node: idx for idx, node in enumerate(GRAPH.nodes())}


def encoding_graph():
    mapping_reverse = dict((v, k) for k, v in dict_graph_index.items())
    return mapping_reverse

def get_graph():
    index_graph = nx.Graph()
    for edge in GRAPH.edges():
        index_graph.add_edge(dict_graph_index[edge[0]], dict_graph_index[edge[1]])
    dict_graph = nx.convert.to_dict_of_lists(index_graph)
    return dict_graph

def get_user_index(user):
    return dict_graph_index[user]

def neights_count(graph, user):

    '''Список для сохранения результата подсчета соседей'''
    cnt_neis = [0] * len(graph)

    '''Список соседей исследуемой вершины'''
    node_neighbours = set(graph[user])

    '''Словарь для списка вершин, не связанных с node, и их соседей'''
    after_one_neigh_dict = {}

    '''Заполнение словаря after_one_neigh_dict'''
    for u in graph[user]:
        for v in graph[u]:
            after_one_neigh_dict[v] = graph[v]

    '''Проход по вершинам в двух шагах от целевой
       Поиск пересечений списков соседей'''
    for i in after_one_neigh_dict:
        check = len(set(after_one_neigh_dict[i]) & node_neighbours)
        cnt_neis[i] = check

    '''Зануление результата для исследуемой вершины и ее реальных соседей'''
    cnt_neis[user] = 0
    for neigh in graph[user]:
        cnt_neis[neigh] = 0

    return cnt_neis


def from_distance(graph, node, time=10, samples=20):
    '''Список для сохранения результата'''
    from_dist = [0] * nodes

    '''Список для подсчета количества раз достижения вершин'''
    ach_times = [0] * nodes

    '''Список для суммы порядковых номеров шагов при достижении'''
    used = [0] * nodes

    '''Совершение блужданий'''
    for iter in range(samples):
        u = node

        '''Список вершин, посещенных в блуждании'''
        visited_nodes = []

        for step in range(time):
            '''Выбор случайной вершины из числа соседних'''
            next_node = random.choice(graph[u])

            '''Проверка наличия вершины в списке посещенных'''
            if next_node not in visited_nodes:
                '''Если вершина не посещена'''

                '''Увеличение значения суммы шагов для текщей вершины'''
                used[next_node] += step + 1

                '''Увеличение значения в списке для фиксации количества
                   блужданий, в которых была достигнута вершина'''
                ach_times[next_node] += 1

                '''Добавление вершины в список посещенных
                   вершин в текущем блуждании'''
                visited_nodes.append(next_node)

            u = next_node

    '''Для каждой вершины считаем количество блужданий, в которые она не была посещена'''
    plus_to_used = [(samples - el) * time for el in ach_times]

    '''Вычисляем среднее количество шагов для каждой вершины'''
    from_dist = [el / samples for el in list(map(sum, zip(used, plus_to_used)))]

    '''Для исследуемой вершины и ее соседей проставляем максимальное количество шагов'''
    from_dist[node] = time * samples
    for neigh in graph[node]:
        from_dist[neigh] = time * samples

    return from_dist


def to_distance(graph, node, time=10):
    '''Формируем матрицу, наполняем нулями'''
    martix = [[0 for _ in range(nodes)] for _ in range(time + 1)]

    '''Цикл расчетов'''
    for t in range(1, time + 1):
        '''Проверка каждой вершины'''
        for curr_node in range(nodes):
            '''Если текущая вершина равна исследуемой, то пропускаем'''
            if curr_node == node or graph.get(curr_node) is None:
                continue
            '''Если не исследуемая'''
            if graph[curr_node]:
                '''Для первого шага всем ставим 1'''
                '''Для остальных делаем расчет по формуле'''
                if t == 1:
                    martix[t][curr_node] = 1
                else:
                    prev_t_sum = 0
                    node_nei = graph[curr_node]
                    for prev_node in node_nei:
                        prev_t_sum += martix[t - 1][prev_node]

                    martix[t][curr_node] = 1 + (1 / len(node_nei))
            else:
                continue

    '''Для исследуемой вершины и ее соседей проставляем максимальное количество шагов'''
    martix[time][node] = time
    for neigh in graph[node]:
        martix[time][neigh] = time

    return martix[time]

def normalize_list(lst, reverse=False):
    min_val = min(lst)
    max_val = max(lst)
    if reverse:
            normalized_list = [1 - (x - min_val) / (max_val - min_val) for x in lst]
    else:
        normalized_list = [(x - min_val) / (max_val - min_val) for x in lst]

    return normalized_list


def combine_ans(data1, data2, data3):
    return [x + y + z for x, y, z in zip(data1, data2, data3)]

def knn(user):
    nc = neights_count(get_graph(), get_user_index(user))
    fd = from_distance(get_graph(), get_user_index(user))
    td = to_distance(get_graph(), get_user_index(user))

    norm_nc = normalize_list(nc, True)
    norm_fd = normalize_list(fd)
    norm_td = normalize_list(td)

    ca = combine_ans(norm_nc, norm_fd, norm_td)
    comb_ans = {}
    for ind, el in enumerate(ca):
        comb_ans[encoding_graph()[ind]] = el
    comb_ans_sorted = dict(sorted(comb_ans.items(), key=lambda x: x[1], reverse=False)[:5])
    return comb_ans_sorted

def recommended_list(user):
    neighbors = knn(user)
    recommended_list = []
    recommended_dict = {}
    for neighbor in neighbors.keys():
        for movie in list(GRAPH[neighbor]):
            if movie not in recommended_list:
                if movie not in list(GRAPH[user]):
                    recommended_list.append(movie)

    for recommended in recommended_list:
        recommended_dict[recommended] = GRAPH.in_degree(recommended)
    sort_recommended_list = list(
        dict(sorted(recommended_dict.items(), key=lambda item: item[1], reverse=True)).keys())
    return sort_recommended_list, neighbors


def recommended_movies(user):
    context_list = []
    movies = Movie.objects.all()
    sort_recommended_list, neighbors = recommended_list(user.pk)
    for neighbor in neighbors.keys():
        for movie in list(GRAPH[neighbor]):
            for sort_recommended_movie in sort_recommended_list:
                if movie == sort_recommended_movie:
                    context_list.append(movies.get(name=sort_recommended_movie))
    for movie in movies:
        if movie.name not in sort_recommended_list:
            for preference in user.preferences.all():
                if preference in movie.category.all():
                    context_list.append(movie)
                    break
    return context_list






