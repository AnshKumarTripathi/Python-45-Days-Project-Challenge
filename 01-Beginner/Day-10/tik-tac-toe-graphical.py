import tkinter

playerX  = "X"
playerO  = "O"

curr_player = playerX

board = [[0,0,0],[0,0,0],[0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_gray_light = "#646464"

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)

window.mainloop()