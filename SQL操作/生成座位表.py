import csv


datas = []
mydict = dict(zip([1, 2, 3, 4, 5], ['A', 'B', 'C', 'E', 'F']))
count = 1
for i in range(5):
    carriage = f"{i+1}C"
    for j in range(20):
        row = []
        seat = f"0{j//5+1}{mydict[j%5+1]}"
        row.append(count)
        row.append(carriage)
        row.append(seat)
        count += 1
        datas.append(row)

for i in datas:
    print(i)
with open('D:\\数据库实训\\Flask\\SQL操作\\数据csv\\SeatTable.csv', 'w', newline='', encoding="utf-16") as f:
    writer = csv.writer(f)
    writer.writerows(datas)
