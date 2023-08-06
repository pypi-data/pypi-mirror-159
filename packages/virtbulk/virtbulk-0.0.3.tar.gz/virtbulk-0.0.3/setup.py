import pathlib
import setuptools

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name='virtbulk',
    version='0.0.3',
    author='Anton Karmanov',
    author_email='a.karmanov@inventati.org',
    license='Apache',
    url='https://gitlab.com/bergentroll/virtbulk',
    description='CLI to operate libvirt machines matched with globs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
        'libvirt-python>=6.0.0',
        'rich>=12<13',
        'importlib-metadata; python_version>="3.6"',
    ],
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    entry_points={
        'console_scripts': [
            'virtbulk = virtbulk.entrypoint:run_cli',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ]
)
