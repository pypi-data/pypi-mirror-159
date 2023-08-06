import pytest
import os
import filecmp
import subprocess


def pytest_addoption(parser):
    parser.addoption(
        "--lib",
        action="store",
        default='off',
        help="check your missing library"
    )


def pytest_sessionstart(session):
    path = session.config.getoption('--lib')
    os.chdir(path)
    file_name = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name.append(file)
    print(file_name)
    if 'requirements.txt' in file_name:
        libs = os.popen('pip list').read()
        with open('libs_backup.txt', 'w')as f:
            f.write(libs)
        with open('libs_backup.txt', 'r')as f:
            lines = f.readlines()
            for i in lines:
                line = i.strip().split(' ')
                if line[0] == 'Package':
                    pass
                elif '---' in line[0]:
                    pass
                else:
                    with open('doc.txt', 'a')as f:
                        f.write(f'{line[0]}=={line[len(line) - 1]}\n')
        os.remove('libs_backup.txt')
        try:
            status = filecmp.cmp('doc.txt', 'requirements.txt')
            if status:
                print('No difference in current version')
            else:
                print('Installing differential version, please wait')
                cmd = 'pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com'
                output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                for line in output.stdout:
                    print(line)
        finally:
            os.remove('doc.txt')
            pass
    else:
        raise ('Not found requirements.txt')
