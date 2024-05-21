import random
import typing
from colorama import Fore, Style, Back
import validators
from exceptions import MoveError

# разобраться с багом передвижения ( при ходьбе в границу)
# добавить логику при инициализации поля, чтобы у игрока была возможность ходить.
# изменить логику появления игрока и ботов(чтобы была рандомная точка старта)
# обновить валидацию в зависимости от новой функциональности
# обновить отображение, чтобы пользователь изначально видел стартовые точки ботов и себя


class Cell:
    def __init__(self, is_active: bool, verbose_mark: str = ' '):
        validators.validate_cell_init(is_active=is_active, verbose_mark=verbose_mark)
        self.__is_active = is_active
        self.__verbose_mark = verbose_mark

    @property
    def is_active(self):
        return self.__is_active

    @property
    def verbose_mark(self):
        return self.__verbose_mark


class Square:
    def __init__(self, width: int, height: int, verbose_mark: str, inactivity_percent: int):
        validators.validate_square_init(width=width, height=height, verbose_mark=verbose_mark)
        self.width: int = width
        self.height: int = height
        self.content: list[list[typing.Any]] = [
            [self.create_random_cell(inactivity_percent=inactivity_percent, verbose_mark=verbose_mark) for _ in range(self.width)]
            for _ in range(self.height)
        ]
        self.verbose_mark = verbose_mark
        self.__tag = 'SQUARE'


    @property
    def _tag(self):
        return self.__tag

    @staticmethod
    def create_random_cell(inactivity_percent: int, verbose_mark: str) -> Cell:
        choices = [1 for _ in range(100 - inactivity_percent)] + [0 for _ in range(inactivity_percent)]
        cell = Cell(is_active=bool(random.choice(choices)), verbose_mark=verbose_mark)
        return cell

    def display(self) -> None:
        print('- ' * (self.width + 2))
        for row in self.content:
            self.__display_row(row=row)
        print('- ' * (self.width + 2))

    @staticmethod
    def __display_row(row: list['Cell | Rover']) -> None:
        print('|', end=' ')
        for element in row:
            if isinstance(element, Rover):
                verbose_mark = element.get_info()['verbose_mark']
                print(Fore.RED + verbose_mark, end=' ')
                print(Style.RESET_ALL + '', end='')
            elif isinstance(element, Cell):
                if element.is_active:
                    print(element.verbose_mark, end=' ')
                else:
                    print(Back.BLUE + element.verbose_mark, end=' ')
                    print(Style.RESET_ALL + '', end='')
        print('|')


class Rover:
    def __init__(self, verbose_mark: str, start_x: int, start_y: int, square: Square):
        validators.validate_rover_init(verbose_mark=verbose_mark, square=square)
        self.__verbose_mark: str = verbose_mark
        self.__x: int = start_x
        self.__y: int = start_y
        self.__square: Square = square
        self.__tag = 'ROVER'
        self.__to_x: int = start_x
        self.__to_y: int = start_y

    @property
    def __target_cell(self) -> 'Cell | Rover | BotRover':
        return self.__square.content[self.__to_y][self.__to_x]

    @property
    def _tag(self):
        return self.__tag

    def get_info(self) -> dict[str, str | int | Square]:
        result = {
            'verbose_mark': self.__verbose_mark,
            'x': self.__x,
            'y': self.__y,
            'square': self.__square,
        }
        return result

    def move(self, to: str) -> None:
        self.set_target_coordinates(to=to)
        self.__check_borders()
        self.__check_collide()
        self.__check_cell_activity()
        self.__move_to_coordinates()
        self.__update_current_coordinates()
        self.__square.display()

    def __move_to_coordinates(self) -> None:
        self.__square.content[self.__y][self.__x] = Cell(is_active=True, verbose_mark=self.__square.verbose_mark)
        self.__square.content[self.__to_y][self.__to_x] = self

    def set_target_coordinates(self, to: str) -> None:
        if to in ['w', 'ц']:
            self.__to_y = self.__y - 1
        elif to in ['s', 'ы']:
            self.__to_y = self.__y + 1
        elif to in ['a', 'ф']:
            self.__to_x = self.__x - 1
        elif to in ['d', 'в']:
            self.__to_x = self.__x + 1

    def __check_borders(self) -> None:
        result = True

        if self.__to_x < 0:
            result = False
        if self.__to_x > self.__square.width - 1:
            result = False
        if self.__to_y < 0:
            result = False
        if self.__to_y > self.__square.height - 1:
            result = False

        if result is False:
            pass
            raise MoveError('Впереди стена, выберите другое направление.')

    def __check_collide(self) -> None:
        if isinstance(self.__target_cell, Rover):
            pass
            raise MoveError('Я не могу пойти в эту сторону, возможно столкновение.')

    def __check_cell_activity(self) -> None:
        target_cell = self.__target_cell
        if isinstance(target_cell, Cell) and not target_cell.is_active:
            pass
            raise MoveError('Я не могу пойти в эту сторону, эта клетка неактивна')

    def __update_current_coordinates(self) -> None:
        self.__x, self.__y = self.__to_x, self.__to_y


class BotRover(Rover):
    def __init__(self, verbose_mark: str, start_x: int, start_y: int, square: Square):
        super().__init__(verbose_mark=verbose_mark, start_x=start_x, start_y=start_y, square=square)
        self.__tag = 'BOTROVER'
        print(f'{self.__tag}')

    @property
    def _tag(self):
        return self.__tag

    def auto_move(self):
        random_to = random.choice(['w', 's', 'a', 'd'])
        while True:
            try:
                self.move(to=random_to)
                break
            except MoveError:
                continue


class Game:
    def __init__(self, square: Square, bots: list[BotRover], player: Rover):  # square тот же что и у всех роверов
        validators.validate_game_init(square=square, rovers=bots, player=player)
        self.__square = square
        self.bots = bots
        self.player = player

    def play(self):
        self.__square.display()
        while True:
            step = input('Введите куда хотели бы передвинуть робота или команду для завершения теста: ').lower()
            if step == 'выход':
                break
            try:
                self.player.move(to=step)
            except MoveError as ex:
                print(ex)
                continue

            for bot in self.bots:
                bot.auto_move()


def main():
    square = Square(width=10, height=10, verbose_mark=' ', inactivity_percent=5)
    rover = Rover(verbose_mark="*", start_x=5, start_y=5, square=square)
    bot_rover = BotRover(verbose_mark="#", start_x=2, start_y=5, square=square)
    game = Game(square=square, bots=[bot_rover], player=rover)
    square.display()
    game.play()


if __name__ == '__main__':
    main()
