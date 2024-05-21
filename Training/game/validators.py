import typing
from test_game import Square, Rover, BotRover
from exceptions import InitialGemaError


def validate_cell_init(is_active: bool, verbose_mark: str) -> None:
    if not isinstance(is_active, bool):
        raise TypeError('Значение "status", должно быть True или False')
    if not isinstance(verbose_mark, str) or len(verbose_mark) != 1:
        raise ValueError('Значение должно состоять из 1 символа и быть типом "str".')


def validate_square_init(width: int, height: int, verbose_mark: str) -> None:
    if not isinstance(width, int) or width < 1:
        raise ValueError('Ширина поля должна быть указана цифрой, не меньше "1".')
    if not isinstance(height, int) or height < 1:
        raise ValueError('Высота поля должна быть указана цифрой, не меньше "1".')
    if not isinstance(verbose_mark, str) or len(verbose_mark) > 1:
        raise ValueError('Значение "verbose_mark" должно быть строкой, состоящей из 1 символа')


def validate_rover_init(verbose_mark: str, square: 'Square') -> None:
    if not isinstance(verbose_mark, str) or len(verbose_mark) > 1:
        raise ValueError('Значение "verbose_mark" должно быть строкой, состоящей из 1 символа')
    if square._tag != 'SQUARE':
        raise ValueError('Значение "square" должно принимать в себя только объект "Square".')


def validate_game_init(square: 'Square', rovers: list[BotRover], player: Rover) -> None:
    if square._tag != 'SQUARE':
        raise ValueError('Значение "square" должно принимать в себя только объект "Square".')
    if not isinstance(rovers, list):
        raise ValueError('Значение "rovers" должно состоять из списка объектов класса "Rover"')
    for rover in rovers:
        if rover._tag != 'BOTROVER':
            raise ValueError('Значение "rover" должно быть классом "Rover"')
    if player._tag != 'ROVER':
        raise ValueError('Значение "player" должно принимать в себя только объект "Rover".')