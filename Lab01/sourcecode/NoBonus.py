import os
import matplotlib.pyplot as plt
from queue import PriorityQueue
import math
import copy

def adj(matrix, u):
    '''
    Trả về những điểm lân cận có thể di chuyển qua từ điểm u
    adjacency 
    '''
    result = []
    try:
        if matrix[u[0]-1][u[1]] != 'x':
            result.append([u[0]-1,u[1]])
    except: 
        pass
    try:
        if matrix[u[0]][u[1]-1] != 'x':
            result.append([u[0],u[1]-1])
    except: 
        pass
    try:
        if matrix[u[0]+1][u[1]] != 'x':
            result.append([u[0]+1,u[1]])
    except: 
        pass
    try:
        if matrix[u[0]][u[1]+1] != 'x':
            result.append([u[0],u[1]+1])
    except: 
        pass
    return result


def dfs(matrix, start, end, visited = [], path = []): 
    '''
    Thuật toán dfs dùng đệ qui để tìm đường ra 
    '''
    if start not in visited and end not in visited: 
        visited.append(start)
        path.append(start)
        for u in adj(matrix, start):
            dfs(matrix, u, end, visited, path) 
        if end not in path: 
            path.pop()
        else:
            return path

def bfs(matrix, start, end):
    '''
    Thuật toán bfs search theo từng tầng trong cây
    '''
    path = []
    path_queue = []
    path_queue.append([start])
    visited = []
    k = 1
    while k and path_queue != []:
        path = path_queue.pop(0)
        x = path[-1]
        for u in adj(matrix, x):
            if u not in visited:
                visited.append(u)
                if u == end: 
                    k = 0
                    break
                path_temp = copy.copy(path)
                path_temp.append(u)
                path_queue.append(path_temp)
    path.append(end)
    return path            

def Heuristic(u, end):
    '''
    Chọn hàm heuristic chính là khoảng cách Manhattan 
    '''
    return math.sqrt(abs(u[0]-end[0])**2+abs(u[1]-end[1])**2)
def greedy_best_first_search(matrix, start, end):
    '''
    Thuật toán tham lam 
    '''
    visited = []
    path_queue = PriorityQueue()
    path_queue.put((0, [start]))
    while path_queue.empty() == False:
        path = path_queue.get()[1] #get list path
        u = path[-1] #last node in the path
        if u == end:
            return path
        for x in adj(matrix, u):
            if x not in visited:
                path_temp = copy.copy(path)
                visited.append(x)
                path_temp.append(x)
                path_queue.put((Heuristic(x,end), path_temp))
    return path



def Manhattan(u, end):
    return abs(u[0]-end[0])+ abs(u[1]-end[1])
#Ham g(n) chính là hàm len(path): Chiều dài path 
# Tuong Tu Nhu Greedy Search nhung them vao do la ham len(path) == g(n)  ham h(n) la mahattan
def A_asterisk(matrix, start, end):
    '''
    Thuật toán A* dùng hàm f(n) = g(n)+h(n)
    g(n) chính là chiều dài đường đi (len(path))
    h(n) là khoảng cách Manhattan
    '''
    visited = []
    path_queue = PriorityQueue()
    path_queue.put((Manhattan(start, end), [start]))
    while path_queue.empty() == False:
        path = path_queue.get()[1] #get list path
        u = path[-1] #last node in the path
        if u == end:
            return path
        for x in adj(matrix, u):
            if x not in visited:
                path_temp = copy.copy(path)
                visited.append(x)
                path_temp.append(x)
                f= len(path_temp) + Manhattan(x,end)
                path_queue.put((f,  path_temp))
    return path
'''
Code thu nghiem
def A_asterisk(matrix, start, end)
    visited = []
    path_queue = PriorityQueue()
    path_queue.put((distance(start, end), [start]))
    while path_queue.empty() == False:
        path = path_queue.get()[1] #get list path
        u = path[-1] #last node in the path
        print(u, end=" ")
        print(len(path) +distance(u, end)- 1)
        if u == end:
            print(path)
            break
        for x in adj(matrix, u):
            path_temp = copy.copy(path)
            path_temp.append(x)
            g= len(path_temp) - 1
            f= g + distance(x,end)
            if x not in visited:
                visited.append((f,g , x))
                path_queue.put((f,  path_temp))
            else:
                try:
                    index = [i[1] for i in visited].index(x)
                    if g < visited[index][1]:
                        visited[index][0] = f
                        visited[index][1] = g
                        path_queue.put((f,  path_temp))
                except: 
                    pass
    visualize_maze(matrix,[], start,end, route=path)

'''