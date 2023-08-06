"""
Integrate with SuprSend platform using python

For more information about this library, checkout the README on GitHub:
    https://github.com/suprsend/suprsend-py-sdk
For the user guide, examples and more, visit the docs page at:
    https://docs.suprsend.com/docs
"""
from .version import __version__
__author__ = 'SuprSend Developers'
__credits__ = 'SuprSend'

from .sdkinstance import Suprsend  # noqa
from .workflow_batch import BatchResponse  # noqa
