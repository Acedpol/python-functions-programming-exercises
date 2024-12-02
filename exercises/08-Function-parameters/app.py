# Your code goes here:
def render_person(name, bday, color_eyes, age, gender):
    final_str = name + " is a " + str(age) + " years old " + gender
    final_str += " born in " + bday + " with " + color_eyes + " eyes"
    return final_str


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))