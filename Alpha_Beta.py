import copy
from decimal import Decimal

my_file=open("input.txt", "r")
player=(my_file.readline()).strip()
depth= int((my_file.readline()).strip())
#print player
#print depth
state=[]
for i in range(8):
    line=list((my_file.readline()).strip())
    state.append(line)
#print state
my_file.close()
temp_state=[]
abc=[]
pass_state=[[]]
temp={80:state, 81:pass_state}
final_move = state
temp1=0
logs = []
#name_stamp={}
depth_counter=0
value_matrix=[["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"], ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
              ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"], ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
              ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"], ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
              ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"], ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
              ["root", "pass"]]
def possible_actions(state, p):
    total_moves = []
    states_ordering={}
    horizontal_actions = []
    vertical_actions = []
    right_diagonal_actions = []
    left_diagonal_actions = []
    if state==[[]]:
        return
    if(p=="X"):
        for i in range(8):
            for j in range(8):
                horizontal_actions=copy.deepcopy(state)
                #print "j: ", horizontal_actions
                if(horizontal_actions[i][j]=="O" and j!=0 and j!=7):
                    for k in range(j+1,8):
                        if(horizontal_actions[i][k]=="O"):
                            continue
                        elif(horizontal_actions[i][k]=="X" and horizontal_actions[i][j-1]=="*"):  #condition might go wrong if the first element of the row is "O"
                            horizontal_actions[i][j-1]="X"
                            for z in range(j,k):
                                horizontal_actions[i][z]="X"
                                #horizontal_actions.append(state)
                            states_ordering[i*10+(j-1)]=horizontal_actions
                            #global name_stamp
                            #name_stamp[i*10+(j-1)]=value_matrix[i][j-1]
                            #print horizontal_actions
                            #total_moves.append(horizontal_actions)
                            #print "break 1"
                            break
                        else: break
                elif(horizontal_actions[i][j]=="X" and j!=6 and j!=7):
                    for l in range(j+1,8):
                        if(horizontal_actions[i][l]=="O" and horizontal_actions[i][l+1]=="*"):
                            horizontal_actions[i][l+1]="X"
                            #horizontal_actions.append(state)
                            for z in range(j+1,l+1):
                                horizontal_actions[i][z]="X"
                            states_ordering[i*10+(l+1)]=horizontal_actions
                            #global name_stamp
                            #name_stamp[i*10+(l+1)] = value_matrix[i][l+1]
                            #print horizontal_actions
                            #total_moves.append(horizontal_actions)
                            #print "break 2"
                            break
                        elif(horizontal_actions[i][l]=="O"):
                            continue
                        else: break

        for i in range(8):
            for j in range(8):
                vertical_actions=copy.deepcopy(state)
                #print vertical_actions
                if(vertical_actions[j][i]=="O" and j!=0 and j!=7):
                    for k in range(j+1,8):
                        if(vertical_actions[k][i]=="O"):
                            continue
                        elif(vertical_actions[k][i]=="X" and vertical_actions[j-1][i]=="*"):  #condition might go wrong if the first element of the column is "O"
                            vertical_actions[j-1][i]="X"
                            #vertical_actions.append(state)
                            for z in range(j,k):
                                vertical_actions[z][i]="X"
                            states_ordering[(j-1)*10+i]=vertical_actions
                            #global name_stamp
                            #name_stamp[(j-1)*10+i] = value_matrix[j-1][i]
                            #print vertical_actions
                            #total_moves.append(vertical_actions)
                            #print "break 1"
                            break
                        else: break
                elif(vertical_actions[j][i]=="X" and j!=6 and j!=7):
                    for l in range(j+1,8):
                        if(vertical_actions[l][i]=="O" and vertical_actions[l+1][i]=="*"):
                            vertical_actions[l+1][i]="X"
                            #vertical_actions.append(state)
                            for z in range(j+1,l+1):
                                vertical_actions[z][i]="X"
                            states_ordering[(l+1)*10+i]=vertical_actions
                            #global name_stamp
                            #name_stamp[(l+1)*10 + (i)] = value_matrix[l+1][i]
                            #print vertical_actions
                            #total_moves.append(vertical_actions)
                            #print "break 2"
                            break
                        elif(vertical_actions[l][i]=="O"):
                            continue
                        else: break

        for i in range(8):
            for j in range(8):
                right_diagonal_actions=copy.deepcopy(state)
                k=i+1
                l=j+1
                if (right_diagonal_actions[i][j] == "O" and i!=0 and j!=0 and i!=7 and j!=7):
                    while(k<8 and l<8):
                        if(right_diagonal_actions[k][l]=="O"):
                            k+=1
                            l+=1
                            continue
                        elif(right_diagonal_actions[k][l]=="X" and right_diagonal_actions[i-1][j-1]=="*"):
                            right_diagonal_actions[i-1][j-1]="X"
                            #right_diagonal_actions.append(state)
                            x = i
                            y = j
                            while (x < k and y < l):
                                right_diagonal_actions[x][y] = "X"
                                x+=1
                                l+=1
                            states_ordering[(i-1)*10+(j-1)]=right_diagonal_actions
                            #global name_stamp
                            #name_stamp[(i-1)* 10 + (j - 1)] = value_matrix[i-1][j - 1]
                            #print right_diagonal_actions
                            #total_moves.append(right_diagonal_actions)
                            k+=1
                            l+=1
                            break
                        else: break
                elif(right_diagonal_actions[i][j]=="X" and i!=6 and j!=6 and i!=7 and j!=7):
                    while(k<8 and l<8):
                        if(right_diagonal_actions[k][l]=="O" and right_diagonal_actions[k+1][l+1]=="*"):
                            right_diagonal_actions[k+1][l+1]="X"
                            #right_diagonal_actions.append(state)
                            x = i + 1
                            y = j + 1
                            while (x <= k and y <= l):
                                right_diagonal_actions[x][y] = "X"
                                x += 1
                                y += 1
                            states_ordering[(k+1)*10+(l+1)]=right_diagonal_actions
                            #global name_stamp
                            #name_stamp[(k+1)*10 + (l+1)] = value_matrix[k+1][l+1]
                            #print right_diagonal_actions
                            #total_moves.append(right_diagonal_actions)
                            k+=1
                            l+=1
                            break
                        elif (right_diagonal_actions[k][l]=="O"):
                            k+=1
                            l+=1
                            continue
                        else: break

        for i in range(8):
            for j in range(8):
                left_diagonal_actions=copy.deepcopy(state)
                k=i+1
                l=j-1
                if(left_diagonal_actions[i][j]=="O" and i!=0 and j!=0 and i!=7 and j!=7):
                    while(k<8 and l>=0):
                        if(left_diagonal_actions[k][l]=="O"):
                            k+=1
                            l-=1
                            continue
                        elif (left_diagonal_actions[k][l]=="X" and left_diagonal_actions[i-1][j+1]=="*"):
                            left_diagonal_actions[i-1][j+1]="X"
                            #left_diagonal_actions.append(state)
                            x=i
                            y=j
                            while(x<k and y>l):
                                left_diagonal_actions[x][y]="X"
                                x+=1
                                y-=1
                            states_ordering[(i-1)*10+(j+1)]=left_diagonal_actions
                            #global name_stamp
                            #name_stamp[(i-1)*10 + (j+1)] = value_matrix[i-1][j+1]
                            #print left_diagonal_actions
                            #total_moves.append(left_diagonal_actions)
                            k+=1
                            l-=1
                            break
                        else: break
                elif(left_diagonal_actions[i][j]=="X" and i!=6 and i!=7 and j!=0 and j!=1):
                    while(k<8 and l>=0):
                        if(left_diagonal_actions[k][l]=="O" and left_diagonal_actions[k+1][l-1]=="*"):
                            left_diagonal_actions[k+1][l-1]="X"
                            #left_diagonal_actions.append(state)
                            x=i+1
                            y=j-1
                            while(x<=k and y>=l):
                                left_diagonal_actions[x][y]="X"
                                x+=1
                                y-=1
                            states_ordering[(k+1)*10+(l-1)]=left_diagonal_actions
                            #global name_stamp
                            #name_stamp[(k+1)*10 + (l - 1)] = value_matrix[k+1][l-1]
                            #print left_diagonal_actions
                            #total_moves.append(left_diagonal_actions)
                            k+=1
                            l-=1
                            break
                        elif(left_diagonal_actions[k][l]=="O"):
                            k+=1
                            l-=1
                            continue
                        else: break

    else:
        for i in range(8):
            for j in range(8):
                horizontal_actions=copy.deepcopy(state)
                if (horizontal_actions[i][j]=="X" and j!=0 and j!=7):
                    for k in range(j+1,8):
                        if(horizontal_actions[i][k]=="X"):
                            continue
                        elif(horizontal_actions[i][k]=="O" and horizontal_actions[i][j-1]=="*"):  #condition might go wrong if the first element of the row is "O"
                            horizontal_actions[i][j-1]="O"
                            for z in range(j,k):
                                horizontal_actions[i][z]="O"
                            #horizontal_actions.append(state)
                            states_ordering[i * 10 + (j - 1)] = horizontal_actions
                            #global name_stamp
                            #name_stamp[i * 10 + (j - 1)] = value_matrix[i][j - 1]
                            #print horizontal_actions
                            #total_moves.append(horizontal_actions)
                            break
                        else: break
                elif(horizontal_actions[i][j]=="O" and j!=6 and j!=7):
                    for l in range(j+1,8):
                        if(horizontal_actions[i][l]=="X" and horizontal_actions[i][l+1]=="*"):
                            horizontal_actions[i][l+1]="O"
                            #horizontal_actions.append(state)
                            for z in range(j+1,l+1):
                                horizontal_actions[i][z]="O"
                            states_ordering[i * 10 + (l + 1)] = horizontal_actions
                            #global name_stamp
                            #name_stamp[i * 10 + (l + 1)] = value_matrix[i][l + 1]
                            #print horizontal_actions
                            #total_moves.append(horizontal_actions)
                            break
                        elif (horizontal_actions[i][l]=="X"):
                            continue
                        else: break

        for i in range(8):
            for j in range(8):
                vertical_actions=copy.deepcopy(state)
                if(vertical_actions[j][i]=="X" and j!=0 and j!=7):
                    for k in range(j+1,8):
                        if(vertical_actions[k][i]=="X"):
                            continue
                        elif(vertical_actions[k][i]=="O" and vertical_actions[j-1][i]=="*"):  #condition might go wrong if the first element of the column is "O"
                            vertical_actions[j-1][i]="O"
                            #vertical_actions.append(state)
                            for z in range(j,k):
                                vertical_actions[z][i]="O"
                            states_ordering[(j - 1) * 10 + i] = vertical_actions
                            #global name_stamp
                            #name_stamp[(j - 1) * 10 + i] = value_matrix[j - 1][i]
                            #print vertical_actions
                            #total_moves.append(vertical_actions)
                            break
                        else: break
                elif(vertical_actions[j][i]=="O" and j!=6 and j!=7):
                    for l in range(j+1,8):
                        if(vertical_actions[l][i]=="X" and vertical_actions[l+1][i]=="*"):
                            vertical_actions[l+1][i]="O"
                            #vertical_actions.append(state)
                            for z in range(j+1,l+1):
                                vertical_actions[z][i]="O"
                            states_ordering[(l + 1) * 10 + i] = vertical_actions
                            #global name_stamp
                            #name_stamp[(l + 1) * 10 + (i)] = value_matrix[l + 1][i]
                            #print vertical_actions
                            #total_moves.append(vertical_actions)
                            break
                        elif(vertical_actions[l][i]=="X"):
                            continue
                        else: break

        for i in range(8):
            for j in range(8):
                right_diagonal_actions=copy.deepcopy(state)
                k=i+1
                l=j+1
                if (right_diagonal_actions[i][j] == "X" and i!=0 and j!=0 and i!=7 and j!=7):
                    while(k<8 and l<8):
                        if(right_diagonal_actions[k][l]=="X"):
                            k+=1
                            l+=1
                            continue
                        elif(right_diagonal_actions[k][l]=="O" and right_diagonal_actions[i-1][j-1]=="*"):
                            right_diagonal_actions[i-1][j-1]="O"
                            #right_diagonal_actions.append(state)
                            x = i
                            y = j
                            while (x < k and y < l):
                                right_diagonal_actions[x][y] = "O"
                                x += 1
                                y += 1
                            states_ordering[(i - 1) * 10 + (j - 1)] = right_diagonal_actions
                            k += 1
                            l += 1
                            #global name_stamp
                            #name_stamp[(i - 1) * 10 + (j - 1)] = value_matrix[i - 1][j - 1]
                            #print right_diagonal_actions
                            #total_moves.append(right_diagonal_actions)
                            break
                        else: break
                elif(right_diagonal_actions[i][j]=="O" and i!=6 and j!=6 and i!=7 and j!=7):
                    while(k<8 and l<8):
                        if(right_diagonal_actions[k][l]=="X" and right_diagonal_actions[k+1][l+1]=="*"):
                            right_diagonal_actions[k+1][l+1]="O"
                            #right_diagonal_actions.append(state)
                            x = i + 1
                            y = j + 1
                            while (x <= k and y <= l):
                                right_diagonal_actions[x][y] = "O"
                                x += 1
                                y += 1
                            states_ordering[(k + 1) * 10 + (l + 1)] = right_diagonal_actions
                            k += 1
                            l += 1
                            #global name_stamp
                            #name_stamp[(k + 1) * 10 + (l + 1)] = value_matrix[k + 1][l + 1]
                            #print right_diagonal_actions
                            #total_moves.append(right_diagonal_actions)
                            break
                        elif (right_diagonal_actions[k][l]=="X"):
                            k+=1
                            l+=1
                            continue
                        else: break

        for i in range(8):
            for j in range(8):
                left_diagonal_actions=copy.deepcopy(state)
                k=i+1
                l=j-1
                if (left_diagonal_actions[i][j] == "X" and i!=0 and j!=0 and i!=7 and j!=7):
                    while(k<8 and l>=0):
                        if(left_diagonal_actions[k][l]=="X"):
                            k+=1
                            l-=1
                            continue
                        elif (left_diagonal_actions[k][l]=="O" and left_diagonal_actions[i-1][j+1]=="*"):
                            left_diagonal_actions[i-1][j+1]="O"
                            #left_diagonal_actions.append(state)
                            x = i
                            y = j
                            while (x < k and y > l):
                                left_diagonal_actions[x][y] = "O"
                                x += 1
                                y -= 1
                            states_ordering[(i - 1) * 10 + (j + 1)] = left_diagonal_actions
                            k += 1
                            l -= 1
                            #global name_stamp
                            #name_stamp[(i - 1) * 10 + (j + 1)] = value_matrix[i - 1][j + 1]
                            #print left_diagonal_actions
                            #total_moves.append(left_diagonal_actions)
                            break
                        else: break
                elif(left_diagonal_actions[i][j]=="O" and i!=6 and i!=7 and j!=0 and j!=1):
                    while(k<8 and l>=0):
                        if(left_diagonal_actions[k][l]=="X" and left_diagonal_actions[k+1][l-1]=="*"):
                            left_diagonal_actions[k+1][l-1]="O"
                            #left_diagonal_actions.append(state)
                            x = i + 1
                            y = j - 1
                            while (x <= k and y >= l):
                                left_diagonal_actions[x][y] = "O"
                                x += 1
                                y -= 1
                            states_ordering[(k + 1) * 10 + (l - 1)] = left_diagonal_actions
                            k += 1
                            l -= 1
                            #global name_stamp
                            #name_stamp[(k + 1) * 10 + (l - 1)] = value_matrix[k + 1][l - 1]
                            #print left_diagonal_actions
                            #total_moves.append(left_diagonal_actions)
                            break
                        elif(left_diagonal_actions[k][l]==""):
                            k+=1
                            l-=1
                            continue
                        else: break
    temp.update(states_ordering)
    for i in range(78):
        key=i
        if key in states_ordering:
            total_moves.append(states_ordering[key])
    global abc
    abc= copy.deepcopy(total_moves)
    #print "before total_moves"
    #print total_moves
    #print "after total_moves"
    #print abc

