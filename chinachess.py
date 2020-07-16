import time
import numpy as np
import os
import table

def print_table(table) :
    print("",0,1,2,3,4,5,6,7,8)
    table_copy = table.tolist()
    for i in range(len(table_copy)) :
        print(i,end = '')
        for j in table_copy[i] :
            print(j,end='')
        print()

def soldier_red(start,end) :
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    if start_x in [5,6] :
        if start_y == end_y and start_x - end_x == 1 :
            return 1
        else :
            return 0
    elif start_x in range(5) :
        if start_y == end_y and start_x - end_x == 1 :
            return 1
        elif start_x == end_x and abs(start_y - end_y) == 1 :
            return 1
        else :
            return 0
    else :
        return 0

def soldier_black(start,end):
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    if start_x in [3,4] :
        if start_y == end_y and end_x - start_x == 1 :
            return 1
        else :
            return 0
    elif start_x in range(5) :
        if start_y == end_y and end_x - start_x == 1 :
            return 1
        elif start_x == end_x and abs(start_y - end_y) == 1 :
            return 1
        else :
            return 0
    else :
        return 0
def lord(start,end,color) :
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    if 2 < end_y < 6 :
        if color == 'red' :
            if 6 < end_x < 10 :
                if abs(start_y - end_y) == 1 and start_x == end_x :
                    return 1
                else :
                    return 0
            else :
                return 0
        elif color == 'black' :
            if -1 < end_x < 3 :
                if abs(start_y - end_y) == 1 and start_x == end_x :
                    return 1
                else :
                    return 0
            else :
                return 0
        else :
            return 0
    else :
        return 0

def waiter(start,end,color) :
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    if 2 < end_y < 6 :
        if color == 'red' :
            if 6 < end_x < 10 :
                if abs(start_x - end_x) == abs(start_y - end_y) == 1 :
                    return 1
                else :
                    return 0
            else :
                return 0
        elif color == 'black' :
            if -1 < end_x < 3 :
                if abs(start_x - end_x) == abs(start_y - end_y) == 1 :
                    return 1
                else :
                    return 0
            else :
                return 0
        else :
            return 0
    else :
        return 0

def ele(table,start,end,color) :
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    if color == 'red' :
        if end_x > 4 :
            return(ele_inside(start_x,start_y,end_x,end_y))
        else :
            return 0
    elif color == 'black' :
        if end_x < 5 :
            return(ele_inside(start_x,start_y,end_x,end_y))
        else :
            return 0
    else :
        return 0

def ele_inside(start_x,start_y,end_x,end_y) :
    if start_x - end_x == end_y - start_y == 2 and table[start_x-1,start_y+1] == '\u3000' :
        return 1
    elif start_x - end_x == start_y - end_y == 2 and table[start_x-1,start_y-1] == '\u3000' :
        return 1
    elif end_x - start_x == start_y - end_y == 2 and table[start_x+1,start_y-1] == '\u3000' :
        return 1
    elif end_x - start_x == end_y - start_y == 2 and table[start_x+1,start_y+1] == '\u3000' :
        return 1
    else :
        return 0
        
def gun(table,start,end,piece_end) :
    shelf = 0
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    table_t = table.T.tolist()
    table = table.tolist()
    if start_x == end_x :
        if start_y < end_y :
            cut_y = table[start_x][start_y+1 : end_y]
        else :
            cut_y = table[start_x][end_y : start_y-1]
        for i in cut_y :
            if i != '\u3000' :
                shelf = shelf+1
        if shelf == 0 :
            return 1
        elif shelf == 2 and piece_end != '\u3000' :
            return 1
        else :
            return 0
    elif start_y == end_y :
        if start_x <end_x :
            cut_x = table_t[start_y][start_x+1 : end_x]
        else :
            cut_x = table_t[start_y][end_x : start_x]
        for i in cut_x :
            if i != '\u3000' :
                shelf = shelf+1
        if shelf == 0 :
            return 1
        elif shelf == 2 and piece_end != '\u3000' :
            return 1
        else :
            return 0
    else :
        return 0

