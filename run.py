from game import Game



def main() -> None:
    """Main function to start the game
    """
    user_name = Game.get_user_name()
    game = Game(user_name)
    print("\nRock paper scissor spock and lizard\n")
    print("---Welcome to the game---\n")
    print("       Game Rules:\n")
    print(" -Scissors decapitate Lizard.\n -Scissors cuts paper.\n -Paper covers rock.\n -Rock crushes lizard.\n -Lizard poisons Spock.\n -Spock smashes scissors.\n -Scissors decapitates lizard.\n -Lizard eats paper.\n -Paper disproves Spock.\n -Spock vaporizes rock.\n -Rock crushes scissors.\n")
    print("------You will play 5 Rounds------\n")
    print("Press [Enter] to start:")
    _ = input()
    game.play()
    game.display_game_winner()
    print("+++++++++++++Game Over++++++++++++\n")
    game.restart()

if __name__ == '__main__':
    main()