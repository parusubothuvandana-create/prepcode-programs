students = int(input("enter the students: "))
bench = int(input("eneter the number of students: "))

total_benches = students // bench
remaining_students = students % bench

print(f"total_benches ={total_benches}")
print(f"remaining_students ={remaining_students}")
