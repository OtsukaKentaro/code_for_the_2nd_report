# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。
def find_smartest_student(students):
    top_score = 0
    top_student = ""
    for student in students:
        avg, total = calc_student_score(student)
        if total > top_score:
            top_score = total
            top_student = student
        print(f"Student: {student}, Total: {total}, Average: {avg}")
    return top_student, top_score


def calc_student_score(student) -> tuple[float | int, int]:
    total = 0
    count = 0
    for score in student:
        total += score
        count += 1
    avg = total / count
    return avg, total


students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = find_smartest_student(students)
print(f"Best student: {top_student} with total score: {top_score}")