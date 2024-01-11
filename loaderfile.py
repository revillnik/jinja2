from jinja2 import Template, FunctionLoader, Environment, FileSystemLoader

lod2 = FileSystemLoader("")
env2 = Environment(loader=lod2)

tm2 = env2.get_template("all.htm")
f2 = tm2.render()
print(f2)
