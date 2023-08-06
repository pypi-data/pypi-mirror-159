from setuptools import setup

setup(
    name='pytest-check-library',
    url='https://github.com/yoyoketang/pytest-change-report',
    version='1.0',
    author="kangkai",
    description='check your missing library',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='proprietary',
    py_modules=['pytest_check_library'],
    keywords=[
        'pytest', 'py.test', 'pytest-check-library',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'check-library = pytest_check_library',
        ]
    }
)