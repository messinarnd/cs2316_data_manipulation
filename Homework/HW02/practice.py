# Christopher Messina
# cmessina6
# 903023165

from practice_data import *

e2f = {en[x]: fr[x] for x in range(0, len(en))}

e2both = {en[x]: {'fr': fr[x], 'de': de[x]} for x in range(0,len(en))}

love_de = [v['de'] for k, v in e2both.items() if k == 'to love'][0]

avoir_en = [k for k, v in e2f.items() if v == 'avoir'][0]

location2temps = {water_temps[x][0]: [water_temps[x][y] for y in range(1, len(water_temps[x]))] for x in range(1, len(water_temps))}

min_miami_temp = min(location2temps['Miami Beach FL'])

avg_location_temps = {water_temps[x][0]: (sum(water_temps[x][1:]) / (len(water_temps[x]) - 1)) for x in range(1, len(water_temps))}

warmest_location = [k for k, v in avg_location_temps.items() if v == max(avg_location_temps.values())][0]

avg_month_temps = {str(water_temps[0][x]): sum(list(water_temps[y][x] for y in range(1, len(water_temps)))) / float(len(list(water_temps[y][x] for y in range(1, len(water_temps))))) for x in range(1, len(water_temps[0]))}

warmest_month = [k for k, v in avg_month_temps.items() if v == max(avg_month_temps.values())][0]
