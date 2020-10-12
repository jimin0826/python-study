import numpy as np
import os
import math

# seoul_point = np.ones((3678, 3030))
'''
velocity_up = np.zeros((3678, 3030, 3))
velocity_down = np.zeros((3678, 3030, 3)) 
velocity_right = np.zeros((3678, 3030, 3))
velocity_left = np.zeros((3678, 3030, 3)) 
count_up = np.zeros((3678, 3030, 3)) 
count_down = np.zeros((3678, 3030, 3))
count_right = np.zeros((3678, 3030, 3))
count_left = np.zeros((3678, 3030, 3))
'''
velocity_up = np.zeros((4000, 4000))
velocity_down = np.zeros((4000, 4000)) 
velocity_right = np.zeros((4000, 4000))
velocity_left = np.zeros((4000, 4000)) 
count_up = np.zeros((4000, 4000)) 
count_down = np.zeros((4000, 4000))
count_right = np.zeros((4000, 4000))
count_left = np.zeros((4000, 4000))
print("<<<<Setting Finish>>>>")

# 7~9  1~3  5~7
# 070000 ~ 090000       130000 ~ 150000     170000 ~ 190000
                                                                                      
Lati_per_index = 0.0000891815                                                         
Long_per_index = 0.000113043
Lati_South = 37.428576
Lati_North = 37.698796
Long_West = 126.767177
Long_East = 127.18295

def gps_to_point(Lati, Long) :
    init_Lati = (Lati - Lati_South)
    init_Long = (Long - Long_West)
    index_Lati = round(init_Lati/Lati_per_index)
    index_Long = round(init_Long/Long_per_index)
    return index_Lati, index_Long

North_index = round((37.533119-Lati_South)/Lati_per_index)
South_index = round((37.454811-Lati_South)/Lati_per_index)
East_index = round((127.075465-Long_West)/Long_per_index)
West_index = round((126.980134-Long_West)/Long_per_index)
print(North_index, South_index, East_index, West_index)

fire_station = [gps_to_point(37.507279, 127.0938799), gps_to_point(37.5157882, 127.0727934), gps_to_point(37.4984323, 126.9919145), 
                gps_to_point(37.4754906, 126.9881933), gps_to_point(37.4694447, 127.0408294), gps_to_point(37.4879992, 127.0275872),
                gps_to_point(37.4990385, 127.0115884), gps_to_point(37.4805791, 127.0238765), gps_to_point(37.51036, 127.0668895),
                gps_to_point(37.5221047, 127.0369213), gps_to_point(37.4970886, 127.0424324), gps_to_point(37.4848802, 127.0928217),
                gps_to_point(37.4746584, 127.0498818), gps_to_point(37.537391, 127.060085), gps_to_point(37.5343446,126.9957743),
                gps_to_point(37.5207629,126.9949692)] 

