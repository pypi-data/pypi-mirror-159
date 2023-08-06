#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "WYDomain",
    version = "0.0.1",
    keywords = ("pip", "WYDomain","domain licensed"),
    description = "A tool of check Chinese domain is licensed",
    long_description = "A tool of check Chinese domain is licensed",
    license = "MIT Licence",

    url = "https://github.com/WYTool/wydomain_python",     #项目相关文件地址，一般是github
    author = "WYTool",
    author_email = "wytoolsoft@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    # install_requires = ["numpy"]          #这个项目需要的第三方库
)