def car(table,start,end) :
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    if start_x == end_x :
        if start_y < end_y :
            cut_y = table[start_x][start_y+1 : end_y]
        else :
            cut_y = table[start_x][end_y+1 : start_y]
        for i in cut_y :
            if i != '\u3000' :
                return 0
        return 1
    elif start_y == end_y :
        if start_x <end_x :
            cut_x = table.T[start_y][start_x+1 : end_x]
        else :
            cut_x = table.T[start_y][end_x+1 : start_x]
        for i in cut_x :
            if i != '\u3000' :
                return 0
        return 1
    else :
        return 0

def horse(table,start,end) :
    list_start = list(start)
    list_end = list(end)
    horse_abs_x = abs(list_start[0]-list_end[0])
    horse_abs_y = abs(list_start[1]-list_end[1])
    horse_x = list_start[0]-list_end[0]
    horse_y = list_start[1]-list_end[1]
    if horse_abs_y == 1 :
        if horse_x == 2 and table[list_start[0]-1,list_start[1]] == '\u3000':
            return 1
        elif horse_x == -2 and table[list_start[0]+1,list_start[1]] == '\u3000':
            return 1
        else :
            return 0
    elif horse_abs_x == 1:
        if horse_y == 2 and table[list_start[1]-1,list_start[0]] == '\u3000':
            return 1
        elif horse_abs_y == -2 and table[list_start[1]+1,list_start[0] ] == '\u3000':
            return 1
        else :
            return 0
    else :
        return 0

def err(table,start,end,group,color) :
    if len(start) != 2 or len(end) != 2 :
        return 0
    table_copy = table
    start = str_to_tuple(start)
    end = str_to_tuple(end)
    start_list = list(start)
    end_list = list(end)
    if start_list[1] not in range(9) : 
        return 0
    elif start_list[0] not in range(10) :
        return 0
    elif end_list[1] not in range(9) :
        return 0
    elif end_list[0] not in range(10) :
        return 0
    piece_start = table_copy[start]
    piece_end = table_copy[end]
    if piece_start not in group or piece_end in group or start == end :
        return 0
    elif piece_start == '马' or piece_start == '馬' :
        return horse(table_copy,start_list,end_list)
    elif piece_start == '车' or piece_start == '車' :
        return car(table_copy,start_list,end_list)
    elif piece_start == '炮' or piece_start == '砲' :
        return gun(table_copy,start_list,end_list,piece_end)
    elif piece_start == '相' or piece_start == '象' :
        return ele(table_copy,start_list,end_list,color)
    elif piece_start == '仕' or piece_start == '士' :
        return waiter(start_list,end_list,color)
    elif piece_start == '帅' or piece_start == '將' :
        return lord(start_list,end_list,color)
    elif piece_start == '兵' :
        return soldier_red(start_list,end_list)
    elif piece_start == '卒' :
        return soldier_black(start_list,end_list)
    else :
        return 0

def str_to_tuple(instr) :
    inside_list = list(instr)
    inside_list = [int(inside_list[i]) for i in range(len(inside_list))]
    inside_list[0],inside_list[1] = inside_list[1],inside_list[0]
    return tuple(inside_list)

def move(table,start,end) :
    start = str_to_tuple(start)
    end = str_to_tuple(end)
    piece = table[start]
    table[start] = '\u3000'
    table[end] = piece
    return table

def piece(color_step,table,group) :
    while True :
        if color_step%2 == 0 :
            color = 'red'
            color_else = 'black'
            group_copy = group[0]
        else :
            color = 'black'
            color_else = 'red'
            group_copy = group[1]
        color_move = input('[' + color + ']' + ">>>" +' ')
        if color_move == '认输' :
            print('['+ color_else + ']' +' ' + 'win')
            print("exiting...")
            time.sleep(5)
            exit()
        color_start = color_move[:2]
        color_end = color_move[2:]
        color_err = err(table,color_start,color_end,group_copy,color)
        if color_err == 0 :
            print("不符合规则，请重试")
        else :
            color_main = move(table,color_start,color_end)
            table = color_main
            print_table(color_main)
            break
    file_move = open("chinachess.txt",'a')
    file_move.write(color_move + '\n')
    file_move.close()
    return table,color_step+1
if __name__ == '__main__' :
    table = table.table
    group = [['车','马','相','仕','帅','炮','兵'],['車','馬','象','士','將','砲','卒']]
    i = 0
    print_table(table)
    file = open("chinachess.txt",'w')
    file.close()
    os.remove("chinachess.txt")
    while True :
        table,i = piece(i,table,group)
    
