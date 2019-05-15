import sys
sys.path.insert(0,"test")
sys.path.insert(0,"src/life")
import unittest

import testSpecie

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(testSpecie))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)