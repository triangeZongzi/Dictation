from fileinput import filename
import PySimpleGUI as sg
import pandas as pd
from playsound import playsound
# import time
import os
import windows as w

def save_error_words(error_words, file_name):
    pass

def main():

        wrongWords = {}
        win2_active = False
        win3_active = False
        ite = 0
        sg.theme('DarkGreen5')
        win1 = w.window1()

        # 主循环开始
        while True:
            # 获取 窗口1 的事件和其返回值
            event1, values1 = win1.read(timeout=100)
            # 如果 事件1 为空或者为 关闭按钮 退出主循环
            if event1 in (None, 'closeAll') or event1 == 'Exit':
                win1.Hide()
                w.popEndWindow()
                break

            for i in range(len(values1)):
                if values1[i] == 'Open':
                    win2_active = True
                    win2 = w.window2()
            # 如果 窗口2 行动值为True
            if win2_active:
                win1.Hide()
                # 获取 窗口2 的事件 和 返回值
                event2, values2 = win2.read(timeout=100)

                if event2 is None:
                    w.popEndWindow()
                    break
                # 如果 事件1 为空或者为 关闭按钮
                if event2 in ['fileBack', 'Exit']:
                    # 设置 窗口2行动值 为False
                    win2_active = False
                    # 关闭窗口2
                    win2.close()
                    win1.un_hide()

                if event2 == 'fileSubmit':
                    win3_active = True
                    fileName = values2['ipt']
                    word_df = pd.read_csv(fileName, encoding='utf-8')
                    num = len(word_df['trans'])
                    win3 = w.window3(word_df['trans'][i])

            if win3_active:
                win2.Hide()
                event3, values3 = win3.read(timeout=100)
                # print(event3)
                # print(values3)

                if event3 is None :
                    if len(wrongWords) != 0:
                        w.popWrongWordsWindow(wrongWords)
                        print(fileName)
                    w.popEndWindow()
                    break

                if event3 in ['wordBack', 'Exit']:
                    win3_active = False
                    win3.close()
                    if len(wrongWords) != 0:
                        eventW = w.popWrongWordsWindow(wrongWords)
                        
                        if eventW == 'sure':
                            print(fileName)
                            w.popEndWindow()
                            break
                    win2.un_hide()

                if event3 == 'redioM':
                    
                    redio_path = os.getcwd() + "\\WordsDictation"  

                    try:
                        if not os.path.exists(redio_path + '\\mp3\\' + fileName[-8:-4] + '\\' + word_df['word'][ite] + '.mp3'):
                            sg.popup('暂时没有音频，请期待后续版本更新~~')
                        else:
                            playsound(redio_path + '\\mp3\\' + fileName[-8:-4] + '\\' + word_df['word'][ite] + '.mp3')
                    except:
                        sg.popup('暂时没有音频，请期待后续版本更新~~')
                        print("redio doesn't found!")
                        
                if event3 == 'wordSubmit':                                                  # 检测单词提交按键
                    if values3['INPUT'] == word_df['word'][ite]:                            # 若输入与听写单词一致
                        win3.Element('OUTPUT').Update(value='恭喜你答对了！！！')            # 更新输出文本框
                        win3.Element("INPUT").Update("")                                    # 清空输入文本框
                        if ite <= num:                                                      # 单词未遍历完
                            ite += 1                            
                            print(ite)
                            win3.Element('wordArea').Update(value=word_df['trans'][ite])    # 更新单词
                        else:
                            sg.popup("到头啦~~~")                                            # 提示单词遍历完  

                    else:                                                                   # 用户判断错误
                        win3.Element('OUTPUT').Update(value='很遗憾你错了，正确答案是： \n'+     
                                                            word_df['word'][ite])           # 提示错误并显示正确单词
                        win3.Element("INPUT").Update("")
                        wrongWords[word_df['word'][ite]] = word_df['trans'][ite]            # 记录错误单词
                        if ite <= num:
                            ite += 1
                            print(ite)
                            win3.Element('wordArea').Update(value=word_df['trans'][ite])
                        else:
                            sg.popup("到头啦~~~")

if __name__ == '__main__':
    main()