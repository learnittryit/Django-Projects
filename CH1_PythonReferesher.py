age = 20
name = "Kunal"
print("My name is ",name," I am ",10," years old")
print(f'Hi My name is {name} and I am {age} years old')

isMale=False

#Single line comment
"""
This is an actual string - or a comment
"""

if(age>20):
    print('oh great you are 20 years')
elif(age<20):
    print(f'you are {age} years great')
else:
    print("Sorry--->")

if(isMale):
    print("He is a male")
else:
    print("She is a female")



# Defining functions
count=0
print(count)
def hello(name):
    age=20
    print('This is a hello function - my name is ',name)
    print(callme(name,age))

def callme(name,age):
#    count=count+1
    return (":- Calling another function - my name is {} and I am {} years old".format(name,age))



hello('Kunal')
sentence =callme("Ram",32)
print(sentence)




def tripleprint(arg="Default"):
    for i in range(3):
        print(arg)
    print(arg*3)

tripleprint()
tripleprint("Hey..")


######## List
lst=["name-"+str(i) for i in range(1,4)]
print(lst)
print(lst[0])
del(lst[2])
print(lst)


#### Loops
dogNames=["Pem","Maxy","dimp","mark"]

for dog in dogNames:
    print(dog)


for val in range(1,11):
    print(val)

print("\n--------------\n")
count=0
while(count<3):
    print(count)
    count=count+1



dict={"name":["Kunal","Kamna","Atulyaa","Harsh"],"age":[10,15,20,25]}
print(dict["name"])
counter=0
for key,val in dict.items():
    counter+=1
    print(key,"<<<<< -  >>>>>",val)
    print(counter)

#### Dictionary - dictionaries
words=["pogo","spang","lifi"]
definitions = ["Def-Pogo","Def-Spang","Def-lifi"]
dict={"word":words,"definition" : definitions}


for val in dict.values():
    print(val)
for key in dict.keys():
    print(key)
for k,v in dict.items():
    print(k,".....---....",v)

dicN={}
for i in range(0,len(words)+1):
    dicN[words[i]]=definitions[i]

print(dicN)
