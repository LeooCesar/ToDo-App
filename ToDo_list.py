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

    def __init__(self, list_of_tasks):
        self.tasks = list_of_tasks[:]
        for task in self.tasks:
            if(task.status == "finished"):
                ToDo_list.number_of_finished_tasks += 1
            else:
                ToDo_list.number_of_unfinished_tasks += 1

    @classmethod
    def add(self, task_name, task_status, task_deadline):
        #this method adds a new task to Todo_list
        new_task = Task(task_name, task_status, task_deadline)
        for task in self.tasks:
            if (new_task.name == task.name):
                print(f"{task.name} is already on your list")
                print(f"if you want to change some information about {task.name}, use the function update")
        self.tasks.append(new_task)

    @classmethod
    def update(self, task_name, new_status):
        for task in self.tasks:
            if(task.name == task_name): 
                task.status = new_status
                print(f"{task.name} is now {task.status}")
                if(new_status == "finished"):
                    ToDo_list.number_of_finished_tasks += 1
                    ToDo_list.number_of_unfinished_tasks -= 1
                elif(new_status == "unfinished"):
                    ToDo_list.number_of_unfinished_tasks += 1
                    ToDo_list.number_of_finished_tasks -= 1
                return
        print("This task is not in your list yet")

    

        