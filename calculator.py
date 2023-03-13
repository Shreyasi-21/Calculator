def add(P, Q):    
     
   return P + Q   
def subtract(P, Q):   
     
   return P - Q   
def multiply(P, Q):   
     
   return P * Q   
def divide(P, Q):   
      
   return P / Q  
def modulus(P, Q):
    
    return P % Q
   
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")
print ("e. Modulus")     
    
choice = input("Please enter choice (a/ b/ c/ d/ e): ")    
    
P= int (input ("Please enter the first number: "))    
Q = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (P, " + ", Q, " = ", add(P, Q))    
    
elif choice == 'b':    
   print (P, " - ", Q, " = ", subtract(P, Q))    
    
elif choice == 'c':    
   print (P, " * ",Q, " = ", multiply(P, Q))    
elif choice == 'd':    
   print (P, " / ", Q, " = ", divide(P, Q))
elif choice == 'e':
    print (P, " % ", Q, " = ", modulus(P, QA))
           
else:    
   print ("This is an invalid input")    
