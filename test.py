import pandas as pd
import os 
import json
from config import Config
import requests
import time
from tqdm import tqdm

def fun1():
    local_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = local_path + "\\save"

    for name in tqdm(os.listdir(file_path)):
        print("="*20 + " processing " + name + " " + "="*20)
        word_dict = {}
        file = pd.read_csv(local_path + "\\save" + "\\" + name, encoding='utf-8')
        words = file['word']
        translates = file['trans']

        for i in range(len(words)):
            word_dict[words[i]] = translates[i]
        

        with open(file_path + "\\" + name.replace(".csv", ".json"), 'w', encoding='utf-8') as f:
            json.dump(word_dict, f, ensure_ascii=False, indent=4)

def fun2():
    
    local_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = local_path + "\\save"
    config = Config()

    for name in os.listdir(file_path):
        if ".json" in name:
            with open(local_path + "\\save" + "\\" + name, "r", encoding='utf-8') as f:
                words_dict = json.load(f)

            listionUrl_AM = config.listionUrl_AM
            listionUrl_EN = config.listionUrl_EN

            for word in tqdm(words_dict.keys()):
                # 下载单词音频
                mp3_data_AM = requests.get(listionUrl_AM + word, headers=config.hd).content
                mp3_data_EN = requests.get(listionUrl_EN + word, headers=config.hd).content

                # 保存单词音频 
                save_path_AM =  local_path + "\\mp3" + "\\" + name.replace(".json", "") + "\\AM"
                save_path_EN =  local_path + "\\mp3" + "\\" + name.replace(".json", "") + "\\EN"

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
                
                time.sleep(0.2)


if __name__ == '__main__':
    fun2()