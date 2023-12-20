import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(176, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(384, 35)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Teal
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(143, 34)
		self._label1.TabIndex = 1
		self._label1.Text = "Kilowatts Used:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Teal
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 105)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(143, 34)
		self._label2.TabIndex = 2
		self._label2.Text = "Base Rate:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Teal
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 150)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(143, 34)
		self._label3.TabIndex = 3
		self._label3.Text = "Surcharge:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Teal
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 194)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(143, 34)
		self._label4.TabIndex = 4
		self._label4.Text = "Citytax:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Teal
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 266)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(168, 34)
		self._label5.TabIndex = 5
		self._label5.Text = "Pay this amount:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Teal
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 309)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(168, 34)
		self._label6.TabIndex = 6
		self._label6.Text = "After May 20th pay:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateGray
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 361)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(167, 59)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateGray
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(204, 361)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(167, 59)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSlateGray
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(394, 361)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(167, 59)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Teal
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(162, 60)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(399, 34)
		self._label7.TabIndex = 10
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Teal
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(161, 105)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(399, 34)
		self._label8.TabIndex = 11
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Teal
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(162, 150)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(399, 34)
		self._label9.TabIndex = 12
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Teal
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(161, 194)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(399, 34)
		self._label10.TabIndex = 13
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Teal
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(187, 266)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(374, 34)
		self._label11.TabIndex = 14
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Teal
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(187, 309)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(374, 34)
		self._label12.TabIndex = 15
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Teal
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(12, 14)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(158, 34)
		self._label13.TabIndex = 16
		self._label13.Text = "Enter KWH used:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSeaGreen
		self.ClientSize = System.Drawing.Size(573, 432)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Kwh = self._textBox1.Text 
		Baserate = Kwh**0.0475
		Surcharge = Baserate / float(10.00)
		Citytax = Baserate / float(3.00)
		Pay = Baserate + Surcharge + Citytax
		AP = Pay * float(4.00)
		self._label7.Text.Add(Kwh)
		self._label8.Text.Add(Baserate)
		self._label9.Text.Add(Surcharge)
		self._label10.Text.Add(Citytax)
		self._label11.Text.Add(Pay)
		self._label12.Text.Add(AP)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text.Clear()
		self._label7.Text.Clear()
		self._label8.Text.Clear()
		self._label9.Text.Clear()
		self._label10.Text.Clear()
		self._label11.Text.Clear()
		self._label12.Text.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label8Click(self, sender, e):
		pass