'''
########## Folder1 Data ###########
Folder1_filename = []
for file in os.listdir("Folder1"):
    if file.endswith(".txt"): #끝이 ".txt"로 끝나는 경우
        Folder1_filename.append(file)


for filename in Folder1_filename :
    with open('Folder1/' + filename, 'r', encoding = 'utf8') as f :
        text = f.read()
        docs = text.split('\n')[3:]
        print(filename)
        len_docs = len(docs)

        if(len_docs > 100) :    
            with open('Folder1_R_2/' + filename, 'w') as g :
                for i in range(len_docs-15) :                           
                    docs[i] = docs[i].split()
                    avg = 0
                    for j in range(i+1, i+11) :
                        doc = docs[j].split()
                        avg += float(doc[2])
                    if(i != 0) and avg/10 > 10 :
                        if(int(docs[i][0]) != int(docs[i-1][0])) :
                        # if(docs[i][2] is not '0' and int(docs[i][0]) != int(docs[i-1][0])) :
                            gtp = gps_to_point(float(docs[i][0][:2] + '.' + docs[i][0][2:]), float(docs[i][1][:3] + '.' + docs[i][1][3:]))
                            g.write(str(gtp[0]) + ' ' + str(gtp[1]) + ' ' + docs[i][2] + ' ' + docs[i][3] + ' ' + docs[i][4] + '\n')
                            # print(gps_to_point(float(docs[i][0][:2] + '.' + docs[i][0][2:]), float(docs[i][1][:3] + '.' + docs[i][1][3:])))

########## Folder2 Data ###########
Folder2_filename = []
for file in os.listdir("Folder2"):
    if file.endswith(".txt"): #끝이 ".txt"로 끝나는 경우
        Folder2_filename.append(file)


for filename in Folder2_filename :
    with open('Folder2/' + filename, 'r', encoding = 'utf8') as f :
        text = f.read()
        docs = text.split('\n')[3:]
        print(filename)
        len_docs = len(docs)

        if(len_docs > 100) :    
            with open('Folder1_R_2/' + filename, 'w') as g :
                for i in range(len_docs-15) :                           
                    docs[i] = docs[i].split()
                    avg = 0
                    for j in range(i+1, i+11) :
                        doc = docs[j].split()
                        avg += float(doc[2])
                    if(i != 0) and avg/10 > 10 :
                        if(int(docs[i][0]) != int(docs[i-1][0])) :
                        # if(docs[i][2] is not '0' and int(docs[i][0]) != int(docs[i-1][0])) :
                            gtp = gps_to_point(float(docs[i][0][:2] + '.' + docs[i][0][2:]), float(docs[i][1][:3] + '.' + docs[i][1][3:]))
                            g.write(str(gtp[0]) + ' ' + str(gtp[1]) + ' ' + docs[i][2] + ' ' + docs[i][3] + ' ' + docs[i][4] + '\n')
                            # print(gps_to_point(float(docs[i][0][:2] + '.' + docs[i][0][2:]), float(docs[i][1][:3] + '.' + docs[i][1][3:])))
                            Folder1_filename = []     

'''

