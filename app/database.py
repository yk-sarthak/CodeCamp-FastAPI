from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


sqlalchemy_database_url=f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine=create_engine(sqlalchemy_database_url)

sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

## RAW SQL CONNECTION

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='Codecamp Fastapi',user='postgres',password='Sarthak@2403',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("error",error)
#         time.sleep(3)
