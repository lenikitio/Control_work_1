import json
import os
import time


def create_note(file_name: str) -> list:
      path = f"{file_name}.json"
      if os.path.isfile(path) == False:
            return []
      else:
            print("Такой файл уже существует")
            return ["error"]

def work_with_note(file_name: str) -> list:
      path = f"{file_name}.json"
      if os.path.isfile(path) == True:
            with open(path, 'r', encoding= 'utf-8') as data:
                  # Проверяем есть ли что-то в файле
                  if os.stat(path).st_size > 0:
                        return eval(data.read())
                  else:
                        return []
                  # Функция eval() выполняет код в строке, тут она иницилизирует лист словарей
                  
      else:
            print("Такого файла не существует")
            return ["error"]
            

def add_note(body: list, name: str, text: str):
      id = len(body) + 1
      modif_time = time.ctime(time.time())
      new_record = {"id": id,"name": name, "time_edit" : modif_time, "text" : text}
      body.append(new_record)

def search_note(body: list, name: str) -> dict:
      result = []
      for dict in body:
            if dict.get("name") == name:
                  result.append(dict)
      if len(result) > 1:
            print("Найдено несколько заметок с таким именем, их id: ")
            for dict in result:
                  print(f"{dict["id"]} ")
            id = int(input("Введите нужный вам id: "))
      elif len(result) == 1:
            id = result[0]["id"]
      elif len(result) == 0:
            print("Такой заметки нет")
            return 0
      return body[id - 1]


def edit_note(body: list, name: str):
      edit_elem = search_note(body, name)
      if edit_elem == 0:
            return
      text = input("Введите новый текст замекти: ")
      modif_time = time.ctime(time.time())
      edit_elem.update(
                  {"time_edit" : modif_time,
                   "text" : text
                  }
            )

            
def delete_note(body: list, name: str):
      delete_elem = search_note(body, name)
      if delete_note == 0:
            return
      body.remove(delete_elem)

def show_note(body: list, name: str):
      show_elem = search_note(body, name)
      if delete_note == 0:
            return
      print(show_elem)

def all_show_note(body: list):
      for dict in body:
            print(dict)

def sort_note(body: list, mode: int):
      if mode == 1:
            body.sort(key = lambda x : x["time_edit"])
      elif mode == 2:
            body.sort(key = lambda x : x["id"])
      else :
            print("Такой сортировки у нас нет")
            return

def save_note(file_name: str, body: list):
      path = f"{file_name}.json"
      with open(path, 'w', encoding= 'utf-8') as data:                      
            data.write(json.dumps(body, indent= 4, ensure_ascii=False))     

print("Список команд для работы с приложением: " 
      + "\n create - создать новый файл заметок"
      + "\n work - работать с существующим файлом заметок"
      + "\n stop - остановаить программу"     
      + "\n      add - дополнить заметку" 
      + "\n      edit - редактировать заметку"
      + "\n      delete - удалить заметку" 
      + "\n      show - вывести заметку"
      + "\n      all - вывести все заметки"
      + "\n      sort - отсортировать заметки"
      + "\n      save- сохранить изменения в файл"
      + "\n      back - закончить изменения файла")

flag = True
work = True
id = 1
while flag == True:
      body = ["error"]
      file_name = ""
      match input("Начнём работу: "):
            case "create":
                  file_name = input("Введите название файла заметок: ")
                  body = create_note(file_name)
            case "work":
                  file_name = input("В какой файл хотите внести изменения: ")
                  body = work_with_note(file_name)
            case "stop":
                  flag = False
      if len(body) == 0 or body[0] != "error":
            while work == True:
                  match input("Что будем делать с файлом: "):
                        case "add":
                              name = input("Название новой заметки: ")
                              text = input("Текст новой заметки: ")
                              add_note(body, name, text)
                        case "back":
                              work = False
                        case "edit":
                              name = input("Название заметки, текст которой хотите изменить: ")
                              edit_note(body, name)
                        case "delete":
                              name = input("Название заметки, которую хотите удалить: ")
                              delete_note(body, name)
                        case "show":
                              name = input("Название заметки, которую хотите вывести: ")
                              show_note(body, name)
                        case "all":
                              all_show_note(body)
                        case "sort":
                              mode = int(input("Отсротируем по 1 - дате изменения или 2 - по id?"
                                               +"\n Введите соответстующию цифру: "))
                              sort_note(body, mode)
                        case "save":
                              save_note(file_name, body)
                              print("Сохранено")
                              
            