def velocity_accumulator(time_index) :
    print("######## Start velocity accumulator #########")
    ########## 속도 측정기 ##########
    Folder_data_filename = []
    for file in os.listdir("Folder1_R_2"):
        if file.endswith(".txt"): #끝이 ".txt"로 끝나는 경우
            Folder_data_filename.append(file)

    for filename in Folder_data_filename :
        print(filename)
        with open('Folder1_R_2/' + filename, 'r', encoding = 'utf8') as f :
            text = f.read()
            docs = text.split('\n')
            #print(filename)
            len_docs = len(docs)

            for i in range(len_docs) :
                docs[i] = docs[i].split()

            for i in range(len_docs-2) :
                # point_previous = [int(docs[i-1][0]), int(docs[i-1][1])]
                point_present = [int(docs[i][1]), int(docs[i][0])]
                point_future = [int(docs[i+1][1]), int(docs[i+1][0])]
                present_time = int(docs[i][4])                          # 현재 시간
                future_time = int(docs[i+1][4])                         # 미래 시간
                present_velocity = int(docs[i][2])                      # 현재 속도  
                N = abs(point_future[0] - point_present[0]) + abs(point_future[1] - point_present[1]) # 이동한 총 거리    
                if(N != 0) :
                    x_weight = present_velocity * abs(point_future[0] - point_present[0]) / N  # x 이동거리 가중치
                    y_weight = present_velocity * abs(point_future[1] - point_present[1]) / N  # y 이동거리 가중치
                else :
                    x_weight = 0
                    y_weight = 0

                if(0 < point_present[0] and point_present[0] < 4000 and point_present[1] > 0 and point_present[1] < 4000) :
                    if(future_time - present_time < 130 and present_velocity < 100) :
                                   ##### 아침 시간대 속도 구하기 #####
                        if(present_time >= 70000 and present_time <= 90000 and time_index == 0) :           # 아침 시간대 속도 구하기   
                            if(point_future[0] == point_present[0]) :       # x축으로 움직이지 않았을 때
                                if(point_future[1] > point_present[1]) :    # 위 방향으로                            1
                                    velocity_up[point_present[0]][point_present[1]] += present_velocity
                                    count_up[point_present[0]][point_present[1]] += 1
                                else :                                      # 아래 방향으로                          2
                                    velocity_down[point_present[0]][point_present[1]] += present_velocity
                                    count_down[point_present[0]][point_present[1]] += 1  
                            elif(point_future[0] > point_present[0]) :   # 오른쪽으로 움직였을 때
                                if(point_future[1] == point_present[1]) :   # y축으로 움직이지 않았을 때             3
                                    velocity_right[point_present[0]][point_present[1]] += present_velocity
                                    count_right[point_present[0]][point_present[1]] += 1
                                if(point_future[1] > point_present[1]) :    # 오른쪽 & 위                            4
                                    velocity_right[point_present[0]][point_present[1]] += x_weight
                                    velocity_up[point_present[0]][point_present[1]] += y_weight
                                    count_right[point_present[0]][point_present[1]]+=1
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 오른쪽 & 아래                          5
                                    velocity_right[point_present[0]][point_present[1]] += x_weight
                                    velocity_down[point_present[0]][point_present[1]] += y_weight
                                    count_right[point_present[0]][point_present[1]]+=1
                                    count_down[point_present[0]][point_present[1]]+=1
                            elif(point_future[0] < point_present[0]) :   # 왼쪽으로 움직였을 때
                                if(point_future[1] == point_present[1]) :   # y축으로 움직이지 않았을 때             6
                                    velocity_left[point_present[0]][point_present[1]] += present_velocity
                                    count_left[point_present[0]][point_present[1]]+=1
                                if(point_future[1] > point_present[1]) :    # 왼쪽 & 위                              7
                                    velocity_left[point_present[0]][point_present[1]] += x_weight
                                    velocity_up[point_present[0]][point_present[1]] += y_weight
                                    count_left[point_present[0]][point_present[1]]+=1
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 왼쪽 & 아래                            8
                                    velocity_left[point_present[0]][point_present[1]] += x_weight
                                    velocity_down[point_present[0]][point_present[1]] += y_weight
                                    count_left[point_present[0]][point_present[1]]+=1
                                    count_down[point_present[0]][point_present[1]]+=1
                                  ###### 보통 시간대 속도 구하기 #####                                                          
                        elif(present_time >= 130000 and present_time <= 150000 and time_index == 1) :    # 보통 시간대 속도 구하기
                            if(point_future[0] == point_present[0]) :       # x축으로 움직이지 않았을 때
                                if(point_future[1] > point_present[1]) :    # 위 방향으로                            1
                                    velocity_up[point_present[0]][point_present[1]] += present_velocity
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 아래 방향으로                          2
                                    velocity_down[point_present[0]][point_present[1]] += present_velocity
                                    count_down[point_present[0]][point_present[1]]+=1
                            elif(point_future[0] > point_present[0]) :   # 오른쪽으로 움직였을 때
                                if(point_future[1] == point_present[1]) :   # y축으로 움직이지 않았을 때             3
                                    velocity_right[point_present[0]][point_present[1]] += present_velocity
                                    count_right[point_present[0]][point_present[1]]+=1
                                if(point_future[1] > point_present[1]) :    # 오른쪽 & 위                            4
                                    velocity_right[point_present[0]][point_present[1]] += x_weight
                                    velocity_up[point_present[0]][point_present[1]] += y_weight
                                    count_right[point_present[0]][point_present[1]]+=1
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 오른쪽 & 아래                          5
                                    velocity_right[point_present[0]][point_present[1]] += x_weight
                                    velocity_down[point_present[0]][point_present[1]] += y_weight   
                                    count_right[point_present[0]][point_present[1]]+=1
                                    count_down[point_present[0]][point_present[1]]+=1                
                            elif(point_future[0] < point_present[0]) :   # 왼쪽으로 움직였을 때
                                if(point_future[1] == point_present[1]) :   # y축으로 움직이지 않았을 때             6
                                    velocity_left[point_present[0]][point_present[1]] += present_velocity
                                    count_left[point_present[0]][point_present[1]] +=1
                                if(point_future[1] > point_present[1]) :    # 왼쪽 & 위                              7
                                    velocity_left[point_present[0]][point_present[1]] += x_weight
                                    velocity_up[point_present[0]][point_present[1]] += y_weight
                                    count_left[point_present[0]][point_present[1]]+=1
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 왼쪽 & 아래                            8
                                    velocity_left[point_present[0]][point_present[1]] += x_weight
                                    velocity_down[point_present[0]][point_present[1]] += y_weight
                                    count_left[point_present[0]][point_present[1]]+=1
                                    count_down[point_present[0]][point_present[1]]+=1
                    
                                    ##### 퇴근 시간대 속도 구하기 #####
                        elif(present_time >= 170000 and present_time <= 190000 and time_index == 2) :    # 퇴근 시간대 속도 구하기
                            if(point_future[0] == point_present[0]) :       # x축으로 움직이지 않았을 때
                                if(point_future[1] > point_present[1]) :    # 위 방향으로                            1
                                    velocity_up[point_present[0]][point_present[1]] += present_velocity
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 아래 방향으로                          2
                                    velocity_down[point_present[0]][point_present[1]] += present_velocity
                                    count_down[point_present[0]][point_present[1]]+=1
                            elif(point_future[0] > point_present[0]) :   # 오른쪽으로 움직였을 때
                                if(point_future[1] == point_present[1]) :   # y축으로 움직이지 않았을 때             3
                                    velocity_right[point_present[0]][point_present[1]] += present_velocity
                                    count_right[point_present[0]][point_present[1]]+=1
                                if(point_future[1] > point_present[1]) :    # 오른쪽 & 위                            4
                                    velocity_right[point_present[0]][point_present[1]] += x_weight
                                    velocity_up[point_present[0]][point_present[1]] += y_weight
                                    count_right[point_present[0]][point_present[1]]+=1
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 오른쪽 & 아래                          5
                                    velocity_right[point_present[0]][point_present[1]] += x_weight
                                    velocity_down[point_present[0]][point_present[1]] += y_weight   
                                    count_right[point_present[0]][point_present[1]]+=1
                                    count_down[point_present[0]][point_present[1]]+=1
                            elif(point_future[0] < point_present[0]) :   # 왼쪽으로 움직였을 때
                                if(point_future[1] == point_present[1]) :   # y축으로 움직이지 않았을 때             6
                                    velocity_left[point_present[0]][point_present[1]] += present_velocity
                                    count_left[point_present[0]][point_present[1]]+=1
                                if(point_future[1] > point_present[1]) :    # 왼쪽 & 위                              7
                                    velocity_left[point_present[0]][point_present[1]] += x_weight
                                    velocity_up[point_present[0]][point_present[1]] += y_weight
                                    count_left[point_present[0]][point_present[1]]+=1
                                    count_up[point_present[0]][point_present[1]]+=1
                                else :                                      # 왼쪽 & 아래                            8
                                    velocity_left[point_present[0]][point_present[1]] += x_weight
                                    velocity_down[point_present[0]][point_present[1]] += y_weight
                                    count_left[point_present[0]][point_present[1]]+=1
                                    count_down[point_present[0]][point_present[1]]+=1
    
    print("######## Normalizing ########")
    for i in range(West_index-150, East_index+150) :
        for j in range(South_index-150, North_index+150) :
            if(velocity_up[i][j] == 0 or (velocity_up[i][j] / count_up[i][j])> 100 or (velocity_up[i][j] > 100)) :
                velocity_up[i][j] = 5
            else : 
                velocity_up[i][j] = velocity_up[i][j] / count_up[i][j]
            if(velocity_down[i][j] == 0 or velocity_down[i][j] / count_down[i][j] > 100 or velocity_down[i][j] > 100) :  # down 
                velocity_down[i][j] = 5
            else : 
                velocity_down[i][j] = velocity_down[i][j] / count_down[i][j]
            if(velocity_right[i][j] == 0 or velocity_right[i][j] / count_right[i][j] > 100 or velocity_right[i][j] > 100) : # right 
                velocity_right[i][j] = 5
            else : 
                velocity_right[i][j] = velocity_right[i][j] / count_right[i][j]
            if(velocity_left[i][j] == 0 or velocity_left[i][j] / count_left[i][j] > 100 or velocity_left[i][j] > 100) :  # left 
                velocity_left[i][j] = 5
            else : 
                velocity_left[i][j] = velocity_left[i][j] / count_left[i][j]
                                                   
    print('######## zero standardization ########')
    for i in range(West_index+150, East_index-150) :
        for j in range(South_index+150, North_index-150) :
            if(velocity_up[i][j] > 100):
                print(i, j, velocity_up[i][j])
                
            ########### UP ############
            if(velocity_up[i][j] == 5) :
                sum = 0
                nonzero_count = 0
                for m in range(i-3, i+3) :      # neighbor 8 X 8
                    for n in range(j-3, j+3) :
                        if(velocity_up[m][n] != 5) :
                            sum += velocity_up[m][n]
                            nonzero_count += 1
                if(nonzero_count > 0) :
                    if((sum / nonzero_count) > 5) : 
                        #print(sum, nonzero_count, sum/nonzero_count)
                        velocity_up[i][j] = sum / nonzero_count
                
            ############ DOWN ###########    
            if(velocity_down[i][j] == 5) :
                sum = 0
                nonzero_count = 0
                for m in range(i-3, i+3) :      # neighbor 8 X 8
                    for n in range(j-3, j+3) :
                        if(velocity_down[m][n] != 5) :
                            sum += velocity_down[m][n]
                            nonzero_count += 1
                if(nonzero_count > 0) :
                    if(sum / nonzero_count > 5) : 
                        velocity_down[i][j] = sum / nonzero_count
               
            ########## RIGHT ###########
            if(velocity_right[i][j] == 5) :
                sum = 0
                nonzero_count = 0
                for m in range(i-3, i+3) :      # neighbor 8 X 8
                    for n in range(j-3, j+3) :
                        if(velocity_right[m][n] != 5) :
                            sum += velocity_right[m][n]
                            nonzero_count += 1
                if(nonzero_count > 0) :
                    if(sum / nonzero_count > 5) : 
                        velocity_right[i][j] = sum / nonzero_count
                  
            ########## LEFT ############
            if(velocity_left[i][j] == 5) :
                sum = 0
                nonzero_count = 0
                for m in range(i-3, i+3) :      # neighbor 8 X 8
                    for n in range(j-3, j+3) :
                        if(velocity_left[m][n] != 5) :
                            sum += velocity_left[m][n]
                            nonzero_count += 1
                if(nonzero_count > 0) :
                    if(sum / nonzero_count > 5) : 
                        velocity_left[i][j] = sum / nonzero_count
               


