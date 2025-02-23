class Earphones:
    """Класс для создания наушников"""
    
    def __init__(self, name: str, manufacturer: str):
        self._name = name
        self._manufacturer = manufacturer

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, new_manufacturer: str):
        self._manufacturer = new_manufacturer

    def __str__(self):
        return f'Наушники "{self._name}" от {self._manufacturer}'

    def __repr__(self):
        return f'Earphones(name={self._name!r}, manufacturer={self._manufacturer!r})'


class WiredEarphones(Earphones):
    """Класс для проводных наушников"""
    
    def __init__(self, name: str, manufacturer: str, condition: str = 'unplugged'):
        super().__init__(name, manufacturer)
        if condition not in ('plugged', 'unplugged'):
            raise ValueError('Состояние может быть только "plugged" или "unplugged"')
        self._condition = condition

    @property
    def condition(self):
        return self._condition

    def plug(self):
        self._condition = 'plugged'

    def unplug(self):
        self._condition = 'unplugged'

    def __str__(self):
        return f'{super().__str__()}, состояние: {self._condition}'

    def __repr__(self):
        return f'WiredEarphones(name={self._name!r}, manufacturer={self._manufacturer!r}, condition={self._condition!r})'


class WirelessEarphones(Earphones):
    """Класс для беспроводных наушников"""
    
    def __init__(self, name: str, manufacturer: str, charge: int):
        super().__init__(name, manufacturer)
        if not (0 <= charge <= 100):
            raise ValueError('Заряд должен быть от 0 до 100')
        self._charge = charge

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, new_charge: int):
        if not (0 <= new_charge <= 100):
            raise ValueError('Заряд должен быть от 0 до 100')
        self._charge = new_charge

    def battery_status(self):
        return 'Заряд в норме' if self._charge > 20 else 'Низкий заряд'

    def __str__(self):
        return f'{super().__str__()}, заряд: {self._charge}%'

    def __repr__(self):
        return f'WirelessEarphones(name={self._name!r}, manufacturer={self._manufacturer!r}, charge={self._charge!r})'
