from conf import (
    LEFT_BORDER,
    RIGHT_BORDER,
    TOP_BORDER,
    BOTTOM_BORDER
)


class Camera:

    def __init__(self):
        self.posx = 0
        self.posy = 0

    def update(self, camera_position):
        if (camera_position[0] < 1366 and 
            camera_position[0] > -1366):
            self.posx = camera_position[0]
        if (camera_position[1] < 768 and 
            camera_position[1] > -768):
            self.posy = camera_position[1]

    @property
    def position(self):
        return self.posx, self.posy