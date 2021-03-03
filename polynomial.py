def display_menu():
    """ Display the list of polynomial available tools"""
    print("1-Insert; 2-Remove; 3-Info; 4-Evaluate; 5-Scaling; 6-Derive; 7-Integrate")
    print("8-Summation; 9-Subtract; 10-Multiply; 11-Divide")
    
def get_polynomial_easy(all_coef):
    """ Easy way out to use if you cannot implement get_polynomial as requested """
    return list(map(float,all_coef.split()))

def get_polynomial(all_coef):
    nums=[]
    num=""
    #I go through each character looking for a space, store each previous character into num. 
    #When I find a space I turn num into a float, save it into nums, and reset num
    for i in all_coef:
        if i== " ":
            nums=nums+[float(num)]
            num=""
        else:
            num=num+i
    if num != "":
        nums=nums+[float(num)]
    return nums
    #returns the list nums which has all the number values

def display_list(list_poly):
    if len(list_poly) !=0:
        for i in range(len(list_poly)):
            if len(list_poly)!=0:
                print(str(i+1)+": "+get_expression(list_poly[i]))
            else:
                print("0.0")
    #I iterate in a for loop and call get_expression for each polynomial unless it has no polynomials

def get_expression(poly_string):
    poly=""
    if len(poly_string)==0:
        return "0.0"
    while poly_string[0]==0:
        poly_string.remove(0)
        if len(poly_string)==0:
            return "0.0"
    #Here I look to remove all starting 0's and checking if the list is all 0's or has no numbers
    if len(poly_string)==2:
        if poly_string[0]!=0:
            poly=poly+str(poly_string[0])+"x"
            if poly_string[1]!=0:
                if poly_string[1]>0:
                    poly=poly+"+"+str(poly_string[1])
                else:
                    poly=poly+str(poly_string[1])
            return poly
        elif poly_string[1]!=0:
            return poly+str(poly_string[1])
        else:
            return "0.0"
    if len(poly_string)==1:
        if poly_string[0]!=0:
            return str(poly_string[0])
        else:
            return "0.0"
    #Here I do the conditional cases for if there are only 1 or 2 numbers in order to correctly place my "+" sign
    #I also check for 0's at the ends or start in case
    for i in range(len(poly_string)):
        if i==(len(poly_string)-1):
            if poly_string[i]!=0:
                if poly_string[i]>0:
                    poly=poly+"+"+str(poly_string[i])
                else:
                    poly=poly+str(poly_string[i])
        elif i==(len(poly_string)-2):
            if poly_string[i]!=0:
                if poly_string[i]>0:
                    poly=poly+"+"+str(poly_string[i])+"x"
                else:
                    poly=poly+str(poly_string[i])+"x"
        elif i==0:
            if poly_string[i]!=0:
                poly=poly+str(poly_string[i])+"x^"+str(len(poly_string)-i-1)
        else:
            if poly_string[i]!=0:
                if poly_string[i]>0:
                    poly=poly+"+"+str(poly_string[i])+"x^"+str(len(poly_string)-i-1)
                else:
                    poly=poly+str(poly_string[i])+"x^"+str(len(poly_string)-i-1)
    return poly
    #Here is my main loop where I loop through to make the string. I check if it has a power if not then it goes into one of the
    #earlier condition. It also checks to skip 0's and puts in the correct power and "+" if its postive or leaves it as it is for the 
    # "-" sign to represant -
def degree(poly):
    if poly==[]:
        return 0
    else:
        while poly[0]==0:
            poly.remove(0)
            if poly==[]:
                return 0
    return len(poly)-1
    #Here I first check if there is nothing in the list, I also remove 0's and after all that I find the highest degree by
    #taking the length of the list minus one
def evaluate(poly,num):
    sum=0
    numb=float(num)
    if len(poly)>1:
        for i in range(len(poly)-1):
            sum=sum+(poly[i]*(numb**(len(poly)-1.0-i)))
    sum=sum+poly[-1]
    return sum
    #Here I evaluate the polynomial first by making the number into a float. Then I do a for loop and sum up all the
    #values for the coefficient * the number except for the last number which has no coefficent. Then I add the last number using
    #list[-1] to recieve the last number and return sum
def scale(poly,scale):
    polyF=[]
    for i in poly:
        polyF.append(i*scale)
    return polyF
