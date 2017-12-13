from random import choice
class RandomWalk():
    def __init__(self,max_point):
        self.max_point = max_point
        self.x_value = [0]
        self.y_value = [0]

    def walk(self):
        while len(self.x_value) < self.max_point:
            x_step=self.getstep()
            y_step=self.getstep()

            if x_step == 0 and y_step == 0:
                continue

            #-1 是切片中取最后一个元素
            x_next = self.x_value[-1] + x_step
            y_next = self.y_value[-1] + y_step
            self.x_value.append(x_next)
            self.y_value.append(y_next)


    def getstep(self):
        direction = choice([1, -1, 2, -2, 3, -3])
        distance = choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        return direction * distance


