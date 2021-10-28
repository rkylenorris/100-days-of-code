import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)

# print(student_data_frame)

# loop through data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of df
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
