list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:

    # Create an empty dictionary to store the merged information
    merged_dict = {}

    # Iterate over the first list and add each student's information to the merged dictionary
    for student in list_1:
        merged_dict[student['id']] = student

    # Iterate over the second list and update each student's information in the merged dictionary
    for student in list_2:
        student_id = student['id']
        if student_id in merged_dict:
            merged_dict[student_id] = {**merged_dict[student_id], **student}
        else:
            merged_dict[student_id] = student

    # Convert the merged dictionary back into a list
    merged_list = list(merged_dict.values())

    return merged_list


list_3 = merge_lists(list_1, list_2)
print(list_3)
