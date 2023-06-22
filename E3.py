def grade(name, math, english, science):
    average = (math + english + science) / 3
    print(name, "'s grades (Math =", math, "| English =", english, "| Science =", science, ") and the average is", average)


grade("John", 13, 12, 99)
grade("Ana", 61, 59, 33)
grade("Frank", 22, 90, 69)