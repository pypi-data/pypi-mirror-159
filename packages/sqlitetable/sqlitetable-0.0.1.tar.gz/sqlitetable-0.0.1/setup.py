from setuptools import setup, find_packages
import sqlitetable

setup(
    name='sqlitetable',
    version=sqlitetable.__version__,
    description=(
        'Use sqlite just like classes!'
    ),
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='Poiuzy',
    author_email='poiuzy-ice@qq.com',
    maintainer='Poiuzy',
    maintainer_email='poiuzy-ice@qq.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"]
)

