import json

BLANK = ""
EOL = "\n"
SEPARATOR = "-"
MARKED = ";"

class Item():
    def __init__(self, name : str):
        self.name = name.replace(MARKED, BLANK)
        self.marked = False
        self.content = []
        self.lvl = 0

def add_item(name : str, target_item : Item, item : Item):
    """
        Adds item to the sub-item called name in target_item
        Traverses target_item using BFS.
    """
    lvl = 1
    if target_item.name == name:
        item.lvl = lvl
        target_item.content.append(item)

    else:
        items = target_item.content
        queue_of_lvl = items 
        
        while queue_of_lvl:
            next_lvl = []
            
            
            for sub_item in queue_of_lvl:
                next_lvl += sub_item.content

                if sub_item.name == name:
                    item.lvl = lvl + 1 
                    sub_item.content.append(item)

            lvl += 1
                    

            queue_of_lvl = next_lvl
            

def item_to_str(item : Item) -> str:
    """
        Converts item to string.
        Traverses item using BFS.
    """
    queue = []
    save = item.name + EOL


    for e in item.content:
    
        queue.append(e)
        while queue:
            
            item_i = queue.pop(0)
            space = SEPARATOR
            space *= item_i.lvl
            
            name = item_i.name

            if item_i.marked:
                item_i.name += MARKED
            
            save += space + item_i.name + EOL
            
            for item_j in item_i.content:
                queue.append(item_j)
    
    save = save[:len(save)-1]
    
    return save


def str_to_dict(txt : str) -> dict:
    """
        Parses txt and transforms it to dict.
    """
    item = Item(BLANK)
    item.name = txt.split(EOL)[0]
    

    lines = txt.split(EOL)
    
    marked = list(map(lambda line: 
        line.count(MARKED) > 0, lines))

    lines = list(map(lambda line:
        line.replace(MARKED, BLANK), lines))

   
    names = list(map(lambda line: 
        line.replace(SEPARATOR, BLANK), lines))
    

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

        item_dict[names[i]].append(marked[i])
    
    return item_dict


def dict_to_item(item_dict : dict) -> Item:
    """
        Transforms dict into item.
    """

    item = Item("")
    keys = item_dict.keys()

    item.name = list(item_dict.keys())[0]
    
    for key in keys:
        sub_items = item_dict[key]
        marked = sub_items.pop()
        
        for name in sub_items:
            sub_item = Item(name)
            items = item_dict[name]
            sub_item.marked = items[len(items)-1]
            add_item(key, item, sub_item)

    return item 

if __name__ == '__main__':
    txt = open('foo.txt')
    txt = txt.read()
    
    med = str_to_dict(txt)
    item = dict_to_item(med)
    print(item_to_str(item))
