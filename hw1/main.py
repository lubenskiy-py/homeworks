from fastapi import FastAPI

app = FastAPI()

list_with_names = []

@app.get("/add-user-name")
def add_user_name(user_name:str):
    if user_name in list_with_names:
        return {"message":"this name is already on the list"}
    else:
        list_with_names.append(user_name)
    return {"message":"your name add"}

@app.get("/print-user-name")
def print_names():
    return {"names":list_with_names}

@app.get("/delete-user-name")
def delete_user_name(user_name_for_delete:str):
    if user_name_for_delete in list_with_names:
        list_with_names.remove(user_name_for_delete)
        return {"message":"username delete"}
    else:
        return {"message":"name not found"}
