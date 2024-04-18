# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
# if __name__ == '__main__':
#     N = int(input())
#     my_list = []

#     for _ in range(N):
#         command = input().split()

#         if command[0] == 'insert':
#             my_list.insert(int(command[1]), int(command[2]))
#         elif command[0] == 'print':
#             print(my_list)
#         elif command[0] == 'remove':
#             my_list.remove(int(command[1]))
#         elif command[0] == 'append':
#             my_list.append(int(command[1]))
#         elif command[0] == 'sort':
#             my_list.sort()
#         elif command[0] == 'pop':
#             my_list.pop()
#         elif command[0] == 'reverse':
#             my_list.reverse()


import math

def find_angle(side):
    angle_radians = math.atan(1) * (side / side)
    print(angle_radians)
    angle_degrees = round(angle_radians * (180 / math.pi))
    print(angle_degrees)
    return angle_degrees

if __name__ == "__main__":
    side1 = float(input())
    side2 = float(input())
    
    angle = find_angle(side1)
    print(str(angle) + "°")
