"""
setattr() => dynamisch Attribut setzen
getattr() => dynamisch Attribut holen
hasattr() => dynamisch Attribut prüfen
"""


class Tree:
    def __init__(self, leaves: int, branches: int):
        self.leaves = leaves
        self.branches = branches


t1 = Tree(leaves=100, branches=4)
print("t1 leaves vorhanden?:", hasattr(t1, "leaves"))
print("t1 leaves:", getattr(t1, "leavess"))  # t.leavess, DEfault ist möglcich
print("t1 set attribute:", setattr(t1, "leaves", 100))
