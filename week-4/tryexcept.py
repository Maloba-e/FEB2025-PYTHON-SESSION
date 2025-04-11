try:
    file= open('multiple_line.txt','r')
    data = file.read()
    print(data)
except:
    print("sorry,file not found")
finally:
    file.close()