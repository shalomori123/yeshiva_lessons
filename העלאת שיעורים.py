import os
import shutil
from re import match

from . import config

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

class Lesson:
	"""class to define one file of record."""
	def __init__(self, dir, file_name):
		self.dir = dir
		self.fname = file_name
		self.path = lambda: os.path.join(self.dir, self.fname)
		self.index_letter = ''
		self.rav = ''
		self.rav_dir = ''
		self.topic = ''
		self.day = ''
		self.month = ''
		self.year = config.CURRENT_YEAR
		self.date = lambda: self.day + ' ' + self.month + ' ' + self.year
		self.title = ''
		self.extension = os.path.splitext(self.path())[1]
		self.name = lambda: ' - '.join([self.index_letter + self.rav, self.topic, self.date(), self.title])

	def listen(self):
		open_file = open(self.path(), 'rb+')
		print('האזן לשיעור')
		os.startfile(self.path())
		open_file.close()

	def delete_file(self):
		os.remove(self.path())
		print('הקובץ נמחק.')

	def copy_file(self, to_dir):
		shutil.copy2(self.path(), os.path.join(to_dir,self.fname))

	def move_file(self, to_dir):
		self.copy_file(to_dir)
		self.delete_file()
		self.dir = to_dir


	def parse_name(self):
		name_parts = self.fname.split('-')
		if len(name_parts) < 4 or len(name_parts) > 5:
			print(f'can\'t parse the filename "{self.fname}" as a Lesson. because there are' + \
	            '5 or more' if len(name_parts) > 5 else '2 or less' + 'seperations with " - " ')
		elif len(name_parts) == 4:
			self.rav = name_parts[0]
			self.topic = name_parts[1]
			self.date = lambda: name_parts[2]
			self.title = name_parts[3]
		elif len(name_parts) == 5:
			self.index_letter = name_parts[0]
			self.rav = name_parts[1]
			self.topic = name_parts[2]
			self.date = lambda: name_parts[3]
			self.title = name_parts[4]
			self.validations()

	def validations(self):
		#TODO
		pass

	def change_name(self, name=None):
		if name is None:
			name = self.name()
		os.rename(self.path(), os.path.join(self.dir,name))
		self.fname = name
		print('שם הקובץ שונה.')

	def set_rav(self, short_name):
		self.rav = self.full_rav_name(short_name)
		self.rav_dir = self.rav_directory(self.rav)

	def full_rav_name(self, short_name):
		while True:
			for lst in config.RAV_NAMES:
				if short_name in lst:
					return lst[0]
			other_rav = input("השם שכתבת אינו מופיע ברשימה. האם זה השם הנכון? (כן/כלום) ")
			if other_rav == "כן":
				return short_name
			short_name = input("בחר שם חדש: ")

	def rav_directory(self, rav):
		if rav in config.rav_correct_dir.keys():
			return os.path.join(config.directory4, config.rav_correct_dir[rav])
		elif os.path.isdir(os.path.join(config.directory4, rav)):
			return os.path.join(config.directory4, rav)
		else:
			return ''

	def set_topic(self):
		if os.path.isdir(self.rav_dir):
			rav_directories = next(os.walk(self.rav_dir))[1]
			rav_directories.append("אחר")
			for i in range(len(rav_directories)):
				if rav_directories[i] in config.topic_correct_dir.keys():
					rav_directories[i] = config.topic_correct_dir[rav_directories[i]]

			for count, item in enumerate(rav_directories, 1):
				print(str(count) + ". " + item)
			choose_num = input("בחר מספר: ")
			while not choose_num.isnumeric() or int(choose_num) > len(rav_directories):
				choose_num = input("בחר מספר: ")
			if int(choose_num) < len(rav_directories):
				self.topic = rav_directories[int(choose_num) - 1]
			elif int(choose_num) == len(rav_directories):
				enter_topic = input("נושא כללי: ")
				self.topic = enter_topic
		else:
			enter_topic = input("נושא כללי: ")
			self.topic = enter_topic

	def set_day(self, day):
		if len(day.split(' ')[-1]) == 1:
			self.day = day + "'"
		else:
			self.day = day[:-1] + "''" + day[-1]

	def set_month(self, month):
		self.month = month

	def set_title(self, title):
		self.title = title

	def set_index(self):
		if os.path.isdir(os.path.join(self.rav_dir, self.topic)):
			check_prev = os.listdir(os.path.join(self.rav_dir, self.topic)) # הוספת אות האינדקס בתחילת שם הקובץ
			check_prev.sort()
			prev_index = check_prev[-1].split(" - ", 1)[0]
			# TODO parse_name method
			# prev_lesson = Lesson(os.path.join(lesson.rav_dir,lesson.topic), check_prev[-1])
			# prev_lesson.parse_name()
			# prev_index = prev_lesson.index_letter
			self.index_letter = "א - "
			for counter, letter in enumerate(ALEPHBET):
				if letter == prev_index:
					self.index_letter = ALEPHBET[counter + 1] + ' - '
			if self.index_letter == "א - ":
				print("\n\n\nשים לב! האות התחילית בתיקיית %s היא א'! תקן זאת בהקדם!\n\n\n\n" % \
				os.path.join(self.rav_dir, self.topic))



