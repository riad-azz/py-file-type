try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "Py File Type could not be installed, probably because "
        "setuptools is not installed on this computer.\n"
        "Install setuptools with $ pip install setuptools"
        "try again."
    )


long_description = open('README.md').read()
long_description_content_type = 'text/markdown'

setup(
    name='py_file_type',
    version='0.1.0',
    author='riad-azz',
    author_email='riadh.azzoun@hotmail.com',
    description='Wrapper for python-magic that includes necessary bin files.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url='https://github.com/riad-azz/py-file-type',
    project_urls={
        "Source": "https://github.com/riad-azz/py-file-type",
    },
    packages=find_packages(exclude=["docs", "tests"]),
    license="MIT License",
    keywords=["python-magic wrapper", "python-magic-bin", "python-magic binaries", "libmagic"],
    data_files=[('py_file_type', ['./py_file_type/libmagic/libmagic.dll', './py_file_type/libmagic/magic.mgc'])],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
