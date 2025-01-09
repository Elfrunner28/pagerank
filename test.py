my_dict = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
new_dict = {}
for i in my_dict:
    new_dict += {value:key for key, value in my_dict.items() if i in value}

print(new_dict)