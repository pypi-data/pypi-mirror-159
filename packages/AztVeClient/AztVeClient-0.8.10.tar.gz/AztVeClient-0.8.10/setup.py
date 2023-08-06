from distutils.core import setup
# python setup.py sdist
# python -m twine upload --repository pypi dist/AztVeClient-0.8.10.tar.gz
# pip install --upgrade AztVeClient
import setuptools

setup(
    name='AztVeClient',  # How you named your package folder (MyLib)
    # packages=['AztVe'],  # Chose the same as "name"
    packages=setuptools.find_packages(),  # Chose the same as "name"
    version='0.8.10',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='AztQuant Virtual Exchange Python Client',  # Give a short description about your library
    author='Qujamlee',  # Type in your name
    author_email='1150728866@qq.com',  # Type in your E-Mail
    url='https://aztquant.com',  # Provide either the link to your github or to your website
    download_url='https://aztquant.com',  # I explain this later on
    keywords=['azt', 'aztve'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        # 'datetime',  # 可以加上版本号，如validators=1.5.1
        'colorlog',
        'pyzmq',
        'grpcio',
        'protobuf',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',  # Again, pick a license
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
