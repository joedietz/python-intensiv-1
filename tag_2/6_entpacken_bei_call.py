"""
Entpacken von Sequencen oder Dictionaries bei Funktionsaufruf
"""


def D3_coords(x, y, z):
    print(x, y, z)


coords = [
    (1, 2, 3),
    (11, 22, 33),
]

coords_dict = {"x": 3, "y": 4, "z": 5}

for coord in coords:
    x, y, z = coord
    D3_coords(x, y, z)
    D3_coords(coord[0], coord[1], coord[2])
    D3_coords(*coord)  # python variante
    D3_coords(**coords_dict)  # D3_coords(x=3, y=4, z=5)
