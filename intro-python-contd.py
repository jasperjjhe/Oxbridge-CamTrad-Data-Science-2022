colleges_to_numbers = {
    "Jesus College": 1,
    "Christ's College": 2,
    "Darwin College": 3,
    "King's College": 4,
    "Pembroke College": 5,
    "Trinity College": 6
}

print(colleges_to_numbers["Trinity College"])

for college, college_number in colleges_to_numbers.items():
    print(f"College number {college_number}: {college}")