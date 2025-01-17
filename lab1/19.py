#Escape Characters 
txt = "We are the so-called \"Vikings\"from the north."
print(txt)


txt = 'It\'s alright.'
print(txt) #It's alright.


txt = "This will insert one \\ (backslash)."
print(txt) #This will insert one \ (backslash).


txt = "Hello\nWorld!" #n = new line
print(txt)


txt = "Hello\rWorld!"
print(txt) #Hello
           #World


txt = "Hello\tWorld!" #t = tab
print(txt) #Hello   World!


#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) #HelloWorld!