import unittest

from DiskLib import *

class TestRequets(unittest.TestCase):
    def setUp(self):
        self.libs = [
            Lib(1, "Музыкальная библиотека"),
            Lib(2, "Архив поэзии"),
            Lib(3, "Архив фото"),
            Lib(11, "Музыкальная библиотека (другая)"),
            Lib(22, "Архив поэзии (другой)"),
            Lib(33, "Архив фото (другой)"),
        ]

        self.disks = [
            Disk(1, "Группа Кино", 650, 1),
            Disk(2, "Сборник Маяковского", 650, 2),
            Disk(3, "Фото с отдыха", 700, 3),
            Disk(4, "Классическая музыка", 700, 1),
            Disk(5, "Рок", 600, 1),
            Disk(6, "Фото с праздника", 750, 3),
        ]
        
        self.disks_libs = [
            DiskLib(1, 1),
            DiskLib(2, 2),
            DiskLib(3, 3),
            DiskLib(1, 4),
            DiskLib(1, 5),
            DiskLib(3, 6),
            DiskLib(11, 1),
            DiskLib(22, 2),
            DiskLib(33, 3),
            DiskLib(11, 4),
            DiskLib(11, 5),
            DiskLib(33, 6),
        ]

        # соединение данных один-ко-многим
        self.one_to_many = [(d.name, d.memory, l.name)
            for l in libs
            for d in disks
            if d.lib_id == l.id]
        # соединение данных многие-ко-многим
        many_to_many_temp = [(l.name, dl.lib_id, dl.disk_id)
            for l in libs
            for dl in disks_libs
            if l.id == dl.lib_id]
        
        self.many_to_many = [(d.name, d.memory, lib_name)
            for lib_name, lib_id, disk_id in many_to_many_temp
            for d in disks if d.id == disk_id]
        
    def test_FirstRequest(self):
        result = FirstRequest(self.one_to_many)

        correct_result = {
            'Архив поэзии': ['Сборник Маяковского'],
            'Архив фото': ['Фото с отдыха', 'Фото с праздника']
        }

        self.assertEqual(result, correct_result)

    def test_SecondRequest(self):
        result = SecondRequest(self.one_to_many)

        correct_result = [
            ('Архив фото', 750),
            ('Музыкальная библиотека', 700),
            ('Архив поэзии', 650),
        ]

        self.assertEqual(result, correct_result)

    def test_ThirdRequest(self):
        result = ThirdRequest(self.many_to_many)

        correct_result = [
            ('Сборник Маяковского', 650, 'Архив поэзии'),
            ('Сборник Маяковского', 650, 'Архив поэзии (другой)'),
            ('Фото с отдыха', 700, 'Архив фото'),
            ('Фото с праздника', 750, 'Архив фото'),
            ('Фото с отдыха', 700, 'Архив фото (другой)'),
            ('Фото с праздника', 750, 'Архив фото (другой)'),
            ('Группа Кино', 650, 'Музыкальная библиотека'),
            ('Классическая музыка', 700, 'Музыкальная библиотека'),
            ('Рок', 600, 'Музыкальная библиотека'),
            ('Группа Кино', 650, 'Музыкальная библиотека (другая)'),
            ('Классическая музыка', 700, 'Музыкальная библиотека (другая)'),
            ('Рок', 600, 'Музыкальная библиотека (другая)')
        ]

        self.assertEqual(result, correct_result)
