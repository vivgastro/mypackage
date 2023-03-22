from setuptools import setup

requirements = ['numpy>=1.0']


setup(name='mymodule',
      version=0.1,
      description="An example module",
      author="Vivek Gupta",
      author_email = "vivg269@gmail.com",
      install_requires=requirements,
      python_requires='>=3.6',
      #entry_points=[{'console_scripts':'mymodule.sky_sim:main'}]
      )
