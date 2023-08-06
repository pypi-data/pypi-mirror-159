"""
这是Fishconsole Project的控制模块，它的作用还是挺大的，至少。。。决定了整个模块的运行状态

----

"""
import pkg_resources


def version():
    """
    FishConsole version模块

    ----

    版本云控，这是一个不重要但又很重要的模块，给setup用的

    :return: 返回版本号
    """
    return '3.0.6'


def f_debug():
    """
    ----
    FishConsole fcv 开发者选项模块
    ----

    ----

    - 欢迎您进入Fishconsole的调试控制模块
    - 我呢，只是一个职高生，做这
    - 个完全是为爱发电，所以，虽然我的模块不会很好，但正在努力前行——鱼几斤（2022/6/17）
    ----

    """
    global main, smtp授权码, threading, os
    from Fishconsole import logs, files, Fishsys
    try:
        import os, pandas as pd
        from openpyxl.utils import get_column_letter
        from pandas import ExcelWriter
        import numpy as np
        import threading
        from pip._internal import main
    except:
        logs.安全退出("fcv依赖包导入出错，程序无法运行")

    def to_excel_auto_column_weight(df: pd.DataFrame, writer: ExcelWriter, sheet_name):
        """DataFrame保存为excel并自动设置列宽"""
        global ExcelWriter, pd
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        #  计算表头的字符宽度
        column_widths = (

            df.columns.to_series().apply(lambda x: len(x.encode('gbk'))).values
        )
        #  计算每列的最大字符宽度
        max_widths = (
            df.astype(str).applymap(lambda x: len(x.encode('gbk'))).agg(max).values
        )
        # 计算整体最大宽度
        widths = np.max([column_widths, max_widths], axis=0)
        # 设置列宽
        worksheet = writer.sheets[sheet_name]
        for i, width in enumerate(widths, 1):
            # openpyxl引擎设置字符宽度时会缩水0.5左右个字符，所以干脆+2使左右都空出一个字宽。
            worksheet.column_dimensions[get_column_letter(i)].width = width + 2

    print(f"Fishconsole fcv_debug [版本 {version()}]")
    print("（C）鱼鱼有几斤，保留所有权利。")
    print("------------")

    while True:

        b = logs.输入("输入指令以执行")

        b = b.split(" ")
        if b[0] == '':
            continue

        # 这是项目b
        if b[0] in ["a"]:
            # 第一个值是a，看后面的值
            for a in b:
                # 循环检测
                if a == "b":
                    print("ok b")
                    # 成功就跳出循环
                    # noinspection PyAssignmentToLoopOrWithParameter
                    for a in b:
                        if a == "c":
                            print("ok c")
                            break
                        if a == "b":
                            print("ok b")
                            break
                    break
            else:
                print(logs.日志(f"这是a的帮助文档", 色选="红色"))



        elif b[0] in ["cls", "CLS"]:
            # 这一条是搞那种cls不能用的情况，如果它能用的话cls了谁也不知道干了啥
            print("\n" * 30)
            os.system("cls")




        elif b[0] in ["view", "VIEW"]:
            未选触发器 = True
            for a in b:
                # 循环检测
                if a == "c":
                    未选触发器 = False
                    # 展示所有的变量，以Dateframe的形式
                    变量组value = files.缓存(2)
                    变量组info = {
                        "updata": "Fishconsole强制更新系统激活状态",
                        "Forcedupdate": "Fishconsole强制更新运行状态",
                        "fup": "Fishconsole强制更新系统自检状态",
                        "year": "上一次更新的年",
                        "month": "上一次更新的月",
                        "day": "上一次更新的日",
                        "UPI": "Fishconsole强制更新系统操作输出开关",
                        "FI": "系统日志总开关",
                        "PI": "passworld系统日志输出控制",
                        "HEI": "helps主程序系统日志输出开关",
                        "ZUI": "字符串转unicode模块系统日志输出开关",
                        'AC': "系统自动存储的smtp授权码",
                        'FHUM': "first help updata message",
                        'FESA': '系统自动存储的邮件发送账号',
                        'Sender': '系统自动存储的发件人姓名'

                    }
                    变量组classification = {
                        "updata": "强制更新系统",
                        "Forcedupdate": "强制更新系统",
                        "fup": "强制更新系统",
                        "year": "强制更新系统",
                        "month": "强制更新系统",
                        "day": "强制更新系统",
                        "UPI": "系统日志",
                        "FI": "系统日志",
                        "PI": "系统日志",
                        "HEI": "系统日志",
                        "ZUI": "系统日志",
                        "AC": "邮件",
                        'FHUM': 'help弹窗',
                        'FESA': "邮件",
                        'Sender': '邮件'
                    }
                    变量组classification = pd.DataFrame(变量组classification.items(), columns=['name', "classification"])
                    变量组info = pd.DataFrame(变量组info.items(), columns=['name', "info about"])
                    变量组value = pd.DataFrame(变量组value.items(), columns=['name', 'value'])
                    pd.set_option('display.unicode.ambiguous_as_wide', True)
                    pd.set_option('display.unicode.east_asian_width', True)

                    res = pd.merge(变量组value, 变量组info)
                    res = pd.merge(res, 变量组classification)
                    try:

                        with pd.ExcelWriter(r'Fishconsole.fcc.xlsx') as writer:
                            to_excel_auto_column_weight(res, writer, f'Fishconsole fcv_debug变量组')

                        def start():
                            os.system("Fishconsole.fcc.xlsx")

                        a = threading.Thread(target=start)
                        a.start()
                    except:
                        print("你个辣鸡，wps或者office都不装一个")
                        print(res)
                    break
            if 未选触发器:
                print(logs.分割线(f"这是view的简介", "fcv_debug console", 色选="红色"))
                print("他的作用就是更改部分变量的值")
                print("可用参数：")
                print("c")
                print("如果想了解具体的用法，请在终端中键入'help'或者'?'")






        elif b[0] in ["exit", "EXIT"]:
            logs.安全退出("fcv_debug正常退出")


        elif b[0] in ["change", "CHANGE"]:
            未选触发器 = True
            for a in b:
                # 循环检测
                if a == "Forcedupdate":
                    未选触发器 = False
                    变量组 = files.缓存(2)
                    if 变量组:
                        mod = 变量组.get("Forcedupdate")
                        if mod:
                            变量组["Forcedupdate"] = False
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[Forcedupdate]", 变量组["Forcedupdate"])
                            break
                        else:
                            变量组["Forcedupdate"] = True
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[Forcedupdate]", 变量组["Forcedupdate"])
                            break
                    else:
                        变量组["Forcedupdate"] = True
                        files.缓存(1, 变量组)
                        break

                if a == "UPI":
                    未选触发器 = False
                    变量组 = files.缓存(2)
                    if 变量组:
                        mod = 变量组.get("UPI")
                        if mod:
                            变量组["UPI"] = False
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[UPI]", 变量组["UPI"])
                            break
                        else:
                            变量组["UPI"] = True
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[UPI]", 变量组["UPI"])
                            break
                    else:
                        变量组["UPI"] = True
                        files.缓存(1, 变量组)
                        break

                if a == "FI":
                    未选触发器 = False
                    变量组 = files.缓存(2)
                    if 变量组:
                        mod = 变量组.get("FI")
                        if mod:
                            变量组["FI"] = False
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[FI]", 变量组["FI"])
                            break
                        else:
                            变量组["FI"] = True
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[FI]", 变量组["FI"])
                            break
                    else:
                        变量组["FI"] = True
                        files.缓存(1, 变量组)
                        break

                if a == "PI":
                    未选触发器 = False
                    变量组 = files.缓存(2)
                    if 变量组:
                        mod = 变量组.get("PI")
                        if mod:
                            变量组["PI"] = False
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[PI]", 变量组["PI"])
                            break
                        else:
                            变量组["PI"] = True
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[PI]", 变量组["PI"])
                            break
                    else:
                        变量组["PI"] = True
                        files.缓存(1, 变量组)
                        break

                if a == "HEI":
                    未选触发器 = False
                    变量组 = files.缓存(2)
                    if 变量组:
                        mod = 变量组.get("HEI")
                        if mod:
                            变量组["HEI"] = False
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[HEI]", 变量组["HEI"])
                            break
                        else:
                            变量组["HEI"] = True
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[HEI]", 变量组["HEI"])
                            break
                    else:
                        变量组["HEI"] = True
                        files.缓存(1, 变量组)
                        break

                if a == "ZUI":
                    未选触发器 = False
                    变量组 = files.缓存(2)
                    if 变量组:
                        mod = 变量组.get("ZUI")
                        if mod:
                            变量组["ZUI"] = False
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[ZUI]", 变量组["ZUI"])
                            break
                        else:
                            变量组["ZUI"] = True
                            files.缓存(1, 变量组)
                            print(logs.日志("操作成功", "绿色"))
                            logs.变量查看("变量组[ZUI]", 变量组["ZUI"])
                            break
                    else:
                        变量组["ZUI"] = True
                        files.缓存(1, 变量组)
                        break

                if a in ["AC", "ac"]:
                    未选触发器 = False
                    try:
                        smtp授权码 = b[2]
                    except:
                        print(logs.日志("参数缺失", "红色"))
                    try:
                        files.缓存(3, 数据={"AC": smtp授权码})
                        print(logs.日志("操作成功", "绿色"))
                        logs.变量查看("smtp授权码", smtp授权码)
                    except:
                        logs.日志("未知错误", "红色")

            if 未选触发器:
                print(logs.分割线(f"这是change的简介", "fcv_debug console", 色选="红色"))
                print("他的作用就是更改fcv_debug掌管的部分变量的值")
                print("可用参数")
                print("Forcedupdate\nUPI\nFI\nPI\nHEI\nZUI\nAC")
                print("如果想了解具体的用法，请在终端中键入'help'或者'?'")


        elif b[0] in ["version", "VERSION", "V", "v"]:
            def start():
                from Fishconsole import Fishconsole_version_a
                Fishconsole_version_a.启动()
            res=threading.Thread(target=start,daemon=True)
            res.start()



        elif b[0] in ["pip", "PIP"]:
            未选触发器 = True
            for a in b:
                # 循环检测
                if a == "install":
                    print(logs.日志("Fishconsole fcv_debug PIP》安装和更新开始", "蓝色"))
                    未选触发器 = False
                    res = Fishsys.官网存活性检测("https://pypi.org/", 3)
                    if res:
                        try:
                            main(['install', '--upgrade', 'pip'])
                            main(['install', f'{b[2]}'])
                            main(['install', '--upgrade', f'{b[2]}'])
                        except:
                            print(logs.日志("Fishconsole fcv_debug PIP》未知错误", "蓝色"))
                        print(logs.日志("Fishconsole fcv_debug PIP》安装和更新结束", "蓝色"))
                    else:
                        print(logs.日志("官网连接失败", "红色"))
                        print(logs.日志("Fishconsole fcv_debug PIP》安装和更新结束", "蓝色"))
            if 未选触发器:
                print(logs.分割线(f"这是pip的简介", "fcv_debug console", 色选="红色"))
                print("他的作用就是执行pip的指令（本来用execute可以解决，但是jupyter不行）")
                print("可用参数")
                print("install"
                      "")
                print("如果想了解具体的用法，请在终端中键入'help'或者'?'")



        elif b[0] in ["help", "?", "？", "HELP"]:
            def 帮助():
                from Fishconsole import helps
                helps.帮助()

            helps_res = threading.Thread(target=帮助)
            helps_res.start()


        elif b[0] in ["updata", "UPDATA"]:
            print(logs.日志("Fcv_debug Console》我们将尝试激活更新，在程序执行完毕以后，我们将阻止强制更新系统在下一次继续运行", "蓝色"))
            files.缓存(3, 数据={'updata': True})
            files.缓存(3, 数据={'FHUM': True})
            Fishsys.Fishconsole_Update()
            files.缓存(3, 数据={'updata': False})

            def temp():
                from Fishconsole import helps
                helps.帮助()
            import time
            time.sleep(3)
            threading.Thread(target=temp).start()


        elif b[0] in ["execute"]:
            未选触发器 = True
            空容器 = ""
            计数器 = 0
            for temp in b[1:]:
                if 计数器 == 0:
                    空容器 = 空容器 + " " + temp
                else:
                    空容器 = " " + 空容器 + " " + temp
            if not 空容器 == "":
                未选触发器 = False
                os.system(空容器)
            if 未选触发器:
                print(logs.分割线(f"execute", "fcv_debug console", 色选="红色"))
                print("他的作用就是调用系统默认的终端来执行指定的内容")
                print("语法就是 execute + 系统指令")


        elif b[0] in ["turn", "turn"]:
            未选触发器 = True
            for a in b:
                # 循环检测

                if a in ['file_protect','FILE_PROTECT']:
                    for a in b:
                        if a in ['on','ON']:
                            print('turn on file_protect')
                            未选触发器 = False
                            break
                        elif a in ['off','OFF']:
                            print('turn off file_protect')
                            未选触发器 = False
                            break

                if a in ['file_protect','FILE_PROTECT','文件保护']:
                    for a in b:
                        if a in ['on','ON']:
                            print('turn on file_protect')
                            未选触发器 = False
                            break
                        elif a in ['random_ip','RANDOM_IP','随机ip','随机IP']:
                            print('turn off file_protect')
                            未选触发器 = False
                            break

            if 未选触发器:
                print(logs.分割线(f"这是turn的简介", "fcv_debug console", 色选="红色"))
                print("他的作用就是对后台的程序进行管理，这样就可以做到控制后台")
                print("可用后台：")
                print("文件保护系统\n随机ip池")
                print('------------------')
                print('可用模式有：')
                print('on（启动）')
                print('off （关闭）')
                print('------------------')
                print('语法是：turn+关键字on/off+关键字可用后台')
                print("如果想了解具体的用法，请在终端中键入'help'或者'?'")

        else:
            print(logs.日志(f"‘{b[0]}’是不受支持的命令，如果想查看命令，请键入'help'或者'?'", 色选="红色"))
