import cv2


def create_certificate(img, name):
    copy_img = img.copy()
    position = (715, 715)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 3.5
    font_color = (51, 51, 52)
    font_thickness = 7
    cv2.putText(copy_img, name, position, font, font_size, font_color, font_thickness)
    return copy_img


def save_img(copy_img, name):
    path = "certi-{}.jpg".format(name)
    cv2.imwrite(path, copy_img)


img = cv2.imread('CertificateTemplate.png')

name = input("write your name: ")
copy_img = create_certificate(img, name)
save_img(copy_img, name)
