class Member :
    """Create a memeber from uname , fname """
    def __init__(self,uname, fname):
        self.username= uname 
        self.fullname =fname

        pass

this_instanse_name = Member('uanme','faname')
new_guy = Member('Rambo ' , 'Rocco Moe')



print("Rambo" , "Defta Andrei")
print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))

