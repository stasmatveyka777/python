# case_1 = ["key1", "key2", "key3"]
# case_2 = ["value_1", "value_2", "value_3"]
# c = {i:g for i in case_1 for g in case_2}
# print(c)
case_1 = ["key1", "key2", "key3"]
case_2 = ["value_1", "value_2", "value_3"]
c = {i:g for i in case_1 for g in case_2}
print(c)
for k,v in c.items():
    print(k,v)