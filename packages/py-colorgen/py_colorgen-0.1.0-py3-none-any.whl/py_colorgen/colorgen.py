import argparse
import random


parser = argparse.ArgumentParser(description="Random color combination generator")
parser.add_argument("-r",
                    "--rgb",
                    default=False,
                    action="count",
                    help="-r or --rgb to generate rgb color")
parser.add_argument("-s",
                    "--hsl",
                    default=False,
                    action="count",
                    help="-s or --hsl to generate hsl color")

args=parser.parse_args()


def colour_combination(rgb,hsl):
    """
    Generate a color combination
    """
    
    def rgb_colour():
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
        rgb= f"rgb{(r, g, b)}"
        return rgb
    
    def hsl_colour() :
        h = random.randint(0,360)
        s = "%s%%"%random.randint(0,100)
        l = "%s%%"%random.randint(0,100) 
        hsl =f"hsl({h},{s},{l})"
        return hsl
    
    
    def hex_colour():
        random_hex=random.randint(0,16777215)
        random_hex=hex(random_hex)       
        random_hex=random_hex.split("x")[1]        #remove "0" and "x" from start
        random_hex="".join("#"+random_hex)
        return random_hex
    
    
    if rgb:
        return rgb_colour()
    if hsl:
        return hsl_colour()
    else:
        return hex_colour()


if __name__ == '__main__':

    print(colour_combination(args.rgb,args.hsl))
    exit(0)
