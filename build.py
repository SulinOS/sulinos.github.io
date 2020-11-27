from sitemaker import *
import sitemaker.themes.classic as theme

def create_menu(current=0):
    i=0
    menu=[]
    items=["Home","Download","Documents","Join Us","Gallery"]
    links=["index.html","download.html","document.html","join.html","gallery.html"]
    for i in range(0,len(links)):
        if i == current:
            menu.append(link(links[i],items[i],cls="current"))
        else:
            menu.append(link(links[i],items[i]))
    return menu

def create_footer():
    footer=[]
    footer.append(tagged("center",item(H("&copy; 2016 - 2020 SulinOS Project",4))))
    footer.append(tagged("center",item("The software used in this project is licensed with GPLv2 GPLv3 LGPLv2 LGPLv3 AGPLv3. Documents are licensed with FDL. <br> The website is under MIT license. <a href=\"https://gitlab.com/sulincix/sitemaker\">Site builder</a> is under WTFPL.")))
    return footer

def create_skeleton(num):
    p=theme.theme_page()
    p.p.addRel("https://distrowatch.com/dwres.php?waitingdistro=579&resource=links")
    p.menu=create_menu(num)
    p.footers=create_footer()
    p.logo.setImage("sulin-logo.svg")
    p.title="Sulin Project"
    p.addCss("main.css")
    return p
    
#css theme
c=theme.theme_css()
c.build()
c_font=css("body",2)
c_font.add("font-family","monospace")
c_menu=css("nav li a",2)
c_menu.add("color","black")
c_menu.add("font-weight", "bold")
c_menu2=css("nav li a:hover, nav li a.current",2)
c_menu2.add("color","white")
c_menu2.add("font-weight", "bold")
c.css.addCss(c_font)
c.css.addCss(c_menu)
c.css.addCss(c_menu2)
c.css.save("main.css")


# index.html
p=create_skeleton(0)

# index content
article=tagged("article")
article.addItem(item(H("What is SulinOS ?",2)))
article.addItem(tagged("p",item(open("src/index/1.txt").read())))
article.addItem(tagged("p",item(open("src/index/2.txt").read())))
article.addItem(tagged("p",item(open("src/index/3.txt").read())))
article.addItem(item(H("Why SulinOS ?",2)))
article.addItem(tagged("p",item(open("src/index/4.txt").read())))
article.addItem(tagged("p",item(open("src/index/5.txt").read())))
p.add(article)
#p.add(item("""<iframe width="99%" height="300" src="https://www.youtube.com/embed/NhWDE5JaJ3o"></iframe>"""))
p.save("index.html")

# download.html
p=create_skeleton(1)

# download content
p.add(tagged("p",item(open("src/download/1.txt").read())))
p.add(tagged("p",item(open("src/download/2.txt").read())))
p.save("download.html")

# document.html
p=create_skeleton(2)

#document content
p.add(tagged("p",item(open("src/document/1.txt").read())))
p.save("document.html")

#join.html
p=create_skeleton(3)

# join content
p.add(tagged("p",item(open("src/join/1.txt").read())))
t=table(3,3)
p.add(tagged("center",item(H("SulinOS Developer Team",3))))
t.setItem(0,0,item(open("src/join/sulincix.txt").read()))
t.setItem(0,1,item(open("src/join/zaryob.txt").read()))
t.setItem(0,2,item(open("src/join/frknkrc44.txt").read()))
t.setItem(1,0,item(open("src/join/koala.txt").read()))
t.setItem(1,1,item(open("src/join/dedeler31.txt").read()))
t.setItem(1,2,item(open("src/join/doop.txt").read()))
t.setItem(2,0,item(open("src/join/eayavas.txt").read()))
t.setItem(2,1,item(open("src/join/hayalet3.txt").read()))
t.setItem(2,2,item(open("src/join/nobugger.txt").read()))
p.add(tagged("center",t))
p.save("join.html")

# gallery.html
p=create_skeleton(4)

# gallery content
p.add(tagged("center",item(open("src/gallery/1.txt").read())))
p.save("gallery.html")


# empty.html
p=create_skeleton(-1)

# empty content
p.save("empty.html")

