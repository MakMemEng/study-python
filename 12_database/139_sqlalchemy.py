import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext import declarative

engine = sqlalchemy.create_engine("sqlite:///test_sqlite2", echo=True)
# engine = sqlalchemy.create_engine("sqllite:///:memory:", echo=True)

Base = declarative.declarative_base()


class Person(Base):
    __tablename__ = "persons"
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name="Mike")
session.add(p1)
p2 = Person(name="Nancy")
session.add(p2)
p3 = Person(name="Jun")
session.add(p3)
# person = Person(name="Mike")
# session.add(person)
session.commit()

p4 = session.query(Person).filter_by(name="Mike").first()
p4.name = "Michel"
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name="Nancy").first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
