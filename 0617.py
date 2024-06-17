def solution(s: str) -> bool:
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0