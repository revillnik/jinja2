from jinja2 import Template, FunctionLoader, Environment, FileSystemLoader

pupil = {"name": "Никита", "age": 20}


def load(x):
    if x == "1":
        return """Меня зовут {{c.name}}, мне {{c.age}}"""
    else:
        return """Такого человека тут нет"""


lod = FunctionLoader(load)
env = Environment(loader=lod)

tm = env.get_template("1")
f = tm.render(c=pupil)
print(f)
