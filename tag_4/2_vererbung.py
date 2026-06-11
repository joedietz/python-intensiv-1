class BaseRobot:
    def __init__(self, name: str) -> None:
        self.name = name

    def walk(self) -> None:
        print(f"{self.name} is walking....")


class Robot(BaseRobot):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power


c3po = Robot(name="C3PO", power=100)
c3po.walk()
