import dis
def myfunc(alist):
    alist=['f','r','a']
    return len(alist)
dis.dis(myfunc)