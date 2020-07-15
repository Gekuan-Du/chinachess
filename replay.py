from chinachess import *
import table
import time
import numpy
file = open('chinachess.txt','r')
move_list = file.readlines()
file.close()
for i in range(len(move_list)) :
    line = move_list[i][:-1]
    move_list[i] = line
table = table.table
print_table(table)
time.sleep(1)
for i in range(len(move_list)) :
    start = move_list[i][:2]
    end = move_list[i][2:]
    table = move(table,start,end)
    print_table(table)
    time.sleep(3)
