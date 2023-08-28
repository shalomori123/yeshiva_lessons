#####################################################
# משתנים שצריך להגדיר כדי שהתוכנה תפעל במלואה:
#####################################################

# הנחיות לאחראי הקלטות:
# הקובץ לרשותך בהתאם להעדפות שלך, רק:
# א. תשמור על השמות באנגלית כמו שהם
# ב. אם אין לך צורך בחלק מסוים אל תמחק אותו לגמרי, אלא רק תרוקן את הרשימה

# הכותב: שלום-אורי דנינו, אחראי הקלטות בשנים תש"ף-תשפ"א
# המקור של הקוד נמצא כאן ואני מעדכן אותו מדי פעם
# https://github.com/shalomori123/yeshiva_lessons

######################################################

# השנה הנוכחית - לשנות בהתאם לשנה
# לשים לב שצריך פעמיים גרש יחיד במקום גרשיים (שם הקובץ לא יכול להכיל גרשיים)
CURRENT_YEAR = "התשפ''א"

# שמות הרבנים - השם הראשון משמאל הוא השם הרשמי שיכנס לשם הקובץ. 
# שאר השמות הם כינויים שאפשר להשתמש בהם לקיצור כאשר התוכנה שואלת מה שם הרב
RAV_NAMES = [
    ["מרן רה''י", "מרן", "הרב שבתי סבתו", "הרב סבתו", "הרב שבתי"],
    ["רה''י הרב יצחק", "רהי", "רה''י", "הרב יצחק", "הרב יצחק סבתו", "יצחק"],
    ["הרב אחיה סנדובסקי", "הרב אחיה", "הרב סנדובסקי", "אחיה", "סנדובסקי"],
    ["הרב אליהו דורדק", "הרב אלי דורדק", "הרב אלי", "הרב דורדק", "דורדק"],
    ["הרב אליסף יעקבסון", "הרב אליסף", "הרב יעקבסון", "הרב יעקובסון", "הרב אליסף יעקובסון", "יעקבסון"],
    ["הרב גבריאל גולדמן", "הרב גולדמן", "גולדמן"],
    ["הרב חיים גרינשפן", "הרב גרינשפן", "הגרח", "הגר''ח", "גרח", "גר''ח", "גרינשפן"],
    ["הרב חיים סבתו", "הרב חיים", "חיים"],
    ["הרב חן חלמיש", "הרב חן", "חן"],
    ["הרב יובל אהרוני", "הרב יובל", "יובל"],
    ["הרב יוסף מימון", "הרב יוסף", "יוסף"],
    ["הרב יעקב חזן", "הרב חזן", "חזן"],
    ["הרב יעקב סבתו", "הרב יעקב", "יעקב"],
    ["הרב יצחק חי זאגא", "הרב יצחק זאגא", "הרב זאגא", "זאגא"],
    ["הרב צבי אליהו סקולניק", "הרב צביאלי סקולניק", "הרב צביאלי", "הרב סקולניק", "צביאלי"],
    ["הרב צדוק אליאס", "הרב צדוק", "צדוק"],
    ["הרב ראובן פיירמן", "הרב פיירמן", "פיירמן"],
    ["הרב ראובן ששון", "הרב ראובן", "ראובן"]]

# שמות תיקיות הרבנים. אם יש הבדל בין השם הנכתב בקובץ לשם התיקיה של הרב, יש להוסיף לכאן.
# פורמט: "השם שיופיע בתחילת הקובץ": "שם התיקייה", ת
rav_correct_dir = {
    "מרן רה''י": "מרן רה''י - הרב שבתי סבתו",
    "רה''י הרב יצחק": "רה''י - הרב יצחק סבתו",
}

# שמות תיקיות הנושאים. אם יש הבדל בין שם הנושא הנכתב בקובץ לשם התיקיה של הנושא, יש להוסיף לכאן.
# פורמט: "שם התיקייה": "השם שיופיע בתחילת הקובץ", (הפוך מהתיקיות של הרבנים, אולי כדאי להחליף)
topic_correct_dir = {
    "כולל - הלכות איסור והיתר": "הלכות איסור והיתר",
    "עיון פרק ראשון שבת": "עיון",
}

# כתובות למקלטים. יש לשנות בהתאם לשינוי המקלט. להיכנס לתיקייה שבה נשמרות ההקלטות ולהעתיק את הכתובת לכאן
recorders_path = {
    "1": r"D:\dvr\hp",
    "מקלט 1": r"D:\dvr\hp",
    "2": r"D:\RECORD",
    "מקלט 2": r"D:\RECORD",
    "3": r"D:\RECORD",
    "מקלט 3": r"D:\RECORD"
}

# תיקיית הקלטות חדשות
directory2 = r"C:\Users\Administrator\Desktop\הקלטות חדשות"
# תיקיית שיעורים מהשבוע האחרון
directory3 = r"C:\Users\Administrator\Desktop\שיעורי הישיבה הגבוהה\שיעורים מהשבוע האחרון"
# תיקיית השנה הנוכחית
directory4 = r"C:\Users\Administrator\Desktop\שיעורי הישיבה הגבוהה\שיעורי הישיבה הגבוהה\שיעורים תשפ''א 81"
