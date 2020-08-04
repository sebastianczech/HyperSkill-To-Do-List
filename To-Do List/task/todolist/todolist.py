# Write your code here
def showTasks(tasks):
    for index, task in enumerate(tasks):
        print(str(index + 1) + ") " + task)


if __name__ == '__main__':
    print("Today:")

    tasks = [
        "Do yoga",
        "Make breakfast",
        "Learn basics of SQL",
        "Learn what is ORM"
    ]
    showTasks(tasks)
