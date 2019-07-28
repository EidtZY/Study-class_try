from my_01_class import MyClass

me = MyClass()

if me.sex == '男':
    print('my name is %s, I am a boy.' % me.name)
elif me.sex == '女':
    print('my name is %s, I am a girl.' % me.name)
else:
    print('my name is %s, I am a ...' % me.name)

me.work()
me.study()
#me.__bank_account()
#me.__bank_password()
