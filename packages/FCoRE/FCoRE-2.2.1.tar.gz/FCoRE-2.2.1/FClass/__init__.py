from FSON import DICT
from FList import LIST
from FDate import DATE
import os

from FLog.LOGGER import Log
Log = Log("FClass.FairClass")

class FairClass:
    pid = None
    isTest = False

    def __init__(self, **kwargs):
        self.pid = os.getpid()
        self.handle_kwargs(**kwargs)

    def handle_kwargs(self, **kwargs):
        self.isTest = DICT.get("isTest", kwargs, default=False)

    def get_func(self, func):
        """ Get a function within the class.
        -> Call with ()
            i = t.get_func(r[38])
            u = i()
        """
        return getattr(self, func)

    def get_callable(self, attr):
        return callable(attr)

    def get_att(self, attr):
        try:
            item = getattr(self, attr)
            return item
        except Exception as e:
            Log.e("Failed to get attribute/function.", error=e)
            return False

    def get_method_names(self):
        return [func for func in dir(self)
                if self.get_callable(self.get_func(func))
                                       and not func.startswith("__")
                           and func.islower()
                           and not func.startswith("constructor")
                           and not func.startswith("construct")]

    @staticmethod
    def get_arg(key, value, default=False):
        return DICT.get(key, value, default=default)

    @staticmethod
    def get_dict(key, dic, default=False):
        return DICT.get(key, dic, default=default)

    @staticmethod
    def get_list(index, listObj, default=False):
        return LIST.get(index, listObj, default)