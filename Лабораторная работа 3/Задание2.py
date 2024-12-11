# TODO Напишите функцию find_common_participants
def find_common_participants (list1, list2, sep = ","):
    set1 = set(list1.split(sep))
    set2 = set(list2.split(sep))
    return list(sorted(set1 & set2))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants (participants_first_group, participants_second_group, "|")
print(result)
