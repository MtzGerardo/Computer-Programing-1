﻿import System.Drawing
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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumPurple
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(3, 103)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(86, 33)
		self._label1.TabIndex = 0
		self._label1.Text = "Guests:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumPurple
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(3, 147)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(86, 33)
		self._label2.TabIndex = 1
		self._label2.Text = "Chairs:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumPurple
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(3, 195)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(145, 33)
		self._label3.TabIndex = 2
		self._label3.Text = "Permutations:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumPurple
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(3, 240)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(190, 33)
		self._label4.TabIndex = 3
		self._label4.Text = "label4"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumPurple
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 330)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(163, 52)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumPurple
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(199, 330)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(163, 52)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumPurple
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(392, 330)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(163, 52)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateBlue
		self.ClientSize = System.Drawing.Size(567, 394)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)

