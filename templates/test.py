#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os, subprocess

test_cases = {
'PLACEHOLDER_TEST_CASES'
}


def main():
    problems = list('PLACEHOLDER_PROBLEMS')
    if len(sys.argv) > 1:
        problems = list(sys.argv[1])

    for problem in problems:
        if problem not in test_cases:
            print('Skip problem {}'.format(problem))
            continue
        success = True
        for i, (test_input, test_output) in enumerate(test_cases[problem]):
            print('Case {}-{}'.format(problem, i + 1))
            p = subprocess.run(['./build/{}'.format(problem)], stdout=subprocess.PIPE,
                    input=test_input, encoding='ascii')
            output = p.stdout
            if test_output != '' and not output.endswith('\n'):
                print('\tExpected newline at end of output')
                success = False
            output = output.rstrip()
            if output != test_output:
                print('\tExpected {}, but got {}'.format(test_output, output))
                success = False
        if success:
            print('Passed problem {}'.format(problem))
        else:
            print('Failed problem {}'.format(problem))


if __name__ == '__main__':
    main()
