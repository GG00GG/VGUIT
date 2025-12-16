# Вариант 5: Rust

import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

def fetch_repo_owner_info():
    repo_input = entry.get().strip()
    if not repo_input:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите имя репозитория")
        return
      
    api_url = f"https://api.github.com/repos/{repo_input}"
    
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 404:
            messagebox.showerror("Ошибка", "Репозиторий не найден. Проверьте правильность ввода.")
            return
        elif response.status_code != 200:
            messagebox.showerror("Ошибка", f"Ошибка GitHub API: {response.status_code}")
            return

        repo_data = response.json()
        owner_data = repo_data.get('owner', {})

        info = {
            'company': owner_data.get('company'),
            'created_at': owner_data.get('created_at'),
            'email': owner_data.get('email'),
            'id': owner_data.get('id'),
            'name': owner_data.get('login'),
            'url': owner_data.get('url')
        }

        safe_name = repo_input.replace('/', '_')
        output_filename = f"Zolotarev_Ilya_Ruslanovich_U-254_vivod.txt"

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Успех", f"Данные сохранены в файл:\n{os.path.abspath(output_filename)}")
        
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Ошибка", "Нет подключения к интернету.")
    except requests.exceptions.Timeout:
        messagebox.showerror("Ошибка", "Превышено время ожидания ответа от GitHub.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{str(e)}")

root = tk.Tk()
root.title("GitHub Repo Info — Zolotarev Ilya Ruslanovich (U-254)")
root.geometry("500x180")
root.resizable(False, False)

tk.Label(root, text="Введите имя репозитория (owner/repo):", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=50, font=("Arial", 11))
entry.pack(pady=5)
entry.insert(0, "rust-lang/rust")

tk.Button(root, text="Получить информацию", command=fetch_repo_owner_info, font=("Arial", 11), bg="#4CAF50", fg="white").pack(pady=15)

tk.Label(root, text="Пример: rust-lang/rust, kubernetes/kubernetes", font=("Arial", 9), fg="gray").pack()

root.mainloop()
