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
    strokeWidth(0.5)
    stroke(0.9, 0.1, 0.1)  
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
#fontSize(12)
#rotate(90)
#text("DrawBot Source: https://github.com/eliheuer/type-specimens/blob/master/eli_heuer_type_specimen.py",  (-1, 0))
font("Toren-Proportional")
fontSize(256)
 
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
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

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

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""
txt_line_eight="""industrial grade Tokyo artisanal A.I. soul-delay Chiba systemic gang. apophenia boy shoes plastic nodal point monofilament smart- concrete. fluidity plastic kanji jeans gang shanty town bicycle singularity. Kowloon euro-pop ablative shoes bridge monofilament motion shrine. disposable realism 8-bit otaku industrial grade marketing shrine neural. post- into savant uplink office geodesic disposable refrigerator. vehicle katana physical chrome neural Chiba marketing corrupted. saturation point plastic systema gang franchise 3D-printed rain range-rover. """

text("72pt", (-1, 704-80))
font("Toren-Proportional")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))
textBox(txt_line_three, (-2, -32, 520, 628-(80*2)))
textBox(txt_line_four, (-2, -32, 520, 628-(80*3)))
textBox(txt_line_five, (0, -32, 520, 628-(80*4)))
textBox(txt_line_six, (0, -32, 520, 628-(80*5)))
textBox(txt_line_seven, (-6, -32, 520, 628-(80*6)))
###############################################################

################################################ page 3 - toren
newPage()

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

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

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""
txt_line_eight="""industrial grade Tokyo artisanal A.I. soul-delay Chiba systemic gang. apophenia boy shoes plastic nodal point monofilament smart- concrete. fluidity plastic kanji jeans gang shanty town bicycle singularity. Kowloon euro-pop ablative shoes bridge monofilament motion shrine. disposable realism 8-bit otaku industrial grade marketing shrine neural. post- into savant uplink office geodesic disposable refrigerator. vehicle katana physical chrome neural Chiba marketing corrupted. saturation point plastic systema gang franchise 3D-printed rain range-rover. """

text("72pt", (-1, 704-80))
font("Toren-Proportional")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))
textBox(txt_line_three, (-2, -32, 520, 628-(80*2)))
textBox(txt_line_four, (-2, -32, 520, 628-(80*3)))
textBox(txt_line_five, (0, -32, 520, 628-(80*4)))
textBox(txt_line_six, (0, -32, 520, 628-(80*5)))
textBox(txt_line_seven, (-6, -32, 520, 628-(80*6)))
###############################################################

# ############################################## page 2 - behrens
# newPage()
# lineHeight(None)

# # grid
# #translate(*origin) # grid off
# grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# # type 
# fontSize(12)
# font("Helvetica Neue Bold")
# tracking(0)
# fill(0.1, 0.1, 0.1)
# stroke(None)
# text("Family Name: Toren", (-1, 704-16))
# text("Style Name: Regular", (-1, 704-32))
# text("Release Date: 2014", (-1, 704-48))

# text("Units Per Em: 1000", (128+32, 704-16))
# text("Cap Height: 700", (128+32, 704-32))
# text("X Height: 500", (128+32, 704-48))

# text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
# text("License: SIL Open Font License v1.1", (256+64, 704-32))
# #text("Release Date: 2014", (256+64, 704-48))

# text("72pt", (-1, 704-96))
# font("BehrensAntiqua-")
# fontSize(72)
# tracking(8)
# lineHeight(50)
# txt_line_one="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890"""
# textBox(txt_line_one, (0, -32, 520, 612))

# newPage()
# lineHeight(None)
# # page 3
# grid(origin, width, height, num_x_units*2, num_y_units*2)

# # type 
# fontSize(12)
# font("Helvetica Neue Bold")
# tracking(0)
# fill(0.1, 0.1, 0.1)
# stroke(None)
# text("Family Name: Toren", (-1, 704-16))
# text("Style Name: Regular", (-1, 704-32))
# text("Release Date: 2014", (-1, 704-48))

# text("Units Per Em: 1000", (128+32, 704-16))
# text("Cap Height: 700", (128+32, 704-32))
# text("X Height: 500", (128+32, 704-48))

# text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
# text("License: SIL Open Font License v1.1", (256+64, 704-32))
# #text("Release Date: 2014", (256+64, 704-48))

# text("72pt", (-1, 704-96))
# font("UPM256-Regular")
# fontSize(72)
# tracking(0)
# lineHeight(13)
# txt_line_one="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+"""
# textBox(txt_line_one, (0, -32, 505, 576))

# newPage()
# lineHeight(None)
# # page Isotherma-Alpha
# translate(*origin)
# #grid(origin, width, height, num_x_units*2, num_y_units*2)

