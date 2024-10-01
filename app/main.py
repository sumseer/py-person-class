class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]

    return person_list
