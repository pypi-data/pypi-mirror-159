from distutils.core import setup
with open("README.md", "r",encoding='UTF-8') as f:
  long_desc = f.read()

setup(name='secuer',
      version='1.0.6',
      description='Secuer: ultrafast, scalable and accurate clustering of single-cell RNA-seq data',
      author='nnwei',
      long_description=long_desc,
      author_email='nanawei11@163.com',
      # py_modules=['Tool'],
      url='https://github.com/nanawei11/Secuer',
      packages=['secuer','bin'],
      license='MIT',
      entry_points={
            'console_scripts': ['secuer = bin.secuer_console:main']}# linux
      )

