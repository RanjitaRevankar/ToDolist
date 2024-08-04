import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("!!To-Do List Application!!")
        
        self.tasks = []
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.update_button = tk.Button(root, text="Update Selected Task", width=48, command=self.update_task)
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Selected Task", width=48, command=self.delete_task)
        self.delete_button.pack(pady=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning!!", "You must enter a task.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks[selected_task_index[0]] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning!!", "You must enter a task.")
        else:
            messagebox.showwarning("Warning!!", "You must select a task to update.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning!!", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
