#Grid to create the matrix of the Tic_Tac_toe game

grid={'7':' ', '8':' ','9':' ',
      '4':' ','5':' ','6':' ',
      '1':' ','2':' ','3':' '}

def printBoard(theBoard):
    print(grid['7'] +'|' + grid['8'] + '|' +grid['9'])
    print("-+-+-")
    print(grid['4'] +'|' + grid['5'] + '|' +grid['6'])
    print("-+-+-")
    print(grid['1'] +'|' + grid['2'] + '|' +grid['3'])


def game():
    turn="X"
    count = 0
    for i in range (1,11):
           
        printBoard(grid)
        print("It's your turn " +turn+ ". Move to which place?")
        move=input()

        if grid[move] == ' ':
            grid[move]= turn
            count +=1
        else:
            print("That cell is taken. Try again... ")
            continue
        if count>=5:
            if grid["7"]==grid["8"]==grid["9"]!=" ":
                printBoard(grid)
                print("Game Over\n")
                print("You have won "+turn+".")
                break
            elif grid["4"]==grid["5"]==grid["6"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            elif grid["1"]==grid["2"]==grid["3"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            elif grid["7"]==grid["4"]==grid["1"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            elif grid["8"]==grid["5"]==grid["2"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            elif grid["9"]==grid["6"]==grid["3"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            elif grid["7"]==grid["5"]==grid["3"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            elif grid["9"]==grid["5"]==grid["1"]!=" ":
                    printBoard(grid)
                    print("Game Over\n")
                    print("You have won "+turn+".")
                    break
            if count==9:
                print("""Game over.
    It is a tie""")
                
        
        
        if turn == "X":
            turn = "O"
        else:
            turn= "X"
        

game()



        
