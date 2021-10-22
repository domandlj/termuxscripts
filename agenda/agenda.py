import json

BLANK_LINE = ""
EOL = "\n"
SEPARATOR = "-"

class Item():
    def __init__(self, name):
        self.name = name
        self.marked = False
        self.content = []
        self.lvl = 0


def see_item(item):
    stack = []
    print(item.name)
    

    for item_i in item.content:
    
        stack.append(item_i)
        while stack != []:
            
            curr = stack.pop()
        
            space = SEPARATOR
            space *= curr.lvl
            print(space + curr.name)
            for item_j in curr.content:
                stack.append(item_j)


def add_item(name, collection, item, lvl = 1):
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
    save = item.name + EOL
    

    for e in item.content:
    
        stack.append(e)
        while stack != []:
            
            curr = stack.pop()
        
            space = SEPARATOR
            space *= curr.lvl
            save += space + curr.name + EOL
            for x in curr.content:
                stack.append(x)
    
    save = save[:len(save)-1]
    
    return save


def txt_to_dict(txt):
    item = Item(BLANK_LINE)
    item.name = txt.split(EOL)[0]
    

    lines = txt.split(EOL)

    names = list(map(lambda line: 
        line.replace(SEPARATOR,BLANK_LINE), lines))
    
    lvls = list(map(lambda line:
        line.count(SEPARATOR), lines))
    
    item_dict = {}

    for i in range(len(lines)):
        item_dict[names[i]] = []

        j = i + 1
        ok = True
        
        while ok and j < len(lines):
            if lvls[j] == lvls[i] + 1:
                item_dict[names[i]].append(names[j])
            
            elif lvls[j] == lvls[i]:
                ok = False
            
            j += 1
    
    return item_dict

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
    item  = txt_to_dict(txt)
    print(item)
