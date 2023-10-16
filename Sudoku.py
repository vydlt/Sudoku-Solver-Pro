import tkinter as tk
from src.gui.sudoku_gui import GUI
from PIL import ImageTk, Image

def main():
    root = tk.Tk()
    root.geometry("1920x1080")
    root.title("Sudoku Pro")
    # root.configure(background='#856ff8')
    img = ImageTk.PhotoImage(file="image\\cute-background-img-1920-1080.png")
    label = tk.Label(root,image=img)
    label.place(x=0,y=0)
    
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