# items_1 = {'color' : 'red', 'speed' : 'medium', 'coins' : 15}
# items_2 = {'color' : 'blue', 'speed' : 'fast', 'coins' : 25}
# items_3 = {'color' : 'white', 'speed' : 'fast', 'coins' : 50}
# gamers = [items_1, items_2, items_3]
# for i in gamers:
#     print(i)

gamers = [];
for i in range(0, 150):
    a = {'color' : 'red', 'speed' : 'medium', 'coins' : 15};
    gamers.append(a);
#print(gamers);
for a in gamers[4:9]:
    if a['color']=='red':
        a['color']='blue';
        a['speed']='fast';
        a['coins']=35;
    if a['color']=='blue':
        a['color']='white';
        a['speed']='super-fast';
        a['coins']=50;
for b in gamers:
    print(b);
print("--------------------------------------------------------");
print(f"Всего {len(gamers)} игроков");