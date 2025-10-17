#oldstyle % - ultrapassada
name = "Robson"
age = 22
job = "Dev"
language = "Python"

print("Hello, my name is %s. I'm %d years old, working as a %s with %s" %(name, age, job, language)) #1
print("Hello, my name is {}. I'm {} years old, working as a {} with {}".format(name, age, job, language)) #2
print("Hello, my name is {a}. I'm {b} years old, working as a {c} with {d}".format(a = name, b = age, c = job, d = language)) #3 útil para quando as variáveis se repetem no escopo da mensagem

#f-string

print(f"Hello, my name is {name}. I'm {age} years old, working as a {job} with {language}.")

#para números
PI = 3.14159
print(f"{PI:.2f}")
print(f"{PI:.3f}")
print(f"Valor de PI: {PI:.2f}")



