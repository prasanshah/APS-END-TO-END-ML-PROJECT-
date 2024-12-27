from setuptools import setup, find_packages
from typing import List


E_DOT = "-e ." 
def get_req(file_path:str)->List[str]:
    requiremnts_list= []
    with open(file_path) as file_obj:
        requiremnts_list = file_obj.readlines()
        requiremnts_list = [req.replace("\n","") for req in requiremnts_list]

        if(E_DOT in requiremnts_list):
            requiremnts_list.remove(E_DOT)
    return requiremnts_list


setup(
name="ASP_ML_END_TO_END",
version="0.0.1",
author="Prasan Shah",
author_email="prasanshah29@gmail.com",
packages=find_packages(),
install_requires = get_req('requirements.txt'),
)