from eqsmart.main.consumer import Consumer
from eqlink.components.remote_server import remote_server
import json

protocol = {
    'type': 'call provider',
    'service_name': '',
    'func': '',
    'args': (),
    'kwargs': {}
}


class RemoteCall:
    def __init__(self, service_path):
        self.service_path = service_path

    # def func_call(self, params):
    #     if type(params) is tuple:
    #         protocol['args'] = params
    #     else:
    #         protocol['kwargs'] = params
    #     service_path = self.service_path.split('/')
    #     protocol['service_name'] = service_path[0]
    #     protocol['func'] = service_path[1]
    #
    #     provider_service_list = remote_server.__get__()
    #     provider_server = provider_service_list[service_path[0]]['remote']
    #     # TODO 增加服务调用权重控制
    #     provider_conf = {
    #         # 远程服务器地址
    #         'IP': provider_server[0]['ip'],
    #         # 远程服务器端口
    #         'PORT': provider_server[0]['port'],
    #         # 消息读取长度
    #         'BUF_SIZE': 1024
    #     }
    #     remote_call = Consumer(provider_conf).func_call_int(protocol)
    #     return json.loads(remote_call)

    def func_call_new(self, params):
        if type(params) is tuple:
            protocol['args'] = params
        else:
            protocol['kwargs'] = params
        service_path = self.service_path.split('/')
        protocol['service_name'] = service_path[:-1]
        protocol['func'] = service_path[-1]
        provider_service_list = remote_server.__get__()
        provider_server = provider_service_list[service_path[0]]['remote']
        # TODO 增加服务调用权重控制
        provider_conf = {
            # 远程服务器地址
            'IP': provider_server[0]['ip'],
            # 远程服务器端口
            'PORT': provider_server[0]['port'],
            # 消息读取长度
            'BUF_SIZE': 1024
        }
        print('[eqsmart] 远程调用', provider_conf, protocol)
        remote_call = Consumer(provider_conf).func_call_int(protocol)
        return json.loads(remote_call)