#I created a new list so I could iterate in the for loop easier, then I appended all the values multiplied by the scalar 
#and returned the new list
def derive(poly):
    polyF=[]
    if len(poly)==1:
        return [0.0]
    else:
        for i in range(len(poly)-1):
            polyF.append(poly[i]*(len(poly)-i-1))
        return polyF
#first I check for 1 polynomial, if so I return [0.0]. If not I loop through all the numbers except the last and I multiple by the 
# exponent. At the end I negate the last polynomial since the derivative of any number times x to the power of 0 is 0
def integrate(poly,lo,up):
    sumU=0.0
    sumL=0.0
    for i in range(len(poly)):
        poly[i]=poly[i]/float(len(poly))
        sumU=sumU+poly[i]*(float(up)**(len(poly)-i))
        sumL=sumL+poly[i]*(float(lo)**(len(poly)-i))
    return sumU-sumL
#Here I ran a for loop through the polynomial that first divides the coefficient and then solves for the integral of the lower 
#and upper bound
def add(list1,list2):
    Flist=[]
    if len(list1)>len(list2):
        size=len(list1)
        smal=size-len(list2)
    else:
        size=len(list2)
        smal=size-len(list1)
    for i in range(size):
        Flist=Flist+[0.0]
    for i in range(size-1,smal-1,-1):
        Flist[i]=list1[len(list1)-(size-i)]+list2[len(list2)-(size-i)]
    if len(list1)>len(list2):
        for i in range(smal):
            Flist[i]=list1[i]
    elif len(list2)>len(list1):
        for i in range(smal):
            Flist[i]=list2[i]
    return Flist
#In this part, I first created an empty list equal to the size of the biggest polynomial. Then I filled that list with 0.0. I then looped
#backwards to sum up the coefficients starting for the least going to the greatest degree for the smaller polynomial. After I looked to find
#the bigger polynomial, then I added the coefficients that was left of the bigger polynomial if they were different sizes
def subtract(list1,list2):
    list3=[]
    for i in list2:
        list3=list3+[i*-1]
    return add(list1,list3) 
#Here I made a new list that stored the negitive polynomial which was being subtracted. Then I added the new polynomial with the first
#one using the fuction add that I created earlier
def multiply(l1,l2):
    p=[0.0]
    ptemp=[]
    for i in range(len(l1)):
        ptemp=scale(l2,l1[len(l1)-i-1])
        for j in range(i):
            ptemp=ptemp+[0.0] 
        p=add(p,ptemp)
        ptemp=[]
    return p
#the first thing i did was scale l2 by the last coefficient by l1. Then i added that to temp and depending on the value of i,
#ptemp would shift. After that I used add to compbine ptemp and my final list p. And then i reset ptemp to do the same for the next
#coefficient in l1
def display_factorization(l1,l2):
    p=[]
    ptemp=l1
    scaler=0.0
    ptemp2=[]
    size=degree(l1)-degree(l2)+1
    for i in range(size):
        scaler=ptemp[0]/l2[0]
        p=p+[scaler]
        ptemp2=scale(l2,scaler)
        if(i!=(size-1)):
            for j in range(size-1):
                ptemp2=ptemp2+[0.0]
        ptemp=subtract(ptemp,ptemp2)
        ptemp=ptemp[1:]
        ptemp2=[]
    print(get_expression(l1),"=","("+get_expression(l2)+")"+"("+get_expression(p)+")",end="")
    if ptemp!=[0.0]:
        if ptemp[0]>0:
            print(" + "+get_expression(ptemp))
        else:
            print(" "+get_expression(ptemp))
    else:
        print()
#here i attempt to itterate through a for loop determined by the difference in degrees + 1 since it indicated how many time it needs
#to be divided. Then i tried to mimick long division using a scaler which divides the first coefficent of ptemp(which is first
# set to l1 and the it represents the remainder for long division)by the first coefficent of l2(denominator).
# I add that scalor as the first coefficent for p(this is our answer) and then save it to ptemp2. ptemp2 then add's 0's to the end of
# it untill it reaches the same power as the numerator. I then subtract ptemp by ptemp2. At the end I display
#the factorization which is (l1)=(l2)(p)+(ptemp(unless ptemp is 0)) which is the remainder


