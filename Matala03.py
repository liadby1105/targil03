#MATALA03 - liad ben yechiel
import json

data_name=dict() #מילון לצורך הכנסת השמות/מספרי טלפון לאיידי סידורי
data_messages=dict() #מילון הכולל את כל המידע על ההתכתבויות - סעיף ב
metadata=dict() #מילון הכולל את כל המידע אודות הקבוצה עצמה - סעיף ג
dicttogether=dict() #מילון המחבר בין 2 המילונים הקודמים - סעיף ד
i=1 #לצורך ספירת אנשים שונים
list1=[] #רשימה המכילה את כל מילון דאטה2

def datetime3(line:str): #פונקצייה למציאת התאריך והשעה
    makaf=line.find("-")
    datetime=line.strip()[:makaf-1]
    datetime=datetime.replace('.','-')
    return(datetime)

handle=open('happybirthday.txt','r', encoding='utf-8') #פתיחת הקובץ
count1=0 #קאונטר לספירת מספר שורה לשם כניסה ל2 השורות הראשונות להוצאת מידע אודות הקבוצה עצמה
for line in handle:
    if line.count(':')>=2: #תנאי שבודק שורות רלוונטיות
        datetime=datetime3(line) #שימוש בפונקציה למציאת התאריך והשעה
        left_side_name= line.find("-")
        right_side_name= line.find(':',left_side_name)
        name=line[left_side_name+1:right_side_name]
        if name not in data_name: #אם אותו שם/מספר לא במאגר יתן לו את המס"ד הבא
            data_name[name]=i
            num_of_participants=i #בודק מהו מספר המשתתפים בקבוצה
            i=i+1
        left_side_text=line.find(':',right_side_name)
        text=line.rstrip()[left_side_text+1:]
        i=i-1
        data_messages["datetime"]=datetime
        data_messages["id"]=data_name[name]
        data_messages["text"]=text #הכנסת המידע על התכתבויות הקבוצה למילון
        list1.append(data_messages.copy()) #הכנסה של כל דאטה2 מאותה שורת התכתבות לרשימה
        i=i+1
    if count1>=3 and line.count(':')==0 :
        data_messages["text"]=(data_messages["text"]+" "+line).strip() #אלס להוספה למילון טקסט בעל יותר משורה אחת
        list1.append(data_messages.copy())
    if count1==0: #הוצאת תאריך ושעת פתיחת הקבוצה משורה 0
        creation_date=datetime3(line)
    if count1==1: #הוצאת מידע רלוונטי משורה 1
        left_side_group=line.find('הקבוצה') #a - תופס את המיקום של שם הקבוצה מצד שמאל
        right_side_group=line.find('נוצרה') #a - תופס את המיקום של שם הקבוצה מצד ימין
        chat_name=line[left_side_group+8:right_side_group-2]
        left_side_creator=line.find("ידי")
        creator=line.strip()[left_side_creator+3:]
    count1=count1+1
    
creator=data_name[name] #הפיכת היוצר משמו/מספרו לID שלו
   
metadata["chat_name :"]=chat_name
metadata["creationdate :"]=creation_date
metadata["num_of_participants :"]=num_of_participants
metadata["creator :"]=creator #מכניס את כל הנתונים אודות הקבוצה עצמה למילון

dicttogether["messages"]=list1 #חיבור סעיפים ב,ג למילון אחד - סעיף ד
dicttogether["metadata"]=metadata

file_json=chat_name+".txt" #ייצוא לגייסון
with open(file_json, 'w', encoding='utf8') as file_json:
    json.dump(dicttogether,file_json,ensure_ascii=False,indent = 4,)