# Iterating through a string
string = "    Apple Apple Apple no apple in the box apple apple             "

stripped_string = string.strip()
print(stripped_string)

left_stripped_string = (
    stripped_string
    .lstrip('Apple')
    .lstrip()
    .lstrip('Apple')
    .lstrip()
    .lstrip('Apple')
    .lstrip()
)
print(left_stripped_string)