from setuptools import find_packages
from setuptools import setup

setup(
    name='nlpchallengespackage',
    version='1.0.0',
    description='trying to understand this packaging stuff',
    packages=["nlpchallengespackage"],
    entry_points={
        'console_scripts': [
            'challenge-1 = nlpchallengespackage.challenge_1:main',
            'challenge-2 = nlpchallengespackage.challenge_2:main',
            'challenge-3 = nlpchallengespackage.challenge_3:main',
        ],
    },
)
