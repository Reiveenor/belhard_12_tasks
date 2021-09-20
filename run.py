import datetime

from sqlalchemy import asc

from db import session_scope, tables

with session_scope() as session:
    # add few new person in bd
    def add_person(name: str, surname: str, birth_date=datetime.datetime.now()):
        person = tables.Person()
        person.name = name
        person.surname = surname
        person.birth_date = birth_date
        session.add(person)
        session.commit()
        session.refresh(person)
        return session.query(tables.Person.name).all()

    # sort by name asc
    def asc_sort():
        result = session.query(tables.Person.name) \
            .order_by(asc(tables.Person.name)) \
            .all()
        return result

    # delete row by name
    def del_row(name):
        result = session.query(tables.Person).filter(tables.Person.name == name).all()
        print(result)
        if len(result) > 0:
            session.query(tables.Person).filter(tables.Person.name == name).delete()
            session.commit()
        else:
            return "BD hasn't this name"
        return session.query(tables.Person.name).all()

    # # добавление какому то логину какой то любимый фильм
    # person = session.query(tables.Person).first()
    # user = session.query(tables.User).first()
    # film = tables.Film()
    # film.duration = 123
    # film.name = "Best Film"
    # film.raiting = 9.8
    # film.director_id = person.id
    # film.release_date = datetime.datetime.now()
    # session.add(film)
    # session.commit()
    # session.refresh(film)
    # user.favorite_films.append(film)
    # session.commit()

if __name__ == '__main__':
    # print(add_person("Ignat", "Oksimchik"))
    # print(add_person("Vasyan", "Strelnikov"))
    # print(add_person("Ignatarius", "Petrov"))
    # print(add_person("Olga", "Nabokova"))
    print(asc_sort())
    # print(del_row("sdfgsdf"))
    # print(del_row("Vasyan"))
