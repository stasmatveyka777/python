mashin = ['Tesla','Bmw','Suzuki','Mers']
mashin.append('honda')
mashin[0] = 'Lexus'
mashin.insert(1, 'Mazda')
mashin.insert(0,'Ducat')
del mashin[3]
del_mashin = mashin.pop(1)
print(mashin)
print(del_mashin)
