from jinja2 import Template

class Person:
	def __init__(self, age, name):
		self.age = age
		self.name = name
per = Person(25, 'Nikita')
x = Template('Меня зовут {{p.name}}, возраст: {{p.age}}')
y = x.render(p = per)
print(y)

