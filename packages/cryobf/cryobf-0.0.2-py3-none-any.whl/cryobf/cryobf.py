from enum import IntEnum
from stat import S_IRGRP, S_IROTH, S_IXUSR, S_IWUSR, S_IRUSR
from pathlib import Path


class ContentType(IntEnum):
    Directory = 1
    File = 2


class CryoBfFile:

    def __init__(self, filepath: Path):
        self._stream = None

        self._file_version = None
        self._header_size = None
        self._top_addr = None
        self._files = None
        self._stream = filepath.open("rb")
        if filepath.exists():
            self.read_file_contents()

    @property
    def top_addr(self):
        return self._top_addr

    @property
    def file_version(self):
        return self._file_version

    @property
    def files(self):
        return self._files

    def read_file_contents(self):
        self.read_header()
        self.read_table_of_contents()

    def read_header(self) -> None:
        self._stream.seek(0)
        data = self._stream.read(0x20)
        self._file_version = data[:15].decode()
        self._top_addr = int.from_bytes(data[-8:-4], "little")
        self._header_size = int.from_bytes(data[-4:], "little")

    def read_table_of_contents(self):
        self._stream.seek(self.top_addr)
        self._files = self.read_binary_file_tree()

    def read_binary_file_tree(self, relpath: Path = Path()) -> dict:
        elems = {}
        number_of_sub_items = int.from_bytes(self._stream.read(4), "little")
        for i in range(number_of_sub_items):
            str_len = int.from_bytes(self._stream.read(4), "little")
            file_name = self._stream.read(str_len).decode()

            type_ = ContentType(int.from_bytes(self._stream.read(4), "little"))

            if type_ == ContentType.File:
                size = int.from_bytes(self._stream.read(4), "little")
                number_of_sub_items = int.from_bytes(self._stream.read(4), "little")
                assert number_of_sub_items == 0
                file_offset = int.from_bytes(self._stream.read(4), "little") + self._header_size
                elem = {
                    "file_name": file_name,
                    "rel_path": str(relpath.joinpath(Path(file_name))),
                    "size": size,
                    "offset": file_offset,
                }
                elems.update({elem.pop("file_name"): elem})

            elif type_ == ContentType.Directory:
                sub_items = self.read_binary_file_tree(relpath=relpath.joinpath(file_name))
                elems.update(sub_items)
        return elems

    def extract_all(self, output_base_dir: Path):
        assert output_base_dir.is_dir()
        for filename in self.files:
            self.extract_file(filename=filename, output_base_dir=output_base_dir)

    def extract_file(self, filename: str, output_base_dir: Path):
        file_data = self.files.get(filename)

        output_file_path = output_base_dir.joinpath(file_data.get("rel_path"))

        if not output_file_path.parent.exists():
            output_file_path.parent.mkdir(mode=(S_IRUSR | S_IWUSR | S_IXUSR | S_IRGRP | S_IROTH), parents=True)
        self._stream.seek(file_data.get("offset"))
        print("Writing {0}".format(output_file_path), end="")
        with output_file_path.open("wb") as output_file:
            bytes_written = output_file.write(self._stream.read(file_data.get("size")))
            print(" - Wrote {0} bytes".format(bytes_written))
