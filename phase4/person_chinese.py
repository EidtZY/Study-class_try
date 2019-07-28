class Person(object):
    '''父类 - 人'''
    def talk(self):
        print('person is talking...')
        return

class Chinese(Person):
    '''子类 - 中国人'''
    def walk(self):
        print('A Chinese is walking...')
        return
