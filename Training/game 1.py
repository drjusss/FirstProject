from Training.game.test_game import RoverGame, Square


def main() -> None:
    width = int(input('Введите ширину поля: '))
    height = int(input('Введите высоту поля: '))

    field = Square(width=10, height=10, start_x=5, start_y=5)
    game1 = RoverGame(width=width, height=height, start_x=5, start_y=5)
    game1.play()


if __name__ == '__main__':
    main()
