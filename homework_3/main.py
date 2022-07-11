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


class CheckableFuel(ABC):
    @abstractmethod
    def check(self):
        pass


class BurnableFuel(ABC):
    @abstractmethod
    def burn(self):
        pass


class Executable(ABC):
    @abstractmethod
    def execute(self):
        pass


class ChangeableVelocity(ABC):
    @abstractmethod
    def change_velocity(self):
        pass


class Move:
    def __init__(self, m: Movable):
        self.m = m

    def execute(self):
        self.m.set_position(
            self.m.get_position(),
            self.m.get_velocity()
        )


class CheckFuel:
    def __init__(self, o: CheckableFuel):
        self.o = o

    def execute(self):
        self.o.check()


class BurnFuel:
    def __init__(self, o: BurnableFuel):
        self.o = o

    def execute(self):
        self.o.burn()


class ChangeVelocity:
    def __init__(self, o: ChangeableVelocity):
        self.o = o

    def execute(self):
        self.o.change_velocity()


class Macro:
    def __init__(self, commands: list):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()