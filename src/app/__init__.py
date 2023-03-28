from importlib.metadata import version

__version__ = version("tempdevicesim")
del version

__all__ = ["__version__"]