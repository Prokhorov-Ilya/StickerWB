from fpdf import FPDF, XPos, YPos
import barcode
from barcode.writer import ImageWriter
import qrcode

AllBarcode = []
WBTasks = []

# append 2d array with All Barcode from Wildberries

with open('AllBar.txt') as textFile:
    for line in textFile:
        AllBar = [item.strip() for item in line.split()]
        AllBarcode.append(AllBar)

# append 2d array with Wildberries Task

with open('WBTask.txt') as textFile:
    for line in textFile:
        WBTask = [item.strip() for item in line.split()]
        WBTasks.append(WBTask)

pdf = FPDF('P', 'mm', [40, 58])
pdf.add_font('DejaVu', fname="D:/Font/DejaVuSansCondensed.ttf")
pdf.add_font('DejaVu', 'B', fname="D:/Font/DejaVuSansCondensed-Bold.ttf")
s = 1
a = 0
def shopper():
    q = 1
    while q < 3:
        pdf.add_page()
        pdf.image('logoAtribootica.png', -2, 0, w=45)
        pdf.ln(1)
        pdf.set_font('DejaVu', '', 7)
        pdf.cell(0, 0, 'Шоппер', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('DejaVu', '', 6)
        pdf.cell(0, 5, 'Ип Панова Светлана Владимировна', align='C', new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(0, 0, 'Артикул: ' + WBTasks[s][1], align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln()
        pdf.image('image2.png', 3, 25, w=35)
        pdf.ln(2)
        pdf.image('Bar/' + WBTasks[s][1] + '.png', 2, 35, w=35, h=20)
        q += 1

def OtherProduct():
    if WBTasks[s][0] == 'Bot':
        a = 'Бутылка'
    elif WBTasks[s][0] == 'Mug':
        a = 'Кружка'
    elif WBTasks[s][0] == 'Elka':
        a = 'Ёлочная Игрушка'
    else:
        a = 'Коврик для Мыши'
    pdf.add_page(orientation='L')
    pdf.image('logoAtribootica.png', 7, 0, w=45)
    pdf.ln(1)
    pdf.set_font('DejaVu', '', 7)
    pdf.cell(0, 0, a, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font('DejaVu', '', 6)
    pdf.cell(0, 5, 'Ип Панова Светлана Владимировна', align='C', new_x=XPos.LMARGIN,
             new_y=YPos.NEXT)
    pdf.set_font('DejaVu', '', 8)
    pdf.cell(0, 0, 'Артикул: ' + WBTasks[s][1], align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)
    pdf.image('Bar/' + WBTasks[s][1] + '.png', 11, 18, w=35, h=20)

def PageAppend():
    if WBTasks[s][0] == 'ShirtBC':
        c = 'Чёрная Хлопок'
    elif WBTasks[s][0] == 'Bot':
        c = 'Бутылка'
    elif WBTasks[s][0] == 'Tote':
        c = 'Шоппер'
    elif WBTasks[s][0] == 'Mug':
        c = 'Кружка'
    elif WBTasks[s][0] == 'MPad':
        c = 'Коврик для Мыши'
    elif WBTasks[s][0] == 'ShirtWC':
        c = 'Белая Хлопок'
    elif WBTasks[s][0] == 'ShirtM':
        c = 'Футболка Унисекс'
    elif WBTasks[s][0] == 'ShirtW':
        c = 'Женская Сублимация'
    elif WBTasks[s][0] == 'ShirtC':
        c = 'Детская Сублимация'
    elif WBTasks[s][0] == 'ShirtMO':
        c = 'Меланж Оливковая'
    elif WBTasks[s][0] == 'ShirtMP':
        c = 'Меланж Розовая'
    elif WBTasks[s][0] == 'Elka':
        c = 'Ёлочная Игрушка'
    else:
        c = 'Свитшот'
    pdf.add_page(orientation='L')
    pdf.set_font('DejaVu', '', 18)
    pdf.ln(5)
    pdf.cell(0, -5, c, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, -6, WBTasks[0][0] + ' ' + WBTasks[0][1], align='C')
    pdf.ln(5)
    pdf.cell(0, 5, 'стр ' + WBTasks[s][7], align='C')

def textile():
    if WBTasks[s][0] == 'ShirtBC':
        b = 'Чёрная Хлопок'
    elif WBTasks[s][0] == 'ShirtWC':
        b = 'Белая Хлопок'
    elif WBTasks[s][0] == 'ShirtM':
        b = 'Футболка Унисекс'
    elif WBTasks[s][0] == 'ShirtW':
        b = 'Женская Сублимация'
    elif WBTasks[s][0] == 'ShirtC':
        b = 'Детская Сублимация'
    elif WBTasks[s][0] == 'ShirtMO':
        b = 'Меланж Оливковая'
    elif WBTasks[s][0] == 'ShirtMP':
        b = 'Мкланж Розовая'
    else:
        b = 'Свитшот'

    q = 1
    while q < 3:
        pdf.add_page()
        pdf.image('logoAtribootica.png', -2, 0, w=45)
        pdf.ln(1)
        pdf.set_font('DejaVu', '', 7)
        pdf.cell(0, 0, b, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('DejaVu', '', 6)
        pdf.cell(0, 5, 'Ип Панова Светлана Владимировна', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(0, 0, 'Артикул: ' + WBTasks[s][1], align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln()
        pdf.cell(0, 7, 'Размер: ' + WBTasks[s][2], align='C')
        pdf.ln(2)
        pdf.image('image2.png', 3, 25, w=35)
        pdf.ln(2)
        pdf.image('Bar/' + WBTasks[s][1] + '_' + WBTasks[s][2] + '.png', 2, 35, w=35, h=20)
        q += 1

def qrmaker():
    pdf.add_page(orientation='L')
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=1)
    qr.add_data(WBTasks[s][3])
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][4] + '.png')
    pdf.set_font('DejaVu', '', 11)
    pdf.cell(20, -10, WBTasks[s][5], align='C', new_y=YPos.BMARGIN)
    pdf.ln()
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(55, -10, WBTasks[s][6], align='C', new_y=YPos.BMARGIN)
    pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][4] + '.png', 14, 8, w=30)

def ElkaQrCode():
    pdf.add_page(orientation='L')
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=1)
    qr.add_data('https://disk.yandex.ru/d/cozIFiozsAEduA')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + 'QrcodeElka' + '.png')
    pdf.set_font('DejaVu', '', 10)
    pdf.cell(0, -10, 'Паттерны для Ёлочной Игрушки', align='C', new_y=YPos.BMARGIN)
    pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + 'QrcodeElka' + '.png', 14, 8, w=30)

