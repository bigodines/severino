import Image
import numpy

class Compare(object):

    def are_equal(self, img_a, img_b):
        img_a = Image.open(img_a)
        img_b = Image.open(img_b)

        if img_a.size != img_b.size or img_a.getbands() != img_b.getbands():
            return False
    
        s = 0
        for band_index, band in enumerate(img_a.getbands()):
            m1 = numpy.array([p[band_index] for p in img_a.getdata()]).reshape(*img_a.size)
            m2 = numpy.array([p[band_index] for p in img_b.getdata()]).reshape(*img_b.size)
            s += numpy.sum(numpy.abs(m1-m2))
            
        print s
        return s == 0
