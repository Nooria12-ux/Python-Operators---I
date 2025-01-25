print("Enter Marks Obtained in 4 Subjects")
math = int(input("maths : "))
english = int(input("english : "))
science = int(input("science : "))
bangla = int(input("bangla : "))

sum = math + english + science + bangla
print(f"Total Marks Obtained : {sum}")
perc = (sum/400)*100
print(f"Percentage Mark = {perc}")