def copy_to_edit(directory1):
	print('מעתיק קבצים...')
	for file in os.listdir(directory1):
		shutil.copy2(os.path.join(directory1, file), os.path.join(config.directory2, file))
		print('קובץ %s הועתק בהצלחה' % file)
	print('הסתיימה העתקת הקבצים!')


def edit_names(month):
	for file in os.listdir(config.directory2):
		lesson = Lesson(config.directory2, file)
		lesson.listen()
		
		is_valid_file = input('האם השיעור תקין? (לא/דלג/כלום) ') # בדיקה אם למחוק את הקובץ או לדלג עליו
		if is_valid_file == "דלג":
			continue
		if is_valid_file == 'לא':
			statinfo = os.stat(os.path.join(config.directory2,file))
			print('גודל הקובץ: ' + str(statinfo.st_size / 1000000) + 'Mb')
			to_remove = input('האם למחוק אותו? (כן/כלום) ')
			if to_remove == 'כן':
				lesson.delete_file()
				continue
			
		lesson_title = input("נושא השיעור: ") # שינוי השם עצמו
		lesson.set_title(lesson_title)

		day_in_month = input("תאריך (היום בחודש בלבד בלי מרכאות, אם לא הגדרת חודש בהתחלה הוסף אותו עכשיו): ")
		split_day = day_in_month.split(' ')
		if match('[א-ל][א-ט]?', split_day[0]):
			fixed_day = split_day[0]
			if len(split_day) > 1:
				month = split_day[1]
		elif match('[א-ל][א-ט]?', split_day[1]):
			fixed_day = ' '.join(split_day[:-1])
			if len(split_day) > 2:
				month = split_day[-1]
		else:
			fixed_day = day_in_month
		lesson.set_day(fixed_day)
		lesson.set_month(month)

		short_rav_name = input('שם הרב: ')
		lesson.set_rav(short_rav_name)
		lesson.set_topic()

		lesson.validations()
		lesson.change_name()


def cut_at_the_end():
	to_move = input('כל השמות שונו, האם להעביר לתיקיות? (כן) ')
	input("סגור את הנגן.")
	while to_move != 'כן':
		to_move = input('האם להעביר לתיקיות? (כן) ')
	delete_old = input("האם לפנות את תיקיית שיעורים מהשבוע האחרון? (כן/כלום) ") # פינוי תיקיית שיעורים מהשבוע האחרון
	if delete_old == "כן":
		for old_file in os.listdir(config.directory3):
			os.remove(os.path.join(config.directory3, old_file))
	for file in os.listdir(config.directory2):
		lesson = Lesson(config.directory2, file)
		lesson.copy_file(config.directory3)
		
		# העברה לתיקיות של כל רב ורב אם אפשר ואם לא לתיקיית השנה
		lesson.set_index()
		lesson.change_name()
		if os.path.isdir(os.path.join(lesson.rav_dir,lesson.topic)):
			lesson.move_file(os.path.join(lesson.rav_dir,lesson.topic))
		else:
			lesson.move_file(config.directory4)
		print('הקובץ %s הועבר והועתק בהצלחה' % file)
	print('כל הקבצים הועתקו בהצלחה!')


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
	
	current_month = input('מה החודש עכשיו? (אם משתנה נא להשאיר ריק) ')
	
	edit_names(current_month)
	cut_at_the_end()
	if directory1:
		delete_recorder(directory1)
	print('\nפעולת התוכנה הסתיימה.\nאנא לא לשכוח לעבור לתיקיית שנת %s כדי לסיים את המלאכה.\nאשריך וטוב לך ובהצלחה במשמר!' % config.CURRENT_YEAR)

if __name__ == '__main__':
	main()
