from flask import Flask, redirect, url_for, render_template, request,jsonify, send_file ,send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap
import base
import PyPDF2
#import textract


Application = Flask(__name__)

Application_ROOT = os.path.dirname(os.path.abspath(__file__))


@Application.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        iptext = request.form["etext"]
        iradioColor = request.form["radioColor"]
        color_choice = iradioColor
        user_name = request.form["uname"]
        uni_check = request.form.getlist("unicheck")
        get_name = request.form["uniname"]
        add_name = request.form.getlist("name_check")
        drop_font = request.form.getlist("drop_font")

        u_id = random.randint(100,9990)
        u_id_name = user_name + str(u_id)


		# Color Choice
        if(color_choice == "black"):
              color = 'rgb(59,59,62)'
        elif(color_choice == "blue"):
            color = 'rgb(22,38,76)'
        elif(color_choice == "red"):
            color = 'rgb(255,0,0)'


        # Generates File Name
        random_number = random.randint(10000000,99999999)
        file_user_name = user_name.replace(" ","_")
        file_name = "ASKStudio-" + str(random_number) + file_user_name
        global des_global
        output_file_name=""
        file_to_download=""
        global mtype
        global f_name
        f_name=file_name



        # Generates PDF files
        output_file_name = file_name + ".pdf"
        output = "output_files\\" + output_file_name
        des_global = output
        mime_type= 'Applicationlication/pdf'
        mtype = mime_type
        file_to_download = "\\output_files\\" + file_name

        #Image to draw on
        image = Image.open('custom_page.jpg')
        draw = ImageDraw.Draw(image)

        font_spacing = 0
        offset_value = 0
        offset_start_x = 0
        offset_start_y = 0
        page_width = 0
        end_offset = 0
        name_x = 0
        name_y = 0

        page = "page.jpg"

        #(x,y) = (200,200)
        name_font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 45)

        # Font Choice
        if(drop_font==["1"]):
            font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 60)
            name_font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 45)
            page = "custom_page.jpg"
            image = Image.open(page)
            #(x,y) = (180,150)
            offset_value = 105
            font_spacing = 20
            offset_start_x = 250
            offset_start_y = 215
            page_width = 85
            end_offset = 200
            name_x = 2000
            name_y = 190


        elif(drop_font==["2"]):
            font = ImageFont.truetype('Fonts/DawningofaNewDay-Regular.ttf',size = 80)
            name_font = ImageFont.truetype('Fonts/DawningofaNewDay-Regular.ttf',size = 45)
            #(x,y) = (200,190)
            font_spacing = -5
            page = "apple-page.jpg"
            offset_value = 30
            offset_start_x = 260
            offset_start_y = 240
            page_width = 80
            end_offset = 200
            name_x = 2000
            name_y = 190

        elif(drop_font==["3"]):
            font = ImageFont.truetype('Fonts/HomemadeApple-Regular.ttf',size = 50)
            name_font = ImageFont.truetype('Fonts/HomemadeApple-Regular.ttf',size = 38)
            page = "apple-page.jpg"
            image = Image.open(page)
            font_spacing = 21
            #(x,y) = (200,215)
            offset_value = 100
            offset_start_x = 260
            offset_start_y = 320
            page_width = 75
            end_offset = 320
            name_x = 2000
            name_y = 200

        elif(drop_font==["4"]):
            font = ImageFont.truetype('Fonts/NanumBrushScript-Regular.ttf',size = 80)
            name_font = ImageFont.truetype('Fonts/NanumBrushScript-Regular.ttf',size = 55)
            page = "nanum_page.jpg"
            image = Image.open(page)
            font_spacing = 22
            #(x,y) = (200,208)
            offset_value = 80
            offset_start_x = 280
            offset_start_y = 220
            page_width = 80
            end_offset = 220
            name_x = 2000
            name_y = 195

        else:
            font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 50)
            name_font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 45)
            font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 60)
            name_font = ImageFont.truetype('Fonts/IndieFlower-Regular.ttf',size = 45)
            page = "custom_page.jpg"
            image = Image.open(page)
            #(x,y) = (180,150)
            offset_value = 105
            font_spacing = 20
            offset_start_x = 250
            offset_start_y = 215
            page_width = 85
            end_offset = 200
            name_x = 2000
            name_y = 190

        # Assignment Tittle
        assignment_tittle = ImageFont.truetype('Fonts/assignment_tittle.ttf',size = 50)


        target = os.path.join(Application_ROOT, 'uploaded files')

        # If user uploads the file
        def FileInput():
            target = os.path.join(Application_ROOT, 'uploaded files')
            if not os.path.isdir(target):
                os.mkdir(target)

            for file in request.files.getlist("fupload"):
                f = request.files['fupload']
                filename = f.filename
                destination = "\\".join([target,filename])
                file.save(destination)

            #Get file type
            name, ext = os.path.splitext(destination)
            #If file type is a .txt file
            if(ext == ".txt"):
                file = open(destination,'r')
                a = file.read()
            """
            #If file type is .pdf file
            elif(ext == ".pdf"):
                text = textract.process(destination, method='pdfminer')
            #If file is .docx file
            elif(ext == ".docx"):
                #.docx file
                print(".docx")
            else:
                print("error")

            """
            image1=base.save_image(a,image,font,color,Application_ROOT,u_id_name,offset_value,offset_start_x,offset_start_y,page_width,end_offset,page,name_font,add_name,user_name,name_x,name_y,assignment_tittle,get_name,uni_check)
            #draw.multiline_text((x,y),a,fill=color,font=font,spacing=font_spacing)
            #image1.save(output)

        # If user adds the text
        def TextInput():
            message = iptext
            image1=base.save_image(message,image,font,color,Application_ROOT,u_id_name,offset_value,offset_start_x,offset_start_y,page_width,end_offset,page,name_font,add_name,user_name,name_x,name_y,assignment_tittle,get_name,uni_check)
            #draw.multiline_text((x,y),message,fill=color,font=font,spacing=font_spacing)
            #image1.save(output)

        # Adds University Name
        def printUniName():
            draw.text((500,40),get_name,fill='rgba(59,59,62,50)',font=assignment_tittle)

        # Adds Client Name
        def printName():
            draw.text((1300,10),user_name,fill='rgba(59,59,62,255)',font=name_font)

        if(uni_check==["yes"]):
            printUniName()

        if(add_name==["name_yes"]):
            printName()

        if(len(iptext) < 1):
            FileInput()
        else:
            TextInput()

        return redirect(url_for("downloadfile",name = output_file_name, folder = u_id_name ))
    else:
        return render_template("index.html")


#Download File
@Application.route('/<name>,/<folder>')
def downloadfile(name,folder):
    try:
        return send_file("temp_f//"+folder+"//"+"final.pdf", attachment_filename=name, as_attachment=True )
    except Exception as e:
        return str(e)

@Application.route("/About")
def About():
    return render_template("about.html")

@Application.route("/Contact")
def Contact():
    return render_template("contact.html")


@Application.route("/Down")
def Down():
    return send_file("DE2020082126912_Travel_PASS.pdf", as_attachment=True)

@Application.route('/test/<int:a>/<int:b>')
def add(a,b):
    sum = a+b
    result={
        "Addition: " : sum
        }
    return jsonify(result)

if __name__ == "__main__":
    Application.run(debug=True)

