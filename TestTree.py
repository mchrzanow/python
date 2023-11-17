import os
import tempfile
import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        # Tworzenie tymczasowego katalogu testowego z pewną strukturą
        self.test_dir = tempfile.TemporaryDirectory()
        self.root_path = self.test_dir.name
        os.mkdir(os.path.join(self.root_path, "subdir1"))
        os.mkdir(os.path.join(self.root_path, "subdir2"))
        with open(os.path.join(self.root_path, "file1.txt"), 'w') as f:
            f.write("Test file 1")

    def tearDown(self):
        # Usuwanie tymczasowego katalogu po zakończeniu testów
        self.test_dir.cleanup()

    def test_tree_structure(self):
        tree = Tree(self.root_path)
        expected_structure = "'%s'\n\t'file1.txt'\n\t'subdir1'\n\t'subdir2'" % self.root_path.replace('\\', '\\\\')
        self.assertEqual(str(tree), expected_structure+'\n')

    def test_empty_directory(self):
        empty_dir_path = os.path.join(self.root_path, "empty_dir")
        os.mkdir(empty_dir_path)
        empty_tree = Tree(empty_dir_path)
        expected_structure = r"'%s'" % empty_dir_path.replace('\\', '\\\\')
        self.assertEqual(str(empty_tree), expected_structure+'\n')

    def test_depth_limited_display(self):
        tree = Tree(self.root_path)
        expected_structure_depth_1 = r"'%s'" % self.root_path.replace('\\', '\\\\')
        self.assertEqual(tree.__str__(depth=1), expected_structure_depth_1 + '\n')

    def test_non_existent_directory(self):
        non_existent_path = "C:/non/existent/directory"
        with self.assertRaises(FileNotFoundError):
            Tree(non_existent_path)

# Uruchomienie testów
unittest.main(argv=[''], exit=False)
