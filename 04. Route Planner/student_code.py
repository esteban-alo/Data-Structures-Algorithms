#!/usr/bin/python

# Libraries
from math import sqrt

class Node:
    
    point = ""
    priority = 0.0
    
    def __init__(self, point, priority):
        self.point = point
        self.priority = priority

class PriorityQueue:
    
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i) for i in self.queue])
    
    def is_empty(self):
        return not self.queue
    
    def enqueue(self, point, priority):
        """
        Inserts an node item in queue, if the node item is in the queue and updates the position in the queue depending the height value of the priority
        """
        node = Node(point, priority)

        if self.is_empty():
            self.queue.append(node)

        try:
            is_node_added = False
            
            if is_node_added == False:
                self.queue.append(node)
                
            for index, queue_node_item in enumerate(self.queue):
                if queue_node_item.priority > node.priority:
                    self.queue.insert(index, node)
                    is_node_added = True
                    break
                    
        except Exception as e:
            print(e)
    
    def dequeue(self):
        return self.queue.pop(0)
    
def calc_distance(origin_point: [float, float], end_point: [float, float]):
    """
    Estimates the straight-line distance between two points in Euclidean space.
    :param: origin_point frointer point in the path
    :param: end_point goal point in the path
    :return: Euclidian distance between frointer and goal point
    """
    return sqrt(pow((end_point[0] - origin_point[0]),2) + pow((end_point[1] - origin_point[1]),2))

def shortest_path(M, start, goal):
    """
    Given a map 'M' a start and goal point this method must return the shortest path, using the A* algorithm. Represented by the formula 'F(n) = G(n) + H(n)', where:
    - F(n): is the total cost
    - G(n): is the heuristic value of the node
    - H(n): is the path cost

    :param M:  map
    :param start:  point in the map
    :param goal:  goal point in the map
    :return: best route path 
    """
    nexplored_path = None
    priority_queue = PriorityQueue()
    priority_queue.enqueue(start, 0)
    explored_path = {}
    explored_path[start] = None
    node_heuristic_cost = {}
    node_heuristic_cost[start] = 0

    if start == goal:
        return [start]

    if priority_queue.is_empty():
        return None

    while not priority_queue.is_empty():
        lowest_node = priority_queue.dequeue()
        current_node = lowest_node.point

        for m_road_item in M.roads[current_node]:
            nodes_distances = node_heuristic_cost[current_node] + calc_distance(M.intersections[current_node], M.intersections[m_road_item])
            if m_road_item not in node_heuristic_cost or nodes_distances < node_heuristic_cost[m_road_item]:
                node_heuristic_cost[m_road_item] = nodes_distances
                cost_value = nodes_distances + calc_distance(M.intersections[m_road_item], M.intersections[goal])
                priority_queue.enqueue(m_road_item, cost_value)
                explored_path[m_road_item] = current_node

        if current_node == goal:
            best_path = []
            while current_node != start:
                best_path.append(current_node)
                current_node = explored_path[current_node]
            best_path.append(start)
            return best_path[::-1]
        
    return None
