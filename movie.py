import os
import sys

#f = open('inputfile.txt','r')                                          #open input file for read
f = open(sys.argv[1],'r')                                               #open input file for read
requests=f.readlines()                          
o = open('seats.txt','w')                                               #open output file for write
status = [[str(0) for x in range(20)] for y in range(10)]               #status map for each seat
seatmap = {}                                                            #dictionary mapping for reservation number with seats

total_seats_free=200
seats_free = [20 for x in range(10)]                                    #free seats per row


def find_seats(req_no, num_tix):                                        #function to assign seats
    global seatmap
    global total_seats_free
    row, row_letter, column = findrow(num_tix)                          #find row which can accomodate the number of tickets requested
    count =1                                                            #counter variable to check how many tickets have been processed
    safety_padding(row,column,num_tix)                                  #add padding
    while(count<=num_tix):                                              #reserve required no of tickets
        status[row][column]=req_no
        if req_no in seatmap:
            seatmap[req_no].append(str(row_letter)+str(column+1))
        else:
            seatmap[req_no]=[str(row_letter)+str(column+1)]
        
        total_seats_free -=1                                            #1 seat assigned
        seats_free[row] -=1
        column+=1                                                       #next seat is in next column
        count+=1                                                        #next ticket
                    
def findrow(num_tix):                                               
    row = int(10/2 - 1)                                                 #start from middle row
    counter = 1                                                         #counter for cycling between rows
    check= False                                                        #check to know if we have available seats
    while(row>=0 and row<=9):   
        check, num = try_grouping(row,num_tix)                          #try to fit group in same row
        if(check):                                                      #if group fits
            row_letter = str(chr(row+65))
            return row, row_letter, num
                                                                        #if group doesnt fit
        if (check == False and counter%2!=0):                       
            row = row + counter
            counter+=1
        elif (check==False and counter%2==0):
            row = row - counter
            counter+=1
    
        
                        
            
def try_grouping(row,num_tix):                              
    
    for i in range(20-num_tix):
        if status[row][i:i+num_tix]==['0' for x in range(num_tix)]:     #check if consecutive seats are empty
            return True, i
    return False, -1


def safety_padding(row,column,num_tix):                                 #add padding for safety (3 seats and 1 row)
    global total_seats_free
    for i in range(3):                                                  #add padding for 3 seats before the first
        if(column-i-1>0 and status[row][column-i-1]=='0'):
            status[row][column-i-1]='P'
            seats_free[row]-=1
            total_seats_free -=1

        if(column+num_tix+i<19 and status[row][column+num_tix+i]=='0'): #add padding for 3 seats after last
            status[row][column+num_tix+i]='P'
            seats_free[row]-=1
            total_seats_free -=1

    if(row-1>=0):                                                       #add padding below
        for i in range(num_tix):
            if(status[row-1][column+i]=='0'):
                status[row-1][column+i]='P'
                seats_free[row-1]-=1
                total_seats_free -=1
    
    if(row+1<9):                                                        #add padding above
        for i in range(num_tix):
            if(status[row+1][column+i]=='0'):
                status[row+1][column+i]='P'
                seats_free[row+1]-=1
                total_seats_free -=1

for request in requests:                                                #process requests one by one
    [req_no, num_tix] = request.split(' ')                              #split into request no and number of tickets reqd.
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
