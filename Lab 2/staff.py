import json


class Person:

    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def __str__(self):
        return f"Person fullname: {self.fullname}," \
               f" age: {self.age}"

    def __repr__(self):
        return f"Person(fullname={self.fullname}," \
               f" age={self.age})"

    def save(self, json_filepath: str):
        to_json = {
            "fullname": self.fullname,
            "age": self.age,
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)

    def load(self, json_filepath: str):
        with open(json_filepath) as file:
            obj = json.load(file)
            self.fullname = obj["fullname"]
            self.age = obj["age"]


class Employee(Person):

    def __init__(self, fullname, age, position):
        super().__init__(fullname, age)
        self.position = position

    def __str__(self):
        return f"Employee fullname: {self.fullname}," \
               f" age: {self.age}," \
               f" position: {self.position}"

    def __repr__(self):
        return f"Employee(fullname={self.fullname}," \
               f" age={self.age}," \
               f" position={self.position})"

    def reposition(self, new_position):
        self.position = new_position

    def save(self, json_filepath: str):
        to_json = {
            "fullname": self.fullname,
            "age": self.age,
            "position": self.position
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)

    def load(self, json_filepath: str):
        with open(json_filepath) as file:
            obj = json.load(file)
            self.fullname = obj["fullname"]
            self.age = obj["age"]
            self.position = obj["position"]
