#coding:utf-8
import urllib

url=['']*500
page=1
while page <=15:
    con =urllib.urlopen(\
        'http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html').read()
    #print con

    i=0
    title=con.find(r'<a title=')
    href=con.find(r'href=',title)
    html=con.find(r'.html',href)

    while title != -1 and href != -1 and html != -1 and i<500:
        url[i]=con[href+6:html+5]
        print url[i]
        title=con.find(r'<a title=',html)
        href=con.find(r'href=',title)
        html=con.find(r'.html',href)
        i+=1

    else:
        print 'find end'

    j=0
    while j<50:
        content=urllib.urlopen(url[j]).read()
        open(r'C:\Users\Administrator\Desktop\data/' +url[j][-26:],'w+').write(content)
        print 'downloading',url[j]
        j+=1
    else:
        print 'ok'
    page+=1    
else:
    print 'finished'
