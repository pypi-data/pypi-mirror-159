from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()
long_description = Path(here / 'README.md').read_text(encoding='utf-8')

setup(
    name='example_package_gz_hejiehui',  # Required
    version='0.0.2',  # Required
    license='MIT',
    description="A sample Python project",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    url="https://github.com/pypa/sampleproject",  # Optional
    author="gz-hejiehui",  # Optional
    author_email="gz-hejiehui@outlook.com",  # Optional
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords="sample, setuptools, development",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    install_requires=["peppercorn"],  # Optional
    extras_require={  # Optional
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },
)
