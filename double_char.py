# command = input()
# result = ""
# while command != "End":
#     string = str(command)
#     for letters in string:
#         result += letters * 2
# print(result)


string = input()
n = 2
repeated_characters = ''.join([character*n for character in string])

print(repeated_characters)