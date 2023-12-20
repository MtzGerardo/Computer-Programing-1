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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.BurlyWood
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 11)
		self._label1.Name = "label1"
		self._label1.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._label1.Size = System.Drawing.Size(175, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.BurlyWood
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 56)
		self._label2.Name = "label2"
		self._label2.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._label2.Size = System.Drawing.Size(175, 31)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay periods per year:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.BurlyWood
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(5, 141)
		self._label3.Name = "label3"
		self._label3.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._label3.Size = System.Drawing.Size(182, 31)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary per pay period:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.BurlyWood
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(197, 141)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(279, 31)
		self._label4.TabIndex = 3
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(193, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(283, 29)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(193, 56)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(283, 29)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.BurlyWood
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(116, 193)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(232, 58)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOrange
		self.ClientSize = System.Drawing.Size(488, 272)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "SalaryCalculation"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		# Salary caluclation
		
		decAnnualSalary = 0.0 # annual salary
		intPayPeriods = 0     # number of pay periods per year
		decSalary = 0.0       # salary per pay period
		
		try:
			decAnnualSalary = float(self._textBox1.Text)
			intPayPeriods = int(self._textBox2.Text)
		except:
			MessageBox.Show("The input files must contain nonzero numeric values.", "Error")
			
		decSalary = decAnnualSalary / intPayPeriods
		self._label4.Text = str(round(decSalary, 2))

	def Label3Click(self, sender, e):
		pass