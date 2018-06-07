import math
from tkinter import *

#stack class; it will be required for evaluation of expressions
class Stack:
	def __init__ (self):
		self.items = []

	def isEmpty (self):
		return self.items == []

	def push (self, item):
		self.items.append (item)

	def pop (self):
		return self.items.pop ()

	def peek (self):
		return self.items [-1]

	def size (self):
		return len (self.items)


#calculator class: this is where all the coding goes.
class Calculator (Stack):
	s = Stack ()

	#this is the expression that will show up on the calculator when we press buttons
	exprsn = "0"

	#this is the actual space separated mathematical expression on which the program operates
	act_exprsn = ""

	state = 0 #changes as we keep performing more operations.

	#the constructor function - puts every visible object in place
	def __init__ (self):

		#creating the root window
		self.root = Tk ()
		self.root.title ("LBCalculator")
		self.root.resizable (0,0)

		#label for credit
		self.calccredit = Label (self.root, text = "\nDeveloper: Livio Beqiri", font = "Candara 12 ", justify = CENTER, anchor = "e", width = 40)
		self.calccredit.grid (row = 8, column = 0, columnspan = 6)

		#label for expression
		self.calcexpr = Label (self.root, text = "", font = "Helvetica 13 italic", anchor = "e", width = 25)
		self.calcexpr.grid (row = 0, column = 0, columnspan = 5)
		self.calcexpr.bind ('<KeyRelease>', self.handleKeypress)
		self.calcexpr.focus_set()

		#this is how I decided to label the answer
		self.calcans = Label (self.root, text = self.exprsn, bg = "white", font = "Helvetica 16", anchor = "e", width = 21, relief = RIDGE)
		self.calcans.grid (row = 1, column = 0, columnspan = 5, pady = 10)

		#adding all buttons from 0 through 9
		self.zero = Button (self.root, text="0", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.zero.grid (row = 7, column = 1, pady = 2)
		self.zero.bind ('<Button-1>', lambda event: self.putDigit (event, 0))

		self.one = Button (self.root, text="1", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.one.grid (row = 6, column = 1, pady = 2)
		self.one.bind ('<Button-1>', lambda event: self.putDigit (event, 1))

		self.two = Button (self.root, text="2", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.two.grid (row = 6, column = 2, pady = 2)
		self.two.bind ('<Button-1>', lambda event: self.putDigit (event, 2))

		self.three = Button (self.root, text="3", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.three.grid (row = 6, column = 3, pady = 2)
		self.three.bind ('<Button-1>', lambda event: self.putDigit (event, 3))

		self.four = Button (self.root, text="4", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.four.grid (row = 5, column = 1, pady = 2)
		self.four.bind ('<Button-1>', lambda event: self.putDigit (event, 4))

		self.five = Button (self.root, text="5", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.five.grid (row = 5, column = 2, pady = 2)
		self.five.bind ('<Button-1>', lambda event: self.putDigit (event, 5))

		self.six = Button (self.root, text="6", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.six.grid (row = 5, column = 3, pady = 2)
		self.six.bind ('<Button-1>', lambda event: self.putDigit (event, 6))

		self.seven = Button (self.root, text="7", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.seven.grid (row = 4, column = 1, pady = 2)
		self.seven.bind ('<Button-1>', lambda event: self.putDigit (event, 7))

		self.eight = Button (self.root, text="8", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.eight.grid (row = 4, column = 2, pady = 2)
		self.eight.bind ('<Button-1>', lambda event: self.putDigit (event, 8))

		self.nine = Button (self.root, text="9", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.nine.grid (row = 4, column = 3, pady = 2)
		self.nine.bind ('<Button-1>', lambda event: self.putDigit (event, 9))

		#buttons for paranthesis
		self.openpar = Button (self.root, text="(", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.openpar.grid (row = 3, column = 1, pady = 2)
		self.openpar.bind ('<Button-1>', self.putOpenPar)

		self.closepar = Button (self.root, text=")", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.closepar.grid (row = 3, column = 2, pady = 2)
		self.closepar.bind ('<Button-1>', self.putClosePar)

		#buttons for mathematical constants, e and pi
		self.pi = Button (self.root, text="π", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.pi.grid (row = 2, column = 3, pady = 2)
		self.pi.bind ('<Button-1>', lambda event: self.putConstant (event, "π", repr (math.pi)))

		self.e = Button (self.root, text="e", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.e.grid (row = 3, column = 3, pady = 2)
		self.e.bind ('<Button-1>', lambda event: self.putConstant (event, "e", repr (math.e)))

		#button for decimal point
		self.decimal = Button (self.root, text=".", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.decimal.grid (row = 7, column = 2, pady = 2)
		self.decimal.bind ('<Button-1>', self.putDecimal)

		#buttons for unary opearators
		self.factorial = Button (self.root, text="!", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.factorial.grid (row = 2, column = 0, pady = 2, padx = (3,0))
		self.factorial.bind ('<Button-1>', self.calcFactorial)

		self.sqrt = Button (self.root, text="√", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.sqrt.grid (row = 2, column = 2, pady = 2)
		self.sqrt.bind ('<Button-1>', self.calcSqrt)

		self.sin = Button (self.root, text="sin", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.sin.grid (row = 3, column = 0, pady = 2, padx = (3,0))
		self.sin.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "sin"))

		self.cos = Button (self.root, text="cos", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.cos.grid (row = 4, column = 0, pady = 2, padx = (3,0))
		self.cos.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "cos"))

		self.tan = Button (self.root, text="tan", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.tan.grid (row = 5, column = 0, pady = 2, padx = (3,0))
		self.tan.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "tan"))

		self.ln = Button (self.root, text="ln", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.ln.grid (row = 6, column = 0, pady = 2, padx = (3,0))
		self.ln.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "ln"))

		self.log = Button (self.root, text="log", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.log.grid (row = 7, column = 0, pady = 2, padx = (3,0))
		self.log.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "log"))

		#buttons for binary operators i.e., +, -, *, /, ^\
		self.add = Button (self.root, text="+", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.add.grid (row = 7, column = 4, pady = 2, padx = (0,3))
		self.add.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "+", "+"))

		self.subtract = Button (self.root, text="-", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.subtract.grid (row = 6, column = 4, pady = 2, padx = (0,3))
		self.subtract.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "-", "-"))

		self.multiply = Button (self.root, text="x", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.multiply.grid (row = 5, column = 4, pady = 2, padx = (0,3))
		self.multiply.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "*", "x"))

		self.divide = Button (self.root, text="÷", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.divide.grid (row = 4, column = 4, pady = 2, padx = (0,3))
		self.divide.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "/", "÷"))

		self.exponent = Button (self.root, text="^", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.exponent.grid (row = 2, column = 1, pady = 2)
		self.exponent.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "^", "^"))

		#clear buttons
		self.allclear = Button (self.root, text="AC", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.allclear.grid (row = 2, column = 4, pady = 2, padx = (0,3))
		self.allclear.bind ('<Button-1>', self.clearAll)

		self.clear = Button (self.root, text="C", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.clear.grid (row = 3, column = 4, pady = 2, padx = (0,3))
		self.clear.bind ('<Button-1>', self.delete)

		#button for the equals to operator
		self.equals = Button (self.root, text="=", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.equals.grid (row = 7, column = 3, pady = 2)
		self.equals.bind ('<Button-1>', self.evaluate)

		#finally set the mainloop
		self.root.mainloop ()
		
	def chcknum (self, token):
		try:
			t = float (token)
			return True
		except ValueError:
			return False

	#this function handles the pressing of keys on keyboard
	def handleKeypress (self, event):
		if event.char in "0123456789":
			try:
				self.putDigit (event, int (event.char))
			except ValueError:
				pass
		elif event.char in "+-*/^":
			oper_sym = {'+': '+', '-': '-', '*': 'x', '/': '÷', '^': '^'}
			self.putBinaryOper (event, event.char, oper_sym [event.char])
		elif event.char == ".":
			self.putDecimal (event)
		elif event.char == '(':
			self.putOpenPar (event)
		elif event.char == ')':
			self.putClosePar (event)
		elif ord (event.char) == 8:
			self.delete (event)
		elif ord (event.char) == 127:
			self.clearAll (event)
		elif ord (event.char) == 13:
			self.evaluate (event)
		# else:
		# 	print event.char, ord (event.char)

	#this function deals with putting digits appropriately
	def putDigit (self, event, digit):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = repr (digit)
			self.exprsn = repr (digit)
			self.state = 1
		elif len (ls) > 0 and ls[-1] in ')!':
			self.act_exprsn += " * " + repr (digit)
			self.exprsn += repr (digit)
		else:
			self.act_exprsn += repr (digit)
			self.exprsn += repr (digit)
		self.calcans.config (text = self.exprsn)

	#puts the mathematical constants, e and Pi, after required checking according to the conditions
	def putConstant (self, event, symbol, val):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = val + " "
			self.exprsn = symbol
			self.state = 1
		elif len (ls) > 0 and (ls[-1] in ')!' or self.chcknum (ls[-1]) in [0,1]):
			self.act_exprsn += " * " + val
			self.exprsn += symbol
		else:
			self.act_exprsn += val
			self.exprsn += symbol
		self.calcans.config (text = self.exprsn)

	#puts the open paranthesis after required checking according to the conditions
	def putOpenPar (self, event):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = "( "
			self.exprsn = "("
			self.state = 1
		elif len (ls) > 0 and self.chcknum (ls[-1]):
			self.act_exprsn += " * ( "
			self.exprsn += "("
		else:
			self.act_exprsn += " ( "
			self.exprsn += "("
		self.calcans.config (text = self.exprsn)

	#puts the closed paranthesis after required checking according to the conditions
	def putClosePar (self, event):
		if self.state == 0 or self.state == 2:
			self.act_exprsn = ") "
			self.exprsn = " )"
			self.state = 1
		else:
			self.act_exprsn += " ) "
			self.exprsn += ")"
		self.calcans.config (text = self.exprsn)
