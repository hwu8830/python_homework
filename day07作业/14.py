# 让用户输入一句话,判断这句话中有没有邪恶,如果有邪
#    恶就替换成这种形式然后输出,如:“老牛很邪恶”,输出后变
#    成”老牛很**”;

def findevil(str,oldword,newword):
  newStr = str.replace(oldword,newword)
  return newStr

str= input("请输入句话")
a = "邪恶"
b = "大"
print(findevil(str,a,b))