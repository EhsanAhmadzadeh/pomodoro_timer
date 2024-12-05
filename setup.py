from setuptools import setup, find_packages

setup(
    name='pomodoro_timer',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'plyer',
        'colorama',
        # Add other dependencies if needed
    ],
    entry_points={
        'console_scripts': [
            'pomodoro = pomodoro.cli:main',
        ],
    },
    author='Ehsan Ahmadzadeh',
    author_email='amirehsansolout@gmail.com',
    description='A simple Pomodoro timer CLI application.',
    url='https://github.com/EhsanAhmadzadeh/pomodoro_timer',
)
