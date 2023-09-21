import os
import shutil

# import test_config as config
import config

ALEPHBET = ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'יהא', 'יוא', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט',
'ס', 'סא', 'סב', 'סג', 'סד', 'סה', 'סו', 'סז', 'סח', 'סט',
'ע', 'עא', 'עב', 'עג', 'עד', 'עה', 'עו', 'עז', 'עח', 'עט',
'פ', 'פא', 'פב', 'פג', 'פד', 'פה', 'פו', 'פז', 'פח', 'פט',
'צ', 'צא', 'צב', 'צג', 'צד', 'צה', 'צו', 'צז', 'צח', 'צט')

MONTHES = ("תשרי", "חשוון", "כסלו", "טבת", "שבט", "אדר", "ניסן", "אייר", "סיוון", "תמוז", "אב", "אלול",
	   "חשון", "מרחשוון", "כסליו", "אדר א", "אדר א'", "אדר ב", "אדר ב'", "סיון", "מנחם אב", "")

MONTH_DAYS = ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט', 'ל')



class Lesson:
	"""Class to define one file of a recording and its funtionality.
	Using to relate to the file with characters of a lesson.
	
	Attributes:
		File:
		dir - directory of the file
		fname - current file name. These two properties are provided by the user.
		path - they both combined
		extension - the extension of the file, for instance .mp3 or .wma

		Content:
		name - a standardized form to name lesson according to the next data
		rav - the Rav (or any person) that taught the lesson
		topic - main topic of the series of lessons
		title - specific content of this lesson
		date - full date according to the hebrew calander
		day - day in month
		month - hebrew month
		year - hebrew year. directly from the config file
		index_letter - numbering in ascending order of lessons in the topic directory

		Helpers:
		rav_dir - according to the rav field, find his final directory path
		topic_dir - according to the topic field, find its directory path in the rav_dir
	
	Methods:
		File operations:
		listen() - open the file (works only in windows)
		delete_file()
		copy_file(to_dir)
		move_file(to_dir)
		is_exists() - validate existence of the file
		parse_name() - to parse the attributes from the file name. doesn't working.
		validations() - to validate the parsing. doesn't working.
		set_fname(name=None) - rename the file to the given parameter or either to the self.name

		Setters:
		set_rav(rav)
		set_topic(topic)
		set_day(day) - also adding ' or " to the letters
		set_month(month)
		set_title(title)
		set_index() - according to the files in topic_dir
	"""

	def __init__(self, directory, file_name):
		self.dir = directory
		self.fname = file_name
		self.extension = os.path.splitext(self.path)[1]
		self.index_letter = ''
		self.rav = ''
		self.topic = ''
		self.day = ''
		self.month = ''
		self.year = config.CURRENT_YEAR
		self.title = ''
		
	path = property(lambda self: os.path.join(self.dir, self.fname))
	date = property(lambda self: self.day + ' ' + self.month + ' ' + self.year)
	
	@property
	def name(self):
		params = [self.index_letter] if self.index_letter else []
		params += [self.rav, self.topic, self.date, self.title]
		return ' - '.join(params) + self.extension
	
	@property
	def rav_dir(self):
		rav = self.rav
		if rav in config.rav_correct_dir:
			return os.path.join(config.directory4, config.rav_correct_dir[rav])
		elif os.path.isdir(os.path.join(config.directory4, rav)):
			return os.path.join(config.directory4, rav)
		return ''
	
	@property
	def topic_dir(self):
		if not os.path.isdir(self.rav_dir):
			return ""
		sub_dir = self.topic
		correct = config.topic_correct_dir
		if self.topic in correct.values():
			sub_dir = {i for i in correct if correct[i] == self.topic}[0]
		full_path = os.path.join(self.rav_dir, sub_dir)
		if os.path.isdir(full_path):
			return full_path
		return ""

	def listen(self):
		if not self.is_exists():
			return print("לא יכול לבצע את הפעולה מפני שהקובץ לא קיים.")
		print('האזן לשיעור')
		print(self.fname)
		# work only on windows
		os.startfile(self.path)

	def delete_file(self):
		if not self.is_exists():
			return print("לא יכול לבצע את הפעולה מפני שהקובץ לא קיים.")
		os.remove(self.path)
		print('הקובץ נמחק.')

	def copy_file(self, to_dir):
		if not self.is_exists():
			return print("לא יכול לבצע את הפעולה מפני שהקובץ לא קיים.")
		shutil.copy2(self.path, os.path.join(to_dir, self.fname))

	def move_file(self, to_dir):
		if not self.is_exists():
			return print("לא יכול לבצע את הפעולה מפני שהקובץ לא קיים.")
		self.copy_file(to_dir)
		self.delete_file()
		self.dir = to_dir
	
	def is_exists(self):
		return os.path.exists(self.path)

	def parse_name(self):
		name_parts = self.fname.split('-')
		name_parts = [p.strip() for p in name_parts]
		if len(name_parts) not in (4, 5):
			print(f'can\'t parse the filename "{self.fname}" '
	 			'as a Lesson. because there are' + 
				'6 or more' if len(name_parts) > 5 else '3 or less' 
				+ 'seperations with "-".')
		elif len(name_parts) == 4:
			self.rav = name_parts[0]
			self.topic = name_parts[1]
			self.day, self.month, self.year = name_parts[2].split()
			self.title = name_parts[3]
		elif len(name_parts) == 5:
			self.index_letter = name_parts[0]
			self.rav = name_parts[1]
			self.topic = name_parts[2]
			self.day, self.month, self.year = name_parts[3].split()
			self.title = name_parts[4]
		self.validations()

	def validations(self):
		#TODO
		pass

	def set_fname(self, name=None):
		if name is None:
			name = self.name
		os.rename(self.path, os.path.join(self.dir, name))
		self.fname = name
		print('שם הקובץ שונה.')

	def set_rav(self, rav):
		self.rav = rav

	def set_topic(self, topic):
		self.topic = topic

	def set_day(self, day):
		assert day in MONTH_DAYS
		if len(day.split(' ')[-1]) == 1:
			self.day = day + "'"
		else:
			self.day = day[:-1] + "''" + day[-1]

	def set_month(self, month):
		assert month in MONTHES
		self.month = month

	def set_title(self, title):
		self.title = title

	def set_index(self):
		if not self.topic_dir:
			return
		# הוספת אות האינדקס בתחילת שם הקובץ
		check_prev = os.listdir(self.topic_dir)
		check_prev.sort()
		prev_index = ""
		if len(check_prev):
			prev_index = check_prev[-1].split(" - ", 1)[0]
		# TODO parse_name method
		# prev_lesson = Lesson(self.topic_dir, check_prev[-1])
		# prev_lesson.parse_name()
		# prev_index = prev_lesson.index_letter
		self.index_letter = "א"
		for counter, letter in enumerate(ALEPHBET):
			if letter == prev_index:
				self.index_letter = ALEPHBET[counter + 1]
		if self.index_letter == "א":
			print(f"\n\n\nשים לב! האות התחילית בתיקיית {self.topic_dir}"
					" היא א'! תקן זאת בהקדם!\n\n\n\n")



