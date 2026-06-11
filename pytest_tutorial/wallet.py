class InsufficientAmount(Exception):
    pass


class Wallet:
    def __init__(self, initial_amount: int = 0) -> None:
        self.balance = initial_amount

    def spend_cash(self, amount: int) -> None:
        if self.balance < amount:
            raise InsufficientAmount("Nicht genug Geld drauf!")
        self.balance -= amount

    def add_cash(self, amount: int) -> None:
        self.balance += amount


if __name__ == "__main__":
    w = Wallet()
    print("Geld drauf:", w.balance)
    w.add_cash(100)
    try:
        w.spend_cash(101)
    except InsufficientAmount as e:
        print(e)

    # assert 1 == 1, "1 und 1 sollte wahr sein"
    # assert 1 == 2, "1 und 2 sollte wahr sein"
