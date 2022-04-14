from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def set_position(self):
        pass

    @abstractmethod
    def get_velocity(self):
        pass


class Rotable(ABC):
    @abstractmethod
    def set_direction(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass

    @abstractmethod
    def get_angular_velocity(self):
        pass


class Move:
    def __init__(self, m: Movable):
        self.m = m

    def execute(self):
        self.m.set_position(
            self.m.get_position(),
            self.m.get_velocity()
        )


class Rotate:
    def __init__(self, r: Rotable):
        self.r = r

    def execute(self):
        self.r.set_direction(
            self.r.get_direction().next(self.r.get_angular_velocity())
        )

