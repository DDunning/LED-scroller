import NeoPixel


# TODO - create a wide buffer, write into it, on show, copy a section to the NeoPixel
# Add a scroll function.

class Buffer(NeoPixel.NeoPixel):



    def plotPoint(self, x, y, colour ):
        # clip to the visible area of the LED display
        if (0 <= x < self.numberOfCols) and (0 <= y < self.numberOfRows):
            offset = (y * self.numberOfCols) + x
            self.pixels_set(offset, colour)

    def plotGlyph(self, leftX, topY, colour, glyph):
        for y in range(0, 10):
            for x in range(0, 8):
                isLit = (glyph[y] << x) & 0x80
                if isLit:
                    self.plotPoint( leftX + x, topY + y, colour)

