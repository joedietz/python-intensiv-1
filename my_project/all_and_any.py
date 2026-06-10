x = 4
if all(
    [
        x > 3,
        x == 3,
        x < 34,
    ]
):
    print("alle Bedingngen sind wahr")


if any(
    [
        x > 3,
        x == 3,
        x < 34,
    ]
):
    print("eine Bedingngen sind wahr")
