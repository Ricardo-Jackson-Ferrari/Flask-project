from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name='delivery',
    version='0.1.0',
    description='Delivery app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    extras_require={'dev': ['black', 'flake8', 'flask-debugtoolbar', 'flask-shell-ipython', 'ipdb', 'ipython', 'isort', 'pytest', 'pytest-flask', 'pytest-cov']}
)
