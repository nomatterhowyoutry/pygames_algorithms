from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    MAP_SIZE,
    TOP_BORDER,
    BOTTOM_BORDER
)

class Map():

    def __init__(self):
       self.size = MAP_SIZE
       self.chunk_range = self.size * 3
       self.chunk_height = SCREEN_HEIGHT
       self.chunk_width = SCREEN_WIDTH
       self.chunks = self.__generate_chunks()


    def __generate_chunks(self):
        self.array = [[0 for _ in range(self.chunk_range)] for _ in range(self.chunk_range)]
        for i in range(0, self.chunk_range):
            for j in range(0, self.chunk_range):
                self.array[i][j] = ((j - self.size) * self.chunk_width, (i - self.size) * self.chunk_height)
        return self.array

    def get_chunk(self, coords):
        x = coords[0]
        y = coords[1]
        for i in range(0, self.chunk_range):
            for j in range(0, self.chunk_range):
                if (x >= self.chunks[i][j][0] and 
                    x < self.chunks[i][j][0] + SCREEN_WIDTH and 
                    y >= self.chunks[i][j][1] and 
                    y < self.chunks[i][j][1] + SCREEN_HEIGHT):
                    return i, j

    def get_renderable_chunks(self, coords):
        array = []
        i, j = self.get_chunk(coords)
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                array.append((k, l))
        return array

