import jieba
import wordcloud
import imageio

import jieba

# 1.聊天记录初始化，去掉表情时间，昵称等
newtext = []
# 打开E盘下的聊天记录文件qq.txt
for word in open('./张文晨15979978677(3235473083).txt', 'r', encoding='utf-8'):
    tmp = word[0:4]
    if tmp == "2022" or tmp == "====" or tmp == "2023":  # 过滤掉聊天记录的时间和qq名称
        continue
    tmp = word[0:2]
    if tmp[0] == '[' or tmp[0] == '/' or tmp[0] == '@':  # 过滤掉图片和表情，例如[图片]，/滑稽
        continue
    newtext.append(word)
# 将过滤掉图片和表情和时间信息和qq名称剩下的文字重新写入E盘下的q1.txt文件中去
with open('./张文晨.txt', 'w', encoding='utf-8') as f:
    for i in newtext:
        f.write(i)
# 打开新生成的聊天记录文件
text = open('./张文晨.txt', 'r', encoding='utf-8').read()
word_jieba = jieba.cut(text, cut_all=True)
word_split = " ".join(word_jieba)


# 2.词云制作
with open('./张文晨.txt', encoding='utf-8') as f:
    t = f.read()  # 我们打开需要制作词云图的文件
ls = jieba.lcut(t)
txt = " ".join(ls)  # 下面我们将文章中的词组提出来,我们现在已经把所有词组提取出来，以空格分开，并保存在txt中
pic = imread(r'D:\\桌面\\代码实验\\测试\\python实验\\词云实验\\heart.png')
w = wordcloud.WordCloud(width=2400, height=1800, scale=16,
                        font_path="msyh.ttc", colormap='cool',
                        background_color='white', mask=pic)
w.generate(txt)
w.to_file(r'D:\\桌面\\代码实验\\测试\\python实验\\词云实验\\666.png')
