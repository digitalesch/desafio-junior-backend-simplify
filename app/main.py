from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud, models, schemas
from database import engine, get_db_connection

models.Base.metadata.create_all(bind=engine)

description = """
# ToDo List API lets you create users and task as simple endpoints.

## Users
API defines two endpoints for users:
* **List users**
- [GET] "/users/{user_id}": lets you search the database for a specific user_id, and if not found, returns the appropriate message!
* **Create users**
- [POST] "/users": lets you create a new user, and if the same email is registered in the database, returns the appropriate message!

## Tasks
* **List tasks**
    - [GET] "/tasks/{user_id}": lets you search the database for a specific user_id or by user_id and task_id (if task_id is provided in request body), and if not found, returns the appropriate message!
* **Create users**
    - [POST] "/tasks/{user_id}": lets you create a new task, bound to a user_id, and if the user is not found, returns the appropriate message!
* **Update task**
    - [PUT] "/tasks/{user_id}/{task_id}": lets you modify a task, bound to a user_id, and if the user / task is not found, returns the appropriate message!
"""

app = FastAPI(
    title="ToDoApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="1.0.0",
)

"""
Task routes
"""
@app.get("/tasks/{user_id}", response_model=list[schemas.Task],tags=['Task'])
def read_user(user_id: int, task_id: int | None = None, db: Session = Depends(get_db_connection)):
    if (task := crud.get_tasks(db, task_id=task_id, user_id=user_id)) is None:
        raise HTTPException(status_code=404, detail="Task / User not found")
    return task

@app.post("/tasks/{user_id}", response_model=schemas.TaskCreate, tags=['Task'])
def create_task(user_id: int, task: schemas.TaskBase, db: Session = Depends(get_db_connection)):
    if (db_user := crud.get_user(db, user_id=user_id)) is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if db_user.is_active:
        created_task = models.Task(
            **task.dict(),
            is_done = False,
            owner_id = user_id,
        )

        db.add(created_task)
        db.commit()

        return created_task
    else:
        raise HTTPException(status_code=404, detail="User is inactive!")


@app.put("/tasks/{user_id}/{task_id}", response_model=schemas.TaskCreate, tags=['Task'])
def update_task(user_id: int, task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db_connection)):
    returned_task = crud.get_tasks(db, task_id=task_id, user_id=user_id)

    if not len(returned_task):
        raise HTTPException(status_code=404, detail="Task / User not found")
    
    #returned_task.
    update_task = returned_task[0]

    for k,v in task.dict().items():
        print(k,v)
        setattr(update_task, k, v)

    db.commit()

    return update_task
"""
User routes
"""
@app.get("/users/{user_id}", response_model=schemas.User,tags=['User'])
def read_user(user_id: int, db: Session = Depends(get_db_connection)):
    if (db_user := crud.get_user(db, user_id=user_id)) is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/", response_model=schemas.User,tags=['User'])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_connection)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    returned_user = crud.create_user(db=db, user=user)
    
    return returned_user