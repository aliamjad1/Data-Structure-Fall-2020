#Queus is also a form of Data Structure....FIF0..means (First in First Out)
from collections import deque

queu=deque()
queu.appendleft("Mango")
queu.appendleft("Orange")
queu.appendleft("Banana")
queu.appendleft("Peach")
queu.appendleft("Strawberry")
print(queu)
queu.pop()
print(queu)