import os
class TextFile:

    def __init__(self, filename):
        self.filename = filename

    def write_txt(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

    def read_txt(self):
        with open(self.filename, 'r') as file:
            return file.read()


    def read_txt(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def append_txt(self, content):
        with open(self.filename, 'a') as file:
            file.write(content)

    def delete_txt(self):
        os.remoTextFilee(self.filename)

    def rename_txt(self, new_filename):
        os.rename(self.filename, new_filename)

    def copy_txt(filename, new_filename):
        with open(filename, 'r') as file:
            with open(new_filename, 'w') as new_file:
                new_file.write(file.read())

    def list_txt(self):
        return os.listdir(self.filename)

    def check_txt(self):
        return os.path.exists(self.filename)

    def check_txt_content(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def count_txt_lines(self):
        with open(self.filename, 'r') as file:
            return len(file.readlines())

    def check_txt_size(self):
        return os.path.getsize(self.filename)

    def check_txt_permissions(self):
        return os.access(self.filename, os.R_OK)

    def check_txt_modification_time(self):
        return os.path.getmtime(self.filename)

    def check_txt_creation_time(self):
        return os.path.getctime(self.filename)

    def check_txt_access_time(self):
        return os.path.getatime(self.filename)

    def check_txt_is_directory(self):
        return os.path.isdir(self.filename)

    def check_txt_is_file(self):
        return os.path.isfile(self.filename)

    def check_txt_is_symlink(self):
        return os.path.islink(self.filename)

    def check_txt_is_block_device(self):
        return os.path.isblockdev(self.filename)

    def check_txt_is_character_device(self):
        return os.path.ischar(self.filename)

    def check_txt_is_fifo(self):
        return os.path.isfifo(self.filename)

    def check_txt_is_socket(self):
        return os.path.issocket(self.filename)

    def check_txt_is_pipe(self):
        return os.path.ispipe(self.filename)

    def check_txt_is_device(self):
        return os.path.isdevice(self.filename)

    def check_txt_is_mount_point(self):
        return os.path.ismount(self.filename)

    def check_txt_is_absolute_path(self):
        return os.path.isabs(self.filename)

    def check_txt_is_relative_path(self):
        return os.path.isrelpath(self.filename)

    def check_txt_is_same_file(self):
        return os.path.samfile(self.filename)





