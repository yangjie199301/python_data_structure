def reverse_string(oldstring):
    if len(oldstring) < 2:
        return oldstring[0]
    else:
        return reverse_string(oldstring[1:]) + oldstring[0]

print(reverse_string('abcd'))
