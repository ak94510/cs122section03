# ----------------------------------------------------------------------
# Name:        HW4
# Purpose:     Practice Problems
#
# Date:       2/18/2019
# ----------------------------------------------------------------------


def top_students(students_to_grades, number_of_students = 3):
    """
    Calculate the the top students in a class
    :param students_to_grades: (dictionary) student names to grade
    :param number_of_students: (number) the number of top students to return
    :return: (list) top students
    """
    return sorted(students_to_grades, key=students_to_grades.get, reverse= True)[:number_of_students]

def extra_credit(students_to_grades, extra_credit = 1):
    """
    Calculate new grades with extra credit
    :param students_to_grades: (dictionary) student names to grade
    :param extra_credit: (number) credit to be added to grade
    :return: (dictionary) updated dictionary of students to grade
    with extra credit
    """
    return {student:students_to_grades.get(student)+extra_credit for student in students_to_grades}

def adjusted_grade(students_to_iClicker, students_to_midterm):
    """
    Calculate the adjusted midterm grades of students
    :param students_to_iClicker: (dictionary) student names to iclicker grade
    :param students_to_midterm: (number) student names to midterm grade
    :return: (dictionary) student names to updated grade. Adding one
    point of iclicker grade >= average
    """
    average_iClicker = sum(students_to_iClicker.values())/ \
                       len(students_to_iClicker) if len(students_to_iClicker) \
                        else 1
    with_midterm = {student: students_to_midterm[student]+1 if student in
                    students_to_iClicker and students_to_iClicker[student] >=
                    average_iClicker else students_to_midterm[student] for
                    student in students_to_midterm}
    with_just_iClicker = {student: 1 if students_to_iClicker[student] >= average_iClicker else
                          0 for student in
                          students_to_iClicker}
    return {**with_just_iClicker,**with_midterm}

def sum_of_inverse_odd(number):
    """
    Calculate the sum of the inverse of every odd number up to "number"
    :param number: (number) roof for odd numbers
    :return: (number) sum of inverse of odd numbers
    """
    return sum(1/x for x in range(1,number+1,2))

def same_length(*strings):
    """
    Check if all strings have same length
    :param string: (*string) Any number of Strings
    :return: (bool) True if all strings are same length. False otherwise
    """
    lengths = {len(string) for string in strings}
    if len(lengths) <= 1:
        return True
    return False


def main():
    iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                'Bryan': 2, 'Andrea': 110}
    exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
            'Bryan': 95, 'Andrea': 86}
    print(adjusted_grade({}, {}))

if __name__ == "__main__":
    main()
