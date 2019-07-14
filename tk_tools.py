
def color_to_tk(color):
    return '#{}{}{}'.format(*["{0:#0{1}x}".format(el, 4).replace("0x", "") for el in color])
