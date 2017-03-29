#
# lookup = {}
# lookup = dict()
# lookup = {'age': 42, 'loc': 'Italy'}
# lookup = dict(age=42, loc= 'Italy')
#
# print(lookup)
# lookup['cat'] = 'Fun code demos'
#
#
# print(lookup['loc'])
# if 'cat' in lookup:
#     print(lookup['cat'])
#
#
#
# class Wizard:
#     def __init__(self, name, level):
#         self.level = level
#         self.name = name
#
# gandolf = Wizard("Gandolf", '59')
# print(gandolf.__dict__)


import collections

User = collections.namedtuple('User', 'id, name, email')

users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
    User(5, 'user5', 'user5@talkpython.fm')

]

print(users)


lookup = dict()

id_count = 0

for u in users:
    id_count += 1

    print(u.name)
print("the number of user is {}".format(id_count))





# lookup = dict()
# for u in users:
#     lookup[u.name] = u
#
#
# print(lookup['user1'])





#
# def count(user):
#

# with open(filename, 'r', encoding='utf-8') as fin:
#     line_num = 0
#     for line in fin:
#         line_num += 1
#         if line.lower().find(search_text) >= 0:
#             m = SearchResult(line=line_num, file=filename, text=line)
#             # matches.append(m)
#             yield m
