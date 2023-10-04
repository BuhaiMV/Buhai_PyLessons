from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres', echo=True)

__session = sessionmaker(bind=engine)
session: Session = __session()

print(session.get())
#session.add({'age': 18, 'first_name': 'test'})
