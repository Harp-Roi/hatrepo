#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, DB_LOCATION, User, Vant, Department, Period, UserVantAccess, UserDepartmentAccess, Report, ReportAccess, Upload, UploadAccess



# Create A Session with my DB_LOCATION
engine = create_engine(DB_LOCATION)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create Records
import jwt
SECRET = 'my_static_secretR'
ALGORITHM = 'HS256'
USER_TABLE = 'users'

def create_user(user_id, password):
    encoded_token = jwt.encode({str(user_id) : str(password)}, SECRET, ALGORITHM)
    return encoded_token

def get_files(path):
    import os
    return os.listdir(path)

def get_users():
    user_query_response = []
    buffer={}
    for x in session.query(User).all():
        buffer= x.__dict__
        del buffer['_sa_instance_state']
        user_query_response.append(buffer)
    return user_query_response


def login_user(user_id, password):
    profile = session.query(User).filter_by(user_id=user_id).first()
    if create_user(user_id,password) == profile.user_token:
        return True
    else:
        return False

def add_department(department_id):
    from datetime import datetime as dd
    new_department = Department(department_id=department_id,created_timestamp = dd.utcnow())
    session.add(new_department)
    session.commit()
    print(session.query(Department).all()[-1].__dict__)


def get_departments():
    department_query_response = []
    buffer={}
    for x in session.query(Department).all():
        buffer= x.__dict__
        del buffer['_sa_instance_state']
        department_query_response.append(buffer)
        print(buffer)
    return department_query_response

def add_user(uid,password):
    new_user = User(user_id=uid,user_token=create_user(uid,password))
    session.add(new_user)
    session.commit()
    print(session.query(User).all()[-1].__dict__)

def flush():
    session.rollback()

if __name__ == '__main__':
    login = ['harp.athwal@Roivant.com','1234']
    add_user(login[0],login[1])
    session.query(User).all()[-1].__dict__
    login = ['john.doe@Roivant.com','12343']
    add_user(login[0],login[1])
    session.query(User).all()[-1].__dict__


