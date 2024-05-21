import random
import typing
from colorama import Fore, Style, Back
import validators
from exceptions import MoveError, InitialGemaError


# Добавить логику стрельбы к роверу
# обновить валидацию в зависимости от новой функциональности


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
        self.__inactivity_percent = inactivity_percent
        self.__verbose_mark = verbose_mark

    @property
    def _tag(self):
        return self.__tag

    def redraw(self) -> None:
        new_content = [
            [self.create_random_cell(inactivity_percent=self.__inactivity_percent, verbose_mark=self.__verbose_mark) for _ in
             range(self.width)]
            for _ in range(self.height)
        ]
        for current_y in range(len(self.content)):
            for current_x in range(len(self.content[current_y])):
                field = self.content[current_y][current_x]
                if not isinstance(field, Cell):
                    new_content[current_y][current_x] = field
        self.content = new_content

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
                    print(Back.YELLOW + element.verbose_mark, end=' ')
                    print(Style.RESET_ALL + '', end='')
        print('|')


class Rover:
    def __init__(self, verbose_mark: str, square: Square):
        validators.validate_rover_init(verbose_mark=verbose_mark, square=square)
        self.__verbose_mark: str = verbose_mark
        self.__x: int = random.randint(1, square.width - 1)
        self.__y: int = random.randint(1, square.height - 1)
        self.__square: Square = square
        self.__tag = 'ROVER'
        self.__to_x: int = self.__x
        self.__to_y: int = self.__y
        self.__square.content[self.__y][self.__x] = self
        self.target = self.__square.content[self.__y][self.__x]
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
        self.__set_target_coordinates(to=to)
        self.__check_possibility_to_move_to_target_coordinates()
        self.__move_to_coordinates()
        self.__update_current_coordinates()
        self.__square.display()

    def __check_possibility_to_move_to_target_coordinates(self) -> None:
        self.__check_borders()
        self.__check_collide()
        self.__check_cell_activity()

    def ghost_move(self, to) -> bool:
        try:
            self.__set_target_coordinates(to=to)
            self.__check_possibility_to_move_to_target_coordinates()
            return True
        except MoveError:
            return False

    def __move_to_coordinates(self) -> None:
        self.__square.content[self.__y][self.__x] = Cell(is_active=True, verbose_mark=self.__square.verbose_mark)
        self.__square.content[self.__to_y][self.__to_x] = self

    def __set_target_coordinates(self, to: str) -> None:
        if to in ['w', 'ц']:
            self.__to_y = self.__y - 1
        elif to in ['s', 'ы']:
            self.__to_y = self.__y + 1
        elif to in ['a', 'ф']:
            self.__to_x = self.__x - 1
        elif to in ['d', 'в']:
            self.__to_x = self.__x + 1

    def __set_previous_target_coordinates(self) -> None:
        self.__to_y, self.__to_x = self.__y, self.__x

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
            self.__set_previous_target_coordinates()
            raise MoveError('Впереди стена, выберите другое направление.')

    def __check_collide(self) -> None:
        if isinstance(self.__target_cell, Rover):
            self.__set_previous_target_coordinates()
            raise MoveError('Я не могу пойти в эту сторону, возможно столкновение.')

    def __check_cell_activity(self) -> None:
        target_cell = self.__target_cell
        if isinstance(target_cell, Cell) and not target_cell.is_active:
            self.__set_previous_target_coordinates()
            raise MoveError('Я не могу пойти в эту сторону, эта клетка неактивна')

    def __update_current_coordinates(self) -> None:
        self.__x, self.__y = self.__to_x, self.__to_y

    # def shoot(self, to: str) -> None:
    #     bullet = '>'
    #     if to in ['d', 'в']:
    #         start_index = self.__x + 1
    #         stop_index = self.__square.width
    #         step = 1
    #     # elif to in ['a', 'ф']:
    #     else:
    #         start_index = self.__x - 1
    #         stop_index = -1
    #         step = -1
    #
    #     for index in range(start_index, stop_index, step):
    #         cell = self.__square.content[self.__y][index]
    #
    #         if isinstance(cell, BotRover):
    #             print('Попали в бота')
    #             break
    #         if isinstance(cell, Cell) and not cell.is_active:
    #             print('Попали в стену')
    #             break
    #         self.__square.content[self.__y][index] = Cell(is_active=True, verbose_mark=bullet)
    #         self.__square.display()
    #         self.__square.content[self.__y][index] = Cell(is_active=True, verbose_mark=self.__square.verbose_mark)
    #     else:
    #         print('Пуля улетела за границы поля')
    def shoot(self, to: str) -> None:
        bullet = '>'
        if to in ['d', 'в']:
            start_index_x = self.__x + 1
            stop_index_x = self.__square.width
            step_index_x = 1
            start_index_y = self.__y
            stop_index_y = self.__y + 1
            step_index_y = 1

        elif to in ['a', 'ф']:
            start_index_x = self.__x - 1
            stop_index_x = -1
            step_index_x = -1
            start_index_y = self.__y
            stop_index_y = self.__y + 1
            step_index_y = 1

        elif to in ['w', 'ц']:
            start_index_x = self.__x
            stop_index_x = self.__x + 1
            step_index_x = 1
            start_index_y = self.__y - 1
            stop_index_y = -1
            step_index_y = -1

        else:
            start_index_x = self.__x
            stop_index_x = self.__x + 1
            step_index_x = 1
            start_index_y = self.__y + 1
            stop_index_y = self.__square.height
            step_index_y = 1

        for index_y in range(start_index_y, stop_index_y, step_index_y):

            for index_x in range(start_index_x, stop_index_x, step_index_x):
                cell = self.__square.content[index_y][index_x]

                if isinstance(cell, BotRover):
                    print('Попали в бота')
                    return
                if isinstance(cell, Cell) and not cell.is_active:
                    print('Попали в стену')
                    return
                self.__square.content[index_y][index_x] = Cell(is_active=True, verbose_mark=bullet)
                self.__square.display()
                self.__square.content[index_y][index_x] = Cell(is_active=True, verbose_mark=self.__square.verbose_mark)

        print('Пуля улетела за границы поля')


