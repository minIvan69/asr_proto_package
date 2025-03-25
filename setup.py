from setuptools import setup, find_packages

setup(
    name='asr_proto_package',              # любое имя пакета
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'grpcio>=1.51.3',
        'protobuf>=5.29.4',
        'grpcio-tools>=1.51.3'
        # если у вас есть ещё зависимости
    ],
    python_requires='>=3.9',          # или другая минимальная версия, если нужно
    description='ASR proto package for gRPC',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/minIvan69/asr_proto_package',  # если есть GitHub
    author='Ivan Mingalev',
    author_email='nero.fan69@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
