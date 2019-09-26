#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os

test_cases = {
    'A': [
        ['', ''],
    ],
}


def main():
    problems = list('ABCDEF')
    if len(sys.argv) > 1:
        problems = list(sys.argv[1])

    for problem in problems:
        if problem not in test_cases:
            print('Skip problem {}'.format(problem))
            continue
        success = True
        for test_input, test_output in test_cases[problem]:
            output = os.popen('./build/{} {}'.format(problem, test_input)).read()
            if output != test_output:
                print('Expected {}, but got {}'.format(test_output, output))
                success = False
        if success:
            print('Passed problem {}'.format(problem))
        else:
            print('Failed problem {}'.format(problem))


if __name__ == '__main__':
    main()
