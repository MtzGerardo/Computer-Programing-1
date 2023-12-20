import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(296, 243)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSteelBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(7, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(82, 25)
		self._label1.TabIndex = 0
		self._label1.Text = "Score 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSteelBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 81)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(83, 25)
		self._label2.TabIndex = 1
		self._label2.Text = "Score 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSteelBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(7, 126)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(83, 25)
		self._label3.TabIndex = 2
		self._label3.Text = "Score 3:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSteelBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(7, 182)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(89, 25)
		self._label4.TabIndex = 3
		self._label4.Text = "Average:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSteelBlue
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(102, 182)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(188, 25)
		self._label5.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(96, 29)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(194, 26)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(96, 81)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(194, 26)
		self._textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(96, 126)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(194, 26)
		self._textBox3.TabIndex = 7
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSteelBlue
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(13, 259)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(296, 28)
		self._label6.TabIndex = 8
		self._label6.Text = "Congratulations! Great Job! "
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Visible = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSteelBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 307)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(135, 56)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate Average"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSteelBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(168, 307)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(135, 31)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightSteelBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(168, 354)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(135, 31)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SlateGray
		self.ClientSize = System.Drawing.Size(321, 394)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg198ScoreAvg"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		socreAvg = 0.0
		
		scoreOne = int(self._textBox1.Text)
		scoreTwo = int(self._textBox2.Text)
		scoreThree = int(self._textBox3.Text)
			
		scoreAvg = scoreOne + scoreTwo + scoreThree // 3
		
		if scoreAvg > 95:
			self._label6.Visible = True
		elif scoreAvg < 95:
			self._label6Visible = False
			
		
		self._label5.Text = str(round(scoreAvg, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._textBox3.Clear()
		self._label5.Text = ""
		self._label6.Visible = False
		pass

	def Button3Click(self, sender, e):
		Applaction.Exit()
		pass