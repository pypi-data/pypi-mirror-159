"""
NamespaceA command line tool (enable `python -m namespaceA` or `python namespaceA` syntax)
"""
# from `site-packages/wheel/__main__.py`
# allows running python code by passing the directory as argument to the python interpreter, i.e:
# `$ /usr/local/bin/python PKGNAMEDIR` or
# `$ /usr/local/bin/python -m PKGNAMEDIR`
# this feature of python can be used to effectively run the cli using the package directory as argument to the python interpreter

import sys


def main():
    if __package__ == '':
        # To be able to run 'python DISTRONAME-VERSION.whl/PKGNAME'; run the package from within the zipped file ? however i think to have this work, the `.whl` must only be archiving/zipping/encapsulating a single global/top-level python namespace/package, here we have namespaceA and namespaceB, both are global/top-level and both have `__main__.py` modules so it doesn't work
        import os.path
        path = os.path.dirname(os.path.dirname(__file__))
        sys.path[0:0] = [path]
    import namespaceA.cli
    sys.exit(namespaceA.cli.execute())


if __name__ == "__main__":
    sys.exit(main())
