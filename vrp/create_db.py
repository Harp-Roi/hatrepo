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

def add_user(uid,password):
    new_user = User(user_id=uid,user_token=create_user(uid,password))
    session.add(new_user)
    session.commit()
    print(session.query(User).all()[-1].__dict__)


if __name__ == '__main__':
    session.query(User).all()[-1].__dict__
    login = ['harp.athwal@Roivant.com','1234']
    add_user(login[0],login[1])
    session.query(User).all()[-1].__dict__
    login = ['john.doe@Roivant.com','12343']
    add_user(login[0],login[1])
    session.query(User).all()[-1].__dict__


