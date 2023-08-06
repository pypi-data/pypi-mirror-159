#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from configparser import ConfigParser
from dataclasses import dataclass

from happy_python import HappyLog
from happy_python.happy_log import HappyLogLevel

hlog = HappyLog.get_instance()


@dataclass
class ZymodConfig:
    mod_name: str
    interval: int
    agent_host: str
    agent_port: int
    active: bool
    debug: int
    dry_run: bool
    token: str
    host: str
    headers: str
    unit: str
    chinese_name: str
    chart_type: str
    json_format: str
    file_path: str


class ZymodConfigParser:
    global hlog
    _filename: str

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def load(self, is_dry_run, is_verbose) -> ZymodConfig:
        conf = ConfigParser()
        conf.read(self._filename)

        if 'zymod' not in conf:
            raise Exception("配置文件缺少section")

        section = conf['zymod']

        _debug = section.getint('debug') if is_verbose is None else HappyLogLevel.DEBUG.value
        _dry_run = section.getboolean('dry_run') if is_dry_run is None else True

        if section.get('mod_name') is None:
            raise Exception("配置文件中mod_name为空")

        if section.get('active') is None:
            raise Exception("配置文件中active为空")

        if section.get('token') is None:
            raise Exception("配置文件中token为空")

        if section.get('host') is None:
            raise Exception("配置文件中host为空")

        if section.get('agent_host') is None:
            raise Exception("配置文件中agent_host为空")

        if section.get('agent_port') is None:
            raise Exception("配置文件中agent_port为空")

        if section.get('interval') is None:
            raise Exception("配置文件中缺少interval为空")

        config_json = {
            "host": section.get("host"),
            "active": section.get("active"),
            "debug": _debug,
            "dry_run": _dry_run,
            "interval": section.get("interval"),
            "mod_name": section.get("mod_name"),
            "headers": section.get("headers"),
            "unit": section.get("unit"),
            "chinese_name": section.get("chinese_name"),
            "chart_type": section.get("chart_type"),
        }
        mod_conf = ZymodConfig(mod_name=section.get('mod_name'),
                               active=section.getboolean('active'),
                               agent_host=section.get('agent_host'),
                               agent_port=section.getint('agent_port'),
                               debug=_debug,
                               dry_run=_dry_run,
                               interval=section.getint('interval'),
                               token=section.get('token'),
                               host=section.get('host'),
                               headers=section.get('headers'),
                               unit=section.get('unit'),
                               chinese_name=section.get('chinese_name'),
                               chart_type=section.get('chart_type'),
                               json_format=json.dumps(config_json),
                               file_path=self._filename
                               )

        hlog.set_level(mod_conf.debug)

        return mod_conf
