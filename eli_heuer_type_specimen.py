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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Wristwatch"""
txt_line_two="""Render-farm"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more. GNU will be able to run Unix programs, but will not be identical to Unix. We will make all improvements that are convenient, based on our experience with other operating systems. In particular, we plan to have longer file names, file version numbers, a crashproof file system, file name completion perhaps, terminal-independent display support, and perhaps eventually a Lisp-based window system through which several Lisp programs and ordinary Unix programs can share a screen."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future. The main significance of this approach is that new symbols can readily be added in such a way that they are automatically consistent with the old ones."""

font("Toren-Proportional")
fontSize(72)
tracking(0)
lineHeight(50)
hyphenation(True)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_three, (0, 0, 256-8, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256-8, (16*26)-4))
           
###############################################################

########################################## toren mono -- page 1
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
txt_line_four="""abcdefghij"""
txt_line_five="""klmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("Toren-Mono")
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
lineHeight(None)
###############################################################

########################################## toren mono -- page 2
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""CLOCKWORK"""
txt_line_two="""Hello World"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more. GNU will be able to run Unix programs, but will not be identical to Unix. We will make all improvements that are convenient, based on our experience with other operating systems. In particular, we plan to have longer file names, file version numbers, a crashproof file system, file name completion perhaps, terminal-independent display support, and perhaps eventually a Lisp-based window system through which several Lisp programs and ordinary Unix programs can share a screen."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future. The main significance of this approach is that new symbols can readily be added in such a way that they are automatically consistent with the old ones."""

font("Toren-Mono")
fontSize(72)
tracking(2)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(14)
hyphenation(True)
textBox(txt_line_three, (0, 0, 256, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256, (16*26)-4))
###############################################################

###################################### toren rotalic --  page 1
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

font("Toren-Rotalic")
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

################################################ Rotalic page 2
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Polyominoes"""
txt_line_two="""Common Lisp"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it.(1) Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc-compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future. The main significance of this approach is that new symbols can readily be added in such a way that they are automatically consistent with the old ones."""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("Toren-Rotalic")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_three, (0, 0, 256, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256, (16*26)-4))
           
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Wristwatch Nano"""
txt_line_two="""Render-farm"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc-compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future. The main significance of this approach is that new symbols can readily be added in such a way that they are automatically consistent with the old ones."""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("BehrensAntiqua-Regular")
fontSize(72)
tracking(0)
hyphenation(True)
lineHeight(50)

ba_pos = 624
textBox(txt_line_one, (1, -32, 520, ba_pos))
textBox(txt_line_two, (-2, -32, 520, ba_pos-80))

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_three, (0, 0, 256, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256, (16*26)-4))
           
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Kowloon Nano"""
txt_line_two="""Denim Courier"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc-compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future."""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("UPM256-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(7)
hyphenation(True)
textBox(txt_line_three, (0, -6, 256, (16*26)-4))
textBox(txt_line_four, (288, -6, 256, (16*26)-4))
           
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
text("Family Name: fony", (-1, 704-16))
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Wristwatch"""
txt_line_two="""Render-farm"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc-compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future."""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("MMXIMedium-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_three, (0, 0, 256, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256, (16*26)-4))
           
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Wristwatch"""
txt_line_two="""Render-farm"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc-compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future."""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("MMXIMediumOblique-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_three, (0, 0, 256, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256, (16*26)-4))
           
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
text("11pt", (-1, 704-(256+16)))

txt_line_one="""Wristwatch"""
txt_line_two="""Render-farm"""
txt_line_three="""GNU, which stands for Gnu's Not Unix, is the name for the complete Unix-compatible software system which I am writing so that I can give it away free to everyone who can use it. Several other volunteers are helping me. Contributions of time, money, programs and equipment are greatly needed. So far we have an Emacs text editor with Lisp for writing editor commands, a source level debugger, a yacc-compatible parser generator, a linker, and around 35 utilities. A shell (command interpreter) is nearly completed. A new portable optimizing C compiler has compiled itself and may be released this year. An initial kernel exists but many more features are needed to emulate Unix. When the kernel and compiler are finished, it will be possible to distribute a GNU system suitable for program development. We will use TeX as our text formatter, but an nroff is being worked on. We will use the free, portable X Window System as well. After this we will add a portable Common Lisp, an Empire game, a spreadsheet, and hundreds of other things, plus online documentation. We hope to supply, eventually, everything useful that normally comes with a Unix system, and more."""
txt_line_four="""Mathematics books and journals do not look as beautiful as they used to. It is not that their mathematical content is unsatisfactory, rather that the old and well-developed traditions of typesetting have become too expensive. Fortunately, it now appears that mathematics itself can be used to solve this problem. A first step in the solution is to devise a method for unambiguously specifying mathematical manuscripts in such a way that they can easily be manipulated by machines. Such languages, when properly designed, can be learned quickly by authors and their typists, yet manuscripts in this form will lead directly to high quality plates for the printer with little or no human intervention. A second step in the solution makes use of classical mathematics to design the shapes of the letters and symbols themselves. It is possible to give a rigorous definition of the exact shape of the letter "a", for example, in such a way that infinitely many styles (bold, extended, sans-serif, italic, etc.) are obtained from a single definition by changing only a few parameters. When the same is done for the other letters and symbols, we obtain a mathematical definition of type fonts, a definition that can be used on all machines both now and in the future."""
txt_line_five="""lmnopqrs"""
txt_line_six="""tuvwxyz"""
txt_line_seven="""1234567890"""

font("MMXIBlack-Regular")
fontSize(72)
tracking(0)
lineHeight(50)

textBox(txt_line_one, (1, -32, 520, 628))
textBox(txt_line_two, (-2, -32, 520, 628-80))

fontSize(11)
tracking(0)
lineHeight(14)
textBox(txt_line_three, (0, 0, 256, (16*26)-4))
lineHeight(14)
textBox(txt_line_four, (288, 0, 256, (16*26)-4))
           
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
text("Release Date: 2011", (128+32, 704-32))

text("Repo: github.com/eliheuer/moves", (256+64, 704-16))
text("License: SIL Open Font License v1.1", (256+64, 704-32))

text("72pt", (-1, 704-80))
text("36pt", (-1, 704-((80*5)+32)))

txt_line_one="""ABCDEFGHIJ"""
txt_line_two="""KLMNOPQRS"""
txt_line_three="""TUVWXYZ"""
txt_line_four=""" """
txt_line_five="""THIS FONT WAS"""
txt_line_six="""DESIGNED BY"""
txt_line_seven="""ASHLEY W"""
txt_line_eight="""IN A WORKSHOP"""
txt_line_nine="""AT POWRPLNT"""

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
