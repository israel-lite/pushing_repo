class Student:
    def __init__(self):
        self.fullname = input("Enter student's full name: ")
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def highest_score(self):
        if self.scores:
            return max(self.scores)
        return None

    def lowest_score(self):
        if self.scores:
            return min(self.scores)
        return None

    def total_score(self):
        return sum(self.scores)

# Example usage:
student = Student()
student.add_score(85)
student.add_score(90)
student.add_score(78)
print("Highest score:", student.highest_score())
print("Lowest score:", student.lowest_score())
print("Total score:", student.total_score())
