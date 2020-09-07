


def check_balanced(inp):

    stack_1 = stack_2 = stack_3 = []
    remains = False

    for char in inp:

        # Only work if the entered characters are any sort of paranthsis
        if char=='(' or char==')' or char=='{' or char=='}' or char=='[' or char==']':
            if char=='(':
                stack_1.append(char)
            elif char=='{':
                stack_2.append(char)
            elif char=='[':
                stack_3.append(char)

            # Catch the exception in case there is an extra closing bracket
            try:
                if char==')':
                    stack_1.pop()
                elif char=='}':
                    stack_2.pop()
                elif char==']':
                    stack_3.pop()
            except:
                remains = True
                break

    if len(stack_1) == 0 and len(stack_2) == 0 and len(stack_3) == 0 and remains == False:
        return True
    else:
        return False


if __name__ == "__main__":

    print("[*] Check for Balanced Paranthesis using Stack")
    print("\n[*] Enter your input")
    inp = list(input())
    
    balanced = check_balanced(inp)

    if balanced == True:
        print("\n[*] You have entered balanced paranthesis")
    else:
        print("\n[*] The paranthesis are not balanced")
    