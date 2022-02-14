import os
import sys

f = open('inputfile.txt','r')
requests=f.readlines()
o = open('seats.txt','w')
status = [[str(0) for x in range(20)] for y in range(10)]
seatmap = {}

total_seats_free=200
seats_free = [20 for x in range(10)]


def find_seats(req_no, num_tix):
    global seatmap
    global total_seats_free
    row, row_letter, column = findrow(num_tix)
    count =1
    safety_padding(row,column,num_tix)
    while(count<=num_tix):
        status[row][column]=req_no
        if req_no in seatmap:
            seatmap[req_no].append(str(row_letter)+str(column+1))
        else:
            seatmap[req_no]=[str(row_letter)+str(column+1)]
        
        total_seats_free -=1
        seats_free[row] -=1
        column+=1
        count+=1
                    
def findrow(num_tix):
    row = int(10/2 - 1)
    counter = 1
    check= False
    while(row>=0 and row<=9):
        check, num = try_grouping(row,num_tix)
        if(check):
            row_letter = str(chr(row+65))
            return row, row_letter, num
        if (check == False and counter%2!=0):
            row = row + counter
            counter+=1
        elif (check==False and counter%2==0):
            row = row - counter
            counter+=1
    
        
                        
            
def try_grouping(row,num_tix):
    
    for i in range(20-num_tix):
        if status[row][i:i+num_tix]==['0' for x in range(num_tix)]:
            return True, i
    return False, -1


def safety_padding(row,column,num_tix):
    global total_seats_free
    for i in range(3):
        if(column-i-1>0 and status[row][column-i-1]=='0'):
            status[row][column-i-1]='P'
            seats_free[row]-=1
            total_seats_free -=1

        if(column+num_tix+i<19 and status[row][column+num_tix+i]=='0'):
            status[row][column+num_tix+i]='P'
            seats_free[row]-=1
            total_seats_free -=1

    if(row-1>=0):
        for i in range(num_tix):
            if(status[row-1][column+i]=='0'):
                status[row-1][column+i]='P'
                seats_free[row-1]-=1
                total_seats_free -=1
    
    if(row+1<9):
        for i in range(num_tix):
            if(status[row+1][column+i]=='0'):
                status[row+1][column+i]='P'
                seats_free[row+1]-=1
                total_seats_free -=1

for request in requests:
    [req_no, num_tix] = request.split(' ')
    if(total_seats_free>=int(num_tix)):
        find_seats(req_no, int(num_tix))
        seats = [x for x in seatmap[req_no]]


        o.writelines(req_no + ' ')
        o.writelines(",".join(seatmap[req_no]))
        o.writelines("\n")
    else:
        o.writelines("Not enough seats for request \n")


filepath = os.path.abspath('seats.txt')
print(str(filepath))
f.close()
o.close()
      


                   
            
    