def terminal_state(state, pl, current_depth, min_or_max, v, alpha, beta,flag, counter):
    global logs
    #print "inside terminal_state",current_depth, flag#needs correction
    counter2=0
    if flag==2:
        #print "inside flag"
        e = temp.keys()[temp.values().index([[]])]
        z = e / 10
        g = e % 10
        logs.append([value_matrix[z][g], str(current_depth), str(utility_value(temp_state, player)), str(alpha), str(beta)])
        global temp1
        temp1=utility_value(temp_state, player)
        #print temp1
        return [True,temp1]
    if current_depth==depth:
        #print "inside depth"
        return [True]
    else:
        #print "inside else"
        if pl=="X":
            possible_actions(state, pl)
            #print "after possible\n\n"
           # print abc
            if not abc:
                #print "okay"
                if flag==0:
                    global  temp_state
                    temp_state=copy.deepcopy(state)
                if(counter==1):
                    h=temp.keys()[temp.values().index([[]])]
                    i=h/10
                    j=h%10
                    #logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    logs.append([value_matrix[i][j],str(current_depth),str(v),str(alpha),str(beta)])
                    counter=0
                    counter2+=1
                else:
                    h = temp.keys()[temp.values().index(state)]
                    i = h / 10
                    j = h % 10
                    logs.append([value_matrix[i][j],str(current_depth),str(v),str(alpha),str(beta)])
                pl = "O"
                if min_or_max=="max":
                    #print "bcz max called"
                    pass_state = copy.deepcopy(state)
                    v=max(v,min_value(pass_state,pl,depth,alpha,beta,current_depth+1,flag+1,counter+1))
                    #print "now v is", v
                    y = temp.keys()[temp.values().index([[]])]
                    l = y / 10
                    m = y % 10
                    if current_depth != depth - 1 and current_depth != 0:
                        #logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                        logs.append([value_matrix[l][m],str(current_depth),str(v),str(alpha),str(beta)])

                    alpha = max(alpha, v)
                    #print current_depth
                    #print "alpha is",alpha
                    #print v,beta
                    #print "counter2", counter2
                    if v >= beta:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        #logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                        logs.append([value_matrix[o][p],str(current_depth),str(v),str(alpha),str(beta)])
                        return v
                    if (counter2!=0):
                        n = temp.keys()[temp.values().index([[]])]
                        o = n / 10
                        p = n % 10
                        #logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                        logs.append([value_matrix[o][p],str(current_depth),str(v),str(alpha),str(beta)])
                    else:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    return v  ###getting v from here
                else:
                    pass_state = copy.deepcopy(state)
                    v=min(v,max_value(pass_state,pl,depth,alpha,beta,current_depth+1,flag+1,counter+1))
                    y = temp.keys()[temp.values().index([[]])]
                    l = y / 10
                    m = y % 10
                    if current_depth != depth - 1 and current_depth != 0:
                        logs.append([value_matrix[l][m], str(current_depth), str(v), str(alpha), str(beta)])
                    beta = min(beta, v)
                    if v <= alpha:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                        return v
                    if (counter2!=0):
                        n = temp.keys()[temp.values().index([[]])]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    else:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    return v
                #print "pass"

                return [True]
            return [False]

        elif pl=="O":
            #print "inside else if"
            possible_actions(state, pl)
            #print abc
            if not abc:
                if flag==0:
                    global temp_state
                    temp_state=copy.deepcopy(state)
                if (counter == 1):
                    h = temp.keys()[temp.values().index([[]])]
                    i = h / 10
                    j = h % 10
                    logs.append([value_matrix[i][j], str(current_depth), str(v), str(alpha), str(beta)])
                    counter = 0
                else:
                    h = temp.keys()[temp.values().index(state)]
                    i = h / 10
                    j = h % 10
                    logs.append([value_matrix[i][j], str(current_depth), str(v), str(alpha), str(beta)])
                pl = "X"
                if min_or_max =="max":
                    pass_state=copy.deepcopy(state)
                    v=max(v,min_value(pass_state, pl, depth, alpha, beta, current_depth + 1, flag + 1, counter+1))
                    '''y = temp.keys()[temp.values().index([[]])]
                    l = y / 10
                    m = y % 10
                    if current_depth != depth - 1 and current_depth != 0:
                        print value_matrix[l][m], ",", current_depth, ",", v, ",", alpha, ",", beta'''

                    alpha = max(alpha, v)
                    if v >= beta:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                        return v
                    if(counter2!=0):
                        n = temp.keys()[temp.values().index([[]])]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    else:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    return v
                else:
                    #print"bcz min called"
                    pass_state=copy.deepcopy(state)
                    v=min(v,max_value(pass_state, pl, depth, alpha, beta, current_depth + 1, flag + 1, counter+1))  ##I'VE CHANGED [[]] IN MAX_VALUE CALL TO STATE
                    #print "v is nowwww", v
                    '''y = temp.keys()[temp.values().index([[]])]
                    l = y / 10
                    m = y % 10'''
                    beta = min(beta, v)
                    '''if current_depth != depth - 1 and current_depth != 0:
                        print "aaaaaaaaaaaa"
                        print value_matrix[l][m], ",", current_depth, ",", v, ",", alpha, ",", beta'''
                    if v <= alpha:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                        return v
                    #print "now counter2 issss", counter2
                    if(counter2!=0):
                        n = temp.keys()[temp.values().index([[]])]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    else:
                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                    #print "now i'm gonnaaaa return", v
                    return v

                #print "pass"
                return [True]
            return [False]


