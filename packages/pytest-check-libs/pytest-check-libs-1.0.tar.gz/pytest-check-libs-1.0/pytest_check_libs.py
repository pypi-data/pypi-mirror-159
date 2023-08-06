import pytest
import os
import filecmp


def pytest_addoption(parser):
    parser.addoption(
        "--lib",
        action="store",
        default='off',
        help="check your missing library"
    )


def pytest_sessionstart(session):
    if session.config.getoption('--lib') == 'on':
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)
        file_name = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_name.append(file)
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
                status = filecmp.cmp('doc.txt', 'requirement.txt')
                if status:
                    print('No difference in current version')
                else:
                    print('Installing differential version, please wait')
                    content = os.popen('pip install -r requirement.txt').read()
                    print(content)
            finally:
                os.remove('doc.txt')
                pass
        else:
            raise ('Not found requirement.txt')




