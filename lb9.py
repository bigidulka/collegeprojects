import tkinter as tk
from tkinter import messagebox
import sqlite3

class Group:
    def __init__(self, teacher, name):
        self.teacher = teacher
        self.name = name
        self.students = []

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Информационное приложение")
        self.create_widgets()
        self.groups = []
        self.load_groups_from_database()
        self.selected_group_index = None

    def create_widgets(self):
        self.groups_frame = tk.Frame(self.root)
        self.groups_frame.pack(side=tk.LEFT, padx=10)
        self.teacher_label = tk.Label(self.groups_frame, text="Учитель:")
        self.teacher_label.pack()
        self.teacher_entry = tk.Entry(self.groups_frame)
        self.teacher_entry.pack()
        self.group_name_label = tk.Label(self.groups_frame, text="Название группы:")
        self.group_name_label.pack()
        self.group_name_entry = tk.Entry(self.groups_frame)
        self.group_name_entry.pack()
        self.add_group_button = tk.Button(self.groups_frame, text="Добавить группу", command=self.add_group)
        self.add_group_button.pack()
        self.listbox = tk.Listbox(self.groups_frame, width=30)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_group_select)

        self.students_frame = tk.Frame(self.root)
        self.students_frame.pack(side=tk.LEFT, padx=10)
        self.students_label = tk.Label(self.students_frame, text="Ученики:")
        self.students_label.pack()
        self.students_text = tk.Text(self.students_frame, height=10, width=30, state='disabled')
        self.students_text.pack()
        self.add_student_label = tk.Label(self.students_frame, text="Добавить ученика:")
        self.add_student_label.pack()
        self.add_student_entry = tk.Entry(self.students_frame)
        self.add_student_entry.pack()
        self.add_student_button = tk.Button(self.students_frame, text="Добавить", command=self.add_student)
        self.add_student_button.pack()

    def save_groups_to_database(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY,
                teacher TEXT,
                name TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                group_id INTEGER,
                name TEXT,
                FOREIGN KEY (group_id) REFERENCES groups (id)
            )
        """)
        cursor.execute("DELETE FROM groups")
        cursor.execute("DELETE FROM students")
        for group in self.groups:
            cursor.execute("INSERT INTO groups (teacher, name) VALUES (?, ?)", (group.teacher, group.name))
            group_id = cursor.lastrowid
            for student in group.students:
                cursor.execute("INSERT INTO students (group_id, name) VALUES (?, ?)", (group_id, student))
        conn.commit()
        conn.close()

    def load_groups_from_database(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='groups'")
        table_exists = cursor.fetchone()
        if not table_exists:
            self.save_groups_to_database()
        else:
            cursor.execute("SELECT id, teacher, name FROM groups")
            rows = cursor.fetchall()
            for row in rows:
                group_id = row[0]
                teacher = row[1]
                name = row[2]
                group = Group(teacher, name)
                cursor.execute("SELECT name FROM students WHERE group_id=?", (group_id,))
                students = cursor.fetchall()
                for student_row in students:
                    student = student_row[0]
                    group.students.append(student)
                self.groups.append(group)
                self.listbox.insert(tk.END, f"{name} - {teacher}")
        conn.close()

    def add_group(self):
        teacher = self.teacher_entry.get()
        group_name = self.group_name_entry.get()
        if not teacher or not group_name:
            messagebox.showerror("Ошибка", "Введите имя учителя и название группы")
            return
        for group in self.groups:
            if group.teacher == teacher and group.name == group_name:
                messagebox.showerror("Ошибка", "Группа с таким учителем и названием уже существует")
                return
        group = Group(teacher, group_name)
        self.groups.append(group)
        self.listbox.insert(tk.END, f"{group_name} - {teacher}")
        self.teacher_entry.delete(0, tk.END)
        self.group_name_entry.delete(0, tk.END)
        self.save_groups_to_database()

    def add_student(self):
        if self.selected_group_index is None:
            messagebox.showerror("Ошибка", "Выберите группу")
            return
        group = self.groups[self.selected_group_index]
        student = self.add_student_entry.get()
        if not student:
            messagebox.showerror("Ошибка", "Введите имя ученика")
            return
        student_number = len(group.students) + 1
        group.students.append(student)
        self.students_text.config(state='normal')
        self.students_text.insert(tk.END, f"{student_number}. {student}\n")
        self.students_text.config(state='disabled')
        self.add_student_entry.delete(0, tk.END)
        self.save_groups_to_database()

    def on_group_select(self, event):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.selected_group_index = None
            return
        selected_index = selected_index[0]
        self.students_text.config(state='normal')
        self.students_text.delete("1.0", tk.END)
        group = self.groups[selected_index]
        for i, student in enumerate(group.students, start=1):
            self.students_text.insert(tk.END, f"{i}. {student}\n")
        self.students_text.config(state='disabled')
        self.add_student_entry.delete(0, tk.END)
        self.selected_group_index = selected_index

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.run()