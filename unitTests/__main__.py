# -*- coding: utf-8 -*-
import unittest


if __name__ == "__main__":
    suite = unittest.TestLoader().discover('unitTests', pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=3).run(suite)
