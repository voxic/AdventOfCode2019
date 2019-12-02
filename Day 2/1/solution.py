

import random
inputs = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0"

pos = 0

p = inputs.split(',')
while(True):
    #print('At pos {0} = {1}'.format(pos, p[pos]))
    if(int(p[pos]) == 1):
        p[int(p[pos+3])] = int(p[int(p[pos+1])]) + int(p[int(p[pos+2])])
        #print("Adding {0} and {1} and saving to {2}".format(p[pos+1],p[pos+2],p[pos+3]))
    elif(int(p[pos]) == 2):
        p[int(p[pos+3])] = int(p[int(p[pos+1])]) * int(p[int(p[pos+2])])
        #print("Multiplying {0} and {1} and saving to {2}".format(p[pos+1],p[pos+2],p[pos+3]))
    elif(int(p[pos]) == 99):
        break
    
    pos = pos + 4

print(p)
