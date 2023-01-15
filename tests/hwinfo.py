import os
import platform
import socket
import subprocess
import time
import random
import asyncio
import functools
import sys
from tempfile import gettempdir

import http.client
import psutil

import speedtest as speed

_state = 'release'
_version = ['1', '4', '4']
git = 'https://github.com/Ulbwaa/HW-Info'
projects = 'https://ulbwa.suicide.today/projects/'


class tools:
    @staticmethod
    def clearConsole():
        if psutil.WINDOWS:
            return os.system("cls")
        else:
            return os.system("clear")

    @staticmethod
    def checkOutput(command: str):
        try:
            return subprocess.check_output(command, shell=True,
                                           universal_newlines=True,
                                           stderr=subprocess.DEVNULL)

        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def run_sync(func, *args, **kwargs):
        """Run a non-async function in a new
        thread and return an awaitable"""
        return asyncio.get_event_loop()\
            .run_in_executor(None,
                             functools.partial(func,
                                               *args,
                                               **kwargs))

    @staticmethod
    def run_async(coro):
        """Run an async function as a
        non-async function, blocking till it's done"""
        return asyncio.run(coro)

    @staticmethod
    def remove_non_ASCII(text):
        otpt_str = str()

        for i in text:
            num = ord(i)
            if num >= 0:
                if num <= 127:
                    otpt_str = otpt_str + i

        return otpt_str


class hwinfoError(Exception):
    def __init__(self, text):
        self.txt = text


def _speedtester(htmlMarkup=True):
    tester = speed.Speedtest()
    tester.get_best_server()
    tester.download(threads=None)
    tester.upload(threads=None)

    download = round(tester.results.dict()["download"] / 2 ** 20)
    upload = round(tester.results.dict()["upload"] / 2 ** 20)
    ping = round(tester.results.dict()["ping"])
    server = tester.results.dict()["server"]["country"] + ', ' + tester.results.dict()["server"]["name"]  # noqa

    output = 'HW-Info SpeedTester\n' \
             '-------------------\n'

    if htmlMarkup:
        output += f'<b>Download</b>: <code>{download} MiB/s</code>\n' \
                  f'<b>Upload</b>: <code>{upload} MiB/s</code>\n' \
                  f'<b>Ping</b>: <code>{ping}ms</code>\n' \
                  f'<b>Server</b>: <code>{server}</code>'
    else:
        output += f'Download: {download} MiB/s\n' \
                  f'Upload: {upload} MiB/s\n' \
                  f'Ping: {ping}ms\n' \
                  f'Server: {server}'

    return output


async def speedtest(htmlMarkup=True):
    return await tools.run_sync(_speedtester, htmlMarkup)


def _hwinfo(htmlMarkup: bool = True, showThreadsPercentage: bool = True, showIP: bool = True) -> str:  # noqa: e501
    if psutil.WINDOWS:
        command = 'powershell neofetch --stdout --config none'
    else:
        if 'aws' not in platform.platform():
            command = 'neofetch --stdout --config none'
        else:
            # Привет от детей хероку сука!!!
            command = 'curl -Ls https://github.com/dylanaraps/neofetch/raw/master/neofetch | bash -s -- --stdout --config none'  # noqa: e501

    output = tools.checkOutput(command)

    try:
        if output:
            fetch = output.split('- \n')[0] + '- '
            out = output.split('- \n')[0] + '- '

            for i in output.split('- \n')[1].split('\n'):
                if i != '' and i != ' ':
                    j = i.split(': ')[0]
                    y = i.split(': ')[1]

                    if j == 'OS' and psutil.WINDOWS:
                        fetch += f'\n{j}: {tools.remove_non_ASCII(y)}'
                        continue

                    if j == 'CPU':
                        fetch += f'\n{j}: {y}'
                        fetch += f'\nCPU Load: {_CPULoad()}'
                        fetch += f'\nCPU Architecture: {_CPUArch()}'
                        continue

                    elif j == 'Memory':
                        fetch += f'\n{j}: {y}'
                        fetch += f'\nSWAP: {_swap()}'
                        fetch += f'\nStorage: {_storage()}'
                        continue

                    elif j == 'Kernel':
                        fetch += f'\n{j}: {y}'

                        if _users():
                            fetch += f'\nUsers: {_users()}'

                        if showIP:
                            if not _IPs_Check():
                                fetch += f'\nGlobal IP: {_http_ip()}'
                                fetch += f'\nLocal IP: {_LocalIP()}'
                            else:
                                fetch += f'\nLocal / Global IP: {_http_ip()}'

                        if _mother_board():
                            fetch += f'\nMotherboard: {_mother_board()}'

                        continue

                    elif j == 'Uptime':
                        fetch += f'\n{j}: {y}'
                        fetch += f'\nBoot Time: {_BootTime()}'
                        continue

                    elif j == 'Host' and 'Hackintosh' in y:
                        pass

                    else:
                        fetch += f'\n{j}: {y}'
                        continue

            fetch += f'\nPython version: {_python_version()}'

            if _where_python():
                fetch += f'\nPython path: {_where_python()}'

            if _java_version():
                fetch += f'\nJAVA version: {_java_version()}'

            if _where_java():
                fetch += f'\nJAVA path: {_where_java()}'

            fetch += f'\nHW-Info version: {_hwinfo_version()}'

            if showThreadsPercentage:
                fetch += '\n'
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
                    fetch += f'\nThread {i + 1} load: {round(percentage)}%'

            for i in fetch.split('- \n')[1].split('\n'):
                if i != '' and i != ' ':
                    j = i.split(': ', maxsplit=1)[0]
                    y = i.split(': ', maxsplit=1)[1]
                    if htmlMarkup:
                        out += f'\n<b>{j}</b>: <code>{y}</code>'

                    else:
                        out += f'\n{j}: {y}'
                else:
                    out += '\n'

            if htmlMarkup and random.randint(1, 3) == 3:
                out += '\n\n<b>HW-Info</b> is an <b>open source project</b>. ' \
                    'You can use this module in your projects by downloading it on <b>GitHub!</b> ' \
                    f'Link to download source: <code>{git}</code>. ' \
                    f'My other projects are available for review at the following link: ' \
                    f'<code>{projects}</code>.'

            return out
        else:
            if htmlMarkup:
                return '<b>Neofetch is not installed!</b>'
            else:
                return 'Neofetch is not installed!'

    except Exception as e:
        if psutil.WINDOWS:
            if htmlMarkup:
                return '<b>Neofetch is not installed!</b>'
            else:
                return 'Neofetch is not installed!'
        else:
            raise hwinfoError(e)


