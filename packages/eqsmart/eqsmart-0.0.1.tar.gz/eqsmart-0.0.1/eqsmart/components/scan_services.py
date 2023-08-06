"""
扫描服务列表
"""
import os
import sys
import importlib


def scan_dir(path):
    """
    扫描服务列表路径下服务文件
    :param path: 待扫描路径（排除 . _ 开头的文件）
    :return: 服务列表
    """
    file_list = {'func': []}
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(path + '/' + file):
            if file[0] != '.' and file[0] != '_':
                files_son = scan_dir(path + '/' + file)
                file_list[file] = files_son
        else:
            if file[0] != '.' and file[0] != '_':
                if file[-3:] == '.py' and file[0] != '_':
                    file_list['func'].append(file[:-3])
    return file_list


def load_services_class(services, son_module=''):
    """
    读取服务对象
    :return: 服务对象列表
    """
    services_class = {}
    for service in services:
        if not hasattr(services_class, service):
            services_class[service] = {}
        for op in services[service]:
            if op == 'func':
                common_service = CommonService()
                for func in services[service][op]:
                    module_name = (service + '.' + func) if son_module == '' else (
                            son_module + '.' + service + '.' + func)
                    func_name = importlib.import_module(module_name)
                    setattr(common_service, func, func_name.service)
                    if not hasattr(services_class[service], op):
                        services_class[service]['func'] = {}
                    services_class[service]['func'] = common_service
            else:
                son_module_name = service if son_module == '' else (son_module + '.' + service)
                services_class[service][op] = load_services_class({op: services[service][op]}, son_module_name)[op]
    return services_class


class CommonService(object):
    """
    公共对象，用于加载服务方法
    """
    pass


class ScanServices:
    def __init__(self, path):
        sys.path.append(path)
        self.scan_path = path
        self.services = {}

    def get_services_new(self):
        """
        服务名扫描
        :return: 服务名列表
        """
        services = scan_dir(self.scan_path)
        del services['func']
        self.services = services
        return services

    def get_services_class_new(self):
        """
        服务对象加载
        :return:
        """
        services_class = load_services_class(self.services)
        return services_class

    def get_services(self):
        """
        读取服务列表
        :return: 服务、方法的字典
        """
        service_list = []
        files = os.listdir(self.scan_path)
        if len(files) == 0:
            return service_list
        for item in files:
            if os.path.isdir(self.scan_path + '/' + item):
                if item[0] != '.' and item[0] != '_':
                    service_list.append(item)
        services = {}
        for service in service_list:
            func_file_path = self.scan_path + '/' + service
            func_files = os.listdir(func_file_path)
            func_list = []
            for f in func_files:
                if os.path.isfile(func_file_path + '/' + f):
                    if f[-3:] == '.py' and f[0] != '_':
                        func_list.append(f[:-3])
            services[service] = func_list
        self.services = services
        return services

    def get_services_class(self):
        """
        读取服务对象
        :return: 服务对象列表
        """
        services_class = {}
        for service in self.services:
            common_service = CommonService()
            for func in self.services[service]:
                func_name = importlib.import_module(service + '.' + func)
                setattr(common_service, func, func_name.service)
            services_class[service] = common_service
        return services_class


def main():
    res = ScanServices('../').get_services_new()
    print(res)


if __name__ == '__main__':
    main()
