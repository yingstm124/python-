def OX():
    # global var
    board = [0,1,2,3,4,5,6,7,8]

    def input_p1():
        pos_ = int(input("Enter X: "))
        return pos_

    def input_p2():
        pos_ = int(input("Enter O: "))
        return pos_

    def draw():
        for i in range (len(board)):
            if i == 3:
                print("")
                print(board[i],end=" ")
            elif i == 6:
                print("")
                print(board[i],end=" ")
            else:
                print(board[i],end=" ") 
        print("") 

    def reset_board(board):
        for i in range (len(board)):
            board[i] = i
        
        return board

    def loop_assign_ls_p1(pos_):
        for i in range (len(board)):
            if pos_ not in board:
                print("plese enter again")
                pos_x = input_p1()
                loop_assign_ls_p1(pos_x)
                break

            if pos_ == board[i]:
                board[i] = "X"
                break
        

    def loop_assign_ls_p2(pos_):
        for i in range (len(board)):
            if pos_ not in board:
                print("plese enter again")
                pos_o = input_p2()
                loop_assign_ls_p2(pos_o)
                break

            if pos_ == board[i]:
                board[i] = "O"
                break

    def win_check(check):

        win = False

        # row horizontial
        first_row = board[:3]
        second_row = board[3:6]
        third_row = board[6:]

        # score   1  2  3
        point_ls = [0,0,0]

        for i in first_row:
            if i == check:
                point_ls[0] += 1 
        
        for i in second_row:
            if i == check:
                point_ls[1] += 1 

        for i in third_row:
            if i == check:
                point_ls[2] += 1 

        if 3 in point_ls:
            return True

        # col vertical
        point_ls = [0,0,0]
        for index in range (len(board)):
            # frist col
            if index%3 == 0 and board[index] == check:
                point_ls[0] += 1
            elif index%3 == 1 and board[index] == check:
                point_ls[1] += 1
            elif index%3 == 2 and board[index] == check:
                point_ls[2] += 1

        if 3 in point_ls:
            return True

        
        # score   L  R 
        point_ls = [0,0]

        # left right diagonal
        for index in range (len(board)):
            if point_ls[0] == 3 or point_ls[1] == 3:
                return True

            if board[index] == check:
                if index == 0 or index == 4 or index == 8 and board[index] == check:
                    point_ls[0] += 1
                if index == 2 or index == 4 or index == 6 and board[index] == check:
                    point_ls[1] += 1
        
        if 3 in point_ls:
            return True
    
    def score_display(score_ls):
        for i in range (len(score_player)):
            if score_player[0] > score_player[1]:
                print("total X win score {0}".format(score_player[0]))
                break
            elif score_player[0] < score_player[1]:
                print("total O win score {0}".format(score_player[1]))
                break
            else:
                print("win win")
                break
 
    # score_player  X O
    score_player = [0,0]
    
    gameover = False
    while not gameover:
        n = 0
        n_p1 = 1
        n_p2 = 1
        win = False
        draw()
        while not win and (n_p1 <= 5  or n_p2 <= 5):
            # player1
            pos_x = input_p1()
            loop_assign_ls_p1(pos_x)
            n_p1 += 1
        
            # check player1
            if n_p1 >= 2 :
                check_x = "X"
                win = win_check(check_x)
                if win == True:
                    score_player[0] += 1
                    draw()
                    print("X win")
                    break

            draw() 

            # player 2
            pos_o = input_p2()
            loop_assign_ls_p2(pos_o)
            n_p2 += 1

            # check player2
            if n_p2 >= 2 :
                check_o = "O"
                win = win_check(check_o)
                if win == True:
                    score_player[1] += 1
                    draw()
                    print("O win")
                    break
        
            draw()
        

        quest = input("do you want the end game (y/n): ")
        quest.lower()

        if quest == "y":
            score_display(score_player)
            gameover = True
        
        else:
            reset_board(board)
            
            

OX()


