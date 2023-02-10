class ThreeStack:
    first=[] 
    second=[] 
    third=[] 

    def __init__(self) -> None:
        pass
    
    def push(self,stackname,object):
        match stackname:
            case 1:
                self.first.append(object)
            case 2:
                self.second.append(object)
            case 3:
                self.third.append(object)
            case _:
                raise Exception


    def pop(self,stackname):
        match stackname:
            case 1:
                return self.poppingFrom(self.first)
            case 2:
                return self.poppingFrom(self.second)
            case 3:
                return self.poppingFrom(self.third)
            case _:
                raise Exception

    def poppingFrom(self,list):
        if list !=[]:
            return list.pop()
        else : raise Exception

def main():
    threeStack = ThreeStack()

    threeStack.push(1, "{name:'object1'}")
    threeStack.push(1, "{name:'object2'}")
    threeStack.push(2, "{name:'object3'}")
    threeStack.push(2, "{name:'object4'}")
    threeStack.push(2, "{name:'object5'}")
    threeStack.push(3, "{name:'object6'}")
    threeStack.push(3, "{name:'object7'}")


    print(threeStack.pop(2))
    print(threeStack.pop(2))
    print(threeStack.pop(1))
    print(threeStack.pop(1))
    print(threeStack.pop(3))
    print(threeStack.pop(1))

if __name__ == "__main__":
    main()