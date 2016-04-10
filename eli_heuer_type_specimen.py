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
    stroke(0.9, 0.1, 0.1, 0.5)  
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

#################################################### page 1 - cover
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
text("Type Specimen", (-1, 704-64))
text("2011—2016", (-1, 704-96))
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

######################################### toren pro -- page 1
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
text("Units Per Em: 1000", (128+32, 704-16))
text("Year: 2014", (128+32, 704-32))
text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""
txt_line_eight="""!?ß&*,.;:"""

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
textBox(txt_line_eight, (-6, -32, 520, 628-(80*7)))
lineHeight(None)
###############################################################

############################################## toren pro page 2
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

text("Units Per Em: 1000", (128+32, 704-16))
text("Year: 2014", (128+32, 704-32))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("11pt", (-1, 704-(512)))

txt_line_one="""Mathematical"""
txt_line_two="""Improvements"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer. That train of thought led to my computer system called METAFONT, which I want to try to show you now. Here is the way I finally desided to create the letter A, for example, using a computer program."""

font("Toren-Proportional")
fontSize(72)
tracking(-1)
lineHeight(50)

textBox(txt_line_one, (-1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 421))
textBox(txt_line_six, (0, -32, 520, (421-32)-16))
textBox(txt_line_seven, (0, -32, 520, (421-64)-32))
textBox(txt_line_eight, (0, -32, 520, (421-96)-48))
lineHeight(None)

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_ten, (0, -32, 290, 205))
lineHeight(None)

###############################################################

######################################### Toren-Mono-- page 1
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
text("Style Name: Mono", (-1, 704-32))
text("Units Per Em: 1000", (128+32, 704-16))
text("Year: 2014", (128+32, 704-32))
text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""
txt_line_eight="""!?ß&*,.;:"""

font("Toren-Mono")
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
textBox(txt_line_eight, (-6, -32, 520, 628-(80*7)))
lineHeight(None)
###############################################################

############################################## Toren-Mono page 2
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
text("Style Name: Mono", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Year: 2014", (128+32, 704-32))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("11pt", (-1, 704-(512)))

txt_line_one="""CLOCKWORK"""
txt_line_two="""HELLO WORLD"""
txt_line_five="""Emacs Hypertext"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer. That train of thought led to my computer system called METAFONT, which I want to try to show you now. Here is the way I finally desided to create the letter A, for example, using a computer program."""

font("Toren-Mono")
fontSize(72)
tracking(-2)
lineHeight(50)

textBox(txt_line_one, (-1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(-1)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 421))
textBox(txt_line_six, (0, -32, 520, (421-32)-16))
textBox(txt_line_seven, (0, -32, 520, (421-64)-32))
textBox(txt_line_eight, (0, -32, 520, (421-96)-48))
lineHeight(None)

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_ten, (0, -32, 420, 205))
lineHeight(None)

###############################################################

######################################### Toren-Rotalic -- page 1
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
text("Style Name: Rotalic", (-1, 704-32))
text("Units Per Em: 1000", (128+32, 704-16))
text("Year: 2014", (128+32, 704-32))
text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))
text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""
txt_line_eight="""!?ß&*,.;:"""

font("Toren-Rotalic")
fontSize(72)
tracking(2)
lineHeight(50)
textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))
textBox(txt_line_three, (-2, -32, 520, 628-(80*2)))
textBox(txt_line_four, (-2, -32, 520, 628-(80*3)))
textBox(txt_line_five, (0, -32, 520, 628-(80*4)))
textBox(txt_line_six, (0, -32, 520, 628-(80*5)))
textBox(txt_line_seven, (-6, -32, 520, 628-(80*6)))
textBox(txt_line_eight, (-6, -32, 520, 628-(80*7)))
lineHeight(None)
###############################################################