class BotRover(Rover):
    def __init__(self, verbose_mark: str, square: Square):
        super().__init__(verbose_mark=verbose_mark, square=square)
        self.__tag = 'BOTROVER'
        print(f'{self.__tag}')

    @property
    def _tag(self):
        return self.__tag

    def auto_move(self):
        choices = ['w', 's', 'a', 'd']
        for _ in range(len(choices)):
            random_to = random.choice(choices)
            try:
                self.move(to=random_to)
                break
            except MoveError:
                choices.remove(random_to)


class Game:
    def __init__(self, square: Square, bots: list[BotRover], player: Rover):  # square тот же что и у всех роверов
        validators.validate_game_init(square=square, rovers=bots, player=player)
        self.__square = square
        self.bots = bots
        self.player = player

    def __start(self):
        while True:
            try:
                self.__square.display()
                self.__check_player_start_position()
                return
            except InitialGemaError:
                self.__square.redraw()

    def __check_player_start_position(self,):
        for to in ['w', 'a', 's', 'd']:
            moving_is_possible = self.player.ghost_move(to=to)
            if moving_is_possible:
                break
        else:
            raise InitialGemaError('Игрок не может ходить, перезапуск игры...')

    def play(self):
        self.__start()
        self.__square.display()
        while True:
            step = input('Введите куда хотели бы передвинуть робота или команду для завершения теста: ').lower()
            if step == 'выход':
                break
            try:
                if step in ['a', 'w', 'd', 's', 'ф', 'ц', 'в', 'ы']:
                    self.player.move(to=step)
                elif 'f-' in step:
                    to = step.split('-')[-1]
                    self.player.shoot(to=to)
            except MoveError as ex:
                print(ex)
                continue

            for bot in self.bots:
                bot.auto_move()


def main():
    square = Square(width=10, height=10, verbose_mark=' ', inactivity_percent=20)
    rover = Rover(verbose_mark="*", square=square)
    bot_rover = BotRover(verbose_mark="#", square=square)
    game = Game(square=square, bots=[bot_rover], player=rover)
    square.display()

    game.play()


if __name__ == '__main__':
    main()
