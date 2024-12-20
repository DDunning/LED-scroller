# On a Waveshare NEO Pixel display, show a scrolling message.
#
import sys
import time
from Font12 import Font12
from GraphicsBuffer import Buffer

message = "Hello"

if __name__=='__main__':
    strip = Buffer()
    font = Font12()
    color1 = 0
    color2 = 15
    num1 = 0
    num2 = 1
    num3 = 15

    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()

    #strip.plotPoint(0, 0, strip.WHITE)
    #strip.plotPoint(15, 0, strip.RED)
    #strip.plotPoint(0, 9, strip.GREEN)
    #strip.plotPoint(15, 9, strip.BLUE)
    #strip.pixels_show()

    # 0x00_00_00_01 = blue
    # 0x00_00_01_00 = red
    # 0x00_01_00_00 = green
    # 0x01_00_00_00 = (nothing)
    #strip.pixels_raw(0x01000000)

    while True:
        for leftEdge in range(130):
            strip.pixels_fill(strip.BLACK)
            #strip.plotGlyph(16                     - leftEdge, -1, strip.CYAN, font.H)
            #strip.plotGlyph(16 + font.Width        - leftEdge, -1, strip.CYAN, font.a)
            #strip.plotGlyph(16 + (font.Width *  2) - leftEdge, -1, strip.CYAN, font.p)
            #strip.plotGlyph(16 + (font.Width *  3) - leftEdge, -1, strip.CYAN, font.p)
            #strip.plotGlyph(16 + (font.Width *  4) - leftEdge, -1, strip.CYAN, font.y)

            #strip.plotGlyph(16 + (font.Width *  6) - leftEdge, -1, strip.YELLOW, font.N)
            #strip.plotGlyph(16 + (font.Width *  7) - leftEdge, -1, strip.YELLOW, font.e)
            #strip.plotGlyph(16 + (font.Width *  8) - leftEdge, -1, strip.YELLOW, font.w)

            #strip.plotGlyph(16 + (font.Width * 10) - leftEdge, -1, strip.YELLOW, font.Y)
            #strip.plotGlyph(16 + (font.Width * 11) - leftEdge, -1, strip.YELLOW, font.e)
            #strip.plotGlyph(16 + (font.Width * 12) - leftEdge, -1, strip.YELLOW, font.a)
            #strip.plotGlyph(16 + (font.Width * 13) - leftEdge, -1, strip.YELLOW, font.r)

            strip.plotGlyph(16 + (font.Width *  1) - leftEdge, -1, strip.RED, font.M)
            strip.plotGlyph(16 + (font.Width *  2) - leftEdge, -1, strip.RED, font.e)
            strip.plotGlyph(16 + (font.Width *  3) - leftEdge, -1, strip.RED, font.r)
            strip.plotGlyph(16 + (font.Width *  4) - leftEdge, -1, strip.RED, font.r)
            strip.plotGlyph(16 + (font.Width *  5) - leftEdge, -1, strip.RED, font.y)

            strip.plotGlyph(16 + (font.Width *  7) - leftEdge, -1, strip.RED, font.C)
            strip.plotGlyph(16 + (font.Width *  8) - leftEdge, -1, strip.RED, font.h)
            strip.plotGlyph(16 + (font.Width *  9) - leftEdge, -1, strip.RED, font.r)
            strip.plotGlyph(16 + (font.Width * 10) - leftEdge, -1, strip.RED, font.i)
            strip.plotGlyph(16 + (font.Width * 11) - leftEdge, -1, strip.RED, font.s)
            strip.plotGlyph(16 + (font.Width * 12) - leftEdge, -1, strip.RED, font.t)
            strip.plotGlyph(16 + (font.Width * 13) - leftEdge, -1, strip.RED, font.m)
            strip.plotGlyph(16 + (font.Width * 14) - leftEdge, -1, strip.RED, font.a)
            strip.plotGlyph(16 + (font.Width * 15) - leftEdge, -1, strip.RED, font.s)
            
            strip.pixels_show()
            #time.sleep(0.005)
        #dummy = input('Press Enter to continue..')
        strip.pixels_fill(strip.BLACK)
        strip.pixels_show()

    print('Done.')
    sys.exit(0)
    
##############
    print(Font12.H()[2] )

    print("chases")

    for color in range(0,160):          
        strip.color_chase(strip.COLORS[color%2], color)
        if (color+1)%16 == 0 or (color+1)%160 == 0:
            strip.pixels_show()
            time.sleep(0.05)
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)
    
    for color in range(159,-1,-1):             
        strip.color_chase(strip.COLORS[color%3], color)
        if color%16 ==0 or color%144 == 0:
            print((color)%15)
            strip.pixels_show()
            time.sleep(0.05)
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)

    for color in range(0,160):
        print("color1:",color1)
        strip.color_chase(strip.COLORS[color%4], color1)
        color1 += 16
        if color1 > 159:
            num1 +=1
            if num1 == 17:
                num1=0
            color1 = num1
        if  color1/num2 == 1 or num1/16 == 1 :
            num2 += 1
            if num2 >16:
                num2=2
            strip.pixels_show()
            time.sleep(0.05)
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)

    for color in range(0,160):
        strip.color_chase(strip.COLORS[color%5], color2)
        color2 += 16
        if color2 > 159:
            num3 -=1
            if num3 < 0:
                num3=15
            color2 = num3
        print("num3:",num3)
        if  color2-1 == num3-1:
            strip.pixels_show()
            time.sleep(0.05)

    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)    
    color1 = 0
    num1 = 0
    num2 = 1       
    for color in range(0,160):
        strip.color_chase(strip.BLACK, color1)
        color1 += 16
        if color1 > 159:
            num1 +=1
            if num1 == 17:
                num1=0
            color1 = num1
        if  color1/num2 == 1 or num1/16 == 1 :
            num2 += 1
            if num2 >16:
                num2=2
            strip.pixels_show()
       
    for color in range(0,160):
        strip.color_chase(strip.lattice[color], color)
    strip.pixels_show()
    time.sleep(1.0)
    print("rainbow")
    while(1):
        strip.rainbow_cycle(0.2)    
