try:
    file= open('samaeple.txt','r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("sorry,this file does not exist")
finally:
    print("End of Code")
    