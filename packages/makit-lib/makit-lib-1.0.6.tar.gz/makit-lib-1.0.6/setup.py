from setuptools import setup

setup(
    name='makit-lib',
    version='1.0.6',
    packages=[
        'makit.lib'
    ],
    namespace_package=['makit'],
    install_requires=[
        'PyYAML'
    ],
    python_requires='>3.3',
    url='',
    license='MIT',
    author='LiangChao',
    author_email='liang20201101@163.com',
    description='实用工具包，对python基础库的扩展'
)
