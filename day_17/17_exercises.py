#   Day 17 - Exception Handling & Packing and Unpacking Arguments

# 1.Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru= names
print(nordic_countries, es, ru)

