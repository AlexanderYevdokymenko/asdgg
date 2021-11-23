class Student():
    def info(self, name, grade):
        self.name = name
        self.grade = grade

    def return_info(self):
        information = self.name + str(self.grade)
        return information

    grade = {
        'task_max': 100, 'laba_max': 20, 'number_of_lab': 5, 'avtomat': 0.8,
    }

    def number_of_labs(self, attempts, last_mark):
        self.attempts = attempts
        self.last_mark =last_mark
        print('Кількість лабараторних робіт та остання оцінка: ' + str(self.attempts) + ', ' + str(self.last_mark))

    def number_of_tasks(self, attempts, last_mark):
        self.attempts = attempts
        self.last_mark =last_mark
        print('Кількість індивідуальних творчих завдань та остання оцінка: ' + str(self.attempts) + ', ' + str(self.last_mark))

student = Student()
student.info('Sasha, ', 5)
student.number_of_labs( 3, 4)
student.number_of_tasks(6, 5, )
print('Дані студента:', student.return_info())