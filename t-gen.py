#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, re, shutil, json
def copy_no_override(src, dst):
    if os.path.exists(dst):
        # if file exists, do not copy
        return
    shutil.copy(src, dst)

def replace_test_placeholder(filepath, problems):
    test_file = ''
    with open(filepath, 'r') as f:
        test_file = f.read()
    test_cases = ''
    deliminator = ''
    for problem in problems:
        test_cases = test_cases + deliminator + '    \'{}\': [\n        [\'\', \'\']\n    ]'.format(problem)
        deliminator = ',\n'
    test_file = test_file.replace('\'PLACEHOLDER_TEST_CASES\'', test_cases)
    test_file = test_file.replace('PLACEHOLDER_PROBLEMS', ''.join(problems))
    with open(filepath, 'w') as f:
        f.write(test_file)

def read_config(config_file, key):
    with open(config_file) as f:
        config = json.load(f)
        if key not in config:
            sys.exit("{} not found in settings.json".format(key), 1)
        return config[key]

def main():
    if len(sys.argv) == 1 or '-h' in sys.argv:
        print('-h                      Displays help')
        print('./t-gen.py ABC001       Infers the number of questions from the contest name')
        print('./t-gen.py ABC001 ABCD  Manually specify the number of questions')
        sys.exit(1)

    contest_name = ''
    contest_number = ''
    contest_questions = []
    if len(sys.argv) == 2:
        # Check for contest name + number
        contest = [i for i in re.split(r'(\d+)', sys.argv[1]) if i]
        if len(contest) != 2:
            sys.exit('Invalid contest name {}'.format(sys.argv[1]))
        contest_name, contest_number = contest
        if contest_name == 'ABC':
            contest_questions = list('ABCDEF')
        elif contest_name == 'ARC':
            contest_questions = list('ABCDEF')
        elif contest_name == 'AGC':
            contest_questions = list('ABCDEF')
        else:
            sys.exit('Contest name: {} not recognized. Please enter the full questions'.format(contest_name), 1)

    if len(sys.argv) == 3:
        # Check for contest name + number + questions
        contest_name, contest_number = [i for i in re.split(r'(\d+)', sys.argv[1]) if i]
        contest_questions = list(sys.argv[2])


    # Set up directory
    project_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(project_dir, 'settings.json')
    root_dir = os.path.expanduser(read_config(config_file, 'root'))
    template_dir = os.path.join(project_dir, 'templates')
    contest_dir = os.path.join(root_dir, contest_name + contest_number)
    os.makedirs(contest_dir, exist_ok=True)

    # Copy template cpp files
    for contest_question in contest_questions:
        copy_no_override(os.path.join(template_dir, 'template.cc'), os.path.join(contest_dir, contest_question + '.cc'))
    # Copy template files into directory
    for template_file in ['CMakeLists.txt', 'Makefile', 'test.py']:
        copy_no_override(os.path.join(template_dir, template_file), os.path.join(contest_dir, template_file))
    # Fill placeholder for the test file
    replace_test_placeholder(os.path.join(contest_dir, 'test.py'), contest_questions)

if __name__ == '__main__':
    main()

