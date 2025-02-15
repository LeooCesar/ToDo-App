class Task:
    number_of_tasks = 0     #class atributes

    def __init__(self, name, status, deadline):
        self.name = name
        self.status = status
        self.deadline = deadline
        Task.number_of_tasks += 1

class ToDo_list:
    number_of_finished_tasks = 0        #class atributes
    number_of_unfinished_tasks = 0
    tasks = []

    def __init__(self, list_of_tasks = None):
        if list_of_tasks is None:
            list_of_tasks = []
        self.tasks = list_of_tasks[:]
        for task in self.tasks:
            if(task.status == "finished"):
                ToDo_list.number_of_finished_tasks += 1
            else:
                ToDo_list.number_of_unfinished_tasks += 1

    def add(self, task_name, task_status, task_deadline):
        #this method adds a new task to Todo_list
        new_task = Task(task_name, task_status, task_deadline)
        for task in self.tasks:
            if (new_task.name == task.name):
                print(f"{task.name} is already on your list. If you want to change some information about {task.name}, use the function update")
                print(" ")
                return
        self.tasks.append(new_task)
        print(f"{new_task.name} is now on your list")
        print(" ")

    def update(self, task_name, new_status, new_deadline):
        #this method update a task that already is in Todo_list
        for task in self.tasks:
            if(task.name == task_name): 
                if(task.status != new_status):
                    print(f"{task.name} is now {new_status}")
                task.status = new_status
                if(task.deadline != new_deadline and new_deadline != " "):
                    print(f"{task.name} deadline is now {new_deadline}")
                task.deadline = new_deadline
                print(" ")
                if(new_status == "finished"):
                    ToDo_list.number_of_finished_tasks += 1
                    ToDo_list.number_of_unfinished_tasks -= 1
                elif(new_status == "unfinished"):
                    ToDo_list.number_of_unfinished_tasks += 1
                    ToDo_list.number_of_finished_tasks -= 1
                return
        print(f"{task_name} is not in your list yet")
        print(" ")


#client test
task1 = Task("japanese_lesson", "unfinished", "06/02")
task2 = Task("groceries", "unfinished", "12/02")
task3 = Task("coding_project", "unfinished", "20/05")
my_list = ToDo_list([task1, task2, task3])

my_list.add("shopping", "unfinished", "05/02")
my_list.add("japanese_lesson", "unfinished", "06/02")         #shouldnt add

my_list.update("groceries", "finished", " ")
my_list.update("coding_project", "unfinished", "20/06")
my_list.update("jogging", "unfinished", "05/02")              #shouldnt update




        