import stat
import os
import unittest
import confuse


def do_something(path, mode):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    return os.fdopen(os.open(path, flags, 0o600), mode)


class TestFileCreation(unittest.TestCase):

    config = confuse.Configuration('python-paypal-api')

    def test_correct_permissions(self):
        """
        Make sure that a file can be created with specific permissions
        """
        test_file = "demo.txt"

        file = os.path.join(self.config.config_dir(), test_file)
        with do_something(file, "w") as fout:
            fout.write("blah blah blah")

        finfo = os.stat(file)
        assert(finfo.st_mode & stat.S_IRUSR)
        assert(finfo.st_mode & stat.S_IWUSR)
        assert(not finfo.st_mode & stat.S_IXUSR)
        assert(not finfo.st_mode & stat.S_IRGRP)
        assert(not finfo.st_mode & stat.S_IWGRP)
        assert(not finfo.st_mode & stat.S_IXGRP)
        assert(not finfo.st_mode & stat.S_IROTH)
        assert(not finfo.st_mode & stat.S_IWOTH)
        assert(not finfo.st_mode & stat.S_IXOTH)

        os.remove(file)

    def test_file_exists(self):
        """
        If the file already exists an OSError should be raised.
        """
        test_file = "demo2.txt"
        file = os.path.join(self.config.config_dir(), test_file)

        # simulate file already placed at location by attacker
        with open(file, "w") as fout:
            fout.write("nasty attacker stuff")

        # ensure that we can't open the file
        with self.assertRaises(OSError):
            with do_something(file, "w") as fout:
                fout.write("this should never happen..")

        os.remove(file)