from setuptools import setup, find_packages

setup(
    name = "paquete-diegogabyolmos",
    version = "0.6",
    description = "Este es un paquete de ejemplo para saludar y despedir",
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author = "Diego Olmos",
    author_email = "diegogabyolmos@gmail.com",
    url = "https://www.facebook.com/ElmsCabin/",
    license_files = ['LICENSE'],
    scripts = [],
    packages = find_packages(), 
    test_suit = 'tests',
    install_requires = [paquete.strip() 
                        for paquete in open("requirements.txt").readlines()],
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
)