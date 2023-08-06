from setuptools import setup

setup(
    name='pytest-check-libs',
    version='3.3',
    author="kangkai",
    description='check your missing library',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='proprietary',
    py_modules=['pytest_check_libs'],
    keywords=[
        'pytest', 'py.test', 'pytest-check-libs',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'check-library = pytest_check_libs',
        ]
    }
)