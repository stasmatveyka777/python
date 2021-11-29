dict={
    'Illia':['task-1','task-2'],
    'Alexey':['task-1','task-2','task-3'],
    'Yaroslave':['task-1'],
    'Rom4ik':['task-1','task-2'],
    'Artemik':['task-1','task-2','task-3','task-4']
    }
for i,b in dict.items():
    print("----------------------------------------------------")
    print(f"{i} решил такие задачи:")
    for a in b:
        print(f"{a}")