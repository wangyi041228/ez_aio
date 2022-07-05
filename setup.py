from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
   name='ez_web',
   version='0.0.1',
   description='Easiest way to get and post with aiohhtp.',
   long_description=long_description,
   author='E',
   author_email='18771051812@qq.com',
   url="https://www.github.com/wangyi041228/ez_web",
   packages=['ez_web'],
   install_requires=['aiohttp'],
   scripts=[]
)
