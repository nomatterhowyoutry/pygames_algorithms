class Camera:

    def __init__(self):
        self.posx = 0
        self.posy = 0

    def update(self, camera_position):
        self.posx = camera_position[0]
        self.posy = camera_position[1]

    @property
    def position(self):
        return self.posx, self.posy