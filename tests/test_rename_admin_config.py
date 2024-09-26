import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestRenameAdminConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_name="/var/www/html/files/opencart-4.0.2.3/upload/admin/config-dist.php"
        cls.file_to_rename="/var/www/html/files/opencart-4.0.2.3/upload/admin/config.php"


    def test_rename_admin_config(self):
        os.rename(self.file_name,self.file_to_rename)

if __name__ == "__main__":
    unittest.main()