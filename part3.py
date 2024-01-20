progress=0
trailer=0
retriever=0
excluded=0
re='y'
while re=='y':
    #pass_mark
    while True:
        try:
            pass_mark= int(input('please enter your credits at pass: '))
            while pass_mark!=0 and pass_mark!=20 and pass_mark!=40 and pass_mark!=60 and pass_mark!=80 and pass_mark!=100 and pass_mark!=120:
                print('out of range. ')
                pass_mark= int(input('please enter your credits at pass: '))
            break
        except ValueError:
            print('Integer required. ')

    #Defer_mark
    while True:
        try:
            defer_mark= int(input('please enter your credit at defer: '))
            while defer_mark!=0 and defer_mark!=20 and defer_mark!=40 and defer_mark!=60 and defer_mark!=80 and defer_mark!=100 and defer_mark!=120:
                print('out of range. ')
                defer_mark= int(input('please enter your credit at defer: '))
            break
        except ValueError:
            print('Integer required. ')

    #Fail_mark
    while True:
        try:
            fail_mark= int(input('please enter your credit at fail: '))
            while fail_mark!=0 and fail_mark!=20 and fail_mark!=40 and fail_mark!=60 and fail_mark!=80 and fail_mark!=100 and fail_mark!=120:
                print('out of range. ')
                fail_mark= int(input('please enter your credit at fail: '))
            break
        except ValueError:
            print('Integer required. ')


    if pass_mark + defer_mark + fail_mark!= 120:
        print('Total incorrect. ')

    if pass_mark==120 and defer_mark==0 and fail_mark==0:
        print('progress')
        progress=progress+1

    elif pass_mark==100 and defer_mark==20 and fail_mark==0:
        print('progress(module trailer)')
        trailer=trailer+1

    elif pass_mark==100 and defer_mark==0 and fail_mark==20:
        print('progress(module trailer)')
        trailer=trailer+1

    elif pass_mark==80 and defer_mark==40 and fail_mark==0:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==80 and defer_mark==20 and fail_mark==20:
        print('Do not progress-module retriever ')
        retriever=retriever+1

    elif pass_mark==80 and defer_mark==0 and fail_mark==40:
        print('Do not progress-module retriever')
        retriever=retriever+1


    elif pass_mark==60 and defer_mark==60 and fail_mark==0:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==60 and defer_mark==40 and fail_mark==20:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==60 and defer_mark==20 and fail_mark==40:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==60 and defer_mark==0 and fail_mark==60:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==40 and defer_mark==80 and fail_mark==0:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==40 and defer_mark==60 and fail_mark==20:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==40 and defer_mark==40 and fail_mark==40:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==40 and defer_mark==20 and fail_mark==60:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==40 and defer_mark==0 and fail_mark==80:
        print('Exclude')
        excluded=excluded+1


    elif pass_mark==20 and defer_mark==100 and fail_mark==0:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==20 and defer_mark==80 and fail_mark==20:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==20 and defer_mark==60 and fail_mark==40:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==20 and defer_mark==40 and fail_mark==60:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==20 and defer_mark==20 and fail_mark==80:
        print('Exclude')
        excluded=excluded+1

    elif pass_mark==20 and defer_mark==0 and fail_mark==100:
        print('Exclude')
        excluded=excluded+1

    elif pass_mark==0 and defer_mark==120 and fail_mark==0:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==0 and defer_mark==100 and fail_mark==20:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==0 and defer_mark==80 and fail_mark==40:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==0 and defer_mark==60 and fail_mark==60:
        print('Do not progress-module retriever')
        retriever=retriever+1

    elif pass_mark==0 and defer_mark==40 and fail_mark==80:
        print('Exclude')
        excluded=excluded+1

    elif pass_mark==0 and defer_mark==20 and fail_mark==100:
        print('Exclude')
        excluded=excluded+1

    elif pass_mark==0 and defer_mark==0 and fail_mark==120:
        print('Exclude')
        excluded=excluded+1
    re=input("Enter 'y' for yes or 'q' to quit and view result : ")

print('Progress',progress,':',progress*'*')
print('Trailer',trailer,':',trailer*'*')
print('Retriever',retriever,':',retriever*'*')
print('Excluded',excluded,':',excluded*'*')