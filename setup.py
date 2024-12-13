from setuptools import find_packages, setup
import os                  #追加。OSの機能のパッケージ
from glob import glob      #追加。グロブ（ワイルドカード）を扱う関数
package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kenta Hirachi',
    maintainer_email='s23c1114qb@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main', #talker.pyのmain関数という意味
            'listener = mypkg.listener:main',
    ],
    },
)
