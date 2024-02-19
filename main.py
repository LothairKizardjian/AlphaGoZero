import tkinter as tk
import threading

from src import GoGUI


def main():
    root = tk.Tk()
    root.title("Go Game")
    gui = GoGUI(root)
    # Start the game loop in a separate thread
    game_thread = threading.Thread(target=gui.run_game_loop)
    game_thread.start()

    root.mainloop()


if __name__ == "__main__":
    main()
