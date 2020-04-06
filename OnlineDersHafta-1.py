import random

s=random.randint(1,100)
def get_n_random_numbers(n=10,min=-s,max=s):
    numbers=[]
    for i in range (n):
        numbers.append(random.randint(min,max))
    return numbers

#print( get_n_random_numbers(10,-5,5))


def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict

#print(my_frequency_with_dict([1,2,3]))
  
  
def my_frequency_with_list_of_tuples(list_1):
 frequency_list=[]
 for i in range(len(list_1)):
     s=False
     for j in range(len(frequency_list[j][0])):
         frequency_list[j][1]=frequency_list[j][1]+1 
         s=True         
     if(s==False):
         frequency_list.append([list_1[i],1])
     return frequency_list
#print(my_frequency_with_list_of_tuples([1,2,3,6,2]))

def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return frequency_max,mode
#print (my_mode_with_dict({1:2,3:2,4:1,5:3}))
    '''
def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max
print(my_mode_with_list([1,2,3,2,4]))
            
'''

def my_search(my_list,item_search):
    found=(-1,1)
    n=len(my_list)
    for indis in range(n):
         if my_list[indis]==item_search:
             found=(my_list[indis],indis)
    return found
    
    
def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean=t/s
    return mean
#print(my_search([1,2,3,4,2],5))



def my_buble_sort(my_list):
    n=len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list           
my_list=get_n_random_numbers(4,-5,5)
#print(my_buble_sort(my_list))
 
def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1
    while low<=high:
        mid=(low+high)//2
        if my_list[mid]==item_search:
            return my_list[mid],mid
        elif my_list[mid]>item_search:
            high=mid-1
        else:
            low=mid+1
    return found
    
    
my_list_1=get_n_random_numbers(4,-5,5)
#print(my_binary_search(my_list,5))
def my_median(my_list):
    my_list_2=my_buble_sort(my_list_1)
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list_2[middle]
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2
    return median
#print(my_median(my_list_1))    
            
            
