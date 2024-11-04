import requests
import tkinter as tk

color = ""
URL = 'http://127.0.0.1:5000/api/randomcolor'

def change_color():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        global color
        color = data["color"]
        root.configure(bg=color)
    else:
        print("failed to receive data:", response.status_code)
        

root = tk.Tk()
root.title("Color")
root.geometry("400x300")

tk.Button(root, text="Change Color", command=change_color).pack()


root.mainloop()
