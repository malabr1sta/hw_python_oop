from typing import List, Dict, Type
from abc import abstractmethod
from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        message = ('Тип тренировки: {training_type}; '
                   'Длительность: {duration:.3f} ч.; '
                   'Дистанция: {distance:.3f} км; '
                   'Ср. скорость: {speed:.3f} км/ч; '
                   'Потрачено ккал: {calories:.3f}.'.format(**asdict(self))
                   )
        return message


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    H_IN_M: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duaration_h = duration
        self.weight_kg = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed = self.get_distance() / self.duaration_h
        return speed

    @abstractmethod
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        example = InfoMessage(self.__class__.__name__,
                              self.duaration_h,
                              self.get_distance(),
                              self.get_mean_speed(),
                              self.get_spent_calories(),
                              )
        return example


class Running(Training):
    """Тренировка: бег."""

    COEFF_CALORIE_1: int = 18
    COEFF_CALORIE_2: int = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        spent_calories = ((self.COEFF_CALORIE_1 * self.get_mean_speed()
                          - self.COEFF_CALORIE_2) * self.weight_kg
                          / self.M_IN_KM * self.duaration_h * self.H_IN_M
                          )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEFF_CALORIE_SW_1: float = 0.035
    COEFF_CALORIE_SW_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height_cm = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        spent_calories = ((self.COEFF_CALORIE_SW_1 * self.weight_kg
                          + (self.get_mean_speed() ** 2 // self.height_cm)
                          * self.COEFF_CALORIE_SW_2 * self.weight_kg)
                          * self.duaration_h * self.H_IN_M
                          )
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    COEFF_CALORIE_SWIM_1: float = 1.1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool_m = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed = (self.length_pool_m * self.count_pool
                 / self.M_IN_KM / self.duaration_h
                 )
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        spent_calories = ((self.get_mean_speed()
                          + self.COEFF_CALORIE_SWIM_1) * 2 * self.weight_kg
                          )
        return spent_calories


DICT_ANOTATION = Dict[str, Type[Training]]


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    encoding_training: DICT_ANOTATION = {'SWM': Swimming,
                                         'RUN': Running,
                                         'WLK': SportsWalking,
                                         }
    try:
        example_traning = encoding_training[workout_type](*data)
    except KeyError:
        print('Неизвестный тип тренировки.')
    return example_traning


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
