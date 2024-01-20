pass_mark= int(input('please enter your credits at pass:'))
defer_mark= int(input('please enter your credit at defer:'))
fail_mark= int(input('please enter your credit at fail:'))

if pass_mark==120 and defer_mark==0 and fail_mark==0:
    print('progress')

elif pass_mark==100 and defer_mark==20 and fail_mark==0:
    print('progress(module trailer)')

elif pass_mark==100 and defer_mark==0 and fail_mark==20:
    print('progress(module trailer)')

elif pass_mark==80 and defer_mark==40 and fail_mark==0:
    print('Do not progress-module retriever')

elif pass_mark==80 and defer_mark==20 and fail_mark==20:
    print('Do not progress-module retriever ')

elif pass_mark==80 and defer_mark==0 and fail_mark==40:
    print('Do not progress-module retriever')

elif pass_mark==60 and defer_mark==60 and fail_mark==0:
    print('Do not progress-module retriever')

elif pass_mark==60 and defer_mark==40 and fail_mark==20:
    print('Do not progress-module retriever')

elif pass_mark==60 and defer_mark==20 and fail_mark==40:
    print('Do not progress-module retriever')

elif pass_mark==60 and defer_mark==0 and fail_mark==60:
    print('Do not progress-module retriever')

elif pass_mark==40 and defer_mark==80 and fail_mark==0:
    print('Do not progress-module retriever')

elif pass_mark==40 and defer_mark==60 and fail_mark==20:
    print('Do not progress-module retriever')

elif pass_mark==40 and defer_mark==40 and fail_mark==40:
    print('Do not progress-module retriever')

elif pass_mark==40 and defer_mark==20 and fail_mark==60:
    print('Do not progress-module retriever')

elif pass_mark==40 and defer_mark==0 and fail_mark==80:
    print('Exclude')

elif pass_mark==20 and defer_mark==100 and fail_mark==0:
    print('Do not progress-module retriever')

elif pass_mark==20 and defer_mark==80 and fail_mark==20:
    print('Do not progress-module retriever')

elif pass_mark==20 and defer_mark==60 and fail_mark==40:
    print('Do not progress-module retriever')

elif pass_mark==20 and defer_mark==40 and fail_mark==60:
    print('Do not progress-module retriever')

elif pass_mark==20 and defer_mark==20 and fail_mark==80:
    print('Exclude')

elif pass_mark==20 and defer_mark==0 and fail_mark==100:
    print('Exclude')

elif pass_mark==0 and defer_mark==120 and fail_mark==0:
    print('Do not progress-module retriever')

elif pass_mark==0 and defer_mark==100 and fail_mark==20:
    print('Do not progress-module retriever')

elif pass_mark==0 and defer_mark==80 and fail_mark==40:
    print('Do not progress-module retriever')

elif pass_mark==0 and defer_mark==60 and fail_mark==60:
    print('Do not progress-module retriever')

elif pass_mark==0 and defer_mark==40 and fail_mark==80:
    print('Exclude')

elif pass_mark==0 and defer_mark==20 and fail_mark==100:
    print('Exclude')

elif pass_mark==0 and defer_mark==0 and fail_mark==120:
    print('Exclude')


