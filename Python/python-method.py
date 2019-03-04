class A(object):
    def foo(x):
        print x**2

    def self_foo(self, x):
        print x**3

    @classmethod
    def class_foo(cls, x):
        print x**4

    @staticmethod
    def static_foo(x):
        print x**5

    #foo(2)
    #self_foo(2)
    #class_foo(2)
    static_foo(2)


a=A()
#print A.foo
#print a.foo
#A.foo.__func__(2)
#a.foo(2)
#print A.self_foo
#print a.self_foo
#A.self_foo(2)
#a.self_foo(2)
#print A.class_foo
#print a.class_foo
#A.class_foo(2)
#a.class_foo(2)
#print A.static_foo
#print a.static_foo
#A.static_foo(2)
#a.static_foo(2)