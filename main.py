import PySimpleGUI as sg
import pandas as pd
from playsound import playsound
import trans
import time
import os
import windows as w
import json


def save_error_words(error_words, filename):
    # name = file_name.split('/')[-1].replace('.csv', '.json')
    error_path = os.path.split(
        os.path.realpath(__file__)
    )[0] + "\\error_words"

    if not os.path.exists(error_path):
        os.makedirs(error_path)

    if filename == '':
        filename = str(time.strftime("%Y-%m-%d", time.localtime(time.time())))

    if os.path.isfile(error_path+ "\\" + filename + "_error.json"):
        with open(error_path+ "\\" + filename + "_error.json", "r", encoding="utf-8") as f:
            words_dict_old = json.load(f)
    
        for word in words_dict_old.keys():
            error_words[word] = words_dict_old[word]

    with open(error_path + "\\" + filename + "_error.json", 'w', encoding='utf-8') as f:
        json.dump(error_words, f, ensure_ascii=False, indent=4)

    return True
            

def main():

        wrongWords = {}
        word_dict = {}
        win2_active = False
        win3_active = False
        win_get_word_active = False
        ite = 0
        sg.theme('DarkGreen5')
        win1 = w.window1()

        # 主循环开始
        while True:
            # 获取 窗口1 的事件和其返回值
            event1, values1 = win1.read(timeout=100)
            # 如果 事件1 为空或者为 关闭按钮 退出主循环
            if event1 in (None, 'closeAll') or event1 == 'Exit':
                if len(wrongWords) != 0:
                    w.popWrongWordsWindow(wrongWords)
                    save_error_words(wrongWords, fileName)
                    if eventW in ['sure', None]:
                        w.popEndWindow()
                        break
                else:
                    w.popEndWindow()
                    break

            if event1 == '-ONLINE-':
                win_get_word_active = True
                win_get_word = w.windows_get_word()

            if win_get_word_active:
                win1.Hide()
                event_word, value_word = win_get_word.read(timeout=100)

                if event_word is None:
                    if len(wrongWords) != 0:
                        w.popWrongWordsWindow(wrongWords)
                        save_error_words(wrongWords, fileName)
                        if eventW in ['sure', None]:
                            w.popEndWindow()
                            break
                    else:
                        w.popEndWindow()
                        break
                
                if event_word == '-WORDBACK-':
                    # 设置 窗口行动值 为False
                    win_get_word_active = False
                    # 关闭窗口
                    win_get_word.close()
                    win1.un_hide()
                
                if event_word == '-UNSAVE-':
                    win_get_word.Element('-WORDSAVE-').hide_row()

                if event_word == '-SAVE-':
                    win_get_word.Element('-WORDSAVE-').unhide_row()
                
                if event_word == '-WORDTRANSLATE-':

                    trans_word = value_word['-WORDINPUT-']
                    word_translate = trans.get_word(trans_word)

                    if word_translate == 'error1':
                        sg.popup_ok("单词错误请重新输入")
                        continue
                    elif word_translate == 'error2':
                        sg.popup_ok("单词错误请重新输入")
                        continue
                    elif type(word_translate) == type(Exception):
                        sg.popup_error(word_translate)
                        continue
                    elif word_translate == []:
                        sg.popup_ok("翻译错误请检查单词 翻译:\n", word_translate)
                        continue

                    word_dict[trans_word] = word_translate

                    win_get_word.Element('-TRANSOUTPUT-').update(word_translate)
                    win_get_word.Element('-WORDINPUT-').update("")
                
                
                if event_word == '-WORDSAVE-':
                    filename = value_word['-FILENAME-']
                    if trans.save(word_dict, filename):
                        w.popSaveOK()
                    else:
                        w.popSaveError()

            if event1 == '-DICTATION-' or event1 == '-REVIEW-':
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
                    filePath = values2['ipt']
                    if '.json' not in filePath:
                        w.popTip("文件格式错误，应为.json结尾！")
                        win3_active = False
                        continue
                    try:
                        word_df = json.load(open(filePath, encoding='utf-8'))
                    except Exception as e:
                        w.popError(e)
                        win3_active = False
                        continue

                    win3_active = True

                    fileName = filePath.split("/")[-1].replace(".json", '')
                    word_ls = list(word_df.keys())
                    num = len(word_ls)
                    ite = 0
                    win3 = w.window3(word_df[word_ls[ite]])

            if win3_active:
                win2.Hide()
                event3, values3 = win3.read(timeout=100)
                # print(event3)
                # print(values3)

                if event3 is None :
                    if len(wrongWords) != 0:
                        w.popWrongWordsWindow(wrongWords)
                        save_error_words(wrongWords, fileName)
                        if eventW in ['sure', None]:
                            w.popEndWindow()
                            break
                    else:
                        w.popEndWindow()
                        break

                if event3 == 'Exit':
                    win3_active = False
                    win3.close()
                    if len(wrongWords) != 0:
                        eventW = w.popWrongWordsWindow(wrongWords)
                        save_error_words(wrongWords, fileName)
                        
                        if eventW in ['sure', None]:
                            w.popEndWindow()
                            break
                    else:
                        w.popEndWindow()
                        break
                
                if event3 == 'wordBack':
                    # 设置 窗口行动值 为False
                    win3_active = False
                    # 关闭窗口
                    win3.close()
                    win2.un_hide()

                if event3 == 'redioAM':
                    redio_path = os.path.split(os.path.realpath(__file__))[0] + \
                        '\\mp3\\' + fileName + '\\AM' + '\\' + word_ls[ite] + '.mp3'

                    try:
                        if not os.path.isfile(redio_path):
                            sg.popup('暂时没有音频，请期待后续版本更新~~')
                        else:
                            playsound(redio_path)
                    except:
                        sg.popup('暂时没有音频，请期待后续版本更新~~')
                        print("redio doesn't found!")

                if event3 == 'redioEN':
                    
                    redio_path = os.path.split(os.path.realpath(__file__))[0] + \
                        '\\mp3\\' + fileName + '\\EN' + '\\' + word_ls[ite] + '.mp3'
                    
                    try:
                        if not os.path.exists(redio_path):
                            sg.popup('暂时没有音频，请期待后续版本更新~~')
                        else:
                            playsound(redio_path)
                    except:
                        sg.popup('暂时没有音频，请期待后续版本更新~~')
                        print("redio doesn't found!")
                        
                if event3 == 'wordSubmit':                                                  # 检测单词提交按键
                    if values3['INPUT'] == word_ls[ite]:                            # 若输入与听写单词一致
                        win3.Element('OUTPUT').Update(value='恭喜你答对了！！！')            # 更新输出文本框
                        win3.Element("INPUT").Update("")                                    # 清空输入文本框
                        if ite <= num:                                                      # 单词未遍历完
                            ite += 1          
                            win3.Element('wordArea').Update(value=word_df[word_ls[ite]])    # 更新单词
                        else:
                            sg.popup("到头啦~~~")                                            # 提示单词遍历完  

                    else:                                                                   # 用户判断错误
                        win3.Element('OUTPUT').Update(value='很遗憾你错了，正确答案是： \n'+     
                                                            word_ls[ite])           # 提示错误并显示正确单词
                        win3.Element("INPUT").Update("")
                        wrongWords[word_ls[ite]] = word_df[word_ls[ite]]            # 记录错误单词
                        if ite <= num:
                            ite += 1
                            win3.Element('wordArea').Update(value=word_df[word_ls[ite]])
                        else:
                            sg.popup("到头啦~~~")

if __name__ == '__main__':
    main()