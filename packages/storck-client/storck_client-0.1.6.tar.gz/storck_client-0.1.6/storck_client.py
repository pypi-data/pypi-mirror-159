import requests
import os
import typing
import json
import hashlib
import shutil
from pathlib import Path
import typing


class StorckClient:
    def __init__(
        self,
        api_host: str = "http://localhost:8000",
        user_token: str = None,
        workspace_token: str = None,
        storck_root_dir: str = None
    ):
        """
        The main class for creating connection to storck database.

        :param api_host: The adress of the storck instance
        :param user_token: the token of the user, if not defined, the environment variable STORCK_USER_TOKEN will be used
        :param user_token: the token of the workspace, if not defined, the environment variable STORCK_WORKSPACE_TOKEN will be used
        """
        self.api_host = os.getenv("STORCK_API_HOST", default=api_host)
        self.user_token = user_token or os.getenv("STORCK_USER_TOKEN")
        self.workspace_token = workspace_token or os.getenv("STORCK_WORKSPACE_TOKEN")
        srd =  storck_root_dir or os.getenv("STORCK_ROOT_DIR")
        srd_path = Path(storck_root_dir) if storck_root_dir is not None else None
        self.storck_root_dir = srd_path

    def auth_verify(self) -> dict:
        """

        Check whether user exists in storck.
        """
        self._is_authorized()
        return self._post(
            "/api/auth", headers={"Authorization": "Token {}".format(self.user_token)}
        )

    def set_workspace_token(self, workspace_token: str):
        """
        Will override the current workspace_token, and also environment variable
        """
        self.workspace_token = workspace_token
        os.putenv("STORCK_WORKSPACE_TOKEN", self.workspace_token)

    def create_workspace(self, name:str) -> dict:
        """
        Will create a workspace with given name.
        """
        self._is_authorized()
        content = self._post(
            "/api/workspace",
            data={"name": name},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["data"]

    def get_workspaces(self) -> dict:
        """
        Gets the list of current workspaces


       :return: dict of workspaces
        """
        self._is_authorized()
        content = self._get(
            "/api/workspaces",
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["data"]["workspaces"]

    def search(self, search_dict:typing.Union[str,dict]=None) -> dict:
        """
        Searches for files. If name_contains will be provided, looks for a filename containig gie string.
        If search_dict is provided, will use it as the JSON encoded string query.

        .. highlight:: python
        .. code-block:: python

            #this will return all of the files in the workspace
            client.search()
            #this will return all files under that path string in their path
            client.search(search_dict={'stored_path':'/some/path/or/name/part')
            #this will return all files containing the partial text of the path string in their path
            client.search(search_dict={'stored_path__contains':'/some/path/or/name/part')
            #this will return a file with id equal to 345
            client.search(search_dict={"id":345})
            #this will search for the file with the metada value ramp_speed equal to 5
            client.search(search_dict={"metadata__ramp_speed":5})
            #this will search for the file with the metada value ramp_speed greater or equal to 5
            client.search(search_dict={"metadata__ramp_speed__gte":5})


        :param search_dict: A stringified JSON containing relevant `django query <https://docs.djangoproject.com/en/4.0/ref/models/querysets/>`_ .
            The contents will be unpacked as python dict and fed to django's `filter() <https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter>`_ method
            This json will be unpacked to python dict, which will be unpacked as arguments of filter function in django.
            If you want to query the metada fields you have to name the keys starting with "metadata" with two underscores (se example) and then proceed with the `jsonfield query <https://docs.djangoproject.com/en/4.0/topics/db/queries/#querying-jsonfield>`_ .
        :return: list of files matching the query
        """
        self._is_authorized()
        self._is_workspace_set()
        query = {"token": self.workspace_token}
        if search_dict is not None:
            if isinstance(search_dict, dict):
                search_dict = json.dumps(search_dict)
            elif not isinstance(search_dict, str):
                raise TypeError("Search dict should of type str or dict.")
            query["query_search"] = search_dict
        #@TODO this option no longer exists
        content = self._get(
            "/api/search",
            query=query,
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["files"]

    def check_file(self, filepath:str, fhash:str) -> dict:
        """
        Searches for a file under the filepath, with specific fhash.

        :param filepath: A storck filepath
        :param fhash: A file hash
        :return: list of files matching the query
        """
        squery = {"hash": fhash, "stored_path":filepath}
        return self.search(search_dict=squery)

    def get_info(self, file_id:int=None, path:str=None) -> dict:
        """
        Gets detailed information about the file.

        :param file_id: id of the file.
        :param path: database path of the file
        """
        self._is_authorized()
        self._is_workspace_set()
        content = self._get(
            "/api/info",
            query={
                "path": path,
                "id": file_id,
                "token": self.workspace_token,
            },
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["file"]

    def send_file_content(self, filename, path, data, query):
        return self._post(
            "/api/file",
            data=data,
            query=query,
            files={"file": open(filename, "rb")},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )

    def upload_file(self,
                    filename:str,
                    path:str=None,
                    metadata_str:str=None,
                    file_hash:str=None,
                    local_transfer=False
        ) -> dict:
        """
        Uploads the file to storck.

        :param filename: Path to the file on the client side.
        :param path: Optional database path to be used in storck. If not provided filename will be used instead.
        :param metadata_str: a metadata json string
        """
        self._is_authorized()
        self._is_workspace_set()
        query={"token": self.workspace_token}
        if file_hash:
            query['hash'] = file_hash
        data = {"path": path or filename}
        if metadata_str is not None:
            data["metadata"] = metadata_str
        if local_transfer:
            data['local'] = True
            data['local_path'] = str(filename)
            return self._post(
                path = "/api/file",
                query={"token": self.workspace_token},
                data=data,
                headers={"Authorization": "Token " + self.user_token},
                )
        else:
            return self.send_file_content(filename, path, data, query)

    def get_file_content(self, file_id: int) -> bytes:
        """
        Downloads the content of the file.

        :param file_id: Id of the file to downloaded.
        """
        self._is_authorized()
        self._is_workspace_set()
        return self._get_raw(
            "/api/file",
            query={"id": file_id, "token": self.workspace_token},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )

    def download_file(
            self,
            file_id : int,
            target_path: typing.Union[str, Path],
            local_transfer=False
    ):
        if not isinstance(target_path, Path):
            if isinstance(target_path, str):
                target_path = Path(target_path)
            else:
                raise ValueError
        self._is_authorized()
        self._is_workspace_set()
        if local_transfer:
            content = self._get(
                "/api/file",
                query={
                    "id": file_id,
                    "token": self.workspace_token,
                },
                headers={"Authorization": "Token {}".format(self.user_token)},
            )
            filepath = content['file']
            shutil.copy(self.storck_root_dir/filepath, target_path)
        else:
            file_content = self.get_file_content(file_id)
            with open(target_path, 'wb') as f:
                f.write(file_content)



    def add_user_to_workspace(self, user_id: int):
        """
        Adds users to workspace.

        :param user_id: the id of the user to be added to the workspace.
        """
        self._is_authorized()
        self._is_workspace_set()
        content = self._post(
            "/api/workspace/user",
            data={"user_id": user_id, "token": self.workspace_token},
            headers={"Authorization": "Token {}".format(self.user_token)},
        )
        return content["data"]

    def _is_authorized(self):
        if self.user_token is None:
            raise Exception("You need to provide user token")

    def _is_workspace_set(self):
        if self.workspace_token is None:
            raise Exception("You need to provide workspace token")

    def _post(self, path, query=None, data=None, files=None, headers=None):
        content = requests.post(
            "{}{}".format(self.api_host, path),
            data=data,
            files=files,
            params=query,
            headers=headers,
        )
        content.raise_for_status()
        return content.json()

    def _get(self, path, query=None, headers=None):
        content = requests.get(
            "{}{}".format(self.api_host, path), params=query, headers=headers
        )
        content.raise_for_status()
        return content.json()

    def _get_raw(self, path, query=None, headers=None):
        content = requests.get(
            "{}{}".format(self.api_host, path),
            params=query,
            headers=headers,
            stream=True,
        )
        content.raise_for_status()
        return content.raw.read()


def md5sum_hash(fpath):
        file_hash = hashlib.md5()
        with open(fpath, 'rb') as f:
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)
        md5 = file_hash.hexdigest()
        return md5
