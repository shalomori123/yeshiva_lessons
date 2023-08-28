import os
import shutil

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
	"""class to define one file of record."""
	def __init__(self, directory, file_name):
		self.dir = directory
		self.fname = file_name
		self.index_letter = ''
		self.rav = ''
		self.topic = ''
		self.day = ''
		self.month = ''
		self.year = config.CURRENT_YEAR
		self.title = ''
		self.extension = os.path.splitext(self.path)[1]
		
	path = property(lambda self: os.path.join(self.dir, self.fname))
	date = property(lambda self: self.day + ' ' + self.month + ' ' + self.year)
	
	@property
	def name(self):
		return ' - '.join([self.index_letter + self.rav, self.topic, 
		     				self.date, self.title])
	
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
		open_file = open(self.path, 'rb+')
		print('האזן לשיעור')
		# work only on windows
		os.startfile(self.path)
		open_file.close()

	def delete_file(self):
		os.remove(self.path)
		print('הקובץ נמחק.')

	def copy_file(self, to_dir):
		shutil.copy2(self.path, os.path.join(to_dir, self.fname))

	def move_file(self, to_dir):
		self.copy_file(to_dir)
		self.delete_file()
		self.dir = to_dir


	def parse_name(self):
		name_parts = self.fname.split('-')
		if len(name_parts) < 4 or len(name_parts) > 5:
			print(f'can\'t parse the filename "{self.fname}" '
	 			'as a Lesson. because there are' + 
				'5 or more' if len(name_parts) > 5 else '2 or less' 
				+ 'seperations with " - " ')
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

	def set_rav(self, name):
		self.rav = name

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
		if self.topic_dir:
			# הוספת אות האינדקס בתחילת שם הקובץ
			check_prev = os.listdir(self.topic_dir)
			check_prev.sort()
			prev_index = check_prev[-1].split(" - ", 1)[0]
			# TODO parse_name method
			# prev_lesson = Lesson(self.topic_dir, check_prev[-1])
			# prev_lesson.parse_name()
			# prev_index = prev_lesson.index_letter
			self.index_letter = "א - "
			for counter, letter in enumerate(ALEPHBET):
				if letter == prev_index:
					self.index_letter = ALEPHBET[counter + 1] + ' - '
			if self.index_letter == "א - ":
				print(f"\n\n\nשים לב! האות התחילית בתיקיית {self.topic_dir}"
	  					" היא א'! תקן זאת בהקדם!\n\n\n\n")



class Editor:
	"""class to implement the edit of file names, in the edit directory."""
	def __init__(self, directory) -> None:
		self.dir = directory
		self.lessons = []
		self.index = 0
		self.exit = False
		self.init_month()
	
	cur_lesson: Lesson = property(lambda self: self.lessons[self.index])

	def init_month(self):
		self.month = input('מה החודש עכשיו? (אם משתנה נא להשאיר ריק) ')
		while self.month not in MONTHES:
			print("שם חודש לא תקין")
			self.month = input('מה החודש עכשיו? (אם משתנה נא להשאיר ריק) ')
	
	def files_to_lessons(self):
		for file in os.listdir(config.directory2):
			self.lessons.append(Lesson(self.dir, file))
	
	def print_lessons(self):
		print("שמות הקבצים בתיקיה כרגע:")
		for i,les in enumerate(self.lessons):
			print(str(i) + ". " + les.name)
	
	def choose_lesson(self):
		self.print_lessons()
		num = input("בחר מס' קובץ לעריכה: (להמשך לפי סדר הקש אנטר/לסיום העריכה כתוב \"יציאה\") ")
		if not num:
			self.index += 1
		elif num.isdigit() and int(num) < len(self.lessons):
			self.index = int(num)
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
		self.cur_lesson.set_fname()
		self.cur_lesson.validations()

	def move_to_dirs(self):
		to_move = input('כל השמות שונו, האם להעביר לתיקיות? (כן) ')
		input("סגור את הנגן.")
		while to_move != 'כן':
			to_move = input('האם להעביר לתיקיות? (כן) ')
		# פינוי תיקיית שיעורים מהשבוע האחרון
		delete_old = input("האם לפנות את תיקיית שיעורים מהשבוע האחרון? (כן/כלום) ")
		if delete_old == "כן":
			for old_file in os.listdir(config.directory3):
				os.remove(os.path.join(config.directory3, old_file))

		for lesson in self.lessons:
			lesson.copy_file(config.directory3)
			# העברה לתיקיות של כל שיעור אם אפשר ואם לא לתיקיית השנה
			lesson.set_index()
			lesson.set_fname()
			if lesson.topic_dir:
				lesson.move_file(lesson.topic_dir)
			else:
				lesson.move_file(config.directory4)
			print('הקובץ %s הועבר והועתק בהצלחה' % lesson.name)
		print('כל הקבצים הועתקו בהצלחה!')

	def run(self):
		self.files_to_lessons()
		while self.index < len(self.lessons):
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
		print('קובץ %s הועתק בהצלחה' % file)
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

	if directory1:
		delete_recorder(directory1)
	print('\nפעולת התוכנה הסתיימה.\nאנא לא לשכוח לעבור לתיקיית שנת '
       f'{config.CURRENT_YEAR} כדי לסיים את המלאכה.\nאשריך וטוב לך ובהצלחה במשמר!')

if __name__ == '__main__':
	main()
