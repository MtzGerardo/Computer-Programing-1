require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlLight
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(12, 237)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(196, 70)
		@button1.TabIndex = 0
		@button1.Text = "Caluclate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlLight
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(214, 237)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(197, 70)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ControlLight
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(417, 237)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(197, 70)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(358, 29)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(239, 20)
		@textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(358, 66)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(239, 20)
		@textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(358, 106)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(239, 20)
		@textBox3.TabIndex = 5
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(358, 144)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(239, 20)
		@textBox4.TabIndex = 6
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ScrollBar
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 104)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(340, 60)
		@label1.TabIndex = 7
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ScrollBar
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(12, 29)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(340, 60)
		@label2.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaption
		self.ClientSize = System::Drawing::Size.new(637, 319)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		number1= int(@textBox1.Text)
		number2 = int(@textBox2.Text)
		number3 = int(@textBox3.Text)
		number4 = int(@textBox4.Text)
		Sum = number1 + number2 + number3 + number4
		Average = Sum/4.0
		@label1.Text = "Sum: " + str(Sum)
		@label2.Text = "Average: " + str(Average)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
		@label1.Text = ""
		@label2.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

