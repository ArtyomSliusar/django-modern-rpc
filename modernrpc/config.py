# coding: utf-8
import django.conf
import sys


class DefaultValues(object):
    #: Override this to use a different JSON serializer when decoding JSON-RPC request
    MODERNRPC_JSON_DECODER = 'json.decoder.JSONDecoder'

    #: Override this to use a different JSON deserializer when encoding JSON-RPC response
    MODERNRPC_JSON_ENCODER = 'django.core.serializers.json.DjangoJSONEncoder'

    #: Override these to change the key used in kwars for entry point name
    MODERNRPC_HANDLERS = [
        'modernrpc.handlers.JSONRPCHandler',
        'modernrpc.handlers.XMLRPCHandler',
    ]

    #: The name set to any entry point which doesn't declare it explicitely
    MODERNRPC_DEFAULT_ENTRYPOINT_NAME = '__default_entry_point__'

    #: Set to False if you want to manipulate dates with DateTime class from Python XML RPC builtin lib.
    #: If set to True, dates will be passed as datetime to the RPC function.
    MODERNRPC_XML_USE_BUILTIN_TYPES = True

    #: Configure the format of the docstring used to document your RPC methods. Possible values are: '', 'rst' or 'md'
    MODERNRPC_DOC_FORMAT = ''

    #: Set the list of python modules that must be looked up to find RPC methods
    MODERNRPC_METHODS_MODULES = []

    #: Set to False if you want to raise an exception when a None value is passed to XML encoder
    MODERNRPC_XMLRPC_ALLOW_NONE = True
    #: Configure the default encoding used by XML encoder
    MODERNRPC_XMLRPC_DEFAULT_ENCODING = None


class SettingsWrapper(object):
    def __getattr__(self, item):
        result = getattr(django.conf.settings, item, None)
        if result:
            return result
        return getattr(DefaultValues, item)


settings = SettingsWrapper()
#sys.modules[__name__] = SettingsWrapper()
