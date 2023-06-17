

ItemsInCart = 0

if ItemsInCart != 2:
    #raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0)

#try, catch

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print("Somehow I reached this block because there is failure in try block.")

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources.")