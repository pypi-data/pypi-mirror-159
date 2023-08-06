#
# Thanks to: https://github.com/msabramo/requests-unixsocket
#

import socket
import sys
from urllib.parse import splitport, unquote, urlparse

import requests
import urllib3
from requests.adapters import HTTPAdapter
# from requests.compat import unquote, urlparse

from wda_python import usbmux

try:
    import http.client as httplib
except ImportError:
    import httplib

DEFAULT_SCHEME = "http+usbmux://"


_usbmux = usbmux.Usbmux()

# The following was adapted from some code from docker-py
# https://github.com/docker/docker-py/blob/master/docker/transport/unixconn.py
class UsbmuxHTTPConnection(httplib.HTTPConnection, object):
    def __init__(self, usbmux_socket_url, timeout=60):
        """Create an HTTP connection to a unix domain socket
        :param usbmux_socket_url: A URL with a scheme of 'http+unix' and the
        netloc is a percent-encoded path to a unix domain socket. E.g.:
        'usbmux://539c5fffb18f2be0bf7f771d68f7c327fb68d2d9/status'
        """
        super(UsbmuxHTTPConnection, self).__init__('127.0.0.1',
                                                   timeout=timeout)
        self.usbmux_socket_url = usbmux_socket_url
        self.timeout = timeout
        self.sock = None

    def __del__(self):  # base class does not have d'tor
        if self.sock:
            self.sock.close()

    def connect(self):
        netloc = unquote(urlparse(self.usbmux_socket_url).netloc)
        udid, port = splitport(netloc)
        if not port:
            port = 8100 # WDA Default port
        if not udid:
            udid = _usbmux.get_single_device_udid()

        _device = _usbmux.device(udid)
        conn = _device.create_inner_connection(int(port))
        self.sock = conn._sock
        self.sock.settimeout(self.timeout)


class UsbmuxHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    def __init__(self, socket_path, timeout=60):
        super(UsbmuxHTTPConnectionPool, self).__init__('127.0.0.1',
                                                       timeout=timeout)
        self.socket_path = socket_path
        self.timeout = timeout

    def _new_conn(self):
        return UsbmuxHTTPConnection(self.socket_path, self.timeout)


class UsbmuxAdapter(HTTPAdapter):
    def __init__(self, timeout=60, pool_connections=25, *args, **kwargs):
        super(UsbmuxAdapter, self).__init__(*args, **kwargs)
        self.timeout = timeout
        self.pools = urllib3._collections.RecentlyUsedContainer(
            pool_connections, dispose_func=lambda p: p.close())

    def get_connection(self, url, proxies=None):
        proxies = proxies or {}
        proxy = proxies.get(urlparse(url.lower()).scheme)

        if proxy:
            raise ValueError('%s does not support specifying proxies' %
                             self.__class__.__name__)

        with self.pools.lock:
            pool = self.pools.get(url)
            if pool:
                return pool

            pool = UsbmuxHTTPConnectionPool(url, self.timeout)
            self.pools[url] = pool

        return pool

    def request_url(self, request, proxies):
        return request.path_url

    def close(self):
        self.pools.clear()

# session对象也是一个非常常用的对象，这个对象代表一次用户会话。一次用户会话的含义是：
# 从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开为止，这个过程就是一次会话。
# session通常用于跟踪用户的会话信息，如判断用户是否登录系统，或者在购物车应用中，用于跟踪用户购买的商品等。
# session范围内的属性可以在多个页面的跳转之间共享。一旦关闭浏览器，即session结束，session范围内的属性将全部丢失。
class Session(requests.Session):
    def __init__(self, url_scheme=DEFAULT_SCHEME, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 修改requests库session默认连接数 
        # https://lequ7.com/guan-yu-python-xiu-gai-requests-ku-session-mo-ren-lian-jie-shu.html
        self.mount(url_scheme, UsbmuxAdapter())

        # set NO_PROXY to skip proxy check
        # For some computer urllib.request.proxy_bypass is very slow
        self.proxies.update({"no_proxy": "*"})
        self.trust_env = False
