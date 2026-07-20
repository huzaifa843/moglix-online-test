def longest_valid_parentheses(s):
    stack = [-1]  # base marker
    max_len = 0

    i = 0
    while i < len(s):
        char = s[i]
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()
            if not stack:
                stack.append(i)  # new base marker
            else:
                max_len = max(max_len, i - stack[-1])
        i += 1

    return max_len


# Take input from user
s = input("Enter a string containing only '(' and ')': ")
result = longest_valid_parentheses(s)
print("Length of longest valid parentheses substring:", result)
