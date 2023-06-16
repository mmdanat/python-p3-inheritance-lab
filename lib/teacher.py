#!/usr/bin/env python

from user import User

import random

knowledge2 = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast"]


class Teacher(User):
    
    def __init__(self,first_name,last_name):
        self.knowledge = knowledge2
        super().__init__(first_name,last_name)


    def teach(self):
      self.random_index =  random.randint(0, len(self.knowledge)-1) 
      return self.knowledge[self.random_index]
        
       

# T = Teacher("karen","good")
# print(T.teach())
