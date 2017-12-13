from src.matplotlib.die import die
import pygal

die1 = die()
die2 = die()
hits = pygal.Bar()
results = []
frequences = []
max_range = die1.numbers_side*2

def draw_svg():
    hits.title = 'Die'
    hits.x_labels= [value for value in range(2,max_range+1)]
    hits._x_title = 'result'
    hits.y_labels = 'frequencey of result'
    hits.add('D6',frequences)
    hits.render_to_file('die_visual.svg')

#生成摇色子结果
for x in range(1,10000):
    result = die1.die_it()+die2.die_it()
    results.append(result)

print(results)

#统计摇色子结果，这个方法有点意思
for value in range(2,max_range+1):
    frequence = results.count(value)
    frequences.append(frequence)

print(frequences)
draw_svg()



