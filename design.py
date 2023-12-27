import tkinter as tk
from PIL import Image, ImageTk

TEXTCOLOR = "black"
BACKGROUND = "#c3e1eb"
WIDGET_BACKGROUND = "#ADD8E6"

window = tk.Tk()
window.geometry("1000x500")
window.title("Instagram Reposter")
# window.resizable(True, True)
window.resizable(False, False)
window.configure(bg = BACKGROUND)

# TODO: make the window full-screen friendly
# window.bind('<Escape>', lambda e: window.state('normal'))
# window.bind('<F11>', lambda e: window.state('zoomed'))

# canvas init
canvas = tk.Canvas(window, width = 1000, height = 500, bg = BACKGROUND)
canvas.pack()

# pfp
pfp = Image.open("assets\\pfp.png")
pfp = pfp.resize((50, 50))
pfp = ImageTk.PhotoImage(pfp)
canvas.create_image(75, 25, anchor = 'nw', image = pfp)

# username
name = "ThisIsAMemeAccount"
canvas.create_text(220, 50, text = f"@{name}", fill = TEXTCOLOR, font = ('Helvetica 13'))

# likes
likes = Image.open("assets\\likes.png")
likes = likes.resize((50, 50))
likes = ImageTk.PhotoImage(likes)
canvas.create_image(800, 25, anchor = 'ne', image = likes)

likes_num = 10000
canvas.create_text(775, 80, text = likes_num, fill = TEXTCOLOR, font = ('Helvetica 10 bold'))

# comments
comments = Image.open("assets\\comments.png")
comments = comments.resize((45, 50))
comments = ImageTk.PhotoImage(comments)
canvas.create_image(865, 25, anchor = 'ne', image = comments)

comments_num = 69690
canvas.create_text(841.5, 80, text = comments_num, fill = TEXTCOLOR, font = ('Helvetica 10 bold'))

# shares
shares = Image.open("assets\\shares.png")
shares = shares.resize((50, 33))
shares = ImageTk.PhotoImage(shares)
canvas.create_image(937, 34, anchor = 'ne', image = shares)

shares_num = 69420
canvas.create_text(910, 80, text = shares_num, fill = TEXTCOLOR, font = ('Helvetica 10 bold'))

# settings
def settingsClick(e):
    print("settings clicky")
    settingsWindow = tk.Tk()
    settingsWindow.geometry('850x450')
    settingsWindow.title("Settings - Instagram Reposter")
    settingsWindow.resizable(False, False)
    settingsWindow.configure(bg = WIDGET_BACKGROUND)

    settingsCanvas = tk.Canvas(settingsWindow, width = 850, height = 450, bg = "#add8e6")
    settingsCanvas.pack()

settings_img = Image.open("assets\\settings.png")
settings = settings_img.resize((35, 35))
settings = ImageTk.PhotoImage(settings)

rotated = settings_img.rotate(-100)
rotated = rotated.resize((35, 35))
rotated = ImageTk.PhotoImage(rotated)

settings_image = canvas.create_image(7, 7, anchor = 'nw', image = settings)

canvas.tag_bind(settings_image, '<Enter>', lambda enter: canvas.itemconfig(settings_image, image = rotated))
canvas.tag_bind(settings_image, '<Leave>', lambda leave: canvas.itemconfig(settings_image, image = settings))

canvas.tag_bind(settings_image, '<Button-1>', settingsClick)

# paginators
# left
def leftPaginatorClick(e):
    print("left paginator click")

left = Image.open("assets\\left.png")
left = left.resize((30, 50))
left = ImageTk.PhotoImage(left)
leftImg = canvas.create_image(25, 220, anchor = 'w', image = left)

canvas.tag_bind(leftImg, "<Button-1>", leftPaginatorClick)

# right
def rightPaginatorClick(e):
    print("right paginator click")

right = Image.open("assets\\right.png")
right = right.resize((30, 50))
right = ImageTk.PhotoImage(right)
rightImg = canvas.create_image(975, 220, anchor = 'e', image = right)

canvas.tag_bind(rightImg, "<Button-1>", rightPaginatorClick)

# image to post
image = Image.open("assets\\test.png")

image = image.resize((500, 285))
image = ImageTk.PhotoImage(image)
canvas.create_image(235, 90, anchor = "nw", image = image)

# caption
def captionClick():
    print("caption clicky")
    captionWindow = tk.Tk()
    captionWindow.geometry("850x450")
    captionWindow.title("Set Caption - Instagram Reposter")
    captionWindow.resizable(False, False)
    captionWindow.configure(bg = WIDGET_BACKGROUND)

    captionCanvas = tk.Canvas(captionWindow, width = 850, height = 450, bg = "#add8e6")
    captionCanvas.pack()

    editableCaptionHolder = tk.Text(captionCanvas, height = 26, width = 87, wrap = tk.WORD, state = tk.NORMAL)
    editableCaptionHolder.place(x = 10, y = 10)
    editableCaptionHolder.insert(tk.END, caption)

    def updateCaption():
        global newCaption
        newCaption = editableCaptionHolder.get("1.0", 'end-1c')

        captionHolder.config(state = tk.NORMAL)
        captionHolder.delete(1.0, tk.END)
        captionHolder.insert(tk.END, newCaption)
        captionHolder.config(state = tk.DISABLED)

    updateBtn = tk.Button(captionCanvas, text = "Update Caption", command = updateCaption)
    updateBtn.place(x = 730, y = 25)

canvas.create_text(80, 390, text = "Caption", fill = TEXTCOLOR, font = ('Helvetica 12 bold'))

caption = "here is some caption text"
captionHolder = tk.Text(canvas, height = 4, width = 90, wrap = tk.WORD, state = tk.DISABLED)
captionHolder.place(x = 50, y = 402)

captionHolder.config(state = tk.NORMAL)
captionHolder.insert(tk.END, caption)
captionHolder.config(state = tk.DISABLED)

captionHolder.bind("<ButtonPress-1>", lambda a: captionClick())

# post button
def post():
    print("possst the post")

postBtn = tk.Button(canvas, text = "POST", background = "darkgreen", foreground = "#ffffff",
                    height = 2, width = 20, command = post)
postWin = canvas.create_window(946, 435, anchor = "se", window = postBtn)

# delete button
def delete():
    print("delette poste")

deleteBtn = tk.Button(canvas, text = "DELETE", background = "darkred", foreground = "#ffffff",
                      height = 2, width = 20, command = delete)
deleteWin = canvas.create_window(946, 478, anchor = "se", window = deleteBtn)

window.mainloop()