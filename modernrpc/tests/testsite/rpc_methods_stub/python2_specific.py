from modernrpc.core import rpc_method
from django.utils import six


# Standardization to 'unicode' type
@rpc_method(str_standardization=six.text_type)
def force_unicode_input(data):
    """Returns a string representation of input argument type"""
    return str(type(data))
