
from tkinter import *
from PIL import Image, ImageTk
from os import listdir
from tkinter import filedialog


def image_list(image_number):
    # global all_images_dict
    global list_dir_len
    global modified_image
    global list_dir

    list_dir = listdir(path)
    list_dir_len = len(list_dir)
    image = list_dir[image_number]
    if image[-3:] in ['jpg', 'JPG', 'png', 'PNG']:
        image_open = Image.open(f'{path}/{image}')
        image_size = image_open.size
        ratio = image_size[1] / image_size[0]
        new_width = 500 / ratio
        resize_image = image_open.resize((int(new_width), 500))
        modified_image = ImageTk.PhotoImage(resize_image)
    else:
        modified_image = ImageTk.PhotoImage(Image.open('alert.png'))
    return modified_image


def navigation_buttons():
    global button_back
    global button_forward

    # navigation buttons
    button_back = Button(
        root, text='<<', command=lambda: back_image())
    button_exit = Button(root, text='Exit', command=root.quit)
    button_forward = Button(
        root, text='>>', command=lambda: next_image())
    butto_open_folder = Button(root, text="open folder", command=open_folder)

    button_back.grid(column=0, row=2, padx=5, pady=5)
    butto_open_folder.grid(column=1, row=2, padx=5, pady=5)
    button_exit.grid(column=2, row=2)
    button_forward.grid(column=3, row=2, padx=5, pady=5)


def open_folder():
    global path
    path = filedialog.askdirectory()
    image_view(path)


def next_image():
    global image_number

    try:
        image_number += 1
        if image_number == list_dir_len:
            image_number = 0
        img_label.configure(image=image_list(image_number))
        label_file_name.configure(text=f'File name: {list_dir[image_number]}')
        label_total_images.configure(
            text=f'image no: {image_number+1} / {list_dir_len}')
    except:
        button_forward.configure(state=DISABLED)


def back_image():
    global image_number

    try:
        image_number -= 1
        if image_number < 0:
            image_number = list_dir_len-1
        img_label.configure(image=image_list(image_number))
        label_file_name.configure(text=f'File name: {list_dir[image_number]}')
        label_total_images.configure(
            text=f'image no: {image_number+1} / {list_dir_len}')
    except:
        button_back.configure(state=DISABLED)


def image_info():
    global label_file_name
    global label_total_images

    label_file_name = Label(
        root, text=f'File name: {list_dir[image_number]}', font=(16))
    label_file_name.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    label_total_images = Label(
        root, text=f'image no: {image_number+1} / {list_dir_len}', font=(16))
    label_total_images.grid(row=1, column=2, columnspan=2, padx=5, pady=5)


def image_view(path=''):
    global img_label
    global image_number

    image_number = 0
    if not path:
        navigation_buttons()
    else:
        img_label = Label(root, image=image_list(
            image_number), anchor=CENTER)
        img_label.grid(column=0, row=0, columnspan=4,
                       padx=20, pady=20)
        image_info()
        navigation_buttons()


root = Tk()
root.title('Image Viewer')

window_width = 1000
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'+{center_x}+{center_y}')

image_view()


root.mainloop()
