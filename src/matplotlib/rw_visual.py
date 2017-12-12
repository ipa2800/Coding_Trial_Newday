import matplotlib.pyplot as plt
from src.matplotlib.random_walk import RandomWalk

x=1
while x in range(1,5):
    rw = RandomWalk(3000)
    rw.walk()
    plt.figure(dpi=128, figsize=(16, 9))
    point_numbers = list(range(rw.max_point))
    plt.plot(rw.x_value,rw.y_value,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')
    plt.scatter(0,0,c='green',s=100)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    x = x+1