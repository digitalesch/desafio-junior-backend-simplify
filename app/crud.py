from sqlalchemy.orm import Session

import models, schemas

"""
Task CRUD
"""
def create_task(db: Session, user_id: int, task: schemas.TaskCreate):
    if (user := db.query(models.User).filter(models.User.id == user_id).first()):
        return None
    
    task_db = models.Task(

    )

def get_tasks(db: Session, user_id: int, task_id: int = None, skip: int = 0, limit: int = 100):
    if task_id is None:    
        return (
            db
                .query(models.Task)
                .filter(models.Task.owner_id == user_id)
                .offset(skip)
                .limit(limit)
                .all()
        )
    else:
        return (
            db
                .query(models.Task)
                .filter(models.Task.owner_id == user_id)
                .filter(models.Task.id == task_id)
                .all()
        )

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user