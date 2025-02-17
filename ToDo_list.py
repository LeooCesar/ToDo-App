class Task:

    def __init__(self, name, status, deadline):
        self.name = name
        self.status = status
        self.deadline = deadline
        Task.number_of_tasks += 1

    def __str__(self):
        return f"Name: {self.name}, Status: {self.status}, Deadline: {self.deadline}"

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
        return
        

    def add(self, task_name, task_status, task_deadline):
        #this method adds a new task to Todo_list
        new_task = Task(task_name, task_status, task_deadline)
        for task in self.tasks:
            if (new_task.name == task.name):
                print(f"{task.name} is already on your list. If you want to change some information about {task.name}, use the function update")
                print(" ")
                return
        self.tasks.append(new_task)
        if(new_task.status == "finished"):
                ToDo_list.number_of_finished_tasks += 1
        else:
            ToDo_list.number_of_unfinished_tasks += 1
        print(f"{new_task} is now on your list")
        print(" ")
        return

    def update(self, task_name, new_status, new_deadline):
        #this method update a task that already is in Todo_list
        for task in self.tasks:
            if(task.name == task_name): 
                if(task.status != new_status):
                    print(f"{task.name} is now {new_status}")
                task.status = new_status
                print(task.status)
                print(new_status)
                print(new_status == "finished")
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
        return

    
    def show(self):
        print(f"You have {ToDo_list.number_of_finished_tasks} finished tasks")          
        print(f"YOu have {ToDo_list.number_of_unfinished_tasks} unfinished tasks")
        print(" ")
        print(f"These are the tasks on the current list:")
        for task in self.tasks:
            print(task)
        print(" ")
        return

    def delete(self, remove_task_name):
        for task in self.tasks:
            if (remove_task_name == task.name):
                if(task.status == "finished"):
                    ToDo_list.number_of_finished_tasks -= 1
                else:
                    ToDo_list.number_of_unfinished_tasks -= 1
                self.tasks.remove(task)
                print(f"{remove_task_name} was removed from your tasks")
                print(" ")
                return
        print(f"{remove_task_name} can't be removed because it's not in your tasks")
        print(" ")
        return




#client test
task1 = Task("japanese_lesson", "unfinished", "06/02")
task2 = Task("groceries", "unfinished", "12/02")
task3 = Task("coding_project", "unfinished", "20/05")
my_list = ToDo_list([task1, task2, task3])

my_list.add("shopping", "unfinished", "05/02")
my_list.add("japanese_lesson", "unfinished", "06/02")         #shouldnt add

my_list.update("groceries", "finished", "05/02")
my_list.update("coding_project", "finished", "20/06")
my_list.update("jogging", "unfinished", "05/02")              #shouldnt update

my_list.show()

my_list.delete("groceries")   
my_list.delete("homework")  
my_list.show()          #without groceries




        