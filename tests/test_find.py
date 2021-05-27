import unittest
from PathFile.PathFile import find_files_dir, my_walk
from os.path import join
from os import getcwd


class MyTest(unittest.TestCase):

    dir_test = join(getcwd(), 'tests', 'test_folder')

    def test_find_in_dir_v1(self):
        self.assertEqual(find_files_dir(join(self.dir_test), 'test.txt'), [
            join(self.dir_test, 'test_1', 'test_in_test', 'test.txt'),
            join(self.dir_test, 'test_2', 'test.txt'),
            join(self.dir_test, 'test_3', 'test.txt'),
        ])

    def test_find_in_dir_v2(self):
        self.assertEqual(find_files_dir(join(self.dir_test), 'test2.txt'), [
            join(self.dir_test, 'test_1', 'test2.txt'),
            join(self.dir_test, 'test_2', 'test2.txt')
        ])

    def test_my_walk_v1(self):
        self.assertEqual(my_walk(self.dir_test), [
            join(self.dir_test, 'test_1', 'test2.txt'),
            join(self.dir_test, 'test_1', 'test_in_test', 'test.txt'),
            join(self.dir_test, 'test_2', 'test.txt'),
            join(self.dir_test, 'test_2', 'test2.txt'),
            join(self.dir_test, 'test_3', 'test.txt')
        ])