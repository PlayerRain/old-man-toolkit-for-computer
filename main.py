import easygui as g
from xes.ext import *
import webbrowser
import openai
from xes.AIspeak import *
import json
import time
import os
from jieba import *

try:
    with open("options.json", 'r') as options_temp:
        options = json.load(options_temp)
        write_options = open("options.json",'w')
        if options['setmode'] == '':
            xuanze = g.buttonbox(msg = '请选择人声', title = '银发辅助 选择', choices = ['女声','男声'])
            if xuanze == '女声':
                speak("女声")
                options["setmode"] = 'girl'
            elif xuanze == '男声':
                speak("男声")
                options['setmode'] = 'boy'
            write_options.write(json.dumps(options))
        write_options.close()
except:
    options={'setmode':"boy","yusu":1,"can_speak":"True"}
    write_options = open("options.json", 'w')
    write_options.write(json.dumps(options))
    write_options.close()
    g.buttonbox(title="银发辅助 报错",msg='防报错退出已生效，现在你可以正常使用软件',choices=["继续"])

setmode(options['setmode'])
setspeed(options["yusu"])
print(options["can_speak"])
can_speak=bool(options["can_speak"])

zhuchuangkou1 = ['看小视频','保健知识','娱乐','便携短信','气温','聊天','设置','时间','关于']
speakertext = {'girl':"女声",'boy':"男声"}
yusu_text={0:"最慢",1:"一般",2:"最快"}
can_speak_text={'True':"已开启",'False':"已关闭"}
weather_text = {1:"明日气温：",0:"今日气温：",-1:"昨日气温："}
qk = ['设置男声', '设置女声', '设置说话快慢', '取消语音','重置设置','保存设置','直接退出']

openai.api_key = "sk-BXVeJgRJFYifUDgP4d61EcB9B7D6426bBe90Ad6bA83f59Bc"
openai.api_base = "https://api.gpt.ge/v1"
current_dir = os.getcwd()
files = os.listdir(current_dir)

def chat(prompt, model="gpt-3.5-turbo", temperature=1):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def ifspeak(a):
    if options['can_speak'] == 'True':
        speak(a)

for file in files:
    if file.endswith(".wav"):
        file_path = os.path.join(current_dir, file)
        os.remove(file_path)
        print(f"已删除文件: {file_path}")

