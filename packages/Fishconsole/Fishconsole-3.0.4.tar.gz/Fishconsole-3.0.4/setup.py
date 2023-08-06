from setuptools import setup, find_packages
from Fishconsole import fcv

filepath = 'README.md'

print("这是Fishcosnole的预设setup嵌入程序，这个程序目前的功能只是输出这一句话，我们在未来可能会添加更多的东西")

setup(
    name="Fishconsole",
    version=fcv.version(),
    author="Fish Console",
    author_email="2645602049@qq.com",
    description="一个有点东西的工具合集，代码上不是很规范，用起来很实在，长期更新（虽然会有bug）",

    # 项目主页
    url="https://space.bilibili.com/698117971?spm_id_from=333.1007.0.0",
    # 长描述
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),


    # 依赖包，没有将会自动下载
    install_requires=['requests', 'easygui', 'matplotlib', 'openpyxl', "pandas",
                      "numpy", "alive_progress","chardet","twine","colorama"],
)
