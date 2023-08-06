from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='CTPreprocessing',
    version='3.0.0',
    license='MIT',
    author='AIMedic',
    author_email='aimedic@gmail.com',
    description="First preprocessing on input dicoms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    install_requires=[
                      'numpy',
                      'scipy',
                      'scikit-image',
                      'pydicom',
                      'simpleitk',
                      'matplotlib',
                      'opencv-python>=4.5'],

    extras_require={
        'interactive': ['matplotlib>=2.2.0', 'jupyter'],  # install using: pip install package[interactive]
    }
)
