##a=10
##b="str"
##print(a+b)
##output:
##TypeError: unsupported operand type(s) for +: 'int' and 'str'


##a=10
##b=True
##print(a+b)
##output:
##11

##a=10
##b=14.35
##print(a+b)
##output:
##24.35

##a=10
##b=5+6j
##print(a+b)
##output:
##(15+6j)

##a=10
##b=[10,20,30]
##print(a+b)
##output:
##TypeError: unsupported operand type(s) for +: 'int' and 'list'

##a=10
##b=("a","b",10)
##print(a+b)
##output:
##TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

##a=10
##b={"a","b","c"}
##print(a+b)
##output:
##TypeError: unsupported operand type(s) for +: 'int' and 'set'

##a=10
##b={"a":10,"b":20}
##print(a+b)
##output:
##TypeError: unsupported operand type(s) for +: 'int' and 'dict'

##operators:
##-----------

##a=10
##b=2
##print(a/b)
##output:
##5.0

##a=10
##b=2
##print(a//b)
##output:
##5

##a=10
##b=2.0
##print(a//b)
##output:
##5.0

##a=10.0
##b=2.0
##print(a//b)
##output:
##5.0

##a=~5
##print(a)
##output:
##-6

##a="python"
##b="PYTHON"
##print(a>b)
##output:
##True

##a=[1,2,3]
##b=[4,5,6]
##print(a+b)
##output:
##[1, 2, 3, 4, 5, 6]

##a=[1,2,3]
##b=[4,5,2]
##print(a-b)
##output:
##TypeError: unsupported operand type(s) for -: 'list' and 'list'

##a=[1,2,3]
##b=[4,5,6]
##print(a*b)
##output:
##TypeError: can't multiply sequence by non-int of type 'list'

##a=[1,2,3]
##b=[4,5,6]
##c=a/b
##print(c)
##output:
##TypeError: unsupported operand type(s) for /: 'list' and 'list'

##a=[1,2,3]
##b=[4,5,6]
##c=a%b
##print(c)
##output:
##TypeError: unsupported operand type(s) for %: 'list' and 'list'

##a=[1,2,3]
##b=[4,5,6]
##c=a**b
##print(c)
##output:
##TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'list'

##a=("a","b","c")
##b=10
##print(a+b)
##output:
##TypeError: can only concatenate tuple (not "int") to tuple

##a=("a","b","c")
##b=10
##print(a-b)
##output:
##TypeError: unsupported operand type(s) for -: 'tuple' and 'int'

##a=("a","b","c")
##b=("d","e","f")
##print(a+b)
##output:
##('a', 'b', 'c', 'd', 'e', 'f')

##a=("a","b","c")
##b=("d","e","f")
##print(a*b)
##output:
##TypeError: can't multiply sequence by non-int of type 'tuple'

##a=(1,2,3,4,5)
##b=(6,7,1,2)
##print(a/b)
##output:
##TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'

##a={"a","b"}
##b={"c","d"}
##print(a+b)
##output:
##TypeError: unsupported operand type(s) for +: 'set' and 'set'

##a={"a","b"}
##b={"c","d","a"}
##print(a-b)
##output:
##{'b'}

##a={1,2,3}
##b={1,3,4}
##print(a/b)
##output:
##TypeError: unsupported operand type(s) for /: 'set' and 'set'

##a={1,2,3,4}
##b={1,2,3}
##print(a*b)
##output:
##TypeError: unsupported operand type(s) for *: 'set' and 'set'

##a={1,2,3}
##b={1,2}
##print(a%b)
##output:
##TypeError: unsupported operand type(s) for %: 'set' and 'set'


##what is the difference between shallow copy and deep copy?
##if we want to perform shallow copy and deep copy then we have to import copy module. copy module contains copy() method and deepcopy() method.
##by using that we can perfrom shallow copy and deepcopy.
##shallow copy: shallow copy does not creagte new object and in the original list if we modify(means insert,update,remove) any immutable elements (like numbers,strings)
##then those changes will not be affected in the shallow copy. however, if we modify(means insert,update,remove) any mutable elements
##(like lists, dictionaries) in the original list then those changes will be affected in the both shallow
##copy and original list because they both reference the same inner mutable objects.

##deepcopy:
##deep copy creates a new object and in original list if we modify (means insert,update,remove) any mutable and immutable elements then those changes will not be affected in the deep copy.
##because deep copy creates an independent set of objects.

##example1:
##import copy
##original_list=[1,2,[3,4]]
##shallow_copy=copy.copy(original_list)
##deep_copy=copy.deepcopy(original_list)
##original_list[2][0]=999
##print("original list is=",original_list,id(original_list),id(original_list[2][0]))
##print("shallow copy is=",shallow_copy,id(shallow_copy),id(shallow_copy[2][0]))
##print("deep copy is=",deep_copy,id(deep_copy),id(deep_copy[2][0]))
##output:
##original list is= [1, 2, [999, 4]] 2618434720448 2618465149680
##shallow copy is= [1, 2, [999, 4]] 2618434720768 2618465149680
##deep copy is= [1, 2, [3, 4]] 2618434721728 2618428490032

