import tkinter as tk
from src.gui.sudoku_gui import GUI

def main():
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Sudoku Pro")
    root.configure(background='#856ff8')
    # img = tk.PhotoImage(file="image\\cute-background-img.png")
    #label = tk.Label(root,image=img)
    #label.place(x=0,y=0)
    
    # my_canvas = tk.Canvas(root, width=800, height=500)
    # my_canvas.pack(fill='both', expand=True)
    # my_canvas.create_image(0, 0, image = img, anchor = 'nw')

    try:
        root.iconbitmap("icon\\sudoku.ico")
    except: pass

    Game = GUI(root)
    Game.generate_sudoku_board()
    Game.right_side_option_block()

    root.mainloop()

if __name__ == '__main__':
    main()