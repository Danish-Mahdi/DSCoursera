
# L=[]
# for i in range(10):
#     print(i+1)
#     L.append(i**2)
# print(L)


# L=[]
# for i in range(2,20,4):
#     print(i)
#     L.append(i**3)
# print(L)


#Else with for
# S={"Abro", 22, "Dani"}
# for x in S:
#     print(x)
# else:
#     print("All iterations completed")



#Else with for and break
# S={"Abro", 22, "Dani"}
# for x in S:
#     if(x!=22):
#         print(x)
#     else: 
#         print("followed by break statement")
#         break
# else:
#     print("All iterations completed")

# S={"apple", 3.0,"banana"}
# i=1
# for x in S:
#     print (x)
#     i+=1
#     if i==3:
#         break
#     else:
#         pass
# else:
#     print("Loop terminates with success")
# print("Outside the loop")




# D={'A':22,'B':76,'C':90}
# for x in D:
#     print(x, D[x])



# Sort array in ascending order
# L=[1,2,4,-5,7,9,3,2]
# first lets find the minimum num and index of the min num
# m=L[0]
# idx=[0]
# c=0
# for i in L:
#     if i<m:
#             m=i
#             idx=c
#     c+=1
# print(idx,m)





# L=[1,2,4,-5,7,9,3,2]
# for j in range(len(L)):
#             m=L[j]
#             idx=j
#             c=j
#             for i in range(j,len(L)):
#                 if L[i]<m:
#                     m=L[i]
#                     idx=c
#                 c+=1
#             tmp=L[j]
#             L[j]=m
#             L[idx]=tmp
# print(L)




# Functions in Python
# def printS():
#     print ("Hello1")
#     print ("Hello2")
#     print ("Hello3")

# print ("We are learning Functions")

# printS()


# def Print2():
#     """ 
#     This is the second print function
#     rfrkmfrfff
#     """
#     print("Danish Here")

# Print2??


# def printmsg2(msg1,msg2):
#     print(msg1, msg2)

# printmsg2("Dani","Abro")



# def mypow(x,y):
#     """" This is a pow function """
#     z=x**y
#     print(z)
# mypow(2,3)


# help(mypow)

# def checkargs(a,b,c):
#     """Function to check datatypes of arguments and then proceed"""
#     if isinstance(a,(int,float)) and  isinstance(b,(int,float)) and isinstance(c,(int,float)):
#         z=a+b+c
#         print("The sum of all the arguments is ", z)
#     else:
#         print("Error: The arguments are not of the expected datatype")

# checkargs(22,33.90,8)

# checkargs(20,"dede",99)
# checkargs(2.09,22)


# def f(a,b,c):
#     print("A is: ",a)
#     print("B is: ",b)
#     print("C is: ",c)

# f("Mahdi","Danish","Abro")

# f(c="Abro", a="Hasni", b="Mahdi")


# def add(x,y):
#     c=x+y
#     return c
# z=add(22,88.9)
# print(z)

"""voutf=22 #global scope variable
def f2():
    voutf=32 #local scope variable
    print(voutf) #local scope variable
    # returns none if return is not defined explicitly
    return voutf


f2()
print(voutf) #global scope variable

print(type(f2()))

"""

# def r():
#     a=90
#     b="You"
#     c=11.8
#     return a,b,c
    
# x,y,z=r()
# print(r())
# print(x,y,z)

""" def sumA(*args):
    s=0
    for i in range(len(args)):
        s+=args[i]
    return(s)
print(sumA(33.9,27.1,100,9))



def printAllvariableNandV(**args):
    for x in args:
        print("Variable name is: ", x, " and the value is: ", args[x])

printAllvariableNandV(a="Abro", b="Kamario", c=22)
    
# default value
def f(s=9): #s=9 will be printed if no other value of s is given
    print(s)

f(22) 

L1=[11,90,22]
L2=L1
L2[1]=3
print(L1)
print(L2)

def ff(L=[1,2]):
    for i in L:
        print(i)
L2=[12,33,22]
ff()

ff(L2)
"""



# function usage for sorting the list

# function for finding the min num
# def findMin(L,startI):
#     m=L[startI]
#     idx=startI
#     for i in range(startI,len(L)):
#         x=L[i]
#         if x<m:
#             m=x
#             idx=i
#         else:
#             pass
#     return m,idx


# L1=[22,90,32,9,8,44]
# print(findMin(L1,0))




#function for swapping the values
# def swapV(L,idx1,idx2):
#     tmp=L[idx1]
#     L[idx1]=L[idx2]
#     L[idx2]=tmp
#     return L

    

# def checkIfNotNumeric2(L):
#     for x in L:
#         if not (isinstance(x, (int, float))):
#             return False
#         return True






# def sortList(L):
#     if not (checkIfNotNumeric2(L)):
#             print("Error: List does not contain numeric values")
#             return
#     else:
#         c=0
#         for x in L:
#             m,idx=findMin(L,c)
#             L=swapV(L,c,idx)
#             c+=1
#         return L


# L2 =sortList( [22, 90, -32, 9, 8, 44])
# print(L2)



# S="Hello"
# D=22
# E=S+" "+ str(D)
# # print(E)
# print(S,D)

# # Multi-line string
# N=""" Dani
#             Mahdi  """
# print(N)

S='    HELLO, g, how are you?  '
# print(S[1])
# print(S[0:5])
# print(S[0:5:3])
# print(len(S))
# print(S[:21])
# print(S[3:])
# print(S[::-1])
# print(S.strip())
# print(S.replace('H','B'))
# print(S.lower())
# print(S.upper())
# W=S.split(',')
# print(W[1])

print("HE" in S)
print("DE" not in S)


# Escape char
print('We are learning  "Maths" ')
print('We are learning \t Maths ')
print('We are learning \n Maths ')
# \n means raw string
print(r'We are learning \n Maths ')


