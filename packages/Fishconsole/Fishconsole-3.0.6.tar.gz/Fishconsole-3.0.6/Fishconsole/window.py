# ecoding=utf-8

"""
这是Fishconsole Project的easygui中文模块，我也没法说什么

----

"""

from Fishconsole import files,logs,fcv,Fishsys#激活强制更新要用
try:
    import easygui
    import datetime
except:
    logs.安全退出("window依赖包导入出错，程序无法运行")




def 弹窗(显示文字, 标题, 确认显示文字):
    显示文字 = str(显示文字)
    标题 = str(标题)
    确认显示文字 = str(确认显示文字)
    easygui.msgbox(显示文字, 标题, 确认显示文字)


# noinspection PyStatementEffect
def 选择对话框(显示文字, 标题, 选项: list, 图片地址: str = None):
    a = files.强制类型检测(选项, ["list"])
    if a:
        1 + 1
    else:
        print(logs.日志(f"Fishconsole{fcv.version()}》window》选择对话框》强制类型检测》请指定list类型的数据源", "红色"))
    显示文字 = str(显示文字)
    标题 = str(标题)
    返回 = easygui.buttonbox(image=图片地址, msg=显示文字, title=标题, choices=选项)
    return 返回


# noinspection PyStatementEffect
def 列表选择对话框(显示文字, 标题, 选项: list):
    a = files.强制类型检测(选项, ["list"])
    if a:
        1 + 1
    else:
        print(logs.日志(f"Fishconsole{fcv.version()}》window》列表选择对话框》强制类型检测》请指定list类型的数据源", "红色"))
    标题 = str(标题)
    返回 = easygui.multchoicebox(msg=显示文字, title=标题, choices=选项)
    return 返回


def 输入框(显示文字, 输入框标题, 标题=None):
    标题 = str(标题)
    显示文字 = str(显示文字)
    返回 = easygui.multenterbox(显示文字, title=标题, fields=输入框标题)
    return 返回


def 输入框a(显示文字, 输入框标题, 标题=None):
    标题 = str(标题)
    显示文字 = str(显示文字)
    返回 = easygui.multenterbox(显示文字, title=标题, fields=输入框标题)

    return 返回


def 密码框(显示文字, 输入框标题, 标题=None):
    标题 = str(标题)
    显示文字 = str(显示文字)
    返回 = easygui.multpasswordbox(显示文字, title=标题, fields=输入框标题)
    return 返回


def 文件选择():
    返回 = easygui.fileopenbox()
    return 返回


def 文件保存():
    返回 = easygui.filesavebox()
    return 返回

def 文件夹选择():
    返回 = easygui.diropenbox()
    return 返回


# 弹窗(1,2,3)
# print(选择对话框(1,2,选项=["ab","cd","ef"],图片地址="h.PNG"))
# print(列表选择对话框(1,2,选项=["ab","cd"]))
# print(输入框("显示文字",["内容1","内容2"],"标题"))
# print(密码框("显示文字",["内容1","内容2"],"标题"))
# print(文件选择())
# print(文件保存())
