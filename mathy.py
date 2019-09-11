responses=["WELCOME","MY NAME IS MUNNA","THANK YOU","SORRY,THIS IS BEYOND MY ABILITY"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
          l.append(float(t))
        except ValueError:
            pass
    return l
def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
      if l%a==0 and l%b==0:
        return l
      l+=1
def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if h%a==0 and h%b==0:
            return h
        h-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input("press enter to exit")
    exit()
def sorry():
    print(responses[3])
def myName():
    print(responses[1])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"LCM":lcm,"HCF":hcf,"MINUS":sub,"SUB":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"PRODUCT":multiply,"DIVISION":division,"DIVIDE":division}
commands={"NAME":myName,"END":end,"STOP":end,"CLOSE":end}
    
        


