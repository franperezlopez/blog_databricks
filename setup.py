from setuptools import setup, find_packages
import os
import json
from etl import _package_name_

metadata_custom = {
    'version': os.getenv('VERSION','0.1.2'),
    'revision': os.getenv('DESCRIBE', '0.1.2-1-ge34ce98'),
    'buildNumber': os.getenv('BUILDNUMBER','etl-main_etl_main_20210101.1')
}

metadata_custom_as_markdown = \
rf"""```json
{json.dumps(metadata_custom)}
```"""

def get_install_requires(file='requirements.txt'):
    with open(file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

setup(
    name=_package_name_,
    packages=find_packages(include=["etl"]),
    include_package_data=False,
    version= metadata_custom["version"],
    description='databricks spark console application',
    author='fran pérez',
    long_description=metadata_custom_as_markdown,
    long_description_content_type="text/markdown",
    platforms=['linux'],
    license='Licensed',
    project_urls={'repository': 'https://fplopez@dev.azure.com/fplopez/mlcourse/_git/databricks'},
    python_requires=">=3.8",
    install_requires=get_install_requires()
)
