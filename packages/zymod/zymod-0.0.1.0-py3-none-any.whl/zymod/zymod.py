#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import json
import signal
import time
from argparse import ArgumentParser
from pathlib import Path

import grpc
from happy_python import HappyLog

from zymod import ZymodConfig
from proto import zhiyan_rpc_pb2
from proto import zhiyan_rpc_pb2_grpc
from zymod.zymod_config import ZymodConfigParser


# noinspection PyUnusedLocal
def interrupt_from_keyboard_handler(signum, frame):
    print('\n检测到用户发送终止信号，退出程序中......')
    exit(1)


def get_linux_kernel_version():
    f = open("/proc/version", encoding="utf-8")
    version = f.read().split(" ")[2]
    f.close()
    split_version = version.split(".")
    return split_version[0]+"."+split_version[1]


class Zymod:
    hlog = HappyLog.get_instance()
    mod_conf: ZymodConfig
    parser: ArgumentParser

    def __init__(self, mod_config: Path, is_dry_run_from_cmd_args, is_verbose_from_cmd_args):
        signal.signal(signal.SIGINT, interrupt_from_keyboard_handler)

        if not mod_config.exists():
            self.hlog.error('智眼模块配置文件（%s）不存在' % mod_config)
            exit(1)

        self.hlog = HappyLog.get_instance(str(mod_config))

        is_dry_run = True if is_dry_run_from_cmd_args else None
        is_verbose = True if is_verbose_from_cmd_args else None
        self.mod_conf = ZymodConfigParser(str(mod_config)).load(is_dry_run, is_verbose)

    def register(self, content: dict):
        while True:
            # 第一次注册
            register_code = self.register_module(content=content)
            if not register_code:
                # 不成功则每隔10秒进行一次注册
                while True:
                    time.sleep(10)
                    upload_code = self.upload_data(content=content)
                    # 注册成功取消循环
                    if upload_code:
                        break
            else:
                break

    def register_module(self, content: dict) -> bool:
        register = True

        fn_name = 'mod_send_request_grpc'

        hlog = HappyLog.get_instance()
        hlog.enter_func(fn_name)

        hlog.var('name', self.mod_conf.mod_name)
        hlog.var('datetime', int(time.time()))

        json_str_content = json.dumps(content)

        hlog.debug('content=\n%s' % json_str_content)

        if self.mod_conf.dry_run:
            hlog.debug('zymod：试运行中，不进行注册.....')
        else:
            hlog.debug('zymod：正在上传到agent.....')
            channel = grpc.insecure_channel(self.mod_conf.agent_host + ':' + str(self.mod_conf.agent_port))
            try:
                client = zhiyan_rpc_pb2_grpc.ZhiYanServiceStub(channel)

                response = client.zyregistermod(zhiyan_rpc_pb2.ZhiYanRegisterModuleRequest(
                    name=self.mod_conf.mod_name,
                    content=json_str_content,
                    token=self.mod_conf.token,
                    host=self.mod_conf.host,
                    config=self.mod_conf.json_format.encode("utf-8").decode("unicode_escape"),
                    kernel_version=get_linux_kernel_version()
                ))

                hlog.info('code:' + response.code + '\tmessage:' + response.message)

                if response.code != '1':
                    register = True
                else:
                    register = False
            except Exception:
                hlog.error('code:' + "1" + '\tmessage:' + 'Agent连接失败,十秒后进行下一次注册')
                register = False

        hlog.exit_func(fn_name)

        return register

    def upload_data(self, content: dict) -> bool:
        global fn
        register = True

        fn_name = 'mod_send_request_grpc'

        hlog = HappyLog.get_instance()
        hlog.enter_func(fn_name)

        hlog.var('name', self.mod_conf.mod_name)
        hlog.var('datetime', int(time.time()))

        json_str_content = json.dumps(content)

        hlog.debug('content=\n%s' % json_str_content)

        if self.mod_conf.dry_run:
            hlog.debug('zymod：在不做任何更改的情况下试运行.....')
        else:
            hlog.debug('zymod：正在上传到agent.....')
            channel = grpc.insecure_channel(self.mod_conf.agent_host + ':' + str(self.mod_conf.agent_port))
            try:
                client = zhiyan_rpc_pb2_grpc.ZhiYanServiceStub(channel)
                response = client.zymod(zhiyan_rpc_pb2.ZhiYanRequest(
                    name=self.mod_conf.mod_name,
                    datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    host=self.mod_conf.host,
                    content=json_str_content,
                    kernel_version=get_linux_kernel_version()
                ))
                time.sleep(self.mod_conf.interval)

                hlog.info('code:' + response.code + '\tmessage:' + response.message)

                if response.code == '1':
                    register = False
                elif response.code == '10':
                    replace_json = response.message.replace('\\', '').replace('"{', '{').replace('}"', '}')
                    format_json = json.loads(replace_json)

                    items = format_json['Config'].items()

                    conf = configparser.ConfigParser()
                    conf.read(self.mod_conf.file_path)
                    for key, value in items:
                        conf.set("zymod", str(key), str(value).replace('\'', '"').replace('%', '%%'))
                        fn = open(self.mod_conf.file_path, 'w')
                        conf.write(fn)

                    fn.close()

                    register = False
                else:
                    register = True
            except Exception as ex:
                hlog.error('code:' + "1" + '\tmessage:' + 'Agent连接失败,十秒后进行下一次尝试\tErrorMessage:' + str(ex))
                register = False

        hlog.exit_func(fn_name)

        return register

    @staticmethod
    def build_help_parser(prog: str, description: str, version: str, mod_config_file_path: str) -> ArgumentParser:
        parser = ArgumentParser(prog=prog + ' ' + version, description=description)
        parser.add_argument('-c',
                            '--conf',
                            help='指定智眼模块配置文件',
                            dest='mod_conf',
                            type=str,
                            default=mod_config_file_path)
        parser.add_argument('-n',
                            '--dry-run',
                            help='在不做任何更改的情况下试运行，通常和"-v"参数一起使用',
                            dest='dry_run',
                            action='store_true')
        parser.add_argument('-v',
                            '--verbose',
                            help='显示详细信息',
                            dest='verbose',
                            action='store_true')
        parser.add_argument('-V',
                            '--version',
                            help='显示版本信息',
                            action='version',
                            version='zymod version: %(prog)s/v' + version)

        return parser

    @staticmethod
    def build_help(prog: str, description: str, version: str, mod_config_file_path: str):
        parser = Zymod.build_help_parser(prog=prog,
                                         description=description,
                                         version=version,
                                         mod_config_file_path=mod_config_file_path,
                                         )
        return parser.parse_args()

    @staticmethod
    def build_help_with_parser(parser: ArgumentParser):
        return parser.parse_args()
