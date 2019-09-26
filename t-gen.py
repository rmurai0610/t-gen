#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, re, shutil

def main():
    if len(sys.argv) == 1 or '-h' in sys.argv:
        print('-h: Display help')
        return
    contest_name = ''
    contest_number = ''
    contest_questions = []
    if len(sys.argv) == 2:
        # Check for contest name + number
        contest_name, contest_number = [i for i in re.split(r'(\d+)', sys.argv[1]) if i]
        if contest_name == 'ABC':
            contest_questions = list('ABCDEF')
        elif contest_name == 'ARC':
            contest_questions = list('ABCDEF')
        elif contest_name == 'AGC':
            contest_questions = list('ABCDEF')
        else:
            print('Contest name: {} not recognized. Please enter the question names', contest_name)
            return

    if len(sys.argv) == 3:
        # Check for contest name + number + questions
        contest_name, contest_number = [i for i in re.split(r'(\d+)', sys.argv[1]) if i]
        contest_questions = list(sys.argv[2])
    print(contest_name, contest_number, contest_questions)


    # Generate directory
    root_dir = os.path.expanduser('~/project/atcoder')
    contest_dir = root_dir + '/' + contest_name + contest_number
    os.makedirs(contest_dir, exist_ok=True)
    # Create cpp files
    for contest_question in contest_questions:
        open(contest_dir + '/' + contest_question + '.cc', 'a').close()
    # Copy template files into directory
    template_dir = os.path.dirname(os.path.realpath(__file__)) + '/templates'
    for template_file in ['CMakeLists.txt', 'Makefile', 'test.sh']:
        shutil.copy(template_dir + '/' + template_file, contest_dir + '/' + template_file)


if __name__ == '__main__':
    main()

