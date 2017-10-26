import os
from setuptools import setup
from shutil import copyfile


try:
    config_dir = os.path.expandvars('$XDG_CONFIG_HOME/sesamo')
except KeyError:
    config_dir = os.path.expanduser('~/.config/sesamo')

os.makedirs(config_dir, exist_ok=True)
current_dir = os.path.dirname(__file__)
copyfile(os.path.join(current_dir, 'config.ini.example'),
         os.path.join(config_dir, 'config.ini'))

setup(
    name='sesamo',
    py_modules=['sesamo'],
    entry_points={
        'console_scripts': [
            'sesamo = sesamo:main',
        ],
    },
)