async def hwinfo(htmlMarkup: bool = True, showThreadsPercentage: bool = True, showIP: bool = True):
    return await tools.run_sync(_hwinfo,
                                htmlMarkup,
                                showThreadsPercentage,
                                showIP)


def _IPs_Check():
    return str(_LocalIP()) == str(_http_ip())


def _LocalIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except ConnectionError:
        ip = '127.0.0.1'

    return str(ip)


def _users():
    try:
        users = []

        for user in psutil.users():
            if str(user.name) not in users:
                users.append(str(user.name))

        if users == [] or len(users) <= 0:
            return False
    except (Exception, BaseException):
        return False

    return ', '.join(users)


def _CPUArch():
    return platform.uname().machine.replace('_', '-')


def _CPULoad():
    return f'{round(psutil.cpu_percent(0.5))}%'


def _BootTime():
    return time.ctime(psutil.boot_time())


def _swap():
    all_ = round(psutil.swap_memory().total / 1e+6)
    used = round(psutil.swap_memory().used / 1e+6)

    return f'{used}MiB / {all_}MiB '


def _storage():
    all_ = round(psutil.disk_usage('/.').total / 1e+9)
    used = round(psutil.disk_usage('/.').used / 1e+9)

    return f'{used}GiB / {all_}GiB '


def _python_version():
    return sys.version.split()[0]


def _java_version():
    command = 'java -version 2>&1 | awk -F[\\\"_] \'NR==1{print $2}\''
    JAVA_temp = tools.checkOutput(command)

    if JAVA_temp:
        try:
            return JAVA_temp.split('\n')[0]
        except IndexError:
            return False
    else:
        return False


def _http_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return conn.getresponse().read().decode('UTF8')


def _hwinfo_version():
    return ".".join(_version) + "-{}".format(_state)


def _mother_board():
    if psutil.WINDOWS:
        command = 'wmic baseboard get Manufacturer'
        mother = tools.checkOutput(command)

        if mother:
            manuf = mother.split('\n')[2]
        else:
            return False

        command = 'wmic baseboard get product'
        mother = tools.checkOutput(command)

        if mother:
            module = mother.split('\n')[2]
        else:
            return False

        return manuf + ' ' + module
    else:
        return False


def _where_python():
    return sys.executable


def _where_java():
    command = 'where java'
    output = tools.checkOutput(command)

    if output:
        try:
            return output.split('\n')[0]
        except IndexError:
            return False
    else:
        command = 'whereis java'
        output = tools.checkOutput(command)

        if output:
            try:
                return output.split('\n')[0].split(' ')[1]
            except IndexError:
                return False
        else:
            return False


def _install_neofetch():
    if psutil.WINDOWS:
        from urllib.request import urlretrieve
        SCOOP_INSTALLER = "https://me.rf0x3d.su/MzM4Mw%3D%3D%2A_%2A7e4d.ps1"
        filename = gettempdir() + "install_scoop.ps1"
        urlretrieve(SCOOP_INSTALLER,
                    filename)
        command = 'powershell neofetch --stdout'
        print("Installing Scoop...")
        output = tools.checkOutput(command)
        if output:
            print("Scoop installed!")
        command = 'powershell scoop install git neofetch'
        print("Installing Neofetch...")
        output = tools.checkOutput(command)
        if output:
            print("Neofetch installed!")
        os.remove(filename)
        return True
    else:
        return True


if __name__ == '__main__':
    tools.clearConsole()
    print('Loading hwinfo...')
    hw = tools.run_async(hwinfo(False, False))
    if hw == "Neofetch is not installed!" and psutil.WINDOWS:
        install = input("Neofetch is not installed. Would you like to install him? (y/N)")
        if install.lower() in ("y", "д", "1"):
            installation = _install_neofetch()
            if installation:
                hw = tools.run_async(hwinfo(False, False))
            else:
                raise hwinfoError("Something went wrong during Neofetch installation")
    tools.clearConsole()
    print(hw)
    exit(0)