##example2:
##import copy
##original_list=[1,2,[3,4]]
##shallow_copy=copy.copy(original_list)
##deep_copy=copy.deepcopy(original_list)
##original_list[0]=999
##print("original list is=",original_list,id(original_list),id(original_list[2][0]))
##print("shallow copy is=",shallow_copy,id(shallow_copy),id(shallow_copy[2][0]))
##print("deep copy is=",deep_copy,id(deep_copy),id(deep_copy[2][0]))
##output:
##original list is= [999, 2, [3, 4]] 1983409623744 1983403393328
##shallow copy is= [1, 2, [3, 4]] 1983409624064 1983403393328
##deep copy is= [1, 2, [3, 4]] 1983409625024 1983403393328


##another example:
##from copy import copy,deepcopy
##x=1000
##y=[1000,2000,3000]
##z="hyd"
##a=[x,y,1000,2000,3000,z]
##k=a
##l=[1000,2000,3000]
##m=a[:]
##n=deepcopy(a)
##o=copy(a)
##a.remove(3000)
##print(m)
##print(n)
##print(k)
##print(a)
##output:
##[1000, [1000, 2000, 3000], 1000, 2000, 3000, 'hyd']
##[1000, [1000, 2000, 3000], 1000, 2000, 3000, 'hyd']
##[1000, [1000, 2000, 3000], 1000, 2000, 'hyd']
##[1000, [1000, 2000, 3000], 1000, 2000, 'hyd']

##another example:
##from copy import copy,deepcopy
##a=[[3000,4000],1000,2000]
##b=a[:]
##d=copy(a)
##e=a
##c=deepcopy(a)
##a[1]=6000
##print(a[1])
##print(b[1])
##print(c[1])
##print(d[1])
##print(e[1])
##output:
##6000
##1000
##1000
##1000
##6000

def order_data(f):#f=get_user
    def wrapper():
        res=f()
        print(res)
        res.sort()
        return res
    return wrapper

def get_users():
    return ["user1","user3","user2","user4"]
def get_products():
    return ["p1","p3","p2","p4"]
def get_orders():
    return ["o1","o3","o2","o4"]
res=order_data(get_users)
print("res=",res)
r1=res()
print("r1=",r1)
output:
res= <function order_data.<locals>.wrapper at 0x000001E007E57520>
['user1', 'user3', 'user2', 'user4']
r1= ['user1', 'user2', 'user3', 'user4']

##explanation:
##decorator is used to modify the behaviour of a function.
##order_data(f) is a decorator function that takes another function f as its argument. it defines an inner function called wrapper().
##inside wrapper(), it first calls the orginal function f by invoking f().
##our passed get_users to order_data, so res will contain the list of users returned by get_users.
##after calling f(), it prints the value of res, which is the original list
##then it sorts the res list using the sort() method
##finally it returns the sorted res list
##in the problem we have 3 functions are
##get_users(), get_products(), and get_orders(), which return lists of data
##it's not the sorted list of users at this point, but a function that wraps the original get_users function with additional behaviour.
##res= <function order_data.<locals>.wrapper at 0x000001E007E57520>
##this output shows that res is a function, specifically the wrapper function created by the decorator
##to actually get the sorted list of users, we need to call res() as we did with r1=res().
##when we do that it executes the wrapper function and sorts the original list.


##res= <function order_data.<locals>.wrapper at 0x000001E007E57520>
##['user1', 'user3', 'user2', 'user4']
##r1= ['user1', 'user2', 'user3', 'user4']
##res is the decorated function, and r1 is the sorted list of users after applying the decorator.
--------------------------------------------------------------------------------------------------------

def order_data(f):
    def wrapper():
        res=f()
        print(res)
        res.sort()
        return res
    return wrapper

@order_data
def get_users():
    return ["user1","user3","user2","user4"]
print(get_users())

@order_data
def get_products():
    return ["p1","p3","p2","p4"]
print(get_products())

@order_data
def get_orders():
    return ["o1","o3","o2","o4"]
print(get_orders())
output:
['user1', 'user3', 'user2', 'user4']
['user1', 'user2', 'user3', 'user4']
['p1', 'p3', 'p2', 'p4']
['p1', 'p2', 'p3', 'p4']
['o1', 'o3', 'o2', 'o4']
['o1', 'o2', 'o3', 'o4']

explanation:

we are using decorators to modify the behaviour of three functions.
get_users, get_products, and get_orders.
these functions returns lists of data.
order_data(f) is a decorator function that takes another function f as its argument.
it defines an inner function called wrapper(). inside wrapper(), it first calls the original function f,
then it prints the value of res, sorts the res list, they are wrapped by the order_data decorator, which modifies their behaviour
for get_users
The original function get_users returns ["user1", "user3", "user2", "user4"].
the decorator order_data sorts this list and prints the original list followed by the sorted list
output for get_user:
['user1', 'user3', 'user2', 'user4']
['user1', 'user2', 'user3', 'user4']

get_products:
the original function get_products returns ["p1", "p3", "p2", "p4"].
the decorator order_data sorts this list and prints the original list followed by the sorted list
Output for get_products:
['p1', 'p3', 'p2', 'p4']
['p1', 'p2', 'p3', 'p4']

For get_orders:
The original function get_orders returns ["o1", "o3", "o2", "o4"].
The decorator order_data sorts this list and prints the original list followed by the sorted list.
Output for get_orders:
['o1', 'o3', 'o2', 'o4']
['o1', 'o2', 'o3', 'o4']

in each case, the decorator modified the behavior of the original functions to sort the lists they return,
and the printed output demonstrates the change in the order of the elements after sorting.






















































































