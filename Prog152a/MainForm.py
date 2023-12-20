import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Coral
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 244)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(199, 59)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Coral
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(276, 244)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(198, 59)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Coral
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(537, 244)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(199, 59)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Coral
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 123)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(257, 50)
		self._label1.TabIndex = 3
		self._label1.Text = "The sum of the mulitples of 3, from 3 to 9669:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Coral
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(276, 123)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(460, 50)
		self._label2.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.OrangeRed
		self.ClientSize = System.Drawing.Size(748, 310)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		Sum3 = 3 + 6 + 9 + 12 + 15 + 18 + 21 + 24 + ... + 9663 + 9666 + 9669
		self._lable2.Text.Add(Sum3)

	def Button2Click(self, sender, e):
		self._lable2.Text.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()