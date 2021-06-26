class Dot:
    id = 0
    x = 0
    y = 0

    def __init__(self, new_id, new_x, new_y):
        self.id = int(new_id)
        self.x = int(new_x)
        self.y = int(new_y)

    def Coords(self):
        return [self.x, self.y]

