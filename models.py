class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class Course:
    def __init__(self, course_id, title, description):
        self.course_id = course_id
        self.title = title
        self.description = description

class Enrollment:
    def __init__(self, enrollment_id, user, course):
        self.enrollment_id = enrollment_id
        self.user = user
        self.course = course

class Lesson:
    def __init__(self, lesson_id, course, title, content):
        self.lesson_id = lesson_id
        self.course = course
        self.title = title
        self.content = content

class Quiz:
    def __init__(self, quiz_id, lesson, questions):
        self.quiz_id = quiz_id
        self.lesson = lesson
        self.questions = questions

class Assignment:
    def __init__(self, assignment_id, lesson, title, description):
        self.assignment_id = assignment_id
        self.lesson = lesson
        self.title = title
        self.description = description

class Discussion:
    def __init__(self, discussion_id, course, title):
        self.discussion_id = discussion_id
        self.course = course
        self.title = title