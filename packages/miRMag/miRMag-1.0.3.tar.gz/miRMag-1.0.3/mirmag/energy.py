#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

from typing import List
from mirmag.logger import get_logger


logger = get_logger(logger_name="energy")


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Energy(metaclass=Singleton):
    """ Class to describe RNA-RNA interaction with some energy.

    Returns
    -------
    Energy object : object with the energy calculation methods
        The Energy object.
    """

    ENERGY_TABLE = dict()   # Таблица энергий для пар нуклеотидов вида AB/CD.
    MAX_ENERGY = 1000       # kcal/mol, предельная [нереальная] энергия структуры.

    def __init__(self):
        """ Инициализация таблицы энергий ENERGY_TABLE.

        Функция заполняет словарь энергиями для пар нуклеотидов вида AB/CD, где AB - пара с направлением 5' → 3',
        а CD - пара из РНК с направлением 3' → 5'. Пара A/C всегда комплементарна (спираль), пара B/D может быть
        некомплементарна (1нт свисающий конец после спирали). Комплементарные пары - GC и AU, пара GU - НЕкомплементарна.
        Энергии взяты из статьи "Improved free-energy parameters for predictions of RNA duplex ..." by Freier et al, 1986.

        :return: None.
        """

        self.ENERGY_TABLE['GA/CA'] = -1.1
        self.ENERGY_TABLE['GA/CC'] = -1.3
        self.ENERGY_TABLE['GA/CG'] = -1.3
        self.ENERGY_TABLE['GA/CU'] = -2.3
        self.ENERGY_TABLE['GC/CA'] = -1.1
        self.ENERGY_TABLE['GC/CC'] = -0.6
        self.ENERGY_TABLE['GC/CG'] = -3.4
        self.ENERGY_TABLE['GC/CU'] = -0.5
        self.ENERGY_TABLE['GG/CA'] = -1.6
        self.ENERGY_TABLE['GG/CC'] = -2.9
        self.ENERGY_TABLE['GG/CG'] = -1.4
        self.ENERGY_TABLE['GG/CU'] = -1.4
        self.ENERGY_TABLE['GU/CA'] = -2.1
        self.ENERGY_TABLE['GU/CC'] = -0.8
        self.ENERGY_TABLE['GU/CG'] = -2.3
        self.ENERGY_TABLE['GU/CU'] = -0.7
        #
        self.ENERGY_TABLE['CA/GA'] = -1.9
        self.ENERGY_TABLE['CA/GC'] = -2.0
        self.ENERGY_TABLE['CA/GG'] = -1.9
        self.ENERGY_TABLE['CA/GU'] = -1.8
        self.ENERGY_TABLE['CC/GA'] = -1.0
        self.ENERGY_TABLE['CC/GC'] = -1.1
        self.ENERGY_TABLE['CC/GG'] = -2.9
        self.ENERGY_TABLE['CC/GU'] = -0.8
        self.ENERGY_TABLE['CG/GA'] = -1.9
        self.ENERGY_TABLE['CG/GC'] = -2.0
        self.ENERGY_TABLE['CG/GG'] = -1.9
        self.ENERGY_TABLE['CG/GU'] = -1.6
        self.ENERGY_TABLE['CU/GA'] = -1.7
        self.ENERGY_TABLE['CU/GC'] = -1.5
        self.ENERGY_TABLE['CU/GG'] = -1.9
        self.ENERGY_TABLE['CU/GU'] = -1.2
        #
        self.ENERGY_TABLE['AA/UA'] = -0.8
        self.ENERGY_TABLE['AA/UC'] = -1.0
        self.ENERGY_TABLE['AA/UG'] = -1.0
        self.ENERGY_TABLE['AA/UU'] = -0.9
        self.ENERGY_TABLE['AC/UA'] = -0.7
        self.ENERGY_TABLE['AC/UC'] = -0.7
        self.ENERGY_TABLE['AC/UG'] = -2.1
        self.ENERGY_TABLE['AC/UU'] = -0.7
        self.ENERGY_TABLE['AG/UA'] = -0.8
        self.ENERGY_TABLE['AG/UC'] = -1.7
        self.ENERGY_TABLE['AG/UG'] = -1.0
        self.ENERGY_TABLE['AG/UU'] = -0.9
        self.ENERGY_TABLE['AU/UA'] = -0.9
        self.ENERGY_TABLE['AU/UC'] = -0.8
        self.ENERGY_TABLE['AU/UG'] = -0.9
        self.ENERGY_TABLE['AU/UU'] = -0.8
        #
        self.ENERGY_TABLE['UA/AA'] = -1.0
        self.ENERGY_TABLE['UA/AC'] = -0.8
        self.ENERGY_TABLE['UA/AG'] = -1.1
        self.ENERGY_TABLE['UA/AU'] = -1.1
        self.ENERGY_TABLE['UC/AA'] = -0.7
        self.ENERGY_TABLE['UC/AC'] = -0.6
        self.ENERGY_TABLE['UC/AG'] = -2.3
        self.ENERGY_TABLE['UC/AU'] = -0.5
        self.ENERGY_TABLE['UG/AA'] = -1.1
        self.ENERGY_TABLE['UG/AC'] = -1.8
        self.ENERGY_TABLE['UG/AG'] = -1.2
        self.ENERGY_TABLE['UG/AU'] = -0.9
        self.ENERGY_TABLE['UU/AA'] = -0.9
        self.ENERGY_TABLE['UU/AC'] = -0.6
        self.ENERGY_TABLE['UU/AG'] = -1.0
        self.ENERGY_TABLE['UU/AU'] = -0.5

    def get_internal_loop_energy(self, length: int) -> float:
        """ Вычисление свободной энергии внутренней (двухсторонней, internal) петли по её длине.

        Пример структуры с internal петлей:
        5' xx     ->     xx 3'
             CUGCAAAAAUCG
             ||||     |||
             GAUGGGGGGAGG
        3' xx     ->     xx 5'

        Петля длиной 1нт считается bulge, а не internal.
        Рассчет реализован без наложения штрафов за асимметричные петли (петли с ветвями разной длины).
        Формула рассчета взята из статьи "Improved predictions ..." by Jaeger et al., PNAS, (1989), v. 86, pp. 7706-7710.

        :param length: Длина петли, равная суммарной длине обоих ветвей.
        :return: Значение свободной энергии.
        """

        try:
            if length < 11:
                return {2: 4.1, 3: 4.5, 4: 4.9, 5: 5.3, 6: 5.7, 7: 5.9, 8: 6.0, 9: 6.1, 10: 6.3}[length]
            else:
                # Formula: dG(n) = dG(n_max) + 1.75 * (0.001 * R) * T * ln(n / 6), n_max = 6.
                return 5.7 + 1.75 * (0.001 * 1.987) * 310.15 * math.log(length / 6.0)
        except Exception:
            logger.exception(f"Запрошена энергия для внутренней петли с некорректно заданной длиной. Длина: {length}.")
            return self.MAX_ENERGY

    def get_bulge_loop_energy(self, length: int) -> float:
        """ Вычисление свободной энергии боковой (bulge) петли по ее длине.

        Пример структуры с bulge петлей:
        5' xx     ->     xx 3'
             CUGC-----UCG
             ||||     |||
             GAUGGGGGGAGG
        3' xx     ->     xx 5'

        Петля длиной 1нт считается bulge, а не internal.
        Формула рассчета взята из статьи "Improved predictions ..." by Jaeger et al., PNAS, (1989), v. 86, pp. 7706-7710.

        :param length: Длина петли.
        :return: Значение свободной энергии.
        """

        try:
            if length < 11:
                return {1: 3.9, 2: 3.1, 3: 3.5, 4: 4.2, 5: 4.8, 6: 5.0, 7: 5.2, 8: 5.3, 9: 5.4, 10: 5.5}[length]
            else:
                # Formula: dG(n) = dG(n_max) + 1.75 * (0.001 * R) * T * ln(n / 5), n_max = 5.
                return 4.8 + 1.75 * (0.001 * 1.987) * 310.15 * math.log(length / 5.0)
        except Exception:
            logger.exception(f"Запрошена энергия для боковой петли с некорректно заданной длиной. Длина: {length}.")
            return self.MAX_ENERGY

    def get_helix_energy(self, up_sequence: str, down_sequence: str) -> float:
        """ Вычисление свободной энергии спирали по двум взаимодействующим последовательностям.

        Энергия вычисляется суммированием энергий пар AB/CD по таблице энергий ENERGY_TABLE.
        Завершающая пара B/D может быть как комплементарной (энергия только спирали), так и нет (свисающие 1нт концы).
        Для последовательностей разной длины выдается максимальная энергия MAX_ENERGY. Это ошибка данных.
        Функция регистроНЕзависимая.

        Пример структуры с спиралью:
        5' xx     ->     xx 3'
             CUGCAUACUUCG
             |||||||||||
             GAUGUAUGAAGG
        3' xx     ->     xx 5'

        Последовательно складываются энергии пар CU/GA, UG/AU, GC/UG и так далее до последней.
        Основано на статье "Improved free-energy parameters for predictions of RNA duplex stability" by Freier et al, 1986.

        :param up_sequence: последовательность РНК, направление 5'→3'.
        :param down_sequence: последовательность РНК, направление 3'→5'.
        :return: Значение свободной энергии спирали.
        """

        # Check input objects
        if not up_sequence or not down_sequence or not isinstance(up_sequence, str) or not isinstance(down_sequence, str):
            logger.error(f"Запрошена энергия спирали для некорректных данных.\n"
                         f"up_sequence: '{up_sequence}', down_sequence: '{down_sequence}'.")
            return self.MAX_ENERGY

        # Check sequences' lengths
        if len(up_sequence) != len(down_sequence):
            logger.error(f"Запрошена энергия спирали для последовательностей разной длины.\n"
                         f"up_sequence: '{up_sequence}', down_sequence: '{down_sequence}'.")
            return self.MAX_ENERGY

        # One nucleotide length
        if len(up_sequence) == 1:
            logger.error(f"Запрошена энергия спирали для 1нт последовательностей.\n"
                         f"up_sequence: '{up_sequence}', down_sequence: '{down_sequence}'.")
            return self.MAX_ENERGY

        try:
            # Prepare input data to uniform view
            up_sequence = up_sequence.upper().replace('T', 'U')
            down_sequence = down_sequence.upper().replace('T', 'U')

            # Calculate energy of the pairs
            energy = 0.0
            for i in range(len(up_sequence) - 1):
                pairs = up_sequence[i:i + 2] + '/' + down_sequence[i:i + 2]     # Format: AB/CD.
                energy += self.ENERGY_TABLE[pairs]
            #
            return energy

        except Exception:
            logger.exception(f"Ошибка при вычислении свободной энергии спирали. Это не спираль.\n"
                             f"up_sequence: '{up_sequence}', down_sequence: '{down_sequence}'.")
            return self.MAX_ENERGY


