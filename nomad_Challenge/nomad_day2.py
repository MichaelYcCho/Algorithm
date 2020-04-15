def is_on_list(d_list, x):
  return x in d_list

def get_x(d_list, index):
  return d_list[index]

def add_x(d_list, x):
  d_list.append(x)

def remove_x(d_list, x):
    d_list.remove(x)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)