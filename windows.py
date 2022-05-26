import PySimpleGUI as sg


def popEndWindow():
    long_string = '感谢您使用本产品go(￣▽￣)ｄ'
    sg.Window(
        '程序结束', 
        [[sg.Text(long_string, font=(15, 20))],
        [sg.Cancel('下次见~', font=(15, 15), pad=((120, 120), (5, 1)),size=(30, 2))]],
        size=(400, 100)
    ).read(close=True)


def popError(error:Exception):
    sg.popup_error(error)

def popTip(txt:str):
    sg.popup_ok(txt)

def popSaveOK():
    sg.popup_ok("保存成功")

def popSaveError():
    sg.popup_ok("保存失败")

def popWrongWordsWindow(wrongWords:dict):
    word = [w for w in wrongWords.keys()]
    chin = [eval(tran)[0] for tran in wrongWords.values()]
    value_ls = [str(i+1) + '.' + word[i] + ' : ' + chin[i] for i in range(len(word))]
    value_str = ""
    for i in value_ls:
        value_str = value_str + i + "\n"

    print(value_str)
    child_layout = [[sg.Multiline(value_str, size=(100,15))]]
    event, value = sg.Window('错误单词统计',[
        [sg.Txt("您本次听写的错误单词如下：")],
        [sg.Frame(layout=child_layout, title="错误单词", relief=sg.RELIEF_SUNKEN,
            tooltip='请多记忆加深印象哦~')],
        [sg.Button('确定', size=(5,1), key='sure')]
    ],
        size=(600, 400)).read(close=True)

    return event

def window1():
    # 设置 窗口2行动值为 True
    # win2_active = True
    # 窗口2 布局
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'],
            ]

    child_layout = [
        # [sg.Txt("请在上方的file菜单中,选择open选项,打开指定单词文件。")]
        
        [sg.Button("在线翻译", key="-ONLINE-", size=(30,3))],
        [sg.Button("单词听写", key="-DICTATION-", size=(30,3))],
        [sg.Button("错词复习", key="-REVIEW-", size=(30,3))],
        [sg.Button('退出', key='closeAll', size=(30,3))]
        ]

    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Frame(layout = child_layout,
            title="选项", relief=sg.RELIEF_SUNKEN,
            tooltip='W1D1 为第一周第一天的单词', pad=((100,1),(2,2))
        )],
        # [sg.Button("在线翻译", key="-ONLINE-", size=(50,50))],
        # [sg.Button("单词听写", key="-DICTAtION-", size=(50,50))],
        # [sg.Button("错词复习", key="-REVIEW-", size=(50,50))],
    ]
    # 建立 窗口1
    window1 = sg.Window("单词听写", size=(550,420), font=(15, 15)).layout(layout)

    return window1


def window2():
    menu_def = [['File', ['&Open', '&Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'],
                ]
    child_layout = [[
        sg.Txt("鼠标单击\"打开\"选择想听写或复习的文件名\n点击提交", key='-TIPAREA-', s=(480,90)), 
    ]]
    layout = [
        [sg.Menu(menu_def)],
        [
            sg.Frame(
                layout = child_layout,
                title="提示", relief=sg.RELIEF_SUNKEN,
                tooltip='W1D1 为第一周第一天的单词',
                size=(530,95)
            )
        ],
        [sg.InputText( key='ipt'),
        sg.FileBrowse("打开", target='ipt', size=(25,1))],
        [sg.Submit('提交',key='fileSubmit'), sg.Button("返回", key='fileBack')]
    ]
    window2 = sg.Window('打开文件', size=(550,220), font=(15, 15)).layout(layout).Finalize()

    return window2


def window3(trans:str):
    menu_def = [
        ['File', ['&Open', '&Save', 'Exit', 'Properties']],
        ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
        ['Help', 'About...'],
    ]
    colum1 = [[
        sg.Multiline(trans, key='wordArea', s=(500,195), disabled=True), 
    ]]

    colum2 = [[sg.Multiline("快听写单词检查对错吧O(∩_∩)O~", key='OUTPUT', s=(545, 195), disabled=True)]]

    layout = [
        [sg.Menu(menu_def)],
        [sg.Frame(layout=colum1, title=" translate ", relief=sg.RELIEF_SUNKEN, s=(550,200))],
        [
            sg.Input("这里输入单词", size=(20, 1), key='INPUT'),
            sg.Submit('提交', key='wordSubmit'),
            sg.B('美', key='redioAM', pad=((300,1),(1,1))), 
            sg.B('英', key='redioEN')
        ],
        [sg.Frame(layout=colum2, title=" result ", relief=sg.RELIEF_SUNKEN, s=(550, 200))],
        [sg.Cancel('返回', key='wordBack')]
    ]

    win3 = sg.Window('听写', size=(600,500)).layout(layout).Finalize()

    return win3

def windows_get_word():

    colum = [[sg.Multiline("", key='-TRANSOUTPUT-', s=(495, 95), disabled=True)]]
    save_radio = [
        sg.Frame(
            '是否保存到本地', 
            [[
                sg.Radio('Yes', 'radio1', default=True, key='-SAVE-', size=(10, 1), change_submits=True),
                sg.Radio('No', 'radio1', key='-UNSAVE-',  size=(10, 1), change_submits=True)
            ]], 
            size=(440, 50),
            pad=((2,1),(2,1)))
    ]

    file_name_input = [
        sg.Frame(
            '请输入保存的文件名', 
            [[
                sg.Txt("文件名:"), 
                sg.Input("", key='-FILENAME-',tooltip="请输入保存文件名(默认为当前日期)", justification='left'),
                sg.Submit('保存', key='-WORDSAVE-')
            ]],
            s=(440, 50),
            pad=((2,1),(2,1)))
    ]
    
    layout = [
        [save_radio],
        [
            sg.Txt("单词:", pad=((2,1),(2,1))), 
            sg.Input("",s=(30,1), key='-WORDINPUT-', tooltip="在这里输入单词", justification='left'),
            sg.Submit('翻译', key='-WORDTRANSLATE-')
        ],
        [sg.Frame(layout=colum, title=" translate ", relief=sg.RELIEF_SUNKEN, s=(500, 175))],
        
        [file_name_input],
        [sg.Cancel('返回', key='-WORDBACK-', pad=((10,0), (10,1)))]
    ]

    window = sg.Window('在线翻译', size=(550,370)).layout(layout).Finalize()

    return window
    