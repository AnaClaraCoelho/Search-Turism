from ..models import Todo


def add_todo(city, touristSpot, description, url_image):
    todo = Todo(city=city, tourist_spot= touristSpot, description=description, url_image=url_image)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    return [todo.to_dict_json() for todo in todos]

def delete_todo(id):
    todo = Todo.objects.filter(id=id["id"]).delete()
    return {"delete_item": id}

# def edit_todo(id):
#     todo_update = Todo.objects.filter(id=id)
#     return todo_update.to_dict_json()