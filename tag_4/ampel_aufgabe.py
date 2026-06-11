from enum import StrEnum


class TrafficLightState(StrEnum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"


class TrafficLight:
    def __init__(self) -> None:
        self.state: TrafficLightState = TrafficLightState.RED

    def next_state(self) -> None:
        transitions: dict[TrafficLightState, TrafficLightState] = {
            TrafficLightState.RED: TrafficLightState.GREEN,
            TrafficLightState.GREEN: TrafficLightState.YELLOW,
            TrafficLightState.YELLOW: TrafficLightState.RED,
        }
        self.state = transitions[self.state]

    def __str__(self) -> str:
        return self.state


if __name__ == "__main__":
    traffic_light: TrafficLight = TrafficLight()

    print("Initial state:", traffic_light)

    for _ in range(5):
        traffic_light.next_state()
        print("Next state:", traffic_light)
