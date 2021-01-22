from setuptools import setup


with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='celare',
    version='0.0.3',
    url='https://github.com/MariaEduardaDeAzevedo/celare',
    license='MIT License',
    author='Maria Eduarda de Azevedo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='maria.silva@ccc.ufcg.edu.br',
    keywords=['token', 'hidden', 'api', 'keys'],
    description=u'Package to write and hide tokens, passwords, secret keys, without having to put them in the code',
    packages=['celare'],
    install_requires=[],
)