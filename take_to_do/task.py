class Task:
    def __init__(self, task_id, title, done):
        self.id = task_id
        self.title = title
        self.done = done

    def __str__(self):
        if self.done == 1:
            status = "✓"
        else:
            status = " "
        return f"{self.id}. {self.title} [{status}]"
