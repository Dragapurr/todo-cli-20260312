tasks = []

while True:
    task = input("Add task (or exit): ")

    if task == "exit":
        break

    tasks.append(task)

print("Tasks:")
for t in tasks:
    print("-",t)
