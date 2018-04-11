#coding=utf-8  
#北京及周边省会城市污染数据、天气数据每小时监测值爬虫程序  
import urllib.request  
import re  
import urllib.error  
import time  
#模拟成浏览器  
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")  
opener = urllib.request.build_opener()  
opener.addheaders=[headers]  
#将opener安装为全局  
urllib.request.install_opener(opener)  
def get_pm25(city):  
    #首先执行获取空气质量数据，返回数据更新时间  
    data_time=getpm25(city)  
    #然后将获取到的数据更新时间赋值给获取天气数据函数使用  
    
    
def getpm25(city):  
    try:  
        #设置url地址  
        url="http://pm25.in/"+city  
        data=urllib.request.urlopen(url).read().decode("utf-8")  
        print("城市："+city)  
        #构建数据更新时间的表达式  
        data_time='<div class="live_data_time">\s{1,}<p>数据更新时间：(.*?)</p>'  
        #寻找出数据更新时间  
        datatime=re.compile(data_time, re.S).findall(data)  
        print("数据更新时间："+datatime[0])  
        #构建数据收集的表达式  
        data_pm25 = '<div class="span1">\s{1,}<div class="value">\n\s{1,}(.*?)\s{1,}</div>'  
        data_o3='<div class="span1">\s{1,}<div class ="value">\n\s{1,}(.*?)\s{1,}</div>'  
        #寻找出所有的监测值  
        pm25list = re.compile(data_pm25, re.S).findall(data)  
        o3list=re.compile(data_o3, re.S).findall(data)  
        #将臭氧每小时的值插入到原列表中  
        pm25list.append(o3list[0])  
        print("AQI指数，PM2.5，PM10，CO，NO2，SO2，O3：（单位：μg/m3，CO为mg/m3）")  
        print(pm25list)  
        #将获取到的值写入文件中  
        writefiles_pm25(city,datatime,pm25list)  
        #返回数据更新时间值  
        return datatime  
    except urllib.error.URLError as e:  
        print("出现URLERROR！一分钟后重试……")  
        if hasattr(e,"code"):  
            print(e.code)  
        if hasattr(e,"reason"):  
            print(e.reason)  
        time.sleep(60)  
        #出现异常则过一段时间重新执行此部分  
        getpm25(city)  
    except Exception as e:  
        print("出现EXCEPTION！十秒钟后重试……")  
        print("Exception："+str(e))  
        time.sleep(10)  
        # 出现异常则过一段时间重新执行此部分  
        getpm25(city)  
def writefiles_pm25(filename,datatime,pm25list):  
    #将获取的数据写入文件中，数据分别为时间，AQI指数，PM2.5，PM10，CO，NO2，SO2，O3。（单位：μg/m3，CO为mg/m3）  
    f = open("F:\work\Programe\Python\Scrap\Beijing_demo\data_pm2.5_"+filename+".txt", "a")  
    f.write(datatime[0])  
    f.write(",")  
    for pm25 in pm25list:  
        f.write(str(pm25))  
        f.write(",")  
    f.write("\n")  
    print("该条空气质量数据已添加到文件中！")  
    f.close()

    


    
#退出循环可用Ctrl+C键  
while True:  
    print("开始工作！")  
    get_pm25("beijing")  
  
    #每一小时执行一次  
    print("休息中……")  
    print("\n")
    #周期一小时
    time.sleep(3600)
