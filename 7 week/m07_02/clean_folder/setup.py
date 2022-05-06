from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Hw 7 clean folder',
    # url='http://github.com/dummy_user/useful',
    author='Mark Podopryhora',
    author_email='44darkos@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.main:start']}
)