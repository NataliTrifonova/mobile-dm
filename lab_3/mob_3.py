import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH

#Возьмем данные, полченные из программ первой и второй лабораторных:
file1 = open("output.txt", "r")
file2 = open("output2.txt", "r")
cost_t = file1.readline()
cost_t = cost_t[(cost_t.index(':') + 2):-2]
cost_s = file1.readline()
cost_s = cost_s[(cost_s.index(':') + 2):-1]
file2.readline()
cost_i = file2.readline()
cost_i = cost_i[(cost_i.index(':') + 2):-1]
print(cost_t, cost_s, cost_i)

#Вставим данные в таблицы файла:
doc = docx.Document('schet.docx')
tables = doc.tables

tables[0].cell(0, 0).text = 'АО "Стоун банк" Г. МОСКВА'
tables[0].cell(0, 3).text = '044525700'
tables[0].cell(1, 3).text = '30101810200000000700'
tables[0].cell(3, 0).text = 'ИНН 7722737766'
tables[0].cell(3, 1).text = 'КПП 772201001'
tables[0].cell(3, 3).text = '40702810900000002453'
tables[0].cell(4, 0).text = 'ООО "Василек"'

tables[1].cell(0, 0).text = 'Счет на оплату №11 от 13 мая 2020 г.'
p = tables[1].rows[0].cells[0].text
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

t_i = 'ООО "ВАСИЛЕК", ИНН 7722737753, КПП 772201001, 109052, '
t_i += 'г. Москва ул. Добрынинская, д. 70, корпус 2, тел: 12345'
p = tables[2].cell(0, 1).text = t_i
t_z = 'ООО "ЛАГУНА", ИНН 77147374567, КПП 772864077, 106752, '
t_z += 'г. Москва ул. Тульская, д. 67, корпус 5, тел: 54321'
p = tables[2].cell(1, 1).text = t_z
p = tables[2].cell(2, 1).text = "№20022016 от 13.05.20"

tables[3].cell(1, 1).text = 'Тарификация услуг типа "Телефония".'
tables[3].cell(1, 4).text = cost_t
tables[3].cell(1, 5).text = cost_t
tables[3].add_row()
tables[3].cell(2, 0).text = '2'
tables[3].cell(2, 1).text = 'Тарификация услуг типа "СМС".'
tables[3].cell(2, 4).text = cost_s
tables[3].cell(2, 5).text = cost_s
tables[3].add_row()
tables[3].cell(3, 0).text = '3'
tables[3].cell(3, 1).text = 'Тарификация услуг типа "Интернет".'
tables[3].cell(3, 4).text = cost_i
tables[3].cell(3, 5).text = cost_i


#p = tables[0].rows[3].cells[0].text
#print(p)

paragraphs = doc.paragraphs

p = paragraphs[5].text
print(p)

doc.save('schet2.docx')