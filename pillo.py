from PIL import Image, ImageDraw, ImageFont

image = Image.open("combo.png").convert("RGBA")
draw = ImageDraw.Draw(image)

subtitle_font = ImageFont.truetype("arial.ttf", 80)
# Define colors
text_color = (0, 0, 0)  # Black
highlight_color = (255, 165, 0)  # Orange




# Add icon descriptions

def get(text,font):
    w,x,y,z = draw.textbbox((0,0),text, font)
    return y-w,z-x

def add_sub(text1,text2,pos):
    tw , th = get(text=text1, font=subtitle_font)
    www = (image.width)/(3*2) - tw/2 + image.width*pos/3

    draw.text((www, 2350), text1, font=subtitle_font, fill=text_color)

    tw , th = get(text=text2, font=subtitle_font)
    www = (image.width)/(3*2) - tw/2 + image.width*pos/3

    draw.text((www, 2470), text2, font=subtitle_font, fill=text_color)



def seamcombo(date,png1,png2,png3,sub1,sub2,sub3,tag1,tag2,tag3):

    # Insert the hamster image at the top
    hamster_img = Image.open(png1).convert("RGBA").resize((525, 525))
    image.paste(hamster_img, (210,1586))
    hamster_img = Image.open(png2).convert("RGBA").resize((525, 525))
    image.paste(hamster_img, (1190,1586))
    hamster_img = Image.open(png3).convert("RGBA").resize((525, 525))
    image.paste(hamster_img, (2150,1586))

    tw , th = get(text=date, font=subtitle_font)
    www = image.width/2 - tw/2
    draw.text((www, 1160), date, font=ImageFont.truetype("arial.ttf", 90), fill=text_color)



    add_sub(sub1,tag1,0)
    add_sub(sub2,tag2,1)
    add_sub(sub3,tag3,2)

    image.save("send-combo.png")

    #image.show()  # Display the created image

#seamcombo("Date: August 19","png1.webp","png2.webp","png3.webp","Anti Money Lun","Anti Money Lun","Anti Money Lun","Market","Market","Market")