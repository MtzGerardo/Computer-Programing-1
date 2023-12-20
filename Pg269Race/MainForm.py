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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SlateBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(434, 65)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the three runner's name and finishing times."
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SlateBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 156)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Runner 1:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SlateBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 197)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Runner 2:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SlateBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 239)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Runner 3:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(119, 156)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(169, 24)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(119, 198)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(169, 24)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(118, 238)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(169, 24)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SlateBlue
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(150, 118)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Names"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SlateBlue
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(306, 89)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(141, 52)
		self._label6.TabIndex = 8
		self._label6.Text = "Finishing Time (in seconds)"
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(294, 155)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(156, 24)
		self._textBox4.TabIndex = 9
		# 
		# textBox5
		# 
		self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox5.Location = System.Drawing.Point(294, 198)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(153, 24)
		self._textBox5.TabIndex = 10
		# 
		# textBox6
		# 
		self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.Location = System.Drawing.Point(294, 238)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(153, 24)
		self._textBox6.TabIndex = 11
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label12)
		self._groupBox1.Controls.Add(self._label11)
		self._groupBox1.Controls.Add(self._label10)
		self._groupBox1.Controls.Add(self._label9)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Location = System.Drawing.Point(12, 277)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(438, 202)
		self._groupBox1.TabIndex = 12
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Race Results"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.SlateBlue
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(67, 46)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 13
		self._label7.Text = "1st Place:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.SlateBlue
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(67, 92)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 14
		self._label8.Text = "2nd Place:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.SlateBlue
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(67, 139)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 15
		self._label9.Text = "3rd Place:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.SlateBlue
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(173, 46)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(158, 23)
		self._label10.TabIndex = 16
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.SlateBlue
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(173, 92)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(158, 23)
		self._label11.TabIndex = 17
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.SlateBlue
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(173, 139)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(158, 23)
		self._label12.TabIndex = 18
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SlateBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 485)
		self._button1.Name = "button1"
		self._button1.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._button1.Size = System.Drawing.Size(142, 63)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate Results"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SlateBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(160, 485)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(142, 63)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SlateBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(308, 485)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(142, 63)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateBlue
		self.ClientSize = System.Drawing.Size(459, 553)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg269Race"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		runnerOne = str(self._textBox1.Text)
		runnerTwo = str(self._textBox2.Text)
		runnerThree = str(self._textBox3.Text)
		
		
		firstPlace =
		seconPlace =
		thirdPlace =
		pass