class Editor:
	"""Class to implement the edit of file names and user interface, 
	during the edit process in the edit field directory.
	There are 2 steps in the editor: a loop on the lessons to edit their names,
	and after moving them to the right places.
	
	Attributes:
	dir - the directory to edit its file. provided by the user.
	lessons - contains the files that in the dir, as "Lesson" instances.
	index - the index of the current lesson in the dir
	cur_lesson - the current lesson that in editing process
	month - if all the lessons belong to the same month, you can 
			define it once at the beginning.
	exit - if set as True the editor will end the editing

	Methods:
	run() - the main method to run the editor
	edit_lesson() - the main method to edit one file, the cur_lesson
	move_to_dirs() - handle the process that moving all 
					the lessons to their new dirs.

	Helper Methods:
	files_to_lessons() - update the lessons according to the file names
	validate_existence() - update lessons list if files was deleted
	init_month() - ask the user to define constant month
	print_lessons() - print the names of the lessons
	choose_lesson() - ask the user which lesson to edit
	is_valid_les() - ask the user if the lesson is valid or to delete it
	skip_move() - ask the user if there are files that shouldn't be moved
	edit_title()
	edit_date()
	edit_rav()
	edit_topic()
	"""
	
	def __init__(self, directory) -> None:
		self.dir = directory
		self.lessons = []
		self.index = -1
		self.exit = False
		self.init_month()
	
	cur_lesson: Lesson = property(lambda self: self.lessons[self.index])

	def init_month(self):
		self.month = input('מה החודש עכשיו? (אם משתנה נא להשאיר ריק) ')
		while self.month not in MONTHES:
			print("שם חודש לא תקין")
			self.month = input('מה החודש עכשיו? (אם משתנה נא להשאיר ריק) ')

	def files_to_lessons(self):
		self.lessons = []
		for file in os.listdir(config.directory2):
			self.lessons.append(Lesson(self.dir, file))
	
	def validate_existence(self):
		lst = []
		for les in self.lessons:
			if les.is_exists():
				lst.append(les)
		self.lessons = lst
	
	def print_lessons(self):
		print()
		print("שמות הקבצים בתיקיה כרגע:")
		for i,les in enumerate(self.lessons, 1):
			print(str(i) + ". " + les.fname)
	
	def choose_lesson(self):
		self.print_lessons()
		num = input("בחר מס' קובץ לעריכה: (להמשך לפי סדר הקש אנטר/לסיום העריכה כתוב \"יציאה\") ")
		if not num:
			self.index += 1
			if self.index >= len(self.lessons):
				self.exit = True
		elif num.isdigit() and int(num) <= len(self.lessons):
			self.index = int(num)-1
		elif num.strip() == "יציאה":
			self.exit = True
		else:
			print("טקסט לא תקין")
			self.choose_lesson()
	
	def is_valid_les(self):
		# בדיקה אם למחוק את הקובץ או לדלג עליו
		user_input = input('האם השיעור תקין? (לא/דלג/כלום) ') 
		if user_input == "דלג":
			return False
		elif user_input == 'לא':
			statinfo = os.stat(self.cur_lesson.path)
			print('גודל הקובץ: ' + str(statinfo.st_size / 1000000) + 'Mb')
			to_remove = input('האם למחוק אותו? (כן/כלום) ')
			if to_remove == 'כן':
				self.cur_lesson.delete_file()
				self.index -= 1
				return False
		elif not user_input:
			return True
		return self.is_valid_les()
	
	def edit_title(self):
		lesson_title = input("נושא השיעור: ")
		self.cur_lesson.set_title(lesson_title)
	
	def edit_date(self):
		day = input("תאריך בחודש: ").replace("'", "").replace('"', '')
		while day not in MONTH_DAYS:
			print("יום בחודש לא תקין")
			day = input("תאריך בחודש: ").replace("'", "").replace('"', '')
		month = self.month
		while not month or month not in MONTHES:
			month = input("חודש: ")
		
		self.cur_lesson.set_day(day)
		self.cur_lesson.set_month(month)
		
	def edit_rav(self):
		short_name = input('שם הרב: ')
		while True:
			for lst in config.RAV_NAMES:
				if short_name in lst:
					return self.cur_lesson.set_rav(lst[0])
			other_rav = input("השם שכתבת אינו מופיע ברשימה. האם זה השם הנכון? (כן/כלום) ")
			if other_rav == "כן":
				return self.cur_lesson.set_rav(short_name)
			short_name = input("בחר שם חדש: ")

	def edit_topic(self):
		rav_dir = self.cur_lesson.rav_dir
		if os.path.isdir(rav_dir):
			rav_directories = next(os.walk(rav_dir))[1]
			rav_directories.append("אחר")
			for i in range(len(rav_directories)):
				if rav_directories[i] in config.topic_correct_dir:
					rav_directories[i] = config.topic_correct_dir[rav_directories[i]]
			for count, item in enumerate(rav_directories, 1):
				print(str(count) + ". " + item)
			
			choose_num = input("בחר מספר: ")
			while not choose_num.isnumeric() or int(choose_num) > len(rav_directories):
				choose_num = input("בחר מספר: ")

			if int(choose_num) < len(rav_directories):
				self.cur_lesson.set_topic(rav_directories[int(choose_num) - 1])
			else:
				enter_topic = input("נושא כללי: ")
				self.cur_lesson.set_topic(enter_topic)
		else:
			enter_topic = input("נושא כללי: ")
			self.cur_lesson.set_topic(enter_topic)
	
	def edit_lesson(self):
		self.cur_lesson.listen()
		if not self.is_valid_les():
			return
		self.edit_title()
		self.edit_date()
		self.edit_rav()
		self.edit_topic()
		self.cur_lesson.set_index()
		self.cur_lesson.set_fname()
		self.cur_lesson.validations()
	
	def skip_move(self):
		"""return tuple that contain list and bool, true = skip the list,
		false = move only the list"""
		self.print_lessons()
		option = input("בחר אפשרות:\n1. העתק הכל.\n2. בחירת קבצים לדילוג.\n"
				 "3. בחירת קבצים להעברה.\n4. לדלג על העברת הקבצים.\nבחירתך: ")
		if option not in ("1", "2", "3", "4"):
			print("טקסט לא תקין.")
			return self.skip_move()
		if option == "1":
			return ([], True)
		if option == "4":
			return ([], False)
		while option == "2":
			to_skip = input("קבצים לדילוג (רווח פשוט ביניהם): ")
			if not to_skip:
				return ([], True)
			elif to_skip.replace(" ", "").isdigit():
				lst = to_skip.split(" ")
				return ([int(i)-1 for i in lst], True)
			print("טקסט לא תקין.")
		while option == "3":
			to_move = input("קבצים להעברה (רווח פשוט ביניהם): ")
			if not to_move:
				return ([], True)
			elif to_move.replace(" ", "").isdigit():
				lst = to_move.split(" ")
				return ([int(i)-1 for i in lst], False)
			print("טקסט לא תקין.")

	def move_to_dirs(self):
		print("עוברים לשלב העברת הקבצים.")
		input("סגור את הנגן.")
		# פינוי תיקיית שיעורים מהשבוע האחרון
		delete_old = input("האם לפנות את תיקיית שיעורים מהשבוע האחרון? (כן/כלום) ")
		if delete_old == "כן":
			for old_file in os.listdir(config.directory3):
				os.remove(os.path.join(config.directory3, old_file))

		to_skip = self.skip_move()
		for i, lesson in enumerate(self.lessons):
			if (to_skip[1] and i in to_skip[0]) or (not to_skip[1] and i not in to_skip[0]):
				continue
			lesson.copy_file(config.directory3)
			# העברה לתיקיות של כל שיעור אם אפשר ואם לא לתיקיית השנה
			if lesson.topic_dir:
				lesson.move_file(lesson.topic_dir)
			else:
				lesson.move_file(config.directory4)
			print(f'הקובץ {lesson.fname} הועבר והועתק בהצלחה')
		print('פעולת ההעברה הסתיימה בהצלחה!')

	def run(self):
		self.files_to_lessons()
		while self.index < len(self.lessons):
			self.validate_existence()
			self.choose_lesson()
			if self.exit:
				break
			self.edit_lesson()
		self.move_to_dirs()



