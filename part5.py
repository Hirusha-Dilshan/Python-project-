progress=0
trailer=0
retriever=0
excluded=0
re='y'

mark=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

for i in mark:
    pass_mark=i[0]
    defer_mark=i[1]
    fail_mark=i[2]

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
    
print('Progress',progress,':',progress*'*')
print('Trailer',trailer,':',trailer*'*')
print('Retriever',retriever,':',retriever*'*')
print('Excluded',excluded,':',excluded*'*')