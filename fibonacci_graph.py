import turtle
n=450
i=1
fib_next=0
prev=1
while i <= n:
    print(i)

    turtle.circle(i,90)

    fib_next=i+prev
    prev=i
    i=fib_next
    