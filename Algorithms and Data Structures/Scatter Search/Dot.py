class Dot:
    id = 0
    x = 0
    y = 0

    def __init__(self, new_id, new_x, new_y):
        self.id = int(new_id)
        self.x = float(new_x)
        self.y = float(new_y)

    def Position(self):
        return [self.x, self.y]
