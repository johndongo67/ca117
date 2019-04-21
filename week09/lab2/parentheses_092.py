from stack_092 import Stack

def matcher(line):
    left = "({["
    right = "]})"
    square = "[]"
    curl = "{}"
    roun = "()"
    s = Stack()
    for char in line:
        try:
            if char in left:
                s.push(char)

            elif char in right and s.top() in square and char in square:
                s.pop()

            elif char in right and s.top() in curl and char in curl:
                s.pop()

            elif char in right and s.top() in roun and char in roun:
                s.pop()

        except IndexError:
            return False

    return s.is_empty()
