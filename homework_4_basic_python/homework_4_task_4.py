casino_blacklist = {"John Doe", "Duke Nukem", "Luke Skywalker", "Naga Sadou"}
poker_blacklist = {"John Doe", "Duke Nukem", "Lion Killer"}
alcohol_blacklist = {"John Doe", "Naga Sadou", "Dart Bane"}

banned_people = casino_blacklist.intersection(alcohol_blacklist, poker_blacklist)
print(banned_people)

# Alternative
banned_people_alternative = casino_blacklist & poker_blacklist & alcohol_blacklist
print(banned_people_alternative)