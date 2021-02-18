my_dict = {}

with open(r'task_6.txt', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        my_dict[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {my_dict}')
