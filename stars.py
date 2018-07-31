# python stars.py
#Part 1
def draw_stars(lst):
    star = "*"
    output = ""
    for number in range(0,len(lst)):
        output += star * lst[number]+"\n"
    print output
draw_stars([4,6,1,3,5,7,25])

#Part 2
def draw_starStr(lst):
    star = "*"
    output = ""
    for value in range(0,len(lst)):
        if isinstance(lst[value], str):    
            output += lst[value][0].lower() * len(lst[value])+"\n"
        if isinstance(lst[value],int):
            output += star * lst[value]+"\n"
        
    print output
draw_starStr([4,'Tom',1,'Michael',5,7,'Jimmy Smith'])
