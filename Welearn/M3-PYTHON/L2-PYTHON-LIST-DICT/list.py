# students = ["alice","javi","damien"]
# students.append("delilah")
# print(students)
#
# students = ["alice","javi","damien"]
# students.insert(1,"zoe")
# print(students)
#
# students = ["alice","javi","damien","javi"]
# students.remove("javi")
# print(students)
#my_list.insert(index,element)

smith_siblings = ["emily","monique","giovani","sonny","bean","erin"]
for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"
    print(smith_siblings)
# for name in smith_siblings:
#     print(name + " Smith")
# print(len(smith_siblings))
super_heroes = ["captain Msrvel","wonder woman","storm","kamala khan","bumblebee","jessica jones"]


print(super_heroes)
demoted_hero = str(raw_input("what superhero do you want to eliminate from the top 5 ?    "))
if demoted_hero in super_heroes:
    super_heroes.remove(demoted_hero)
    print("top 5 super_heroes:" ,superheroes )
else:
    print("hero not found.   ")
