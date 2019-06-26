from unittest import TestCase
from Main.extensionManager import extensionManager


class Tester(TestCase):

    #Extension Manager Tester
    def test_extensionReader(self):
        print ('Starting Extension Reader Test')
        print ('\n')
        print ('Testing CSV extension detector:')
        ext_mng = extensionManager('dummy.csv')
        print ('CSV File Loaded')
        if self.assertEqual(ext_mng.extensionReader(), 1):
            print ('CSV extension file successfully detected')

        print ('\n')
        print ('Testing DAT extension detector:')
        ext_mng = extensionManager('dummy.dat')
        print ('DAT File Loaded')
        if self.assertEqual(ext_mng.extensionReader(), 2):
            print ('DAT extension file successfully detected')

        print ('\n')
        print ('Testing H5 extension detector:')
        ext_mng = extensionManager('ccnfile.h5')
        print ('H5 File Loaded')
        if self.assertEqual(ext_mng.extensionReader(), 3):
            print ('H5 extension file successfully detected')


