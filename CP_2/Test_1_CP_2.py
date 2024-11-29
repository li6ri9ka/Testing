import pandas as pd

def calculatingTheArithmeticMean(dataFrame):
    averageValue = ["test1","test2","test3","test4"]
    dataFrame['Average'] = dataFrame[averageValue].mean(axis=1)

    grade_ranges = {
        'A+': (97, 100),
        'A': (93, 96),
        'A-': (90, 92),
        'B+': (87, 89),
        'B': (83, 86),
        'B-': (80, 82),
        'C+': (77, 79),
        'C': (73, 76),
        'C-': (70, 72),
        'D+': (67, 69),
        'D': (63, 66),
        'D-': (60, 62),
        'F': (0, 59)
    }

    def get_grade(average):
        for grade, (min, max) in grade_ranges.items():
            if min <= average <= max:
                return grade
        return 'F'


    dataFrame['CalculatedGrade'] = dataFrame['Average'].apply(get_grade)


    return dataFrame


def test_comparison_of_ratings():
    dataFrame = pd.read_csv('/Users/li6ri9ka/PycharmProjects/pytest/src/grades.csv')
    dataFrame = calculatingTheArithmeticMean(dataFrame)
    errors = []

    for index, row in dataFrame.iterrows():
        if row[('Grade')] != row['CalculatedGrade']:
            errors.append(index)

    if errors:
        for error in errors:
            print(error)
        assert False
