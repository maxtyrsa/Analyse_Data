P = int(input())
N = 200
B = 150
kpi = round((P-B)/(N-B)*100, 2)
if kpi > 100:
    print("Good KPI +", kpi-100, "%")
else:
    print("Bad KPI", kpi-100, "%")
