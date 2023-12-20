import datetime
import System.Drawing
import System.Windows.Forms

from datetime import *
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._label21 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label17 = System.Windows.Forms.Label()
		self._label18 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._label19 = System.Windows.Forms.Label()
		self._label20 = System.Windows.Forms.Label()
		self._label22 = System.Windows.Forms.Label()
		self._label23 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.IndianRed
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(138, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(288, 44)
		self._label1.TabIndex = 0
		self._label1.Text = "Highlander Hotel"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.IndianRed
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 155)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(262, 134)
		self._label2.TabIndex = 1
		self._label2.Text = "Room Information"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.RosyBrown
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 193)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(120, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Nights:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.RosyBrown
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 236)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(120, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Nightly Charge:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.RosyBrown
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(286, 217)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(120, 23)
		self._label3.TabIndex = 9
		self._label3.Text = "Telephone:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.RosyBrown
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(286, 179)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(120, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "Room Service:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.IndianRed
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(286, 155)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(262, 134)
		self._label7.TabIndex = 7
		self._label7.Text = "Addtional Information"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.RosyBrown
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(286, 251)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(120, 23)
		self._label8.TabIndex = 12
		self._label8.Text = "Misc:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.IndianRed
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(237, 73)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(140, 23)
		self._label9.TabIndex = 14
		self._label9.Text = "Today's Date:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.IndianRed
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(237, 117)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(140, 23)
		self._label10.TabIndex = 15
		self._label10.Text = "Time:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.IndianRed
		self._label11.Cursor = System.Windows.Forms.Cursors.Default
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.SystemColors.ControlText
		self._label11.Location = System.Drawing.Point(13, 293)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(535, 207)
		self._label11.TabIndex = 18
		self._label11.Text = "Total Charges"
		self._label11.Click += self.Label11Click
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.RosyBrown
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(216, 311)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(161, 23)
		self._label12.TabIndex = 19
		self._label12.Text = "Room Charges:"
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.RosyBrown
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(216, 345)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(161, 23)
		self._label13.TabIndex = 20
		self._label13.Text = "Addtional Charges:"
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.RosyBrown
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(216, 381)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(161, 23)
		self._label14.TabIndex = 21
		self._label14.Text = "Subtotal:"
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.RosyBrown
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(216, 418)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(161, 23)
		self._label15.TabIndex = 22
		self._label15.Text = "Tax:"
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.RosyBrown
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(216, 453)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(161, 23)
		self._label16.TabIndex = 23
		self._label16.Text = "Total Charges:"
		# 
		# label21
		# 
		self._label21.BackColor = System.Drawing.Color.RosyBrown
		self._label21.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label21.Location = System.Drawing.Point(383, 453)
		self._label21.Name = "label21"
		self._label21.Size = System.Drawing.Size(161, 23)
		self._label21.TabIndex = 28
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.IndianRed
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 503)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(133, 54)
		self._button1.TabIndex = 29
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.IndianRed
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(216, 503)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(133, 54)
		self._button2.TabIndex = 30
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.IndianRed
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(415, 503)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(133, 54)
		self._button3.TabIndex = 31
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.Color.RosyBrown
		self._label17.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label17.Location = System.Drawing.Point(383, 117)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(161, 23)
		self._label17.TabIndex = 36
		# 
		# label18
		# 
		self._label18.BackColor = System.Drawing.Color.RosyBrown
		self._label18.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label18.Location = System.Drawing.Point(383, 73)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(161, 23)
		self._label18.TabIndex = 37
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(138, 238)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(123, 20)
		self._textBox1.TabIndex = 38
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(138, 193)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(123, 20)
		self._textBox2.TabIndex = 39
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(415, 254)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(123, 20)
		self._textBox3.TabIndex = 40
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(415, 217)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(123, 20)
		self._textBox4.TabIndex = 41
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(415, 179)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(123, 20)
		self._textBox5.TabIndex = 42
		# 
		# label19
		# 
		self._label19.BackColor = System.Drawing.Color.RosyBrown
		self._label19.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label19.Location = System.Drawing.Point(383, 345)
		self._label19.Name = "label19"
		self._label19.Size = System.Drawing.Size(161, 23)
		self._label19.TabIndex = 43
		# 
		# label20
		# 
		self._label20.BackColor = System.Drawing.Color.RosyBrown
		self._label20.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label20.Location = System.Drawing.Point(383, 311)
		self._label20.Name = "label20"
		self._label20.Size = System.Drawing.Size(161, 23)
		self._label20.TabIndex = 44
		# 
		# label22
		# 
		self._label22.BackColor = System.Drawing.Color.RosyBrown
		self._label22.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label22.Location = System.Drawing.Point(383, 381)
		self._label22.Name = "label22"
		self._label22.Size = System.Drawing.Size(161, 23)
		self._label22.TabIndex = 45
		# 
		# label23
		# 
		self._label23.BackColor = System.Drawing.Color.RosyBrown
		self._label23.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label23.Location = System.Drawing.Point(383, 418)
		self._label23.Name = "label23"
		self._label23.Size = System.Drawing.Size(161, 23)
		self._label23.TabIndex = 46
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCoral
		self.ClientSize = System.Drawing.Size(560, 561)
		self.Controls.Add(self._label23)
		self.Controls.Add(self._label22)
		self.Controls.Add(self._label20)
		self.Controls.Add(self._label19)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label18)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label21)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg162RoomCharge"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox6TextChanged(self, sender, e):
		pass

	def Label11Click(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		decRoomCharges = 0.0
		decAddCharges = 0.0
		decSubtotal = 0.0
		decTax = 0.0
		decTotal = 0.0
		decTAX_RATE = 0.08
		
		try:
			decAddCharges = float(self._textBox5.Text) * float(self._textBox4.Text) + float(self._textBox3.Text)
			self._label19.Text = str(round(decAddCharges, 2))
		except:
			MessageBox.Show("Room service, Telephone, and Mis. must be numbers", "Error")
			
		try:
			decRoomCharges = float(self._textBox2.Text) * float(self._textBox1.Text)
			self._label20.Text = str(round(decRoomCharges, 2))
		except:
			MessageBox.Show("Nights and Nightly Charge must be numbers", "Error")
			
		decSubtotal = decRoomCharges + decAddCharges
		self._label22.Text = str(round(decSubtotal, 2))
		
		decTax = decSubtotal * decTAX_RATE
		self._label23 = str(round(decTax, 2))
		
		decTotal = decSubtotal + decTax
		self._label21 = str(round(decTotal, 2))

	def MainFormLoad(self, sender, e):
		self._label18.Text = date.today().strftime("%A, %B, %d, %Y")
		self._label17.Text = time.strftime("%I:%M:%S %p")

	def Button2Click(self, sender, e):
		self._textBox2.Clear()
		self._textBox1.Clear()
		self._textBox5.Clear()
		self._textBox4.Clear()
		self._textBox3.Clear()
		
		self._label20.Text = ""
		self._label19.Text = ""
		self._label22.Text = ""
		self._label23.Text = ""
		self._label21.Text = ""
		
		self._label18.Text = date.today().strftime("%A, %B %d, %Y")
		self._label17.Text = time.strftime("%I:%M:%S %p")
		self._textBox2.Focus()

	def Button3Click(self, sender, e):
		Application.Exit()