#utility value function

def utility_value(state, plyr):
    #print "Inside utility_value"
    value_matrix=[[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6],
                  [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]
    utility_X=0
    utility_O=0
    utility=0
    if player=="X":
        #print "yes player is X"
        #print "and the state is", state
        for i in range(8):
            for j in range(8):
                if(state[i][j]=="X"):
                    utility_X+=value_matrix[i][j]
                elif(state[i][j]=="O"):
                    utility_O+=value_matrix[i][j]
        utility=utility_X-utility_O
        #print utility
        return utility
    else:
        #print "yes player is O"
        for i in range(8):
            for j in range(8):
                if (state[i][j] == "X"):
                    utility_X += value_matrix[i][j]
                elif (state[i][j] == "O"):
                    utility_O += value_matrix[i][j]
        utility = utility_O - utility_X
        #print utility
        return utility


#Alpha Beta Pruning begins:


def max_value(state, play, dep, alpha, beta, current_depth, flag, counter, **kwargs):
    global final_move
    #print  current_depth, flag, counter
    #print state
    v = Decimal('-Infinity')
    #print terminal_state(state, play, current_depth, "max", v, alpha, beta, flag)
    xyz=terminal_state(state, play, current_depth, "max", v, alpha, beta, flag, counter)
    #print "yeyeyeyyey", xyz
    if isinstance(xyz, list):
        if len(xyz)==1:
            if xyz[0]==True:
                e = temp.keys()[temp.values().index(state)]
                z = e / 10
                g = e % 10
                logs.append([value_matrix[z][g], str(current_depth), str(utility_value(state, player)), str(alpha), str(beta)])
                return utility_value(state, player)
            else:
                #print "hi"
                #print temp
                h = temp.keys()[temp.values().index(state)]
                i = h / 10
                j = h % 10
                logs.append([value_matrix[i][j], str(current_depth), str(v), str(alpha), str(beta)])
                possible_actions(state, play)
               # print abc
                if current_depth < depth:
                    for f in abc:
                        if play=="X":
                            move_next="O"
                            #p=min_value(f, move, dep, alpha, beta, current_depth+1, flag)
                            #print "p",p
                            temp_min_value = min_value(f, move_next, dep, alpha, beta, current_depth+1, flag, counter)
                            if v < temp_min_value:
                                v = temp_min_value
                                if "root" in kwargs:
                                    final_move = f
                            #print "v",v
                        elif play=="O":
                            move_next="X"
                            v=max(v, min_value(f, move_next, dep, alpha, beta, current_depth+1, flag, counter))
                        y = temp.keys()[temp.values().index(f)]
                        l = y / 10
                        m = y % 10
                        if current_depth!=depth-1 and current_depth!=0:
                            logs.append([value_matrix[l][m], str(current_depth), str(v), str(alpha), str(beta)])

                        alpha = max(alpha, v)
                        #print v,beta
                        if v>=beta:
                            n = temp.keys()[temp.values().index(state)]
                            o = n / 10
                            p = n % 10
                            #print "dguegfuygefuew"
                            logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                            return v

                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        #print "------------------------"
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])

        else:
            #print xyz[1]
            return xyz[1]
        return v
    else:
        return xyz


