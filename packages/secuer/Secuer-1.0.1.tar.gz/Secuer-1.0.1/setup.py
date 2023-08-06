from distutils.core import  setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='Secuer',
      version='1.0.1',
      description='Secuer: ultrafast, scalable and accurate clustering of single-cell RNA-seq data.',
      author='Nana Wei',
      author_email='nanawei11@163.com',
      packages=['Secuer'],# import shangchuan
      entry_points={
            'console_scripts': [#console_srcipts是固定的不能改
                  'Secuer = bin.Secuer_console:main'#shangchuan(服务器唤醒的命令，相当于ls等） = mhaptkckw.mhap_console:main
            ]
      }# linux
      )

