from interfaces.iread import Read
from txt_reader import TxtReader
from txt_writer import TxtWriter
from interfaces.iwrite import Write


class ProxyTxtRW(Read, Write):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.writer = real_writer
        self.__result = ''
        self.__is_actual = None
        self.__real_reader = real_reader

    def write(self, data):
        if self.__result == data:
            print("This data is already written")
        else:
            self.writer.write(data)
            self.__result = data
            self.__is_actual = False

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
            return self.__result


if __name__ == '__main__':
    reader_reader = TxtReader('my_file.txt')
    writer = TxtWriter('my_file.txt')
    proxy = ProxyTxtRW(reader_reader, writer)
    print(proxy.read())  # тут прочитали файл
    print(proxy.read())  # тут вже не читаємо, а забираємо текст файлу
    proxy.write("text")  # тут перезаписываем
    proxy.write("new text")  # тут перезаписываем
    proxy.write("new text")  # тут выводим сообщение что эти данные уже были записаны
    print(proxy.read())  # тут читаем снова






