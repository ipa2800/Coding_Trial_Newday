from src.matplotlib.die import die
import pygal

die1 = die()
results = []
hits = pygal.Bar()

for x in range(1,1000):
    result = die1.die_it()
    results.append(result)

print(results)

frequences = []
for value in range(1,die1.numbers_side+1):
    frequence = results.count(value)
    frequences.append(frequence)

print(frequences)
hits.title = 'Die'
hits.x_labels= ['1','2','3','4','5','6']
hits._x_title = 'result'
hits.y_labels = 'frequencey of result'
hits.add('D6',frequences)
hits.render_to_file('die_visual.svg')


