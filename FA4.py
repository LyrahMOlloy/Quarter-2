class colorz:
    RED = '\033[91m'
    LUVGREEN = '\033[92m'
    PURPLE = "\033[95m" 
    LUVRESET = "\033[0m"

print(colorz.PURPLE + "Student and Class Average Calculator" + colorz.LUVGREEN)

stud_num = int(input("Enter the number of students: "))
sub_num = int(input("Enter the number of subjects: "))
class_total = 0

for x in range(1, stud_num + 1):
    print("Student", x)
    stud_total = 0
    for y in range(1, sub_num + 1):
        stud_score = float(input("Enter score " + str(y) + ": "))
        stud_total += stud_score
    stud_avg = stud_total/sub_num
    print("Average for student", x," =", stud_avg)
    class_total += stud_avg

class_avg = class_total/stud_num
print("Class Average =", class_avg)
print(colorz.PURPLE + "Thanks for using this program!!!"+ colorz.LUVRESET)