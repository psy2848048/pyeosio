from setuptools import setup

setup(name='pyeosio',
      version='0.1.0',
      description='EOSIO node connector for Python',
      url='https://github.com/psy2848048/pyeosio',
      author='Junhang (Bryan) RHEE',
      author_email='bryan@langchain.io',
      license='MIT',
      packages=['pyeosio'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
