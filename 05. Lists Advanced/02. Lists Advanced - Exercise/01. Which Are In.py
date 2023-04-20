# def substring_find(str1, str2):
#     newest = []
#     for i in str1:
#         for j in str2:
#             if i in j and i not in newest:
#                 newest.append(i)
#     return newest


substring_list = input().split(", ")
string_list = input().split(", ")

output = list(filter(lambda substring: any(substring in string for string in string_list), substring_list))

print(output)
