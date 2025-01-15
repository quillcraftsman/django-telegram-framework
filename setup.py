"""
Setup.py file to build and install package
"""
import codecs
import os
from setuptools import setup, find_packages


def open_local(paths, mode="r", encoding="utf8"):
    """
    Open local package file
    :param paths: list of paths to file
    :param mode: read, write, ...
    :param encoding: Encoding
    :return: file object
    """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)
    return codecs.open(path, mode, encoding)


def get_value_from_package_info(line, value, old_value):
    """
    Get value from text line
    :param line: file text line
    :param value: value to parse
    :param old_value: if value has already founded
    :return:
    """
    if old_value:
        return old_value
    if line.startswith(value):
        _, val = line.split('=')
        return val.strip().replace("'", '')
    return None


PACKAGE_NAME = "pygenesis_django"

PROJECT_URLS = {
    'Documentation': 'https://pygenesis-django.libresource.info',
    'Source': 'https://github.com/libresource/pygenesis-django',
    'Tracker': 'https://github.com/libresource/pygenesis-django/issues',
    'Release notes': 'https://github.com/libresource/pygenesis-django/releases',
    'Changelog': 'https://github.com/libresource/pygenesis-django/releases',
    'Download': 'https://pypi.org/project/pygenesis-django/',
}

with open_local([PACKAGE_NAME, "package.py"]) as fp:
    package_pypi_name, package_version, package_status = None, None, None
    for file_line in fp:
        package_pypi_name = get_value_from_package_info(file_line, 'name', package_pypi_name)
        package_version = get_value_from_package_info(file_line, 'version', package_version)
        package_status = get_value_from_package_info(file_line, 'status', package_status)

    if not (package_pypi_name and package_version and package_status):
        raise RuntimeError("Unable to determine Package Info.")

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def read(filename):
    """
    read some file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

setup(
    name=package_pypi_name,
    version=package_version,
    packages=find_packages(
        include=[PACKAGE_NAME, f'{PACKAGE_NAME}.*']
    ),

    include_package_data=True,
    license="MIT",
    description="Python Django package repository template",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/libresource/pygenesis-django",
    author="quillcraftsman",
    author_email="quill@craftsman.lol",
    keywords=["python", "django", "package", "template-repository"],
    # install_requires=[
    #     'Django==5.0.6',
    # ],
    python_requires=">=3",
    classifiers=[
        f'Development Status :: {package_status}',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Environment :: Web Environment',
        'Framework :: Django',
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls=PROJECT_URLS,
)
