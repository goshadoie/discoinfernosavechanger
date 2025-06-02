from tkinter import *
from tkinter import ttk
from tkinter import filedialog as filedialog
import os


root = Tk()
root.geometry("280x330")
root.resizable(width=False, height=False)
root.title("Редактор сохранений")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.iconbitmap("disco.ico")



skill_name_mid = ""
skill_value = 0
isDone = None
global discosave
global array_skill_count


discosave = ""
skill_names = ["Логика", "Энциклопедия", "Риторика", "Драма", "Концептуализация", "Визуальный анализ", "Сила воли", "Внутренняя империя", "Эмпатия", "Авторитет", "Внушение", "Полицейская волна", "Грубая сила", "Электрохимия", "Стойкость", "Сумрак", "Болевой порог", "Трепет", "Координация", "Восприятие", "Скорость реакции", "Эквилибристика", "Техника", "Самообладание", ]
skill_names_code = ['"LOGIC": [', '"ENCYCLOPEDIA": [', '"RHETORIC": [', '"DRAMA": [', '"CONCEPTUALIZATION": [', '"VISUAL_CALCULUS": [', '"VOLITION": [', '"INLAND_EMPIRE": [', '"EMPATHY": [', '"AUTHORITY": [', '"SUGGESTION": [', '"ESPRIT_DE_CORPS": [', '"PHYSICAL_INSTRUMENT": [', '"ELECTROCHEMISTRY": [', '"ENDURANCE": [', '"HALF_LIGHT": [', '"PAIN_THRESHOLD": [', '"SHIVERS": [', '"HE_COORDINATION": [', '"PERCEPTION": [', '"REACTION": [', '"SAVOIR_FAIRE": [', '"INTERFACING": [', '"COMPOSURE": [']



def ask_to_open_file():

    discosave = filedialog.askopenfilename()
    print(discosave)
    print(os.path.basename(discosave))

def show_skill_and_amount_name():
    skill_name_mid = skill_combobox.get()
    skill_value = entry_skill.get()
    array_skill_count = 0
    print(skill_name_mid, skill_value)
    while skill_name_mid != skill_names[array_skill_count]:
        if array_skill_count <= 1:
            array_skill_count += 1
    else:
        change_skill_value(skill_names_code[array_skill_count],skill_value)


def change_skill_value(skill_name, skill_value):

    with open(os.path.basename(discosave), 'r') as file_read, open("discosave.txt", 'w') as file_write:
        lines = file_read.readlines()
        for i, line_name in enumerate(lines):


            if line_name.strip() == skill_name.strip():
                print(i, line_name)
                lines[i + 3] = f'                    "amount": {skill_value},\n'
                file_write.writelines(lines)


                file_write.close()
                file_read.close()
                os.rename(os.path.basename(discosave), f'{discosave} + 1')
                os.rename("discosave.txt", os.path.basename(discosave))







label0_text = ttk.Label(text = "Выбери сохранение")
label0_text.pack(anchor = "center", pady = 20)

file_button = ttk.Button(text = "Выбрать", command = lambda: ask_to_open_file())
file_button.pack(anchor = "center")


label_text1 = ttk.Label(text="Выбери навык")
label_text1.pack(anchor = "center", pady = 20)

skill_combobox = ttk.Combobox(values = skill_names, state = "readonly")
skill_combobox.pack(anchor = "center")

label_text2 = ttk.Label(text="Введи значение навыка")
label_text2.pack(anchor = "center", pady = 10)

entry_skill = ttk.Entry()
entry_skill.pack(anchor = "center")

confirm_button = ttk.Button(text = "Подтвердить", command = show_skill_and_amount_name)
confirm_button.pack(anchor = "center", pady = 40)








root.mainloop()