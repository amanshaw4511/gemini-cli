from setuptools import setup

setup(
    name='ai',
    version='0.1',
    py_modules=['ai'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ai=app:cli
    ''',
)
