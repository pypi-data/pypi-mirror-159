


"""
这是Fishconsole Project的file模块，所有跟文件有关的项目都会被放到这里

----

虽然这个做法拆分了Fishsys，但是作为20的全新架构，牺牲一点还是值得的

"""



from Fishconsole import logs


def 强制类型检测(任意变量, 预期类型:list):
    """

    Fishconsole files 强制类型检测

    ----

    - 就是检测目标变量的类型和指定的类型是不是一样的，如果是一样的，就返回ture，如果不是，就返回False

    - 目标类型可根据所加的其他模块自动适应

    :param 任意变量: 你需要比对的变量
    :param 预期类型: 你需要验证的类型比如a=1，强制类型检测（a,'int'）
    :return: bool
    """
    type值 = str(type(预期类型))

    变量类型 = type值.split("'")[1]
    if 变量类型!="list":
        logs.安全退出("强制类型检测》你必须指定list类型的预期类型")

    type值 = str(type(任意变量))
    变量类型 = type值.split("'")[1]
    if 变量类型 in 预期类型:
        return True
    else:
        return False






def 文件存在性检测(文件名: str):
    """

    Fishconsole Fishsys 文件存在性检测模块

    ----

    :param 文件名:你需要检测的文件

    :return: 布尔值
    """
    import os
    if not os.path.exists(文件名):
        file = False
    else:
        file = True
    return file










def 缓存(模式, 数据: dict = None, 文件名="Fishconsole.fcc",变量名=None):
    """

    Fishconsole Fishsys 缓存模块

    ----

    就是存数据，方便程序在下一次运行的时候调用


    语法就是\n\n"


    files.缓存(1,数据={})【这个是覆盖写入，原来的所有东西会消失】\n\n"


    files.缓存(2,变量名='缓存名')【这个是读取，如果你指定了变量名，我们就会返回这个值对应的内容,反之返回全部（返回全部是针对大规模读写性能太差的问题的解决方案）】\n\n"


    files.缓存(3,数据)【这个是插入，修改或增加部分缓存内容】"
    """
    模式 = str(模式)
    if 模式 == "1":
        a = 强制类型检测(数据, 'dict')
        if a:
                数据 = str(数据)
                数据 = bytes(数据, encoding="utf-8")
                with open(f'{文件名}', "wb") as file:
                    file.write(数据)

        else:
            logs.安全退出("请使用dict的数据", 数据)
    elif 模式 == "2":
        # 我是狠人/doge，我就要检测这个文件
        if 文件存在性检测(文件名):
            with open(f'{文件名}', "rb") as file:
                a = file.read()
            解密 = str(a, encoding="utf-8")
            try:
                解密 = eval(解密)
                解密 = dict(解密)
            except SyntaxError:
                logs.变量查看("解密",解密)
                logs.安全退出("缓存》模式2》变量名提取》操作失败【目标不为dict类型】")
            except NameError:
                logs.变量查看("解密", 解密)
                logs.安全退出("缓存》模式2》变量名提取》操作失败【目标被非法篡改】")
            if 变量名 is None:
                return 解密
            else:
                try:
                    res=解密.get(变量名)
                    if res is None:
                        # print("变量不存在")
                        return "error"
                    else:
                        return res
                except AttributeError:
                    logs.安全退出("缓存》模式2》变量名提取》操作失败【未知错误】")
        else:
            # 如果它返回这个布尔值，那就说明它没有检测到这个文件
            # print("文件没有找到")
            return False
    elif 模式 == "3":
        if 文件存在性检测(文件名):
            with open(f'{文件名}', "rb") as file:
                a = file.read()
            解密 = str(a, encoding="utf-8")
            try:
                解密 = eval(解密)
            except SyntaxError:
                logs.变量查看("解密", 解密)
                logs.安全退出("缓存》模式3》变量名提取》操作失败【目标不为dict类型】")
            except NameError:
                logs.变量查看("解密", 解密)
                logs.安全退出("缓存》模式3》变量名提取》操作失败【目标被非法篡改】")
            if 强制类型检测(数据,"dict"):
                解密=dict(解密,**数据)
                数据 = str(解密)
                数据 = bytes(数据, encoding="utf-8")
                with open(f'{文件名}', "wb") as file:
                    file.write(数据)
            else:
                logs.安全退出("缓存》模式3》变量名提取》操作失败【请指定dict类型的数据】")
        else:
            # 如果它返回这个布尔值，那就说明它没有检测到这个文件
            # print("文件没有找到")
            return False
    else:
        logs.安全退出("缓存》请选择合法的模式")