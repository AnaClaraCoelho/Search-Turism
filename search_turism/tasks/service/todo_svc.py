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

def edit_todo(id, city, tourist_spot, description, url_image):
    todo_update = Todo.objects.get(id=id)
    todo_update.city = city
    todo_update.tourist_spot = tourist_spot
    todo_update.description = description
    todo_update.url_image= url_image
    todo_update.save()