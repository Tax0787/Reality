l_m = lambda name, dx, sose: '{} = lambda {}: {}'.format(name, dx, sose) #lambda_maker def
d_m = lambda name, dx, sose: 'def {}({}):\n{}'.format(name, dx, sose) #def_maker def
c_m = lambda name, sose: 'class {}:\n    {}'.format(name, sose)
'''test sose :
    exec(l_m('hi','','print(\'hi\')'))
    hi()
    exec(d_m('bye','','    print(\'bye\')'))
    bye()
'''
class a:
    def ____