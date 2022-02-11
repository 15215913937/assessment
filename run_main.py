# coding = utf-8
# Author: Shenbq
# Date: 2022/1/22 10:57
import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./report/allure_xml -o ./report/allure_html --clean")