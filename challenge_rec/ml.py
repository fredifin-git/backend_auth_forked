"""
Student Table:
| studentId | teacherId | strongPoints | weakPoints |

Challenge History Table:
| studentId | challengeId | status | timestamp |

Challenge Description Table:
| challengeId | challengeDescription |

"""

from django.db import connection
import csv
from utils.split_database import SplitDatabase
from item_recommendation.user_attribute_knn import UserAttributeKNN
from item_recommendation.user_attribute_knn import UserKNN

"""
# Test run for csv writer using small lists.
students_1 = ((1, (0, 1, 5, 1, 0, 3), (4, 0, 3, 0)), (2, (5, 5, 1, 5, 1, 3), (1, 3, 3, 3)))
students_2 = [(student[0], student[1] + student[2]) for student in students_1]  # Concatenation
with open('students.csv', mode='w', newline='') as hist_file:
    students_writer = csv.writer(hist_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    students_writer.writerows(students_2)

ch_hist = ((1, 1, 1), (1, 2, 1), (2, 1, 1), (2, 3, 1))
with open('challenge_history.csv', mode='w', newline='') as hist_file:
    challenge_writer = csv.writer(hist_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    challenge_writer.writerows(ch_hist)
"""

with connection.cursor() as cursor:
    cursor.execute("SELECT studentId, strongPoints, weakPoints FROM users_studentprofile")
    student_raw = cursor.fetchall()
    student_data = [(student[0], student[1] + student[2]) for student in student_raw]  # Concatenation
    with open('./data/students.csv', mode='w', newline='') as hist_file:
        students_writer = csv.writer(hist_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        students_writer.writerows(student_data)
        
    cursor.execute("SELECT studentId, challengeId, status FROM challenges_challenges_students WHERE status=1")
    history_data = cursor.fetchall()
    with open('./data/challenge_history.csv', mode='w', newline='') as hist_file:
        challenge_writer = csv.writer(hist_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        challenge_writer.writerows(history_data)

# Run with our data. Writes rankings in output file
train = './data/challenge_history.csv'
output = './data/rankings.txt'
metadata = './data/students.csv'
UserAttributeKNN(train, output_file=output, metadata_file=metadata).compute()

# Test run with ml-100k dataset
# tr = './ml-100k/folds/0/train.dat'
# te = './ml-100k/folds/0/test.dat'
# UserKNN(train_file=tr, test_file=te, output_file='./data/rankings.txt', as_binary=True).compute()







