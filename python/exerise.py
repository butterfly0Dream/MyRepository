#-*- coding: utf-8 -*-

"""
四则运算题目生成器
"""

import random
import os
import tkinter
import tkinter.messagebox

def get_desk_top():
    desk = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
    return desk

def save_file(dict,file_path = r"C:\Users\fallgod\Desktop"):
    if len(dict) <= 0:
        print("空的数据无法保存！！！")
    filename1 = file_path + "\题目.txt"
    filename2 = file_path + "\题目+答案.txt"
    fs_list = []
    try:
        file1 = open(filename1,"w",encoding="utf-8")
        file2 = open(filename2,"w",encoding="utf-8")
        fs_list.append(file1)
        fs_list.append(file2)
        for key,value in dict.items():
            file1.write(key + "\n")
            file2.write(key + str(value) + "\n")
    except IOError as ex:
        print(ex)
        print("写文件时发生错误")
    finally:
        for fs in fs_list:
            fs.close()

def generate_question(num = 10,size = 2,operation = ("+","-","*","/")):
    #题目-结果存储到dict
    result={}
    len_oper = len(operation)
    while len(result) < num:
        a = random.randint(0,10 ** size - 1)
        b = random.randint(0,10 ** size - 1)
        str_operat = operation[random.randint(0,len_oper - 1)]
        if str_operat == "+":
            a = random.randint(10 ** (size - 1),10 ** size - 1)
            b = random.randint(10 ** (size - 1),10 ** size - 1)
            key = str(a) + " + " + str(b) + " = "
            value = a + b
            result[key] = value
        elif str_operat == "-":
            a = random.randint(10 ** (size - 1),10 ** size - 1)
            b = random.randint(10 ** (size - 1),10 ** size - 1)
            #a小于b时交换二者
            if(a < b):
                a,b = b,a
            if(a == b):
                continue
            key = str(a) + " - " + str(b) + " = "
            value = a - b
            result[key] = value
        elif str_operat == "*":
            key = str(a) + " x " + str(b) + " = "
            value = a * b
            result[key] = value
        elif str_operat == "/":
            while a in (0,1) or b in (0,1) or a % b != 0 or a == b:
                a = random.randint(0,10 ** size - 1)
                b = random.randint(0,10 ** size - 1)
            key = str(a) + " ÷ " + str(b) + " = "
            value = int(a / b)
            result[key] = value
    print(result)
    return result

def show_window():
    operation = []

    #生成题目
    def generate_ques():
        print(f"运算时的参数为:num = {num_selection()},size={bit_selection()},operation={operation}")
        d = generate_question(num_selection(),bit_selection(),operation)
        save_file(d,get_desk_top())

    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel\
            ("温馨提示","确定要退出吗？"):
            top.quit()
    
    #题目数量
    def num_selection():
        num = var.get()
        print("您选择的题目数量是%d"%num)
        return num

    #题目位数
    def bit_selection():
        size = var_bit.get()
        print("您选择的题目位数是%d"%size)
        return size

    #运算规则
    def cb_selection():
        operation.clear()
        if (var1.get() == 1):
            operation.append("+")
        if (var2.get() == 1):
            operation.append("-")
        if (var3.get() == 1):
            operation.append("*")
        if (var4.get() == 1):
            operation.append("/")
        print(f"您选择的运算规则是{operation}")

    #创建顶层窗口
    top = tkinter.Tk()
    #设置窗口大小
    top.geometry("320x240")
    #设置窗口标题
    top.title("四则运算题目生成器")
    #创建标签对象并添加到顶层窗口
    lable = tkinter.Label(top,text="勾选条件后点击生成",\
        font="Atial -28",fg="red")
    lable.pack(expand=1)

    #创建一个装选项的容器
    panel_cb = tkinter.Frame(top)
    var1 = tkinter.IntVar()
    var2 = tkinter.IntVar()
    var3 = tkinter.IntVar()
    var4 = tkinter.IntVar()
    c1 = tkinter.Checkbutton(panel_cb, text='加法', variable=var1, onvalue=1, offvalue=0,command=cb_selection)
    c2 = tkinter.Checkbutton(panel_cb, text='减法', variable=var2, onvalue=1, offvalue=0,command=cb_selection)
    c3 = tkinter.Checkbutton(panel_cb, text='乘法', variable=var3, onvalue=1, offvalue=0,command=cb_selection)
    c4 = tkinter.Checkbutton(panel_cb, text='除法', variable=var4, onvalue=1, offvalue=0,command=cb_selection)
    c1.pack(side="right")
    c2.pack(side="right")
    c3.pack(side="right")
    c4.pack(side="right")
    panel_cb.pack(side="top")

    #题目数量单选框
    panel_num = tkinter.Frame(top)
    var = tkinter.IntVar()
    r1 = tkinter.Radiobutton(panel_num, text='10',variable=var, value='10',command=num_selection)
    r2 = tkinter.Radiobutton(panel_num, text='100',variable=var, value='100',command=num_selection)
    r3 = tkinter.Radiobutton(panel_num, text='1000',variable=var, value='1000',command=num_selection)
    r1.pack(side="right")
    r2.pack(side="right")
    r3.pack(side="right")
    panel_num.pack(side="top")

    #题目位数单选框
    panel_bit = tkinter.Frame(top)
    var_bit = tkinter.IntVar()
    r_b1 = tkinter.Radiobutton(panel_bit, text='一位数',variable=var_bit, value='1',command=bit_selection)
    r_b2 = tkinter.Radiobutton(panel_bit, text='二位数',variable=var_bit, value='2',command=bit_selection)
    r_b3 = tkinter.Radiobutton(panel_bit, text='三位数',variable=var_bit, value='3',command=bit_selection)
    r_b4 = tkinter.Radiobutton(panel_bit, text='四位数',variable=var_bit, value='4',command=bit_selection)
    r_b1.pack(side="right")
    r_b2.pack(side="right")
    r_b3.pack(side="right")
    r_b4.pack(side="right")
    panel_bit.pack(side = "top")

    #创建一个装按钮的容器
    panel = tkinter.Frame(top)
    #创建按钮对象，指定添加到哪个容器中，通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel,text="生成",command=generate_ques)
    button2 = tkinter.Button(panel,text="退出",command=confirm_to_quit)
    button1.pack(side="left")
    button2.pack(side="right")
    panel.pack(side="top")
    #开启主事件循环
    tkinter.mainloop()

def main():
    # num = 10
    # size = 2
    # operation = ("+","-")
    # d = generate_question(num = 10,size = 2)
    # save_file(d,get_desk_top())
    show_window()

if __name__ == "__main__":
    main()