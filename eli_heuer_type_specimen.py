#!/usr/bin/env python
# -*- coding: utf-8 -*-

from drawBot import *

# set a size for the canvas *792 x 612 pixels
size(612, 792)

# using the functions width, height and pageCount
print "width:", width()
print "height:", height()
print "pageCount:", pageCount()
print installedFonts()

# gird variables
origin = (34, 44)
width = 544
height = 704
center = width/2
num_x_units = 17
num_y_units = 22

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(0.9, 0.9, 0.9)  
    #stroke(1)  
    fill(None)
    
    step_x = 0 
    unit_x = width / num_x_units
    for x in range(num_x_units + 1):
        line((step_x, 0), (step_x, height))
        step_x += unit_x
        
    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
###################################################################

           
##################################################### page 1 - cover

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on
    
# type 
openTypeFeatures(pnum=True)
fontSize(24)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Eli Heuer", (-1, 704-32))
text("Type Specimens", (-1, 704-64))
text("2011—2016", (-1, 704-96))
fonrSize(12)
text("https://github.com/eliheuer/type-specimens/blob/master/eli_heuer_type_specimen.py",  (-1, 0))
font("Toren-Proportional")
fontSize(256)
 
(34, 64)
rx = -4
ry = 0
cfs = 134
for i in range(24):
    fontSize(cfs)
    stroke(None)
    fill(1,1,1)
    text("R", (rx, ry))
    stroke(0.1, 0.1, 0.1)
    fill(None)
    text("R", (rx, ry))
    cfs += 24
    rx += 5.7
    ry += 0
#############################################################



############################################## page 2 - toren
newPage()

# grid
#translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Toren", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("Toren-Proportional")
fontSize(72)
tracking(8)
lineHeight(50)
toren_txt_a="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890"""
textBox(toren_txt_a, (0, -32, 520, 612))

newPage()
lineHeight(None)
# page 3
grid(origin, width, height, num_x_units*2, num_y_units*2)

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Toren", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))
text("72pt", (-1, 704-96))
font("Toren-Proportional")
fontSize(72)
tracking(8)
lineHeight(50)
Toren_Txt_A="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890"""
textBox(toren_txt_a, (0, -32, 520, 612))
###################################################################################


################################################################ page 2 - toren mono
newPage()
lineHeight(None)

# grid
#translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Toren", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("BehrensAntiqua-")
fontSize(72)
tracking(8)
lineHeight(50)
toren_txt_a="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890"""
textBox(toren_txt_a, (0, -32, 520, 612))

newPage()
lineHeight(None)
# page 3
grid(origin, width, height, num_x_units*2, num_y_units*2)

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Toren", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("UPM256-Regular")
fontSize(72)
tracking(0)
lineHeight(13)
upm_txt_a="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+"""
textBox(upm_txt_a, (0, -32, 505, 576))

newPage()
lineHeight(None)
# page Isotherma-Alpha
translate(*origin)
#grid(origin, width, height, num_x_units*2, num_y_units*2)

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Isotherma", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("Isotherma-Alpha")
fontSize(72)
tracking(16)
lineHeight(64)
iso_txt_a="""CEFGHIJKLOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"""
iso_txt_b="""X"""
textBox(iso_txt_a, (0, -32, 505, 576))
textBox(iso_txt_b, (0, -32, 505, 100))

newPage()
lineHeight(None)
# page MMXI Regular 1
translate(*origin)
#grid(origin, width, height, num_x_units*2, num_y_units*2)

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Isotherma", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("MMXIMedium-Regular")
fontSize(72)
tracking(0)
lineHeight(64)
iso_txt_a="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+"""
iso_txt_b="""X"""
textBox(iso_txt_a, (0, -32, 505, 576))

newPage()
lineHeight(None)
# page MMXI MMXIMediumOblique-Regular page 1
translate(*origin)
#grid(origin, width, height, num_x_units*2, num_y_units*2)

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Isotherma", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("MMXIMediumOblique-Regular")
fontSize(72)
tracking(0)
lineHeight(64)
iso_txt_a="""ABCDEFGHIJKLMN  OPQRSTUVWXYZ abcdefghijklmn  opqrstuvwxyz 1234567890!@#$%^&*()_+"""
iso_txt_b="""X"""
textBox(iso_txt_a, (0, -32, 505, 576))

newPage()
lineHeight(None)
# page MMXI MMXIBlack-Regular page 1
translate(*origin)
#grid(origin, width, height, num_x_units*2, num_y_units*2)

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
stroke(None)
text("Family Name: Isotherma", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))
text("Release Date: 2014", (-1, 704-48))

text("Units Per Em: 1000", (128+32, 704-16))
text("Cap Height: 700", (128+32, 704-32))
text("X Height: 500", (128+32, 704-48))

text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
#text("Release Date: 2014", (256+64, 704-48))

text("72pt", (-1, 704-96))
font("MMXIBlack-Regular")
fontSize(72)
tracking(0)
lineHeight(64)
iso_txt_a="""ABCDEFGHIJK   LMNOPQRST   UVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+"""
iso_txt_b="""X"""
textBox(iso_txt_a, (0, -32, 505, 576))


saveImage([u"~/type/type-specimens/Eli_Heuer_Type_Specimen.pdf",])
