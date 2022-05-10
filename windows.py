import PySimpleGUI as sg


def popEndWindow():
    long_string = '感谢您使用本产品go(￣▽￣)ｄ'
    sg.Window(
        '程序结束', 
        [[sg.Text(long_string, font=(15, 20))],
        [sg.Cancel('下次见~', font=(15, 15), pad=((120, 120), (5, 1)),size=(30, 2))]],
        size=(400, 100)
    ).read(close=True)


def popWrongWordsWindow(wrongWords):
    word = [w for w in wrongWords.keys()]
    chin = [eval(tran)[0] for tran in wrongWords.values()]
    value = [str(i+1) + '.' + word[i] + ' : ' + chin[i] + '\n' for i in range(len(word))]
    print(value, type(value))
    child_layout = [[sg.Multiline(value, size=(100,15))]]
    event, value = sg.Window('错误单词统计',[
        [sg.Txt("您本次听写的错误单词如下：")],
        [sg.Frame(layout=child_layout, title="错误单词", relief=sg.RELIEF_SUNKEN,
            tooltip='请多记忆加深印象哦~')],
        [sg.Button('确定', size=(5,1), key='sure')]
    ],
        size=(600, 400)).read(close=True)

    return event


def window():
    layout = [
        ["欢迎使用本软件"],
        # window1
        ["在线翻译"],
        # window2
        ["单词听写"],
        # window3
        ["错词复习"],
        ["退出"]
    ]

def window1():
    # 设置 窗口2行动值为 True
    # win2_active = True
    # 窗口2 布局
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'],
            ]

    child_layout = [
        [sg.Txt("请在上方的file菜单中,选择open选项,打开指定单词文件。")]]

    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Frame(layout = child_layout,
            title="打开指定单词文件", relief=sg.RELIEF_SUNKEN,
            tooltip='W1D1 为第一周第一天的单词'
        )],
        [sg.Button('关闭',key='closeAll', size=(10,3), pad=((430,1),(2,2)))]
    ]
    # 建立 窗口1
    window1 = sg.Window("单词听写", size=(550,120), font=(15, 15)).layout(layout)

    return window1


def window2():
    menu_def = [['File', ['&Open', '&Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'],
                ]
    layout = [
              [sg.Menu(menu_def)],
              [sg.InputText( key='ipt'),
               sg.FileBrowse("打开", target='ipt', size=(25,1))],
              [sg.Submit('提交',key='fileSubmit'), sg.Button("返回", key='fileBack')]
              ]
    window2 = sg.Window('Test', size=(550,120), font=(15, 15)).layout(layout).Finalize()

    return window2


def window3(word):
    menu_def = [['File', ['&Open', '&Save', 'Exit', 'Properties']],
                 ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                 ['Help', 'About...'],
                ]
    colum1 = [[sg.Multiline(word, key='wordArea', s=(480,115)), sg.B('美', key='redioM')]]

    colum2 = [[sg.Multiline("快听写单词检查对错吧O(∩_∩)O~", key='OUTPUT', s=(480, 95))]]

    layout = [
        [sg.Menu(menu_def)],
        [sg.Frame(layout=colum1, title=" word ", relief=sg.RELIEF_SUNKEN, s=(500,120))],
        [sg.Input("这里输入单词", size=(20, 1), key='INPUT'),
         sg.Submit('提交', key='wordSubmit')],
        [sg.Frame(layout=colum2, title=" translate ", relief=sg.RELIEF_SUNKEN, s=(500, 100))],
        [sg.Cancel('返回', key='wordBack')]
    ]

    win3 = sg.Window('听写', size=(600,300)).layout(layout).Finalize()

    return win3