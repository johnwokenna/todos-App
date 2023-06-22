names = ["john smith", "jay santi", "eva kuki"]
new_names = [name.title() for name in names]
print (new_names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
new_usernames = [len(user) for user in usernames]
print (new_usernames)

new_items = []
for item in usernames:
    new_items.append(len(item))
print (new_items)

user_entries = ['10', '19.1', '20']
new_items = [float(item) for item in user_entries]
print (new_items)
sum1 = 0
for item in user_entries:
    sum1 = sum1 + float(item)
print (sum1)