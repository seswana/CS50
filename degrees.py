from collections import deque

def shortest_path(source, target):
    """
    Returns the shortest path from source to target using BFS.
    If no path exists, returns None.
    """
    # Очередь для BFS, храним путь как список кортежей (movie_id, person_id)
    frontier = deque([[(None, source)]])
    explored = set()

    while frontier:
        path = frontier.popleft()  # Берем первый путь из очереди
        current_person = path[-1][1]  # Последний человек в пути

        # Если нашли цель, возвращаем путь без стартового (None, source)
        if current_person == target:
            return path[1:]

        # Отмечаем человека как посещённого
        explored.add(current_person)

        # Проходим по всем соседям (людям, снимавшимся в фильмах вместе)
        for movie_id, neighbor in neighbors_for_person(current_person):
            if neighbor not in explored and not any(neighbor == p[-1][1] for p in frontier):
                new_path = path + [(movie_id, neighbor)]
                frontier.append(new_path)
    
    return None
