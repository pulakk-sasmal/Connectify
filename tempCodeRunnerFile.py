import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def show_page(page):
    for p in pages.values():
        p.pack_forget()
    pages[page].pack()

def like_post(post_id):
    # Add your like logic here for the specific post
    pass

def comment_post(post_id):
    # Add your comment logic here for the specific post
    pass

def share_post(post_id):
    # Add your share logic here for the specific post
    pass

root = tk.Tk()
root.title("iConnnect")
root.geometry("1000x600")

main_page = tk.Frame(root)
home_page = tk.Frame(root)
friends_page = tk.Frame(root)
messages_page = tk.Frame(root)
notifications_page = tk.Frame(root)

pages = {
    "Main": main_page,
    "Home": home_page,
    "Friends": friends_page,
    "Messages": messages_page,
    "Notifications": notifications_page,
}

show_page("Main")

header = tk.Label(root, text="CONNECTIFY connecting people 🪁", font=("Arial", 18), background="light blue", height=1, padx=20, pady=10, width=400)
header.pack()

navbar = tk.Frame(root)
navbar.pack()

home_image = Image.open("home.png")
home_image = home_image.resize((50, 50), Image.NEAREST)
home_image = ImageTk.PhotoImage(home_image)

friends_image = Image.open("friends.png")
friends_image = friends_image.resize((50, 50), Image.NEAREST)
friends_image = ImageTk.PhotoImage(friends_image)

messages_image = Image.open("messages.png")
messages_image = messages_image.resize((50, 50), Image.NEAREST)
messages_image = ImageTk.PhotoImage(messages_image)

notifications_image = Image.open("notifications.png")
notifications_image = notifications_image.resize((50, 50), Image.NEAREST)
notifications_image = ImageTk.PhotoImage(notifications_image)

button_width = 250

home_button = tk.Button(navbar, image=home_image, command=lambda: show_page("Home"), background="white", width=button_width)
friends_button = tk.Button(navbar, image=friends_image, command=lambda: show_page("Friends"), background="white", width=button_width)
messages_button = tk.Button(navbar, image=messages_image, command=lambda: show_page("Messages"), background="white", width=button_width)
notifications_button = tk.Button(navbar, image=notifications_image, command=lambda: show_page("Notifications"), background="white", width=button_width)

home_button.pack(side="left")
friends_button.pack(side="left")
messages_button.pack(side="left")
notifications_button.pack(side="left")

home_posts = tk.Text(home_page, wrap="word", font=("Arial", 17), width=50, height=100, padx=15)
home_posts.pack(padx=10, pady=10)

post1 = "\n😎 Walton_Smith - Motivation is all you need\n\n"
post2 = "👨 Elon_Musk - Another boring day at the office\n\n"
post3 = "🐶 Weed_Walker - Cool as I am\n\n"
home_posts.insert("end", post1)

image1 = Image.open("image1.png")
image1 = image1.resize((600, 400), Image.NEAREST)
image1 = ImageTk.PhotoImage(image1)
home_posts.insert("end", " " * 5)
home_posts.image_create("end", image=image1)
home_posts.insert("end", "\n\n\n")

home_posts.insert("end", post2)

image2 = Image.open("third_image.jpg")
image2 = image2.resize((600, 400), Image.NEAREST)
image2 = ImageTk.PhotoImage(image2)
home_posts.insert("end", " " * 5)
home_posts.image_create("end", image=image2)
home_posts.insert("end", "\n\n\n")

home_posts.insert("end", post3)

image3 = Image.open("another_image.jpg")
image3 = image3.resize((600, 700), Image.NEAREST)
image3 = ImageTk.PhotoImage(image3)
home_posts.insert("end", " " * 5)
home_posts.image_create("end", image=image3)
home_posts.insert("end", "\n")

# Like, Comment, and Share buttons for each post
like_button1 = tk.Button(home_page, text="Like", font=("Arial", 12), command=lambda: like_post(1))
comment_button1 = tk.Button(home_page, text="Comment", font=("Arial", 12), command=lambda: comment_post(1))
share_button1 = tk.Button(home_page, text="Share", font=("Arial", 12), command=lambda: share_post(1))
like_button1.pack()
comment_button1.pack()
share_button1.pack()

like_button2 = tk.Button(home_page, text="Like", font=("Arial", 12), command=lambda: like_post(2))
comment_button2 = tk.Button(home_page, text="Comment", font=("Arial", 12), command=lambda: comment_post(2))
share_button2 = tk.Button(home_page, text="Share", font=("Arial", 12), command=lambda: share_post(2))
like_button2.pack()
comment_button2.pack()
share_button2.pack()

like_button3 = tk.Button(home_page, text="Like", font=("Arial", 12), command=lambda: like_post(3))
comment_button3 = tk.Button(home_page, text="Comment", font=("Arial", 12), command=lambda: comment_post(3))
share_button3 = tk.Button(home_page, text="Share", font=("Arial", 12), command=lambda: share_post(3))
like_button3.pack()
comment_button3.pack()
share_button3.pack()

friends_list = tk.Listbox(friends_page)
friends = ["👩‍🦰 Walton Smith", "😎 Chris Gayle", "🥸 Mitron Modi", "👲 Adolf Hitler", "👧 Anchal Rai", "😎 Joseph Stalin", "🥺 Genghis khan"]
friend_buttons = []
for friend in friends:
    button = tk.Button(friends_page, text=friend, font=("arial", 17), background="white", width=20)
    friend_buttons.append(button)

for button in friend_buttons:
    button.pack(fill=tk.X, pady=10)

messages_text = tk.Text(messages_page, wrap="word", font=("Arial", 17), width=50, height=14, padx=15, pady=15)
messages_text.insert("1.0", "🧑‍🦱Me: Hi there!\n\n👩‍🦰Priyanshi: How are you?\n\n🧑‍🦱Me: I'm good. Are you still busy!")
messages_text.grid(row=0, column=0, columnspan=2, pady=10)

entry = tk.Entry(messages_page, font=("Arial", 18), width=40)
entry.grid(row=1, column=0, pady=8)

def send_message():
    message = entry.get()
    if message:
        messages_text.insert("end", f"\n\nMe: {message}")
        entry.delete(0, "end")

send_button = tk.Button(messages_page, text="Send➡️", font=("Arial", 16), command=send_message, background="sky blue")
send_button.grid(row=1, column=1, pady=8)

notifications_label = tk.Label(notifications_page, text="No new notifications", font=("arial", 20))
notifications_label.pack(pady=50)

root.mainloop()
