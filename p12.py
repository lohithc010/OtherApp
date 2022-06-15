def new_pin():
    list1 = []
    c= 0 
    while(c<=3): 
        p = input("Enter the pin") 
        l1 = list1.append(p) 
        c = c + 1 
    y1 = input("Do you want to view your pin ? y/n ") 
    if (y1 == 'y' or 'yes' or 'Yes'): 
        print('Your PIN is {}'.format(list1))
    else:
        print('PIN failed')

new_pin()