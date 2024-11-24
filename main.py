import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os


class FileManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Файловый менеджер")
        self.geometry("600x400")
        self.copied_file = None

        # Кнопки для управления файлами
        open_button = tk.Button(self, text="Открыть файл", command=self.open_file)
        open_button.pack(pady=10)

        copy_button = tk.Button(self, text="Скопировать файл", command=self.copy_file)
        copy_button.pack(pady=10)

        paste_button = tk.Button(self, text="Вставить файл", command=self.paste_file)
        paste_button.pack(pady=10)

        delete_button = tk.Button(self, text="Удалить файл", command=self.delete_file)
        delete_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            messagebox.showinfo("Содержимое файла", content)

    def copy_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.copied_file = file_path
            messagebox.showinfo("Копирование", "Файл скопирован.")

    def paste_file(self):
        if self.copied_file:
            destination_path = os.path.join(os.getcwd(), os.path.basename(self.copied_file))
            shutil.copy(self.copied_file, destination_path)
            messagebox.showinfo("Вставка", "Файл успешно вставлен!")
        else:
            messagebox.showwarning("Ошибка", "Нет скопированного файла.")

    def delete_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            if messagebox.askyesno("Подтверждение удаления", "Вы действительно хотите удалить этот файл?"):
                os.remove(file_path)
                messagebox.showinfo("Удаление", "Файл успешно удалён!")


if __name__ == "__main__":
    app = FileManager()
    app.mainloop()