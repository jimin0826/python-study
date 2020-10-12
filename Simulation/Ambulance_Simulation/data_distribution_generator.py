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

Folder1_filename = []
for file in os.listdir("Folder1_K"):
    if file.endswith(".txt"): #끝이 ".txt"로 끝나는 경우
        Folder1_filename.append(file)
pretime = 0
with open('Folder1_K/Interarrival', 'w') as g :
    for filename in Folder1_filename :
        with open('Folder1_K/' + filename, 'r', encoding = 'utf8') as f :
            text = f.read()
            docs = text.split('\n')[3:]
            print(filename)
            len_docs = len(docs)

            if(len_docs > 100) :  
                for i in range(10, len_docs-1) :                           
                    docs[i] = docs[i].split()
                    gps = gps_to_point(float(docs[i][0][:2] + '.' + docs[i][0][2:]), float(docs[i][1][:3] + '.' + docs[i][1][3:]))
                    if(gps[1] > West_index and gps[1] < East_index and gps[0] > South_index and gps[0] < North_index) :
                        sum = 0 
                        for k in range(1, 10) :
                            sum += int(docs[i-k][2])
                        if(sum == 0 and int(docs[i][2]) != 0 and int(docs[i][4]) - pretime > 0) :
                            g.write(str(int(docs[i][4]) - pretime) + '\n')
                            pretime = int(docs[i][4])
