import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
 
 
# open the files on the system using tk
def open_local_file():
    if save_file_entry.get() == '':
        messagebox.showerror("Error", "Save file entry cannot be empty")
        return
    filepaths = filedialog.askopenfilenames(filetypes=[('Image files', '*.png'), ('Image files', '*jpeg')])
    print('filepath: ', filepaths)
    convert_file(filepaths)
 
 
def get_save_path():
    filepath = filedialog.askdirectory()
    save_file_entry.insert(0, filepath)
 
 
def convert_file(filepaths):
    for file in filepaths:
        with Image.open(file).convert('RGBA') as image:
            imsize = image.size
            imname = file.split('/')[-1]
            print(imname)
            txt = Image.new('RGBA', imsize, (255, 255, 255, 0))
            font = ImageFont.truetype('FREESCPT.TTF', 20)
            draw = ImageDraw.Draw(txt)
            watermark_text = watermark_entry.get()
            draw.text((imsize[0] - 100, imsize[1] - 50),
                      text=watermark_text, fill=(255, 255, 255, 185), font=font)
            marked_im = Image.alpha_composite(image, txt)
            save_file_1(marked_im, imname)
 
 
def save_file_1(image, imname):
    image.convert('RGB')
    image.save(f"{save_file_entry.get()}/{imname}")
 
 
# ----------------------- UI --------------------- #
window = tk.Tk()
window.title('Watermarking App')
window.config(padx=50, pady=50)
 
logo = tk.PhotoImage(file='img.png')
my_canvas = tk.Canvas(width=400, height=200)
my_canvas.create_image(300, 100, image=logo)
my_canvas.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))
 
watermark_label = tk.Label(text='Watermark:  ')
watermark_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
 
watermark_entry = tk.Entry(width=50)
watermark_entry.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))
watermark_entry.insert(0, "LCF Inc.")
 
save_file = tk.Button(text='save path', command=get_save_path)
save_file.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
 
save_file_entry = tk.Entry(width=50)
save_file_entry.grid(row=2, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))
 
upload_button = tk.Button(text='Upload', command=open_local_file)
upload_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))
 
window.mainloop()import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
 
 
# open the files on the system using tk
def open_local_file():
    if save_file_entry.get() == '':
        messagebox.showerror("Error", "Save file entry cannot be empty")
        return
    filepaths = filedialog.askopenfilenames(filetypes=[('Image files', '*.png'), ('Image files', '*jpeg')])
    print('filepath: ', filepaths)
    convert_file(filepaths)
 
 
def get_save_path():
    filepath = filedialog.askdirectory()
    save_file_entry.insert(0, filepath)
 
 
def convert_file(filepaths):
    for file in filepaths:
        with Image.open(file).convert('RGBA') as image:
            imsize = image.size
            imname = file.split('/')[-1]
            print(imname)
            txt = Image.new('RGBA', imsize, (255, 255, 255, 0))
            font = ImageFont.truetype('FREESCPT.TTF', 20)
            draw = ImageDraw.Draw(txt)
            watermark_text = watermark_entry.get()
            draw.text((imsize[0] - 100, imsize[1] - 50),
                      text=watermark_text, fill=(255, 255, 255, 185), font=font)
            marked_im = Image.alpha_composite(image, txt)
            save_file_1(marked_im, imname)
 
 
def save_file_1(image, imname):
    image.convert('RGB')
    image.save(f"{save_file_entry.get()}/{imname}")
 
 
# ----------------------- UI --------------------- #
window = tk.Tk()
window.title('Watermarking App')
window.config(padx=50, pady=50)
 
logo = tk.PhotoImage(file='img.png')
my_canvas = tk.Canvas(width=400, height=200)
my_canvas.create_image(300, 100, image=logo)
my_canvas.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))
 
watermark_label = tk.Label(text='Watermark:  ')
watermark_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
 
watermark_entry = tk.Entry(width=50)
watermark_entry.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))
watermark_entry.insert(0, "LCF Inc.")
 
save_file = tk.Button(text='save path', command=get_save_path)
save_file.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
 
save_file_entry = tk.Entry(width=50)
save_file_entry.grid(row=2, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))
 
upload_button = tk.Button(text='Upload', command=open_local_file)
upload_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))
 
window.mainloop()