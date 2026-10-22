import numpy as np

# 1. Create the marks array (4 students x 3 subjects)
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print("Shape:", marks.shape)
print("Dtype:", marks.dtype)
print("Size:", marks.size)

# 2. Slice the first two students

print(marks[:2] ,"\n")

# Slice the last subject for all students

print(marks[:,-1])

# 3. Compute each student's average (axis=1)
student_averages = np.mean(marks, axis=1)
print("\nStudent averages:", student_averages)

# Compute each subject's average (axis=0)
subject_averages = np.mean(marks, axis=0)
print("Subject averages:", subject_averages)

# 4. Broadcasting: add 5 grace marks to every value
grace_marks = marks + 5
print(grace_marks)

# 5. Compute weighted scores using dot product
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("\nWeighted scores:", weighted_scores)

# 6. Reshape numbers from 0 to 11 into a 3x4 array
reshaped = np.arange(12).reshape(3, 4)
print("\nReshaped array:")
print(reshaped)