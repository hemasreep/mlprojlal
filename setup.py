from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","") for req in requirements]

         if HYPHEN_E_DOT in requirements :
              requirements.remove(HYPHEN_E_DOT)

    return requirements          







setup(
name='mlproject',
version='0.0.1',
author='Hemasree',
author_email='hemasree.pediredla2015@gmail.com',
packages=find_packages(),        # it willt check in how many packages __init__.py exists.and it will trate as package
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')



)