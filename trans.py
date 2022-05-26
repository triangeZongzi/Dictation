import pandas as pd
import os
import requests
import re
import time
import json
from config import Config

def get_cwd():

    return os.path.split(os.path.realpath(__file__))[0]

def get_word(word:str):

    try:
        unique = []
        config = Config()

        #   获取单词中文意思，并将单词与其翻译保存在字典里，单词为key
        url = r'http://dict.youdao.com/w/' + word + '/#keyfrom=dict2.top'

        req = requests.get(url,headers=config.hd).text
        regular = re.compile(config.regular)
        data = regular.findall(req)
        # print(data)
        if(word == data or data == '' or data == ' ' or data == config.er):
            return "error1"
        elif(word == '' or word == ' '):
            return "error2"
        else:
            for item in data:
                if (item[0] in "ivnap"):
                    unique.append(item)
            # 去重
            unique = list(set(unique))        
            word_translate = unique
    except Exception as e:
        return e

    return word_translate


#   将单词字典保存为csv格式并输出所有单词
def save(words_dict, filename):

    config = Config()
    local_path = get_cwd()
    if filename == '':
        filename = str(time.strftime("%Y-%m-%d", time.localtime(time.time())))

    # 单词发音url
    listionUrl_AM = config.listionUrl_AM
    listionUrl_EN = config.listionUrl_EN

    for word in words_dict.keys():
        # 下载单词音频
        mp3_data_AM = requests.get(listionUrl_AM + word, headers=config.hd).content
        mp3_data_EN = requests.get(listionUrl_EN + word, headers=config.hd).content

        # 保存单词音频
        save_path_AM =  local_path + "\\mp3" + "\\" + filename + "\\AM"
        save_path_EN =  local_path + "\\mp3" + "\\" + filename + "\\EN"

        if not os.path.exists(save_path_AM):
            os.makedirs(save_path_AM)
        if not os.path.exists(save_path_EN):
            os.makedirs(save_path_EN)

        with open(save_path_AM + "\\" + word +'.mp3', 'wb') as f:
            f.write(mp3_data_AM)
            f.close()

        with open(save_path_EN + "\\" + word +'.mp3', 'wb') as f:
            f.write(mp3_data_EN)
            f.close()

    save_path = get_cwd() + "\\save" + "\\" + filename + ".json"

    if os.path.isfile(save_path):
        with open(save_path, "r", encoding="utf-8") as f:
            words_dict_old = json.load(f)
    
        for word in words_dict_old.keys():
            words_dict[word] = words_dict_old[word]

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(words_dict, f, ensure_ascii=False, indent=4)
    
    return True