def copy_to_edit(directory1):
	print('מעתיק קבצים...')
	for file in os.listdir(directory1):
		shutil.copy2(os.path.join(directory1, file), 
	       			os.path.join(config.directory2, file))
		print(f'קובץ {file} הועתק בהצלחה')
	print('הסתיימה העתקת הקבצים! עכשיו לעריכה:\n')


def delete_recorder(directory1):
	to_delete = input("האם לרוקן את המקלט? (כן/כלום) ")
	if to_delete == "כן":
		for old_file in os.listdir(directory1):
			os.remove(os.path.join(directory1, old_file))


def define_recorder():
	recorder = input("מספר מקלט: ")
	if recorder in config.recorders_path.keys():
		return config.recorders_path[recorder]
	elif recorder == "":
		dont_copy = input("האם לדלג על העתקה מהמקלט? (כן/כלום) ")
		if dont_copy == "כן":
			return ""


def main():
	print('ברוך הבא לתוכנת העלאת השיעורים!\n אשריך!')
	to_start = input('כדי להתחיל כתוב "התחל": ')
	while to_start != 'התחל':
		to_start = input('כדי להתחיל כתוב "התחל": ')

	directory1 = define_recorder() #המיקום של הקבצים במקלט
	while directory1 is None:
		directory1 = define_recorder()
	if directory1:
		copy_to_edit(directory1)
	
	Editor(config.directory2).run()

	# if directory1:
		# delete_recorder(directory1)
	print('\nפעולת התוכנה הסתיימה.\nאנא לא לשכוח לעבור לתיקיית שנת '
       f'{config.CURRENT_YEAR} כדי לסיים את המלאכה.\nאשריך וטוב לך ובהצלחה במשמר!')

if __name__ == '__main__':
	main()
