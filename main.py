import cv2
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile, askopenfilename
from tkinter.filedialog import *
import datetime, random, time
import os

cwd = os.getcwd()

try:
    os.makedirs("images")
except FileExistsError:
    pass

root = Tk()

def sketch(fileinput):
    path = fileinput
    label2_info.config(text="Pending...", font=("Courier 13 bold"))
    img = cv2.imread(fileinput)

    plt.imshow(img)
    plt.axis(False)
    # plt.show()

    # METHOD 1
    plt.imshow(img[:,:,::-1])
    plt.axis(False)
    # plt.show()

    # METHOD 2
    RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(RGB_image)
    plt.axis(False)

    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    invert_img = cv2.bitwise_not(grey_img)
    #invert=255-grey_img

    blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

    invblur_img = cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    index = path.find(".")
    f_ext = path[index+1:]
    tan = random.randint(100, 10684)
    outfile = str("Sketchify_" + str(tan))# + f_ext)
    cv2.imwrite((f"images/{outfile}.{f_ext}"), sketch_img)

    # cv2.imshow("Original image", img)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    plt.title("Original Image", size=18)
    plt.imshow(RGB_image)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title("Sketch", size=18)
    rgb_sketch = cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis("off")
    plt.show()

def open_file():
    path = askopenfilename(title="Select an Image", filetypes=(("Portable Network Graphics","*.png"), ("Joint Photographic Experts Group", "*.jpg"), ("Joint Photographic Experts Group", "*.jpeg")))
    # date = datetime.datetime.now().strftime("%d/%m/%Y - %I:%M:%S %p")
    index = path.rfind("/")
    fname = path[index+1:]
    label_info.config(text=fname, font=("Courier 10 bold"))
    sketch(fileinput=path)
    label2_info.config(text="Complete", font=("Courier 13 bold"))
    

Label(root, text="SKETCHIFY", font=("Courier 20 bold")).pack(padx=100, pady=20)

wrapper1 = LabelFrame(root, text='File Input')
wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)

wrapper2 = LabelFrame(root, text='File Information')
wrapper2.pack(fill='both', expand='yes', padx=10, pady=10)


choose = Button(wrapper1, text="Select a File to Sketchify", command= lambda:open_file())
choose.grid(row=1, column=0, padx=20)

label2 = Label(wrapper2, text="Staus: ", font=("Courier 13 bold"))
label2.grid(row=0, column=0)

label2_info = Label(wrapper2, text="N/A", font=("Courier 13 bold"))
label2_info.grid(row=0, column=1)

label = Label(wrapper2, text="File name: ", font=("Courier 13 bold"))
label.grid(row=1, column=0)

label_info = Label(wrapper2, text="N/A", font=("Courier 13 bold"))
label_info.grid(row=1, column=1)

exit = Button(wrapper2, text="EXIT APP", command= lambda:root.quit())
exit.grid(row=2, column=1, padx=20)


root.geometry('380x300')
root.title("Sketchify")
# root.resizable(False, False)
# root.iconbitmap()
print(cwd)

root.mainloop()