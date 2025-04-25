# Write a class called Password_manager.
# The class should have a list called old_passwords that holds all of the user’s past passwords.
# The last item of the list is the user’s current password.
# There should be a method called get_password that returns the current password and a method called set_password that sets the user’s password.
# The set_password method should only change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or False depending on whether the string is equal to the current password or not.

class paasword_manager:
    def __init__(self,old_passwords):

        self.old_passwords=old_passwords

     #method to get current password
    def get_password(self):
        return self.old_passwords[len(self.old_passwords)-1]  
      
    #method to set password

    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False
    
    
    def is_correct(self,password):
        return password==self.get_password()



 #for testing   
s1=paasword_manager([1,23,45])   
s1.set_password(50) 
print(s1.get_password())
print(s1.is_correct(70))