if __name__ == "__main__":
    """ Examples / Use cases. """

    eng = Energy()
    print(f"Энергия пары GA/CA: {eng.ENERGY_TABLE['GA/CA']}")

    print()
    print("Internal loop energy.")
    print("Negative length:", eng.get_internal_loop_energy(-1))
    print("Correct short length:", eng.get_internal_loop_energy(3))
    print("Correct long length:", eng.get_internal_loop_energy(15))

    print()
    print("Bulge loop energy.")
    print("Negative length:", eng.get_bulge_loop_energy(-1))
    print("Correct short length:", eng.get_bulge_loop_energy(3))
    print("Correct long length:", eng.get_bulge_loop_energy(15))

    print()
    print("Helix energy.")
    print("Empty sequences:", eng.get_helix_energy("", ""))
    print("Correct sequences:", eng.get_helix_energy("UGGUA", "ACCAA"))
    # ENERGY_TABLE['UG/AC'] = -1.8    1
    # ENERGY_TABLE['GG/CC'] = -2.9    2
    # ENERGY_TABLE['GU/CA'] = -2.1    3
    # ENERGY_TABLE['UA/AA'] = -1.0    4

    eng1 = Energy()
    eng2 = Energy()
    print(eng1 == eng2, id(eng1) == id(eng2))
