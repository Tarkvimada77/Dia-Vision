from PIL import Image

# конвертируем bgr в rgb 
def dia_bgr(cortesh):
    cortesh = list(cortesh)
    for i in range(len(cortesh)):
        if cortesh[i] < 0:
            cortesh[i] = 0
        if cortesh[i] > 255:
            cortesh[i] = 255
    return tuple(cortesh)            


# проверяем пиксели на их серость
def pixel_cont(imago):
    img = Image.open(imago)

    pixels = list(img.getdata())
    final_res = []
    for i in pixels:
        if abs(i[0] - i[1] - i[2]) > 3 and not (abs(i[1] - i[2]) == 0 and abs(i[1] - i[0]) == 0) and (i[2], i[1], i[0]) not in final_res:

            result = (i[2], i[1], i[0])
            final_res.append(result)
    
    return final_res

# Генерация минимально допустимого значения пикселей
def create_min(cor):
    res = []
    for i in cor:
        res.append(i - 5)
    return dia_bgr(tuple(res))

# Генерация максимально допустимого значения пикселей
def create_max(cor):
    res = []
    for i in cor:
        res.append(i + 5)
    return dia_bgr(tuple(res))




# Переворачиваем изображение для удобной работы
def rotata(img):
    imaga = Image.open(img)

    img_rotata = imaga.rotate(180, expand=True) 

    img_rotata.save(img + "rotate" + ".png")

    return img + "rotate" + ".png"