############################################## Toren-Rotalic page 2
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
text("Style Name: Rotalic", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Year: 2014", (128+32, 704-32))

text("Repo: github.com/eliheuer/Toren", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("11pt", (-1, 704-(512)))

txt_line_one="""Mathematical"""
txt_line_two="""Improvements"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer. That train of thought led to my computer system called METAFONT, which I want to try to show you now. Here is the way I finally desided to create the letter A, for example, using a computer program."""

font("Toren-Rotalic")
fontSize(72)
tracking(1)
lineHeight(50)

textBox(txt_line_one, (-1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(1)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 421))
textBox(txt_line_six, (0, -32, 520, (421-32)-16))
textBox(txt_line_seven, (0, -32, 520, (421-64)-32))
textBox(txt_line_eight, (0, -32, 520, (421-96)-48))
lineHeight(None)

fontSize(11)
tracking(1)
lineHeight(14)
textBox(txt_line_ten, (0, -32, 290, 205))
lineHeight(None)

###############################################################

####################################################### behrens
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
text("Revival: Behrens Antiqua", (-1, 704-16))
text("Foundry: Klingspor", (-1, 704-32))

text("Designer: Peter Behrens", (128+32, 704-16))
text("Year: 1907", (128+32, 704-32))

text("github.com/eliheuer/behrens-antiqua", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijklmn"""
txt_line_five="""opqrstuvwxyz"""
txt_line_six="""1234567890"""
txt_line_seven="""&*?!ß"""

font("BehrensAntiqua-Regular")
fontSize(72)
tracking(2)
lineHeight(50)

ba_pos = 624
textBox(txt_line_one, (1, -32, 520, ba_pos))
textBox(txt_line_two, (-2, -32, 520, ba_pos-80))
textBox(txt_line_three, (-2, -32, 520, ba_pos-(80*2)))
textBox(txt_line_four, (-2, -32, 520, ba_pos-(80*3)))
textBox(txt_line_five, (0, -32, 520, ba_pos-(80*4)))
textBox(txt_line_six, (0, -32, 520, ba_pos-(80*5)))
textBox(txt_line_seven, (-6, -32, 520, ba_pos-(80*6)))
lineHeight(None)
###############################################################

################################################ behrens
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

text("Revival: Behrens Antiqua", (-1, 704-16))
text("Foundry: Klingspor", (-1, 704-32))

text("Designer: Peter Behrens", (128+32, 704-16))
text("Year: 1907", (128+32, 704-32))

text("github.com/eliheuer/behrens-antiqua", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))


text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("11pt", (-1, 704-(512)))

txt_line_one="""Mathematical"""
txt_line_two="""Improvements"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer. That train of thought led to my computer system called METAFONT, which I want to try to show you now. Here is the way I finally desided to create the letter A, for example, using a computer program."""

font("BehrensAntiqua-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (-1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 421))
textBox(txt_line_six, (0, -32, 520, (421-32)-16))
textBox(txt_line_seven, (0, -32, 520, (421-64)-32))
textBox(txt_line_eight, (0, -32, 520, (421-96)-48))
lineHeight(None)

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_ten, (0, -32, 320, 205))
lineHeight(None)

###############################################################

####################################################### upm 256
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
text("Family Name: UPM256", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 256", (128+32, 704-16))
text("Year: 2015", (128+32, 704-32))

text("Repo: github.com/eliheuer/upm256", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJK"""
txt_line_two="""LMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""   """

font("UPM256-Regular")
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
lineHeight(None)
###############################################################

################################################ upm 256
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
text("Family Name: UPM256", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 256", (128+32, 704-16))
text("Year: 2015", (128+32, 704-32))

text("Repo: github.com/eliheuer/upm256", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))


text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("11pt", (-1, 704-(512)))

txt_line_one="""Mathematical"""
txt_line_two="""Improvements"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer. That train of thought led to my computer system called METAFONT, which I want to try to show you now. Here is the way I finally desided to create the letter A, for example, using a computer program."""

font("UPM256-Regular")
fontSize(72)
tracking(0.5)
lineHeight(50)

textBox(txt_line_one, (-1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(0.5)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 421))
textBox(txt_line_six, (0, -32, 520, (421-32)-16))
textBox(txt_line_seven, (0, -32, 520, (421-64)-32))
textBox(txt_line_eight, (0, -32, 520, (421-96)-48))
lineHeight(None)

fontSize(11)
tracking(0.5)
lineHeight(7)
textBox(txt_line_ten, (0, -32, 300, 205))
lineHeight(None)
           
###############################################################

############################################### Isotherma-Alpha
newPage()

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
lineHeight(None)
stroke(None)
text("Family Name: Isotherma", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Release Date: 2014", (128+32, 704-32))

text("Repo: github.com/eliheuer/isotherma", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-((80*5)+32)))

txt_line_one="""CEFGHKOPRT"""
txt_line_two="""abcdefghijklmnop"""
txt_line_three="""qrstuvwxy"""
txt_line_four="""X"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""

font("Isotherma-Alpha")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))
textBox(txt_line_three, (-2, -32, 520, 628-(80*2)))
textBox(txt_line_four, (32, -32, 520, 628-(80*3)))

font("Isotherma-Alpha")
fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 260))
textBox(txt_line_six, (0, -32, 520, (260-32)-16))
textBox(txt_line_seven, (0, -32, 520, (260-64)-32))
textBox(txt_line_eight, (0, -32, 520, (260-96)-48))
textBox(txt_line_nine, (0, -32, 520, (260-128)-64))
lineHeight(None)
###############################################################

###################################################### Heuer NU
newPage()

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
lineHeight(None)
stroke(None)
text("Name: Heuer Schrift", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/HeuerSchrift", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-((80*5)+32)))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQR"""
txt_line_three="""STUVWXYZ"""
txt_line_four="""1234567890"""
txt_line_five="""EMACS HYPERTEXT RENDERING"""
txt_line_six="""GEODESIC HAPPY HARDCORE"""
txt_line_seven="""TSCHICHOLDIAN ALGORITHMS"""
txt_line_eight="""OPEN BEAUTIFUL DOCUMENT"""
txt_line_nine="""FUNCTIONAL PROGRAMMING LANGUAGE"""

font("HeuerSchrift-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (1, -32, 520, 628-80))
textBox(txt_line_three, (1, -32, 520, 628-(80*2)))
textBox(txt_line_four, (1, -32, 520, 628-(80*3)))

font("HeuerSchrift-Regular")
fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 260))
textBox(txt_line_six, (0, -32, 520, (260-32)-16))
textBox(txt_line_seven, (0, -32, 520, (260-64)-32))
textBox(txt_line_eight, (0, -32, 520, (260-96)-48))
textBox(txt_line_nine, (0, -32, 520, (260-128)-64))
lineHeight(None)
###############################################################

############################################### moves nu update
newPage()

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
lineHeight(None)
stroke(None)
text("Family Name: Moves", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Release Date: 2011", (128+32, 704-32))

text("Repo: github.com/eliheuer/moves", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-((80*5)+32)))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""1234567890"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""

font("Nu-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (0, -32, 520, 628))
textBox(txt_line_two, (0, -32, 520, 628-80))
textBox(txt_line_three, (0, -32, 520, 628-(80*2)))
textBox(txt_line_four, (0, -32, 520, 628-(80*3)))

font("Nu-Regular")
fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 260))
textBox(txt_line_six, (0, -32, 520, (260-32)-16))
textBox(txt_line_seven, (0, -32, 520, (260-64)-32))
textBox(txt_line_eight, (0, -32, 520, (260-96)-48))
textBox(txt_line_nine, (0, -32, 520, (260-128)-64))
lineHeight(None)
###############################################################

############################################### fony update
newPage()

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
lineHeight(None)
stroke(None)
text("Family Name: Fony", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/fony", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-((80*5)+32)))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""1234567890"""
txt_line_five="""EMACS HYPERTEXT"""
txt_line_six="""GEODESIC HAPPY HARDCORE"""
txt_line_seven="""TSCHICHOLDIAN ALGORITHMS"""
txt_line_eight="""OPEN BEAUTIFUL DOCUMENTS"""
txt_line_nine="""FUNCTIONAL PROGRAMMING"""

font("Fony-Bold")
fontSize(72)
tracking(1)
lineHeight(50)

textBox(txt_line_one, (0, -32, 520, 628))
textBox(txt_line_two, (0, -32, 520, 628-80))
textBox(txt_line_three, (0, -32, 520, 628-(80*2)))
textBox(txt_line_four, (0, -32, 520, 628-(80*3)))

font("Fony-Bold")
fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 260))
textBox(txt_line_six, (0, -32, 520, (260-32)-16))
textBox(txt_line_seven, (0, -32, 520, (260-64)-32))
textBox(txt_line_eight, (0, -32, 520, (260-96)-48))
textBox(txt_line_nine, (0, -32, 520, (260-128)-64))
lineHeight(None)
###############################################################

############################################### MMXIMedium-Regular
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
text("Family Name: MMXI", (-1, 704-16))
text("Style Name: Medium", (-1, 704-32))

text("Units Per Em: 2048", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/MMXI", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("MMXIMedium-Regular")
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
lineHeight(None)
###############################################################

################################################ MMXIMedium-Regular
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
text("Family Name: MMXI", (-1, 704-16))
text("Style Name: Medium", (-1, 704-32))

text("Units Per Em: 2048", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/MMXI", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("12pt", (-1, 704-(512+(16+32))))

txt_line_one="""Mathematical"""
txt_line_two="""Artificial"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer."""
txt_line_eleven="""Functional programming language"""

font("MMXIMedium-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 422))
textBox(txt_line_six, (0, -32, 520, (422-32)-16))
textBox(txt_line_seven, (0, -32, 520, (422-64)-32))
textBox(txt_line_eight, (0, -32, 520, (422-96)-48))
textBox(txt_line_nine, (0, -32, 520, (422-128)-64))
lineHeight(None)

fontSize(12)
tracking(0)
lineHeight(15)
textBox(txt_line_ten, (0, -32, 380, 156))
lineHeight(None)
           
###############################################################

######################################  MMXIMediumOblique-Regular
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
text("Family Name: MMXI", (-1, 704-16))
text("Style Name: Med Oblique", (-1, 704-32))

text("Units Per Em: 2048", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/MMXI", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("MMXIMediumOblique-Regular")
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
lineHeight(None)
###############################################################

###################################  #MMXIMediumOblique-Regular
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
text("Family Name: MMXI", (-1, 704-16))
text("Style Name: Med Oblique", (-1, 704-32))

text("Units Per Em: 2048", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/MMXI", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("12pt", (-1, 704-(512+(16+32))))

txt_line_one="""Mathematical"""
txt_line_two="""Artificial"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming language"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer."""
txt_line_eleven="""Functional programming language"""

font("MMXIMediumOblique-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 422))
textBox(txt_line_six, (0, -32, 520, (422-32)-16))
textBox(txt_line_seven, (0, -32, 520, (422-64)-32))
textBox(txt_line_eight, (0, -32, 520, (422-96)-48))
textBox(txt_line_nine, (0, -32, 520, (422-128)-64))
lineHeight(None)

fontSize(12)
tracking(0)
lineHeight(15)
textBox(txt_line_ten, (0, -32, 380, 156))
lineHeight(None)
           
###############################################################

######################################  MMXIBlack-Regular
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
text("Family Name: MMXI", (-1, 704-16))
text("Style Name: Black", (-1, 704-32))

text("Units Per Em: 2048", (128+32, 704-16))
text("Release Date: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/MMXI", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four="""abcdefghijk"""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("MMXIBlack-Regular")
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
lineHeight(None)
###############################################################

############################################  MMXIBlack-Regular
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
text("Family Name: MMXI", (-1, 704-16))
text("Style Name: Black", (-1, 704-32))

text("Units Per Em: 2048", (128+32, 704-16))
text("Year: 2013", (128+32, 704-32))

text("Repo: github.com/eliheuer/MMXI", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-(256+16)))
text("12pt", (-1, 704-(512+(16+32))))

txt_line_one="""Mathematical"""
txt_line_two="""Artificial"""
txt_line_five="""Emacs Hypertext Rendering"""
txt_line_six="""Geodesic Happy Hardcore"""
txt_line_seven="""Tschicholdian algorithms"""
txt_line_eight="""Open beautiful documents"""
txt_line_nine="""Functional programming"""
txt_line_ten="""Finally, a simple thought struck me. Those letters were designed by people. If I could understand what those people had in their minds when they were drawing the letters, then I could program a computer to carry out the same ideas. Instead of merely copying the form of the letters, my new goal was therefore to copy the intelligence underlying that form. I decided to learn what type designers knew, and to teach that knowledge to a computer."""
txt_line_eleven="""Functional programming language"""

font("MMXIBlack-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 422))
textBox(txt_line_six, (0, -32, 520, (422-32)-16))
textBox(txt_line_seven, (0, -32, 520, (422-64)-32))
textBox(txt_line_eight, (0, -32, 520, (422-96)-48))
textBox(txt_line_nine, (0, -32, 520, (422-128)-64))
lineHeight(None)

fontSize(12)
tracking(0)
lineHeight(15)
textBox(txt_line_ten, (0, -32, 380, 156))
lineHeight(None)
###############################################################

############################################### ashley update
newPage()

# grid
translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# type 
fontSize(12)
font("Helvetica Neue Bold")
tracking(0)
fill(0.1, 0.1, 0.1)
lineHeight(None)
stroke(None)
text("Family Name: Ashley", (-1, 704-16))
text("Style Name: Regular", (-1, 704-32))

text("Units Per Em: 1000", (128+32, 704-16))
text("Release Date: 2014", (128+32, 704-32))

text("Repo: None", (256+64, 704-16))
text("License: None", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-((80*5)+32)))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four=""" """
txt_line_five="""THIS FONT WAS"""
txt_line_six="""DESIGNED BY ASHLEY"""
txt_line_seven="""IN A WORKSHOP"""
txt_line_eight="""ELI TAUGHT AT"""
txt_line_nine="""POWRPLNT"""

font("Ashley'sFont-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (0, -32, 520, 628))
textBox(txt_line_two, (0, -32, 520, 628-80))
textBox(txt_line_three, (0, -32, 520, 628-(80*2)))
textBox(txt_line_four, (0, -32, 520, 628-(80*3)))

font("Ashley'sFont-Regular")
fontSize(36)
tracking(0)
lineHeight(12)
textBox(txt_line_five, (0, -32, 520, 260))
textBox(txt_line_six, (0, -32, 520, (260-32)-16))
textBox(txt_line_seven, (0, -32, 520, (260-64)-32))
textBox(txt_line_eight, (0, -32, 520, (260-96)-48))
textBox(txt_line_nine, (0, -32, 520, (260-128)-64))
lineHeight(None)
###############################################################

######################################  colophone
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
text("Info:", (-1, 704-16))
text("git repo here: https://github.com/eliheuer/type-specimens", (-1, 704-96))

###############################################################

saveImage([u"~/type/type-specimens/Eli_Heuer_Type_Specimen.pdf",])
