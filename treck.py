class inc_gen:
    def __init__(self,*args):
        narg=len(args)
        if nargs < 1:
            raise TypeError('needs atleast one parameter')
        elif nargs==1:
            self.stop=args[0]
            self.start=0
            self.step=1
        elif nargs==2:
            (self.stop,self.start)=args
            self.step=1
        elif nargs==3:
            (self.stop,self.start, self.step)=args
        else:
            raise TypeError('expeceted at most 3 parameters got
                            {}').format(nargs)

    def __iter__(self):
        i=self.start
        while i<=self.stop:
            yield i
            i += self.step

def main():
    buffersize =50000
    infile = open('some.jpg', 'rb')
    outfile = open('new.jpg', 'wb')
    while True:



if __name__=="__main__": main()
