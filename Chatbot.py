def initials(full_name):
    first_letter = []
    for i in full_name.split():
        first_letter.append(i[0].upper())
    return '.'.join(first_letter)
    
print(initials("Wazih Tausif"))
    