'''Exercise 2.6 – The game of Nims/Stones'''

#Set amount of Stones per row
rows = [x+1 for x in range(int(input("\nRows for NIM?\n")))]
picks = [x for x in rows]

#Set max pick
max_picks = int(input("\nMax number of picks per row?\n"))

def execute_move(row, amount, player):
    ''' Execute player movement: access row and remove amount '''
    picks[row-1] = picks[row-1] - amount
    match(player)

def ask_player():
    ''' Ask player for a row and amount to be picked '''
    player_row = input("\nWhich row you want to pick a stone from?\n\n")
    player_amount = input("\nHow much you want to pick from row " + player_row + "?\n\n")
    while is_invalid(int(player_row), int(player_amount)):
        player_row, player_amount = ask_player()
   
    return (int(player_row), int(player_amount))

def is_invalid(row, amount):
    ''' Validates if the player movement is allowed '''
    if amount > max_picks or amount < 1:
        print("Invalid move, min pick is 1 and max pick is", max_picks)
        return True
    elif row not in rows:
        print("Invalid move, available rows are", rows, "\n")
        return True
    elif (picks[row-1] - amount < 0):
        print("Invalid move, there is", picks[row-1], "picks available for this row \n")
        return True 
    else:
        return False

def match(player):
    '''Checks if a player has own the game, if not, prints the game status'''
    if sum(picks) == 0:
        print("Player", player, "has won the game!")
        print("Game over!!!")
        exit()

    else: 
        print("\n"+"||||"*len(rows))
        print("Available picks:", sum(picks))
        print("rows ", rows)
        print("picks", picks) 
        print("||||"*len(rows))

def play_nims(rows, max_picks):  
    while True:
        row = 0
        amount = 0

        print("\n|| Player 1 turn ||")
        row, amount = ask_player()
        execute_move(row, amount, 1)      
   
        print("\n|| Player 2 turn ||")
        row, amount = ask_player()
        execute_move(row, amount, 2)

match(0)
play_nims(rows, max_picks)
