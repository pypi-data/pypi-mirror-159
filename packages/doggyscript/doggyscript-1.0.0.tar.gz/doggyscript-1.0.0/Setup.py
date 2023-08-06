from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='doggyscript',
  version='1.0.0',
  description='yay',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='dbcjdc sdjsdu',
  author_email='itggpqjodjplsdrhmt@nthrl.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Assist mode', 
  packages=find_packages(),
  install_requires=[''],
  long_description_content_type='text/markdown'
)