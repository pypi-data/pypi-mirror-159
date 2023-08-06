import json
import subprocess
import os
import re
import sys


def show_json(data: dict, sort_keys=False):
    try:
        print(json.dumps(data, sort_keys=sort_keys, indent=4, separators=(', ', ': '), ensure_ascii=False))
    except:
        if isinstance(data, dict):
            for k, v in data.items():
                print(k, ' --- ', v)
        else:
            for k, v in data:
                print(k, ' --- ', v)


def show_ls(data: list, ks=None):
    for dc in data:
        if ks:
            if isinstance(ks, str):
                ks = [ks]
            d = [dc.get(k) for k in ks]
        else:
            d = dc
        print(d)


class PackageVesionUtils:
    @staticmethod
    def get_latest_version(package):
        """
        检查已安装的package是否最新
        :param package:pip包
        :return: is_latest, latest_version, msg
        """
        check = f'pip install {package}=='
        p = subprocess.Popen(check, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        assert b'from versions:' in error, f"命令[{check}]运行结果有误!"
        e_str = error.decode('utf-8')
        reg = re.compile(r':(.*?)\)')
        match = reg.search(e_str)
        assert match, '正则match结果为空!'
        group_1 = match.group(1)
        try:
            latest_version = group_1.rsplit(',', 1)[-1].strip()
        except Exception as e:
            raise ValueError(f"正则解析latest_version失败? group_1: {group_1}, error: {e}")
        return latest_version

    @staticmethod
    def get_current_version(package):
        """
        检查已安装的package是否最新
        :param package:pip包
        :return: is_latest, latest_version, msg
        """
        if sys.platform == 'win32':
            cmd1 = 'findstr'
        else:
            cmd1 = 'grep'

        check = f'pip list | {cmd1} {package}'
        p = subprocess.Popen(check, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        assert output, f'请确定您是否已安装了{package}包? 尝试: [pip install {package}]'
        text = output.decode('utf-8')
        text = text.replace('\r\n', '\n')
        version_key = 'version'
        reg = re.compile(rf'^{package} *(?P<{version_key}>\d+\.\d+\.\d+) *$')
        match = reg.search(text)
        current_version = match.group(version_key)
        return current_version

    @staticmethod
    def compare_version(current_version, latest_version):
        """
        检查已安装的package是否最新
        即current_version和latest_version是否相同
        """
        if latest_version == current_version:
            is_latest = True
        else:
            is_latest = False
        msg = f"is_latest: {is_latest} | current_version: {current_version} | latest_version: {latest_version}"
        return is_latest, msg

    @staticmethod
    def check_version_by_package_name(package_name):
        """
        检查已安装的package是否最新
        即current_version和latest_version是否相同
        """
        current_version = PackageVesionUtils.get_current_version(package_name)
        last_version = PackageVesionUtils.get_latest_version(package_name)
        is_latest, msg = PackageVesionUtils.compare_version(current_version, last_version)
        return is_latest, current_version, last_version, msg


package_version_utils = PackageVesionUtils()
