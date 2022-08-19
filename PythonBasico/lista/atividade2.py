import turtle as t

bob = t.Turtle()
print(bob) 

"""
bob.lt(90)
bob.fd(100)
bob.rt(90)
bob.fd(200)
bob.lt(90)
bob.fd(150)
bob.lt(90)
bob.fd(300)
bob.lt(90)
bob.fd(250)
bob.lt(90)
bob.fd(90)

bob.lt(90)
bob.fd(110)
bob.rt(90)
bob.fd(200)
bob.lt(90)
bob.fd(130)
bob.lt(90)
bob.fd(280)
bob.lt(90)
bob.fd(230)
bob.lt(90)
bob.fd(70)
"""

for i in range(4): print("Hello!")

"""
for i in range(4):
    bob.fd(100)
    bob.lt(90)
"""
bob.rt(90)
for i in range(4):
    bob.fd(100)
    bob.lt(90)
bob.lt(180)
for i in range(3):
    bob.fd(100)
    bob.rt(90)

t.mainloop()