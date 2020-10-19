from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
from fpdf import FPDF
import os
from PyPDF2 import PdfFileReader



def makePdf(pdfFileName, listPages, dir = '',user_name="ask"):
    if (dir):
        dir += "/"
    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")



def save_image(text,img,fonts,color,path,uname,off_value,off_x,off_y,pa_width,e_offset,ip_page,n_font,a_name,u_name,n_x,n_y,a_tittle,g_name,u_check):
    i=0
    temp_word=text[0]
    f_path=path+"/temp_f/"+uname
    os.mkdir(f_path,0o777)
    draw = ImageDraw.Draw(img)
    if(a_name==["name_yes"]):
        draw.text((n_x,n_y),u_name,fill='rgba(59,59,62,255)',font=n_font)
    if(u_check==["yes"]):
            draw.text((800,50),g_name,fill='rgba(59,59,62,50)',font=a_tittle)
    margin = off_x
    offset = off_y
    de = os.path.join(f_path, "input.txt")
    fi = open(de,"w")
    fi.write(text)
    fi.close
    file = open(de,'r')
    a = file.read()
    body=a
    lines = text.split("\n")
    lists = (textwrap.TextWrapper(width=pa_width,break_long_words=False).wrap(line) for line in lines)
    body  = "\n".join("\n".join(list) for list in lists)
    #print(body)
    #draw.multiline_text((margin,offset),body,font=fonts,fill=color)
    for line in body.split("\n"):
        offset += fonts.getsize(line)[1]
        #print(fonts.getsize(line)[1])
        if line in "\n":
           offset += off_value
        if offset< 3200: #2356:
            draw.text((margin, offset), line, font=fonts,fill=color)
        else:
            output=path+"/temp_f/"+uname+"/"+str(i)+".jpg"
            img.save(output)
            img=Image.open(ip_page)
            draw = ImageDraw.Draw(img)
            offset=e_offset
            i=i+1

    if offset<= 3200: #2356:
        img.save(path+"/temp_f/"+uname+"/"+str(i)+".jpg")

    def pdf_number():
        list = os.listdir("temp_f/"+uname)
        number_files = len(list)
        file_number = []
        for i in range(0, number_files-1):
            file_number.append(i)
        return file_number

    makePdf("final",pdf_number(),path+"/temp_f/"+uname,uname)
    return img








