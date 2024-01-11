from jinja2 import Template  # , escape


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name


per = Person(25, "Nikita")
x = Template("Меня зовут {{p.name}}, возраст: {{p.age}}")
y = x.render(p=per)
print(y)

cities = ["Москва", "Белогор", "Новгород"]
s = """Города:
{% for i in cities -%}
{% if i == 'Москва' -%}
{{i}}
{% elif i == 'Новгород' -%}
{{i}}
{% else -%}
Это не Москва и не Новгород
{% endif -%}
{% endfor -%}"""
x = Template(s)
y = x.render(cities=cities)
print(y)

# s = """https://www.youtube.com/watch?v=F63wc5nPdho&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=2"""
# f = escape(s)
# print(f)

person = [
    {"name": "Никита", "age": 25},
    {"name": "Володя", "age": 28},
    {"name": "Ася", "age": 2},
]

s = """
{%- macro pupil(x) -%}
{%- for i in x %}
{{i.name}}{{caller(i)}}
{%- endfor -%}
{%- endmacro -%}

{% call(user) pupil(p) %}
{{user.age}}
{% endcall -%}

"""
t = Template(s)
f = t.render(p=person)
print(f)
