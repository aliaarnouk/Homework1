name=input("ENTER USERNAME")
numoftrue=0
infile=open("أسئلة.txt",'r')
outfile=open("النتيجة.txt","w")
l1=[line.rstrip() for line in infile]
infile.close()
print("أجب عن الأسئلة التالية")
for q in l1:
    print(q[0:q.index(',')])
    a=input()
    if a==q[q.index(",")+1:]:
        numoftrue+=1
result=f"your name is {name} and your true answers is {numoftrue}"
print(result)
outfile.write(result)
outfile.close()
