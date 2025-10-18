# chess.py
# Made with 💙 by Team Peace & Senthil
# Simple 2-player chess in terminal

import chess
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    board = chess.Board()

    print("♟️ Welcome to Terminal Chess by Senthil!")
    print("Type moves like e2e4 or g8f6. Type 'exit' to quit.\n")

    while True:
        clear()
        print(board)
        print("\nTurn:", "White" if board.turn else "Black")

        if board.is_check():
            print("⚠️ Check!")

        if board.is_checkmate():
            print("🏁 Checkmate! Winner:", "Black" if board.turn else "White")
            break

        move = input("\nYour move: ").strip().lower()
        if move == "exit":
            print("👋 Exiting game...")
            break

        try:
            chess_move = chess.Move.from_uci(move)
            if chess_move in board.legal_moves:
                board.push(chess_move)
            else:
                print("❌ Illegal move. Try again.")
                input("Press Enter...")
        except Exception:
            print("❌ Invalid input. Example: e2e4")
            input("Press Enter...")

if __name__ == "__main__":
    main()

