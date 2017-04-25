from .messages import *
import abci.types_pb2 as types

def str_to_bytes(data):
    if isinstance(data, str):
        return data.encode('utf-8')
    return data

class Result(object):
    def __init__(self, code=types.OK, data=b'', log=''):
        self.code = code
        self.data = str_to_bytes(data)
        self.log = log

    def ok(data=b'', log=''):
        data = str_to_bytes(data)
        return Result(types.OK, data, log)

    def error(code='', data=b'',log=''):
        data = str_to_bytes(data)
        return Result(code, data, log)

    def is_ok(self):
        return self.code == types.OK

    def str(self):
        return "ABCI[code:{}, data:{}, log:{}]".format(self.code, self.data, self.log)

class BaseApplication(object):
    """
    Base App extends this and override what's needed for your app
    """
    def info(self):
        r = types.ResponseInfo()
        r.data = "default"
        return r

    def set_option(self, k, v):
        return 'key: {} value: {}'.format(k,v)

    def deliver_tx(self, tx):
        return Result.ok(data='delivertx')

    def check_tx(self, tx):
        return Result.ok(data='checktx')

    def query(self, reqQuery):
        rq = types.ResponseQuery(code=types.OK, key=reqQuery.data, value=b'example result')
        return rq

    def commit(self):
        return Result.ok(data='commit #')

    def init_chain(self, validators):
        return

    def begin_block(self, hash, header):
        return

    def end_block(self, height):
        return types.ResponseEndBlock()
