from NoBonus import *
def LeastCost(matrix, start, end, bonus_xy, bonus_value):
    '''
    Hàm tìm đường đi tối ưu với chi phí thấp nhất
    Dùng giải thuật đệ qui 
    bonus_xy = [[ , ], [ , ]] lưu tọa độ các điểm bonus
    bonus_value = [ , , ] là giá trị tương ứng với các tọa độ trên
    Giải thuật: Với mỗi điểm bắt đầu có 2 TH xảy ra: 
                TH1: Không đi qua điểm thưởng nào cả -> Ta tính được đường đi và 
    '''

    ## TH: Khong qua diem thuong
    path = A_asterisk(matrix, start, end)
    cost = len(path) - 1
    if bonus_xy == []: 
        return (cost, path)
    minimum = cost
    minimum_path = path 
    # TH: Qua Diem Thuong 
    for u in bonus_xy: 
        
        bonus_xy_temp = copy.copy(bonus_xy) 
        bonus_value_temp = copy.copy(bonus_value)
        path_start_u = A_asterisk(matrix, start, u) # Đường đi ngắn nhất từ start->u (không qua điểm thưởng)
        cost_start_u = len(path_start_u) - 1

        bonus_value_temp.pop(bonus_xy_temp.index(u))
        bonus_xy_temp.remove(u)
        
        (cost_u_end, path_u_end) = LeastCost(matrix, u, end, bonus_xy_temp, bonus_value_temp) # Tìm đường đi ngắn nhất từ u->end (kể cả qua điểm thưởng)
        if minimum > cost_start_u + bonus_value[bonus_xy.index(u)] + cost_u_end: 
            minimum = cost_start_u + bonus_value[bonus_xy.index(u)] + cost_u_end
            minimum_path = path_start_u+path_u_end
            
    if cost <= minimum:
        return (cost, path)
    else: 
        return (minimum, minimum_path)
    
            
        