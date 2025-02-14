class Task:
    number_of_tasks = 0
    number_of_finished_tasks = 0
    number_of_unfinished_tasks = 0

    def __init__(self, name, status, deadline):
        self.name = name
        self.status = status
        self.deadline = deadline
        Task.number_of_tasks += 1
        if(deadline == "finished"):
            Task.number_of_finished_tasks += 1
        else:
            Task.number_of_unfinished_tasks += 1


class ToDo_list:
    def __init__(self, list_of_tasks):
        self.tasks = list_of_tasks[:]
        