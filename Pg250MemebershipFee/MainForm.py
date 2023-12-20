import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.decDiscount4to6 = 0.05
		self.decDiscount7to9 = 0.08
		self.decDiscount10orMore = 0.1
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.Teal
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(262, 165)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Type of Membership"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(345, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(262, 165)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Options"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._textBox1)
		self._groupBox3.Controls.Add(self._label1)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(12, 184)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(262, 165)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Membership Length"
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._label5)
		self._groupBox4.Controls.Add(self._label4)
		self._groupBox4.Controls.Add(self._label3)
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox4.Location = System.Drawing.Point(345, 184)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(262, 165)
		self._groupBox4.TabIndex = 2
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Membership Fees"
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.CadetBlue
		self._radioButton1.Location = System.Drawing.Point(7, 26)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(205, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Standard Adult"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.CadetBlue
		self._radioButton2.Location = System.Drawing.Point(6, 56)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(205, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child (12 and Under)"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.CadetBlue
		self._radioButton3.Location = System.Drawing.Point(7, 86)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(205, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.Color.CadetBlue
		self._radioButton4.Location = System.Drawing.Point(6, 116)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(205, 24)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior Citizen"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.CadetBlue
		self._checkBox1.Location = System.Drawing.Point(22, 25)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(212, 39)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Yoga"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.CadetBlue
		self._checkBox2.Location = System.Drawing.Point(22, 71)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(212, 39)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Karate"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.CadetBlue
		self._checkBox3.Location = System.Drawing.Point(22, 116)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(212, 39)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CadetBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(26, 32)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(212, 55)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the Number of Months:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(26, 91)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(212, 26)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CadetBlue
		self._label2.Location = System.Drawing.Point(22, 35)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(110, 26)
		self._label2.TabIndex = 0
		self._label2.Text = "Monthly Fee:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.CadetBlue
		self._label3.Location = System.Drawing.Point(22, 94)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(110, 26)
		self._label3.TabIndex = 1
		self._label3.Text = "Total:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.CadetBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 366)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(187, 70)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.CadetBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(215, 366)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(187, 70)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.CadetBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(420, 366)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(187, 70)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.CadetBlue
		self._label4.Location = System.Drawing.Point(138, 35)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(118, 26)
		self._label4.TabIndex = 2
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.CadetBlue
		self._label5.Location = System.Drawing.Point(138, 94)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(118, 26)
		self._label5.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(619, 448)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg250MemebershipFee"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		"""
		Standard Adult membership:    $40/month
		Child (12 and Under):         $20/month
		Student:                      $25/month
		Senior Citizen (65 and over): $30/month
		
		Yoga lessons:        Add $10 to the monthly fee
		Karate lessons:      Add $30 to the monthly fee
		Personal Trainer:    Add $50 to the monthly fee
		
		1 - 3 months:        No discount
		4 - 6 months:        5% discount
		7 - 9 months:        8% discount
		10 or more months:   10% discount
		"""

	def Button1Click(self, sender, e):
		decBaseFee = 0.0
		decDiscount = 0.0
		decTotalFee = 0.0
		intMonths = 0
		
		try:
			intMonths = int(self._textBox1.Text)
		except:
			MessageBox.Show("Months must be valid integer", "Input Error")
			return
		if intMonths < 1 or intMonths > 24:
			MessageBox.Show("Months must be vaild integer", "Input Error")
			return
		
		if self._radioButton1.Checked == True:
			decBaseFee = 40
		elif self._radioButton2.Checked == True:
			decBaseFee = 20
		elif self._radioButton3.Checked == True:
			decBaseFee = 25
		elif self._radioButton4.Checked == True:
			decBaseFee = 30
			
		if self._checkBox1.Checked == True:
			decBaseFee += 10
		elif self._checkBox2.Checked == True:
			decBaseFee += 30
		elif self._checkBox1.Checked == True:
			decBaseFee += 50
			
		if intMonths <= 3:
			decDiscount = 0.0
		elif intMonths >= 4 and intMonths <= 6:
			decDiscount = decBaseFee * self.decDiscount4to6
		elif intMonths >= 7 and intMonths <= 9:
			decDiscount = decBaseFee * self.decDiscount7to9
		elif intMonths >= 10:
			decDiscount = decBaseFee * self.decDiscount10orMore
			
		decBaseFee -= decDiscount
		decTotalFee = decBaseFee * intMonths

		self._label4.Text = str(round(decBaseFee, 2))
		self._label5.Text = str(round(decTotalFee, 2))

	def Button2Click(self, sender, e):
		self._radioButton1.Checked = True
		self._checkBox1.Checked = False
		self._checkBox2.Checked = False
		self._checkBox3.Checked = False
		self._textBox1.Clear()
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()