# Start with an empty list.
users = []
# Make a new user, and add them to the list.
new_user = {'last': 'fermi', 'first': 'enrico', 'username': 'efermi', }
users.append(new_user)
# Make another new user, and add them as well.
new_user = {'last': 'curie', 'first': 'marie', 'username': 'mcurie', }
users.append(new_user)
# Show all information about each user.
# for user_dict in users:
#     for k, v in user_dict.items():
#         print(k + ": " + v)
#         print("\n")

print(users)
