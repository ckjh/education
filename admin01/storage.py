import os
from django.conf import settings
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client

from education.settings import BASE_DIR


class FastDFSStroage(Storage):
    """定义FastDFS客户端类"""

    def __init__(self):
        self.conf = os.path.join(BASE_DIR, 'fdfs.conf')
        self.host = 'http://116.62.155.103:8888'

    def _open(self, name, mode='rb'):
        """
        打开文件
        :param name:
        :param mode:
        :return:
        """
        pass

    def _save(self, name, content):
        """
        保存文件
        :param name: 传入文件名
        :param content: 文件内容
        :return:保存到数据库中的FastDFSDE文件名
        """
        client = Fdfs_client(self.conf)
        ret = client.upload_by_buffer(content.read())
        if ret.get("Status") != "Upload successed.":
            raise Exception("upload file failed")
        file_name = ret.get("Remote file_id")
        return file_name

    def exists(self, name):
        """
        检查文件是否重复, FastDFS自动区分重复文件
        :param name:
        :return:
        """
        return False

    def url(self, name):
        """
        获取name文件的完整url
        :param name:
        :return:
        """
        return self.host + name
