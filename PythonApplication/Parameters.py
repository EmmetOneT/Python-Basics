#x_pos = 0

#def move(by_amount):
#    global x_pos
#    x_pos += by_amount 


#move(5)
#print(x_pos)


start_pos = 0
end_pos = 10
x_pos = 0

def move(x_pos, by_amount=1):
    global start_pos,end_pos
    x_pos += by_amount
    if x_pos < start_pos:
        return start_pos
    elif x_pos > end_pos:
        return end_pos
    return x_pos
    

x_pos = move(x_pos, 15)
print(x_pos)

