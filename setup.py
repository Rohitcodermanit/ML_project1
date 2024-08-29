from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines
        requirements = [req.replace("\n", "") for req in requirements]  # Strip newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ML_project1',
    version='0.0.1',
    author='Rohit',
    author_email='rohitahirwar9718@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
