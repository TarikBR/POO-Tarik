import turtle as t

screen = t.Turtle()

num1 = 1
num2 = 0
fibo = None

for i in range(15):
	fibo = num1
	print(fibo)
	screen.circle(fibo, 180)
	num1 = num1 + num2
	num2 = fibo

t.mainloop()
