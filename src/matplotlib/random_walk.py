from random import choice
class RandomWalk():
    def __init__(self,max_point=5000):
        self.max_point = max_point
        self.x_value = [0]
        self.y_value = [0]

    def walk(self):
        while len(self.x_value) < self.max_point:
            x_direction = choice([1,-1])
            x_distance = choice([1,2,3,4,5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            #-1 是切片中取最后一个元素
            x_next = self.x_value[-1] + x_step
            y_next = self.y_value[-1] + y_step
            self.x_value.append(x_next)
            self.y_value.append(y_next)

