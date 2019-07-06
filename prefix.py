def common_prefix_string(strings_input):

    if len(strings_input) == 1:
        return strings[0]

    prefix = strings_input[0]

    for string_cond in strings_input[1:]:
        while string_cond[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break

    return prefix

strings_input=[]
n=int(input())
for x in range(0,n):
    b=input()
    strings_input.append(b)
print (common_prefix_string(strings_input))
