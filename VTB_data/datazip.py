import zipfile
import os


class Datazip:
    def __init__(self, filename):
        self.filename = filename

    def data_to_zip(self):
        name = self.__get_filename()
        ext = self.__get_ext()
        my_zip = zipfile.ZipFile(f'{name}.zip', 'w')
        my_zip.write(f'{self.filename}', compress_type=zipfile.ZIP_DEFLATED)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{self.filename}')
        os.remove(path)
        return name, ext

    def zip_to_data(self):
        name = self.__get_filename()
        my_zip = zipfile.ZipFile(f'{name}.zip')
        my_zip.extract(f'{self.filename}')

    def __get_ext(self):
        temp = self.filename.split('.')
        return temp[-1]

    def __get_filename(self):
        temp = self.filename.split('.')
        del temp[-1]
        result = ""
        for word in temp:
            result += word + "."
        return result[:-1]


flname = "check.txt"
dz = Datazip(flname)
dz.data_to_zip()
