from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

engine = create_engine('sqlite:///:memory:', echo = False)
Base = declarative_base()

class Competition(Base):
    __tablename__ = 'Competition'
    competition_id = Column(Integer, primary_key = True)
    competition_name = Column(String)
    world_record = Column(String)
    set_date = Column(String)
    def __init__(self, competition_name, world_record, set_date):
        self.competition_name = competition_name
        self.world_record = world_record
        self.set_date = set_date
    def __repr__(self):
        return "An item has a current record: {}. That's happened in {}".format(self.world_record, self.set_date)


class Sportsman(Base):
    __tablename__ = 'Sportsman'
    sportsman_id = Column(Integer, primary_key = True)
    sportsman_name = Column(String)
    rank = Column(String)
    year_of_birth = Column(String)
    personal_record = Column(String)
    country = Column(String)
    def __init__(self, sportsman_name, rank, year_of_birth, personal_record, country):
        self.sportsman_name = sportsman_name
        self.rank = rank
        self.year_of_birth = year_of_birth
        self.personal_record = personal_record
        self.country = country
    def __repr__(self):
        return "The sportsman named {} and born in {} has a rank {}. His personal record: {}. His motherland is {}.".format(self.sportsman_name, self.year_of_birth, self.rank, self.personal_record, self.country)


class Result(Base):
    __tablename__ = 'Result'
    competition_id = Column(Integer, primary_key = True)
    sportsman_id = Column(Integer, primary_key = True)
    _result = Column(String)
    city = Column(String)
    hold_date = Column(String)
    def __init__(self, _result, city, hold_date):
        self._result = _result
        self.city = city
        self.hold_date = hold_date
    def __repr__(self):
        return "The event had happened on {} in {}. Final result was {}".format(self.hold_date, self.city, self._result)


Session = sessionmaker(bind = engine)
session = Session()

long_leaps = Competition('long_leaps', '12m', '15.05.2010')
push_ups = Competition('push-ups', '43 thousand times', '12.05.2010')
high_leaps = Competition('high_leaps', '2.8', '25.04.2005')
timing_backflips = Competition('timing_backflips', '0.8', '03.08.1995')
chestpress = Competition('chestpress', '380kg', '07.05.2002')

session.add(long_leaps)
session.add(push_ups)
session.add(high_leaps)
session.add(timing_backflips)
session.add(chestpress)

peter = Sportsman('Peter', 4, '1977', 'The longest leap', 'Scotland')
collins = Sportsman('Collins', 2, '1990', 'Number of pushups', "Portugal")
damian = Sportsman('Damian', 3, '1979', 'The leap for 2.0m', 'France')
kate = Sportsman('Kate', 1, '1992', 'backflip in 1.5 sec', 'Poland')
felix = Sportsman('Felix', 4, '1990', 'chestpress for 210kg', 'Latvia')

session.add(peter)
session.add(collins)
session.add(damian)
session.add(kate)
session.add(felix)

L = Result('6.8m', 'L.A', '05.05.2012')
new_york = Result('12 thousand times', 'New-York', 'Lissabon')
lissabon = Result('1.9m', 'Lissabon', '13.02.2002')
sophia = Result('1.8 sec', 'Sophia', '23.03.2010')
rio = Result('179kg', 'Rio-de-Janeiro', '17.09.2007')

session.add(L)
session.add(new_york)
session.add(lissabon)
session.add(sophia)
session.add(rio)

task1 = session.query(Competition).filter_by(competition_name = push_ups)
print(task1)
task2 = session.query(Result).filter_by(_result = '1.8 sec')
print(task2)
task3 = session.query(Sportsman).filter_by(rank = 1)
print(task3)