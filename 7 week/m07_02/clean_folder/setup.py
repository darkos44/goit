from setuptools import setup, find_namespace_packages

setup(
    name='hello_world_lomaster',
    version='1.0.0',
    description='Hello world testing',
    # url='http://github.com/dummy_user/useful',
    author='Mark Podopryhora',
    author_email='44darkos@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting = hello_world_lomaster.main:greeting']}
)