class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        self.message = (f'Тип тренировки: {self.training_type}; '
                        f'Длительность: {self.duration:.3f} ч.; '
                        f'Дистанция: {self.distance:.3f} км; '
                        f'Ср. скорость: {self.speed:.3f} км/ч; '
                        f'Потрачено ккал: {self.calories:.3f}.'
                        )
        return self.message


class Training:
    """Базовый класс тренировки."""

    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duaration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        self.distance = self.action * self.LEN_STEP / self.M_IN_KM
        return self.distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        self.speed = self.get_distance() / self.duaration
        return self.speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        self.example = InfoMessage(self.__class__.__name__,
                                   self.duaration,
                                   self.get_distance(),
                                   self.get_mean_speed(),
                                   self.get_spent_calories(),
                                   )
        return self.example


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        self.coeff_calorie_1 = 18
        self.coeff_calorie_2 = 20
        self.spent_calories = ((self.coeff_calorie_1 * self.get_mean_speed()
                               - self.coeff_calorie_2) * self.weight
                               / self.M_IN_KM * self.duaration * 60
                               )
        return self.spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        self.coeff_1 = 0.035
        self.coeff_2 = 0.029
        self.spent_calories = ((self.coeff_1 * self.weight
                               + (self.get_mean_speed() ** 2 // self.height)
                               * self.coeff_2 * self.weight)
                               * self.duaration * 60
                               )
        return self.spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        self.speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duaration
                      )
        return self.speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        self.coeff_1 = 1.1
        self.spent_calories = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return self.spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    encoding_training = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    if workout_type == 'SWM':
        example_traning = encoding_training[workout_type](data[0],
                                                          data[1],
                                                          data[2],
                                                          data[3],
                                                          data[4],
                                                          )
    elif workout_type == 'RUN':
        example_traning = encoding_training[workout_type](data[0],
                                                          data[1],
                                                          data[2],
                                                          )
    else:
        example_traning = encoding_training[workout_type](data[0],
                                                          data[1],
                                                          data[2],
                                                          data[3],
                                                          )
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
