"""Classes for reading/writing data from the pod store file. Used by the
`pod_store.store.Store` coordinating class.

Delegating the file handling behavior to these classes allows swapping in a different
file handler without changing the core `Store` class to handle encrypted vs.
unenecrypted store files.
"""
import json
import os
from abc import ABC, abstractmethod

from .exc import GPGCommandError
from .util import run_shell_command


class StoreFileHandler(ABC):
    """`StoreFileHandler` classes are used to read/write data from the store file.

    They should implement these methods:

        def read_data(self):
            ...

        def write_data(self, data: dict):
            ...

    Attributes
    ----------
    store_file_path (str): file system location of the store file
    """

    def __init__(self, store_file_path: str) -> None:
        self.store_file_path = store_file_path

    @classmethod
    def create_store_file(
        cls, store_file_path: str, store_data: dict = None, **kwargs
    ) -> None:
        """Creates an initial store file with the store data provided.

        If no store data is passed in, the store will be initialized as an empty dict.
        """
        store_data = store_data or {}

        file_handler = cls(store_file_path=store_file_path, **kwargs)
        file_handler.write_data(store_data)

    @abstractmethod
    def read_data(self) -> dict:
        pass

    @abstractmethod
    def write_data(self, data: dict) -> None:
        pass


class EncryptedStoreFileHandler(StoreFileHandler):
    """Class for reading/writing data from an encrypted store file.

    Data is encrypted/decrypted using GPG public/private keys.

    Attributes
    ----------
    store_file_path (str): store file location

    _gpg_id (str): used to look up the GPG keys in the keyring
    """

    def __init__(self, gpg_id: str, *args, **kwargs) -> None:
        self._gpg_id = gpg_id
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f"<EncryptedStoreFileHandler({self.store_file_path!r})>"

    def read_data(self) -> dict:
        """Retrieve encrypted json data from the store file."""

        gpg_cmd = f"gpg -d {self.store_file_path}"
        decrypted = run_shell_command(gpg_cmd)
        return json.loads(decrypted)

    def write_data(self, data: dict) -> None:
        """Write encrypted json data to the store file."""
        try:
            with open(self.store_file_path, "rb") as f:
                existing_data = f.read()
            os.remove(self.store_file_path)
        except FileNotFoundError:
            existing_data = b""

        tmp_file = os.path.join(os.path.dirname(self.store_file_path), ".tmp")
        with open(tmp_file, "w") as f:
            json.dump(data, f)

        try:
            gpg_cmd = (
                f"gpg --output {self.store_file_path} "
                "--encrypt "
                f"--recipient {self._gpg_id} "
                f"{tmp_file}"
            )
            run_shell_command(gpg_cmd)
        except Exception as err:
            os.remove(tmp_file)
            with open(self.store_file_path, "wb") as f:
                f.write(existing_data)
            raise GPGCommandError(str(err))

        os.remove(tmp_file)


class UnencryptedStoreFileHandler(StoreFileHandler):
    """Class for reading/writing data from an unencrypted store file.

    store_file_path (str): file system location of the json file that holds store data.
    """

    def __repr__(self) -> None:
        return f"<UnencryptedStoreFileHandler({self.store_file_path!r})>"

    def read_data(self) -> dict:
        """Retrieve unencrypted json data from the store file."""
        with open(self.store_file_path) as f:
            return json.load(f)

    def write_data(self, data: dict) -> None:
        """Write unencrypted json data to the store file."""
        with open(self.store_file_path, "w") as f:
            json.dump(data, f, indent=2)