def making_velocity_accum_file(time_index) :
    print("######## Start making velocity accum file ########")
    for i in range(4) :
        time_list = ['Morning_', 'Afternoon_', 'Evening_']
        direction_list = ['up', 'down', 'right', 'left']
        with open('Result/' + time_list[time_index] + direction_list[i] + '1', 'w') as g :
            if(i == 0) :
                print('up')
                for i in range(West_index-150, East_index+150) :
                    for j in range(South_index-150, North_index+150) :
                        g.write(str(i) + ' ' +  str(j) + ' ' + str(velocity_up[i][j]) + '\n')
            elif(i == 1) :
                print('down')
                for i in range(West_index-150, East_index+150) :
                    for j in range(South_index-150, North_index+150) :
                        g.write(str(i) + ' ' +  str(j) + ' ' + str(velocity_down[i][j]) + '\n')
            elif(i == 2) :
                print('right')
                for i in range(West_index-150, East_index+150) :
                    for j in range(South_index-150, North_index+150) :
                        g.write(str(i) + ' ' +  str(j) + ' ' + str(velocity_right[i][j]) + '\n')
            else :             
                print('left')
                for i in range(West_index-150, East_index+150) :
                    for j in range(South_index-150, North_index+150) :
                        g.write(str(i) + ' ' +  str(j) + ' ' + str(velocity_left[i][j]) + '\n')


def main() :
    velocity_accumulator(0)
    making_velocity_accum_file(0)

main()