while True:
    print(options)
    windows = g.buttonbox(msg = '请单击按钮启动程序', title = '银发辅助', choices = zhuchuangkou1)

    if windows == '时间':
        clock = time.strftime("%H:%M:%S")
        ifspeak('当前时间为' + clock)

    if windows == '看小视频':
        ifspeak("看小视频")
        qudao = g.buttonbox(msg = '请选择渠道', title = '电脑辅助使用软件 渠道', choices = ['bilibili','抖音','退出'])
        if qudao == 'bilibili':
            ifspeak("bilibili")
            url = 'https://www.bilibili.com/tv/?spm_id_from=333.1007.0.0'
            webbrowser.open(url)

        elif qudao == '退出':
            pass

        else:
            ifspeak("抖音")
            url = 'https://www.douyin.com'
            webbrowser.open(url)
    if windows == '保健知识':
        ifspeak("保健知识")
        webbrowser.open('https://www.39.net/')
    if windows == '娱乐':
        ifspeak("娱乐")
        yule = g.buttonbox(msg = '请选择游戏', title = '电脑辅助使用软件 游戏', choices = [
            '纸牌',
            '麻将',
            '象棋',
            '音乐',
            "退出"])
        if yule == '纸牌':
            ifspeak("纸牌")
            url = 'https://www.4399.com/flash/117945_4.htm'
            webbrowser.open(url)
        if yule == '麻将':
            ifspeak("麻将")
            url = 'https://www.4399.com/flash/110975_1.htm'
            webbrowser.open(url)
        if yule == '象棋':
            ifspeak("象棋")
            url = 'https://www.4399.com/flash/36944_3.htm'
            webbrowser.open(url)

        if yule == '退出':
            ifspeak("退出")
            continue

        if yule == '音乐':
            ifspeak("音乐")
            music = g.choicebox('请选择音乐', choices = ('周杰伦-晴天.mp3', '刘德华-忘情水.mp3', '童安格-明天你是否依然爱我.mp3', '王杰-一场游戏一场梦.mp3', '张镐哲-不是我不小心.mp3', '张雨生-我的未来不是梦.mp3'))

            if music == '周杰伦-晴天.mp3':
                ifspeak("周杰伦-晴天")
                play_mp3('周杰伦-晴天.mp3')
                zhuchuangkou1.append('暂停音乐')
            if music == '刘德华-忘情水.mp3':
                ifspeak("刘德华-忘情水")
                play_mp3('刘德华-忘情水.mp3')
                zhuchuangkou1.append('暂停音乐')
            if music == '童安格-明天你是否依然爱我.mp3':
                ifspeak("童安格-明天你是否依然爱我")
                play_mp3('童安格-明天你是否依然爱我.mp3')
                zhuchuangkou1.append('暂停音乐')
            if music == '王杰-一场游戏一场梦.mp3':
                ifspeak("王杰-一场梦一场戏")
                play_mp3('王杰-一场游戏一场梦.mp3')
                zhuchuangkou1.append('暂停音乐')
            if music == '张镐哲-不是我不小心.mp3':
                ifspeak("张镐哲-不是我不小心")
                play_mp3('张镐哲-不是我不小心.mp3')
                zhuchuangkou1.append('暂停音乐')
            if music == '张雨生-我的未来不是梦.mp3':
                ifspeak("张雨生-我的未来不是梦")
                play_mp3('张雨生-我的未来不是梦.mp3')
                zhuchuangkou1.append('暂停音乐')
    if windows == '便携短信':
        ifspeak("便携短信")
        dianhuahaoma = g.enterbox('请输入要发送电话号码：')
        ifspeak("请输入要发送的电话号码")
        if dianhuahaoma == None:
            pass
        else:
            xiaoxi = g.buttonbox(msg = '请选择快捷语句', title = '电脑辅助使用软件', choices = [
                '快点回家',
                '买点菜',
                '家里出事了',
                '自定义'])
            int(dianhuahaoma)
            if xiaoxi == '自定义':
                xiaoxi = g.enterbox('请输入要发送语句：')
                ifspeak("请输入要发送的短信")
                send_msg(dianhuahaoma, xiaoxi)
    if windows == '气温':
        ifspeak("气温")
        ifspeak("请输入要查询气温的城市")
        city = g.enterbox('请输入要查询气温的城市：')
        if city == None:
            continue
        ifspeak("请选择查询气温的日期")
        day = g.choicebox('请选择查询气温的日期', choices = ('今天气温', '昨天气温', '明天气温'))
        if day == None:
            continue
        if day == '今天气温':
            ifspeak("今天气温")
            day = 0
            int(day)
        if day == '昨天气温':
            ifspeak("昨天气温")
            day = -1
            int(day)
        if day == '明天气温':
            ifspeak("明天气温")
            day = 1
            int(day)
        weather = air_temp(city, day)
        wd_text = weather_text[day]+str(weather)+"度"
        ifspeak(wd_text)
        weathers = g.buttonbox(msg = wd_text, title = '银发辅助', choices = ['退出'])

    if windows == "聊天":
        ifspeak("聊天")
        msg=''
        while True:
            if msg == '':
                q1=g.textbox(msg='请输入', title='聊天', text='', codebox=False, callback=None, run=True)
            else:
                q1=g.textbox(msg=msg, title='聊天', text='', codebox=False, callback=None, run=True)
            if q1 == None:
                break
            else:
                try:
                    try:
                        msg=chat(q1)
                        ifspeak(msg)
                    except:
                        msg=chat(q1)
                except:
                    msg="出现了一些问题"
                    ifspeak(msg)


    if windows == "暂停音乐":
        ifspeak("暂停音乐")
        play_mp3("周杰伦-晴天.mp3",0)
        del zhuchuangkou1[9]

    if windows == None:
        with open("options.json","w") as write_options:
            write_options.write(json.dumps(options))
            write_options.close()
        break

    if windows == "关于":
        ifspeak("关于")
        text = "应用名称：银发辅助\n版本号：1.0.0\n发布日期：2024/6/22\n开发者信息：yywuhuy工作室(成员：义务互，Rain)\n功能简介：银发辅助是一款集成多种实用功能的辅助工具，旨在帮助老年人如\n何更好的电脑。主要功能包括智能语音、一键操作、AI人工等。\n联系方式：yywuhuy@qq.com\n版权声明: © 2024 yywuhuy工作室。保留所有权利。"
        g.textbox(text,'银发辅助 关于')
    if windows == "设置":
        ifspeak("设置")
        with open('options.json','w') as write_options:
            while True:
                test="请单击按钮设置\n声音:"+speakertext[options['setmode']]+",\n语速："+yusu_text[options["yusu"]]+",\n语音："+can_speak_text[options['can_speak']]
                setting = g.buttonbox(msg=test, title='银发辅助 设置', choices = qk)
                if setting == '设置男声':
                    ifspeak("设置男声")
                    options['setmode'] = 'boy'
                elif setting == '设置女声':
                    ifspeak("设置女声")
                    options['setmode'] = 'girl'
                elif setting == '保存设置':
                    ifspeak("保存设置")
                    setmode(options['setmode'])
                    setspeed(options["yusu"])
                    write_options.write(json.dumps(options))
                    write_options.close()
                    break
                elif setting == '重置设置':
                    options = {'setmode': "boy", "yusu": 1, "can_speak": "True"}
                    can_speak = True
                elif setting == '设置说话快慢':
                    speak("设置说话快慢")
                    yusu_set=g.buttonbox(msg="请设置语速",title="银发辅助 设置 说话快慢",choices = ['慢','一般','快'])
                    if yusu_set =="快":
                        options['yusu'] = 2
                    elif yusu_set == '慢':
                        options['yusu'] = 0
                    elif yusu_set == '一般':
                        options['yusu'] = 1

                elif setting == "取消语音":
                    qk[3]="开启语音"
                    options['can_speak']= 'False'

                elif setting == "开启语音":
                    qk[3] = "取消语音"
                    options['can_speak'] = 'True'





