
print("list to stack\n")

class StackL:
    def __init__(self):
        self.menu()
        
    def add(self,my_list,l):
        val=input("value:")
        if len(my_list)==l:
            print("\nStack is full.\nCannot add further.\nYou may choose to delete items to proceed.")
        else:
            my_list.append(val)
            print("\ncurrent list is:",my_list)
            print("\nDo you want to add more elements?Y/N")
            c=input()
            if c=="y":
                self.add(self.my_list,self.l)
            elif c=="n":
                self.dele(self.my_list,self.l)
        
    def dele(self,my_list,l):
        if len(my_list)==0:
            print("\nStack is empty.\nCannot delete further")
        else:
            print("list is:",my_list)
            print("\n Sure you want to delete the last ele added?y/n\n")
            k=input()
            if k=='y':
                my_list.pop()
                print("\ncurrent list is:",my_list)
                print("\ndo you further want to delete?Y/N")
                c=input()
                if c=="y":
                    self.dele(my_list,l)
                elif c=="n":
                    sel.add(self.my_list,self.l)
            else:
                print("current list:",my_list)
    
    def menu(self):
        self.my_list=[]
        print("choose an operation:\n")
        print("\n1.Add\n2.Delete\n3.Exit")
        op=input()
        if op !="3":
            print("\nEnter the length of the list?\n")
            self.l=int(input())
            if op=='1':
                self.add(self.my_list,self.l)
            
                    
                self.menu()

            elif op=='2':
                self.dele(self.my_list,self.l)
                self.menu()
        else:
            exit()

myob=StackL()

                
