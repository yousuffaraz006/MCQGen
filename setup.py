from setuptools import find_packages, setup

setup(
  name='mcqgenerator',
  version='0.0.1',
  description='A small project for generating MCQs.',
  author='Yousuf Faraz',
  author_email='yousuffaraz006@gmail.com',
  install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
  packages=find_packages(),
)