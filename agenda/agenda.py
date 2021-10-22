import json


class Item():
    def __init__(self, name):
        self.name = name
        self.marked = False
        self.content = []
        self.lvl = 0


def see_item(item):
    stack = []
    print(item.name)
    

    for e in item.content:
    
        stack.append(e)
        while stack != []:
            
            curr = stack.pop()
        
            space = "  "
            space *= curr.lvl
            print(space + curr.name)
            for x in curr.content:
                stack.append(x)


def add_item(name, collection, item, lvl=1):
    if collection.name == name:
        item.lvl = lvl 
        collection.content.append(item)

    elif collection.content == []:
        return

    else:
        for content in collection.content:
            add_item(name,content, item, lvl + 1) 



def item_to_txt(item):
    stack = []
    save = item.name + "\n"
    

    for e in item.content:
    
        stack.append(e)
        while stack != []:
            
            curr = stack.pop()
        
            space = "-"
            space *= curr.lvl
            save += space + curr.name + "\n"
            for x in curr.content:
                stack.append(x)

    return save


def txt_to_item(txt):
    item = Item("")
    last_name = txt.split("\n")[0]
    item.name = last_name

    
    
    lines = txt.split("\n")
    names = list(map(lambda l: l.replace("-",""),lines))
    lvls = list(map(lambda l: l.count("-"), lines))
    
    asoc = {}

    for name in names:
        asoc[name] = []

    for i in range(len(lines)):
        name = names[i]
        ok = True
        for j in range(i,len(lines)):
            if lvls[j] == lvls[i]+1 and ok:
                asoc



    return item

if __name__ == '__main__':
    libro = Item("libro")
    cap1 = Item("cap1")
    murakami = Item("murakami")
    pajaro = Item("pajaro que da cuerda...")
    cap2 = Item("cap2")
    borges = Item("borges") 
    quiroga = Item("quiroga")
    add_item( "libro", libro,  cap1)
    add_item("cap1", libro, murakami)
    add_item("murakami", libro, pajaro)
    add_item("libro", libro, cap2)
    add_item("cap1", libro, borges)
    add_item("cap2",libro, quiroga)
    
    txt = item_to_txt(libro)
    print(txt)
    item  = txt_to_item(txt)
    see_item(item)
