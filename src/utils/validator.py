def is_valid_student_id(student_id):
    for ch in student_id:
        if not (ch.isdigit() or ch == "-"):
            return False
    return True