def min_value(state, play, dep, alpha, beta, current_depth, flag, counter):
    #print  current_depth, flag, counter
   # print state
    v = Decimal('Infinity')
    xyz=terminal_state(state, play, current_depth, "min", v, alpha, beta, flag, counter)
    if isinstance(xyz,list):
        if len(xyz)==1:
            if xyz[0]==True:
                e = temp.keys()[temp.values().index(state)]
                z = e / 10
                g = e % 10
                logs.append([value_matrix[z][g], str(current_depth), str(utility_value(state, player)), str(alpha), str(beta)])
                return utility_value(state, player)
            else:
                h = temp.keys()[temp.values().index(state)]
                i = h / 10
                j = h % 10
                logs.append([value_matrix[i][j], str(current_depth), str(v), str(alpha), str(beta)])
                possible_actions(state, play)
                if current_depth < depth:
                    for k in abc:
                        if play=="X":
                            move_next="O"
                            v=min(v, max_value(k, move_next, dep, alpha, beta, current_depth+1, flag, counter))
                        elif play=="O":
                            move_next="X"
                            v=min(v, max_value(k, move_next, dep, alpha, beta, current_depth+1, flag, counter))
                            #print v
                        y = temp.keys()[temp.values().index(k)]
                        l = y / 10
                        m = y % 10
                        if current_depth!=depth-1 and current_depth!=0:
                            logs.append([value_matrix[l][m], str(current_depth), str(v), str(alpha), str(beta)])
                        beta = min(beta, v)
                        if v<=alpha:
                            n = temp.keys()[temp.values().index(state)]
                            o = n / 10
                            p = n % 10
                            logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                            return v

                        n = temp.keys()[temp.values().index(state)]
                        o = n / 10
                        p = n % 10
                        logs.append([value_matrix[o][p], str(current_depth), str(v), str(alpha), str(beta)])
                          #####making change here
        else:
            #print "this returns", xyz[1]
            return xyz[1]

        return v
    else:
        return xyz


def alpha_beta(state, d):
    #print "inside alpha_beta"
    v=max_value(state, player, d, Decimal('-Infinity'), Decimal('Infinity'), 0, 0, 0, root=True)
    #return the action in Actions(state) with value v
    #print "everything returned correctly"

#execution code
alpha_beta(state, depth)

with open("output.txt", "w") as fh:
    board = ""
    for line in final_move:
        board += "".join(line) + "\n"
    fh.write(board)
    fh.write("Node,Depth,Value,Alpha,Beta")
    for line in logs:
        fh.write("\n" + ",".join(line))


#have to return the state with value v as well
