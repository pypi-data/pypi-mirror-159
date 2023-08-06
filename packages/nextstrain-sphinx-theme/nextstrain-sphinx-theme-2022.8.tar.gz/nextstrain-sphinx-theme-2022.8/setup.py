from pathlib import Path
from setuptools import setup

repo = Path(__file__).resolve().parent
version_path = repo / "lib/nextstrain/sphinx/theme/VERSION"
readme_path = repo / "README.rst"

with version_path.open(encoding = "utf-8") as version_file:
    __version__ = version_file.readline().strip()

setup(
    name = 'nextstrain-sphinx-theme',
    version = __version__,
    license = 'MIT',

    author       = 'Thomas Sibley',
    author_email = 'tsibley@fredhutch.org',

    description = 'Nextstrain theme for Sphinx and Read The Docs',
    long_description = readme_path.read_text(encoding = 'utf-8'),

    packages = ['nextstrain.sphinx.theme'],
    package_dir = {"": "lib"},

    # Includes files listed in MANIFEST.in as package data files, see
    # <https://packaging.python.org/guides/using-manifest-in/>.
    include_package_data = True,

    # See <http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package>
    entry_points = {
        'sphinx.html_themes': [
            'nextstrain-sphinx-theme = nextstrain.sphinx.theme',
        ]
    },
    install_requires = [
        'sphinx_rtd_theme >=1.0.0',
        'sphinx-copybutton',

        # Many of our projects use sphinx-markdown-tables, which is
        # incompatible with markdown 3.4.0 due to API changes.¹  Fix this with a
        # single dep pin here instead of pins in all of those projects.  The
        # upshot is that previously-broken stable builds of projects (e.g. past
        # releases) can be fixed retroactively since when re-built from the
        # same source they'll find this new theme dep.  The same wouldn't be
        # true if we patched each repo individually.
        #
        # XXX TODO: Remove this once the compat issue¹ is resolved.
        #   -trs, 18 July 2022
        #
        # ¹ https://github.com/ryanfox/sphinx-markdown-tables/issues/36
        'markdown <3.4.0',
    ],
    classifiers = [
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
