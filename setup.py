import os
from setuptools import setup, find_packages

VERSION = "0.1.0.dev0"


# Read description
with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()


def write_version_py():
    plugins = ['ES_example']
    for plugin in plugins:
        filename = os.path.join(
            os.path.dirname(__file__),
            plugin,
            'version.py')
        ver = "__version__ = '{}'\n"
        with open(filename, 'w') as fh:
            fh.write(ver.format(VERSION))


write_version_py()

setup(
    name="ES_example",
    version=VERSION,
    # The entry point "force.bdss.extensions" is where the extension mechanism
    # takes place. You have to specify a path to the plugin class, as given
    # below. The name (before the '=') of the plugin is irrelevant, but try to
    # use the name of the module.
    # Also, it is good practice to use the name of your organization, like
    # we did here.
    entry_points={
        "force.bdss.extensions": [
            "ES_example = "
            "es_example.es_plugin:ESPlugin",
        ]
    },
    packages=find_packages(),
    install_requires=[
        "force_bdss >= 0.2.0",
    ]
)
