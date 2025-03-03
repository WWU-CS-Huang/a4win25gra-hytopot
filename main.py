#!/usr/bin/env python3

def char_at(pattern, n, x, y):
    if n == 1:
        return 'o'

    if n == 2:
        return pattern[y][x]

    f = pattern[y//pow(3, n-2)][x//pow(3, n-2)]

    if f == 'o':
        c = char_at(pattern, n-1, x%pow(3, n-2), y%pow(3, n-2))
        return c
    return ' '


def main():
    m = int(input())
    patterns = []

    for _ in range(m):
        n = int(input())
        pattern = []
        for _ in range(3):
            pattern_line = input()
            if len(pattern_line) > 3:
                pattern_line = pattern_line[:3]
            while len(pattern_line) < 3:
                pattern_line += ' '

            pattern.append(list(pattern_line))

        patterns.append((n, pattern))
    print('')

    for n, pattern in patterns:
        for y in range(pow(3, n-1)):
            line = ''
            for x in range(pow(3, n-1)):
                line += char_at(pattern, n, x, y)
            line = line.rstrip()
            print(line)

        print('')

main()


