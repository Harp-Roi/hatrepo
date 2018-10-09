#!/usr/bin/python

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime

DB_LOCATION = 'sqlite:///sqlite_database_files/tester.db'
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Define columns for the table users
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250))
    user_token = Column(String(250), nullable=False)
    last_login_timestamp =  Column(DateTime,  default=datetime.utcnow)
    created_timestamp = Column(DateTime,  default=datetime.utcnow)

class Vant(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'vants'
    vant_id = Column(String(250))
    created_timestamp = Column(DateTime, nullable=False)

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    department_id = Column(String(250))
    created_timestamp = Column(DateTime, nullable=False)

class Period(Base):
    __tablename__ = 'periods'
    id = Column(Integer, primary_key=True)
    period_id = Column(String(250))
    frequency_id = Column(String(250))
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=False)
    created_timestamp = Column(DateTime, nullable=False)
   
class UserVantAccess(Base):
    __tablename__ = 'users_vants_access'
    id = Column(Integer, primary_key=True)
    # For now, use a concatenation as a key hash function
    users_vants_access_id =  Column(String(500))
    user_id = Column(String(250), ForeignKey('users.user_id'))
    vant_id = Column(String(250), ForeignKey('vants.vant_id'))
    created_timestamp = Column(DateTime, nullable=False)

class UserDepartmentAccess(Base):
    __tablename__ = 'users_departments_access'
    id = Column(Integer, primary_key=True)
    # For now, use a concatenation as a key hash function
    users_departments_access_id =  Column(String(500))
    user_id = Column(String(250), ForeignKey('users.user_id'))
    department_id = Column(String(250), ForeignKey('departments.department_id'))
    created_timestamp = Column(DateTime, nullable=False)

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    # Here we define columns for the table reports.
    report_id = Column(String(250))
    department_id = Column(String(250))
    # Frequency should be = 'Month End', 'Period End', 'Year End' .. etc
    frequency_id = Column(String(250), ForeignKey('periods.frequency_id'))
    created_timestamp = Column(DateTime, nullable=False)
    
class ReportAccess(Base):
    __tablename__ = 'reports_access'
    id = Column(Integer, primary_key=True)
    report_access_id = Column(String(500))
    report_id = Column(String(250), ForeignKey('reports.report_id'))
    user_id = Column(String(250), ForeignKey('users.user_id'))
    access_level = Column(String(250), nullable=False)
    created_timestamp = Column(DateTime, nullable=False)

class Upload(Base):
    __tablename__ = 'uploads'
    id = Column(Integer, primary_key=True)
    upload_id = Column(String(500))
    vant_id = Column(String(250))
    department_id = Column(String(250), ForeignKey('departments.department_id'))
    report_id = Column(String(250), ForeignKey('reports.report_id'))
    period_id = Column(String(250), ForeignKey('periods.period_id'))
    uploader_user_id = Column(String(250), ForeignKey('users.user_id'))
    created_timestamp = Column(DateTime, nullable=False)
    
class UploadAccess(Base):
    __tablename__ = 'uploads_access'
    id = Column(Integer, primary_key=True)
    report_access_id = Column(String(500))
    vant_id = Column(String(250))
    report_id = Column(String(250), ForeignKey('reports.report_id'))
    user_id = Column(String(250), ForeignKey('users.user_id'))
    created_timestamp = Column(DateTime, nullable=False)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine(DB_LOCATION)
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)


# HelpFul Hints
# SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as autoincrement=True
