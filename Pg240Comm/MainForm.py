import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(4, 25)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(164, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Sales for the month:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(4, 65)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(164, 23)
		self._label2.TabIndex = 1
		self._label2.Text = " Advance pay reward:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(4, 126)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(164, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Comission Rate:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(4, 168)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(164, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Comission:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(4, 203)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(164, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Net Pay:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(4, 265)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(109, 44)
		self._button1.TabIndex = 5
		self._button1.Text = "Caluclate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(129, 265)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(109, 44)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(255, 265)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(109, 44)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(174, 25)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(189, 26)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(175, 65)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(189, 26)
		self._textBox2.TabIndex = 9
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(174, 126)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(190, 23)
		self._label6.TabIndex = 10
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(174, 168)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(190, 23)
		self._label7.TabIndex = 11
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(174, 203)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(190, 23)
		self._label8.TabIndex = 12
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SeaGreen
		self.ClientSize = System.Drawing.Size(376, 315)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		decSalesAmount = 0.0
		decAdvancePayAmount = 0.0
		decComissionRate = 0.0
		decComissionAmount = 0.0
		decNetPay = 0.0
		
		try:
			decSalesAmount = float(self._textBox1.Text)
		except:
			self._lblErrorMessage.Text = "Sales amount must be numeric"
			self._lblErrorMessage.Visiable = True
			return
		
		try:
			decAdvancePayAmount = float(self._textBox2.Text)
		except:
			self._lblErrorMessage.Text = "Advance pay amount must be numeric"
			self.lblErrorMessage.Visiable = True
			return
		
		if decSalesAmount < 10000:
			decComissionRate = 0.05
		elif decSalesAmount >= 10000 and decSalesAmount < 15000:
			decComissionRate = 0.1
		elif decSalesAmount >= 15000 and decSalesAmount < 18000:
			decComissionRate = 0.12
		elif decSalesAmount >= 18000 and decSalesAmount < 22000:
			decComissionRate = 0.14
		elif decSalesAmount >= 2200:
			decCommissionRate = 0.15
			
		decComissionAmount = decSalesAmount * decComissionRate
		decNetPay = decComissionAmount - decAdvancePayAmount
		
		
		self._label6.Text = str(round(decComissionRate, 2))
		self._label7.Text = str(round(decComissionAmount, 2))
		self._label8.Text = str(round(decNetPay, 2))