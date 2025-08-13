import re

### for finding pattern and substring and replace



### findall, search, sub, split



string1="HHHHeElo world Hhhhhhhow are you hello again aaaaaaaab are how are howbla bla bla"

#string2=re.findall(".",string1)

# string2=re.findall("H{3}",string1)
# print(string2)



#x=re.sub("\s","    ",string1)
#print(x)

#\b[how]{3}\b
# x=re.sub("h*","    ",string1)
# print(x)


x=re.sub(r"\bhow\b", "dello",string1)
print(x)