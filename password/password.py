password = 'a123456'
i = 3
while True:
    password1 = input('please enter password: ')

    if password1 == password:
        print('log in sucessfully')
        break
    else:
        i = i - 1 
        print('incorrect password, you have ',i ,' chances left')
        if i == 0:
            break
    

        
         

                        
        
        




