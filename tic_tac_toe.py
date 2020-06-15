class tic:
    turn = 0
    def check_goal(self):
        # print("result game end",game_board)

        for i in range(0,7,3):
            if game_board[i]==game_board[i+1]==game_board[i+2] and not game_board[i]=='-':
                return game_board[i]

        for i in range(0,3):
            if game_board[i]==game_board[i+3]==game_board[i+6] and not game_board[i]=='-':
                return game_board[i]

        if game_board[0]==game_board[4]==game_board[8] and not game_board[0]=='-':
            return game_board[0]

        elif game_board[2]==game_board[4]==game_board[6] and not game_board[2]=='-':
            return game_board[2]

        for i in range(9):
            if game_board[i]=='-':
                return None

        else:
            return '-'


    def print_graph(self):
        print("--- GAME BOARD ----")
        for i in range(9):
            print(game_board[i], end="    |   ")
            if i in [2,5]:
                print()


    def player_move(self):
        print("Your Turn ---")
        self.print_graph()
        print()
        print("Enter the position of move 'X' from 1-9")


        p=int(input())
        if p>0 and p<10:
            if game_board[p-1]=='-':
                game_board[p-1]='X'
                return

            else:
                print("Invalid position entered !, Please enter again")
                self.player_move()

        else:
            print("Invalid position entered !, Please enter again")
            self.player_move()



    def game_play(self):

        result=self.check_goal()
        if not result==None:
            if result=='X':
                print(self.print_graph())
                print("--- Congrats! You WON ---")
                exit(0)


            elif result=='O':
                print((self.print_graph()))
                print("--- Oh ! You LOOSE ---")
                exit(0)

            elif result=="-":
                print((self.print_graph()))
                print("--- It's a TIE ---")
                exit(0)


        elif self.turn==0:
            self.player_move()
            self.turn = 1
            self.game_play()


        elif self.turn==1:
            (m,pos)=self.botmove_max(-2,2)
            # print("score",m,"pos",pos)
            game_board[pos]='O'
            # print("now game",game_board)
            self.turn=0
            self.game_play()


    def botmove_max(self,alfa,beta):
        pos=None
        max_value=-2
        result=self.check_goal()
        # print(result,"result")
        if result=='X':
            return (-1,0)

        elif result=='O':
            return (1,0)

        elif result=='-':
            return (0,0)

        # print("hi")
        for i in range(9):
            # print("maxboard",game_board)
            if game_board[i]=='-':
                game_board[i]='O'
                # self.print_graph()
                (m,min_pos)=self.botmov_min(alfa,beta)

                if m>max_value:
                    max_value=m
                    pos=i

                game_board[i]='-'

                if max_value>=beta:
                    return (max_value,pos)
                # print("asas",alfa)
                if max_value>alfa:
                    alfa=max_value

        return (max_value,pos)


    def botmov_min(self,alfa,beta):
        pos1=None
        min_value=2

        result=self.check_goal()
        # print("result2",result)

        if result=='X':
            return (-1,0)

        elif result=='O':
            return (1,0)

        elif result=='-':
            return (0,0)

        for i in range(9):
            # print(game_board)
            if game_board[i]=='-':
                game_board[i]='X'
                # self.print_graph()

                (m,min_p)=self.botmove_max(alfa,beta)
                # print("yes2",m,min_value)
                # print("ada",alfa)

                if m<min_value:
                    min_value=m
                    pos1=i

                game_board[i]='-'

                if min_value<=alfa:
                    return (min_value,pos1)

                if min_value<beta:
                    beta=min_value

        return (min_value,pos1)




tac=tic()
print("--- TIC TAC TOE ---")
print("--- GAME IS LOADING ---")
print("Your Move is 'X'")
print()

game_board=['-']*9



tac.game_play()


