from NoBonus import *
from Matrix import *
from WithBonus import *

# Bản đồ không có điểm thưởng
'''
In ra các bản đồ và đường đi tìm kiếm tương ứng
'''
for index in range(1,6):
    bonus_points, matrix = read_file(f'maze_map_no_bonus{index}.txt')
    # Find Start and End corodinate 
    end = [0,0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=[i,j]
            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=[i,j]

            else:
                pass
    visited = []
    path = []
    print('------------------------------------------------------------------------------------')
    print(f'matrix{i}X{j}')
    print(f"Ma trận Không có điểm thưởng thứ {index}")
    print('Depth-First_Search')
    visualize_maze(matrix, bonus_points, start,end, dfs(matrix, start, end, visited, path))
    print('Breadth First Search')
    visualize_maze(matrix, bonus_points, start,end, bfs(matrix, start,end))
    print('greedy_best_first_search')
    visualize_maze(matrix, bonus_points, start,end, greedy_best_first_search(matrix,start,end))
    print('A_Star_Search')
    visualize_maze(matrix, bonus_points, start,end, A_asterisk(matrix, start,end))

#Bản đồ có điểm thưởng
for index in range(1,4):
    bonus_points, matrix = read_file(f'maze_map_with_bonus{index}.txt')
    # Find Start and End corodinate 
    end = [0,0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=[i,j]
            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=[i,j]

            else:
                pass

    bonus_xy = [[x[0],x[1]] for x in bonus_points]
    bonus_value = [x[2] for x in bonus_points]
    print(f"Ban do thuong thu: {index}")
    (cost, path) = LeastCost(matrix, start, end,bonus_xy,bonus_value)
    print(f"Chi phi duong di {cost}")
    visualize_maze(matrix, bonus_points, start,end, path)



