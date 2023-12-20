import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.DarkSlateGray
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(252, 257)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets Sold"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label12)
		self._groupBox2.Controls.Add(self._label11)
		self._groupBox2.Controls.Add(self._label8)
		self._groupBox2.Controls.Add(self._label9)
		self._groupBox2.Controls.Add(self._label10)
		self._groupBox2.Controls.Add(self._label5)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Location = System.Drawing.Point(292, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(257, 257)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Revenue Generated"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Teal
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 281)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 40)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate Revenue"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Teal
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(198, 281)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 40)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Teal
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(385, 281)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 40)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Teal
		self._label1.Location = System.Drawing.Point(6, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(227, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of tickets sold for each class of seats "
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Teal
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 82)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(71, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Class A:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Teal
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 116)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(71, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Class B:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Teal
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(6, 152)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(71, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Class C:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(84, 82)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(162, 24)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(84, 116)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(162, 24)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(84, 152)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(162, 24)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Teal
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(6, 152)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(71, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Class C:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Teal
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(6, 116)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(71, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "Class B:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Teal
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(6, 82)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(71, 23)
		self._label7.TabIndex = 7
		self._label7.Text = "Class A:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Teal
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(85, 152)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(166, 23)
		self._label8.TabIndex = 12
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Teal
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(85, 116)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(166, 23)
		self._label9.TabIndex = 11
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Teal
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(85, 82)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(165, 23)
		self._label10.TabIndex = 10
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Teal
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(6, 189)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(118, 23)
		self._label11.TabIndex = 13
		self._label11.Text = "Total Revenue:"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Teal
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(130, 189)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(121, 23)
		self._label12.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateGray
		self.ClientSize = System.Drawing.Size(554, 333)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg186StadiumSeating"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		classA = 15
		classB = 12
		classC = 9
		totalReve = 0.0
		
		intSeatA = int(self._textBox1.Text)
		intSeatB = int(self._textBox2.Text)
		intSeatC = int(self._textBox3.Text)
		
		revenueA = intSeatA * classA
		
		revenueB = intSeatB * classB
		
		revenueC = intSeatC * classC
		
		totalReve = revenueA + revenueB + revenueC
		
		self._label10.Text = str(round(revenueA, 2))
		self._label9.Text = str(round(revenueB, 2))
		self._label8.Text = str(round(revenueC, 2))
		self._label12.Text = str(round(totalReve, 2))
		
		pass

	def MainFormLoad(self, sender, e):
		
	

	def Button2Click(self, sender, e):
		self._textBox1.Text.Clear()
		self._textBox2.Text.Clear()
		self._textBox3.Text.Clear()
		self._label10.Text = ""
		self._label9.Text = ""
		self._label8.Text = ""
		self._label12.Text = ""
		pass

	def Button3Click(self, sender, e):
		Applaction.Exit()
		pass