# # type 
# fontSize(12)
# font("Helvetica Neue Bold")
# tracking(0)
# fill(0.1, 0.1, 0.1)
# stroke(None)
# text("Family Name: Isotherma", (-1, 704-16))
# text("Style Name: Regular", (-1, 704-32))
# text("Release Date: 2014", (-1, 704-48))

# text("Units Per Em: 1000", (128+32, 704-16))
# text("Cap Height: 700", (128+32, 704-32))
# text("X Height: 500", (128+32, 704-48))

# text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
# text("License: SIL Open Font License v1.1", (256+64, 704-32))
# #text("Release Date: 2014", (256+64, 704-48))

# text("72pt", (-1, 704-96))
# font("Isotherma-Alpha")
# fontSize(72)
# tracking(16)
# lineHeight(64)
# txt_line_one="""CEFGHIJKLOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"""
# txt_line_two="""X"""
# textBox(txt_line_one, (0, -32, 505, 576))
# textBox(txt_line_two, (0, -32, 505, 100))

# newPage()
# lineHeight(None)
# # page MMXI Regular 1
# translate(*origin)
# #grid(origin, width, height, num_x_units*2, num_y_units*2)

# # type 
# fontSize(12)
# font("Helvetica Neue Bold")
# tracking(0)
# fill(0.1, 0.1, 0.1)
# stroke(None)
# text("Family Name: Isotherma", (-1, 704-16))
# text("Style Name: Regular", (-1, 704-32))
# text("Release Date: 2014", (-1, 704-48))

# text("Units Per Em: 1000", (128+32, 704-16))
# text("Cap Height: 700", (128+32, 704-32))
# text("X Height: 500", (128+32, 704-48))

# text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
# text("License: SIL Open Font License v1.1", (256+64, 704-32))
# #text("Release Date: 2014", (256+64, 704-48))

# text("72pt", (-1, 704-96))
# font("MMXIMedium-Regular")
# fontSize(72)
# tracking(0)
# lineHeight(64)
# txt_line_one="""ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+"""
# textBox(txt_line_one, (0, -32, 505, 576))

# newPage()
# lineHeight(None)
# # page MMXI MMXIMediumOblique-Regular page 1
# translate(*origin)
# #grid(origin, width, height, num_x_units*2, num_y_units*2)

# # type 
# fontSize(12)
# font("Helvetica Neue Bold")
# tracking(0)
# fill(0.1, 0.1, 0.1)
# stroke(None)
# text("Family Name: Isotherma", (-1, 704-16))
# text("Style Name: Regular", (-1, 704-32))
# text("Release Date: 2014", (-1, 704-48))

# text("Units Per Em: 1000", (128+32, 704-16))
# text("Cap Height: 700", (128+32, 704-32))
# text("X Height: 500", (128+32, 704-48))

# text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
# text("License: SIL Open Font License v1.1", (256+64, 704-32))
# #text("Release Date: 2014", (256+64, 704-48))

# text("72pt", (-1, 704-96))
# font("MMXIMediumOblique-Regular")
# fontSize(72)
# tracking(0)
# lineHeight(64)
# txt_line_one="""ABCDEFGHIJKLMN  OPQRSTUVWXYZ abcdefghijklmn  opqrstuvwxyz 1234567890!@#$%^&*()_+"""
# iso_txt_b="""X"""
# textBox(txt_line_one, (0, -32, 505, 576))

# newPage()
# lineHeight(None)
# # page MMXI MMXIBlack-Regular page 1
# translate(*origin)
# #grid(origin, width, height, num_x_units*2, num_y_units*2)

# # type 
# fontSize(12)
# font("Helvetica Neue Bold")
# tracking(0)
# fill(0.1, 0.1, 0.1)
# stroke(None)
# text("Family Name: Isotherma", (-1, 704-16))
# text("Style Name: Regular", (-1, 704-32))
# text("Release Date: 2014", (-1, 704-48))

# text("Units Per Em: 1000", (128+32, 704-16))
# text("Cap Height: 700", (128+32, 704-32))
# text("X Height: 500", (128+32, 704-48))

# text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
# text("License: SIL Open Font License v1.1", (256+64, 704-32))
# #text("Release Date: 2014", (256+64, 704-48))

# text("72pt", (-1, 704-96))
# font("MMXIBlack-Regular")
# fontSize(72)
# tracking(0)
# lineHeight(64)
# txt_line_one="""ABCDEFGHIJK   LMNOPQRST   UVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+"""
# textBox(txt_line_one, (0, -32, 505, 576))


saveImage([u"~/type/type-specimens/Eli_Heuer_Type_Specimen.pdf",])