for s in range(len(WBTasks)):
    for a in range(len(AllBarcode)):
        if WBTasks[s][1] == AllBarcode[a][0]:
            if WBTasks[s][2] == AllBarcode[a][1]:
                if WBTasks[s][2] == '0':
                    code = barcode.get('code128', AllBarcode[a][2], writer=ImageWriter())
                    code.get_fullcode()
                    options = dict(compress=True)
                    filename = code.save('Bar/' + AllBarcode[a][0], options)

                else:
                    code = barcode.get('code128', AllBarcode[a][2], writer=ImageWriter())
                    code.get_fullcode()
                    options = dict(compress=True)
                    filename = code.save('Bar/' + AllBarcode[a][0] + '_' + AllBarcode[a][1], options)

                if WBTasks[s][0] == 'Bot':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtBC':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtWC':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtM':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtW':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtC':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtMO':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'ShirtMP':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'SMS':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        textile()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'MPad':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'Mug':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()

                elif WBTasks[s][0] == 'Tote':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        shopper()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                    else:
                        shopper()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                elif WBTasks[s][0] == 'Elka':
                    if WBTasks[s][7] != '0':
                        PageAppend()
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                        ElkaQrCode()
                    else:
                        OtherProduct()
                        if WBTasks[0][2] == 'png':
                            pdf.add_page(orientation='L')
                            pdf.image('Qr-code/Этикетки ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '/' + WBTasks[s][3] + '.png', 7, 0, w=45)
                        else:
                            qrmaker()
                        ElkaQrCode()
            else:
                a += 1
        else:
            a += 1

pdf.output('Этикетки/' + 'Этикетки' + ' ' + WBTasks[0][0] + ' ' + WBTasks[0][1] + '.pdf')


