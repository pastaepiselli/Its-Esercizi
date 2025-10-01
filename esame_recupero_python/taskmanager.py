class TaskManager:  
    def __init__(self) -> None:
        self.tasks = {}

    def create_task(self, task_id: str, descrizione: str) -> dict | str:
        if task_id in self.tasks:
            return "Errore: task esiste gia"
        self.tasks[task_id] = {'descrizione': descrizione, 'completato': False}
        return {task_id: {'descrizione': descrizione, 'completato': False}}
    
    def complete_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]['completato'] = True
        return {task_id: self.tasks[task_id]}
    
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]['descrizione'] = nuova_descrizione
        return {task_id: self.tasks[task_id]}

    def remove_task(self, task_id) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        task_rimosso = self.tasks.pop(task_id)
        return {task_id: task_rimosso}

    def list_tasks(self) -> list[str]:
        return [self.tasks.keys()]

    def get_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        return self.tasks[task_id]

a = []
for i in range(10):
    for f in range(4):
        if f == 1:
            break
    else:
        print('sono nel break')
