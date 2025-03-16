import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageEnhance, ImageDraw
import requests
from io import BytesIO
import threading
import time

# Set appearance mode and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main window
root = ctk.CTk()
root.title("Netflix Clone")
root.geometry("1200x700")
root.resizable(False, False)

# Sample data with TMDB poster URLs
movies = {
    "Action": [
        {"title": "The Dark Knight", "image": "https://image.tmdb.org/t/p/w500/1hRoyzDtpgMU7Dz4JF22RANzQO7.jpg"},
        {"title": "Mad Max: Fury Road", "image": "https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg"},
        {"title": "John Wick", "image": "https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3t7r.jpg"}
    ],
    "Comedy": [
        {"title": "The Hangover", "image": "https://image.tmdb.org/t/p/w500/jjCzf8gi70RJW7eA1VN7xfb4ZfR.jpg"},
        {"title": "Superbad", "image": "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2Epx5n2v7sylCSL.jpg"},
        {"title": "Deadpool", "image": "https://image.tmdb.org/t/p/w500/xrGydPD6QSXch4sZxoO7kXf0xdC.jpg"}
    ],
    "Drama": [
        {"title": "The Shawshank Redemption", "image": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
        {"title": "Forrest Gump", "image": "https://image.tmdb.org/t/p/w500/saHP97rXYjJ57L8KIF3OQXv40v2.jpg"},
        {"title": "The Godfather", "image": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"}
    ]
}

# Sidebar frame
sidebar = ctk.CTkFrame(root, width=200, corner_radius=0)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Netflix logo
logo_label = ctk.CTkLabel(sidebar, text="NETFLIX", font=("Arial", 24, "bold"), text_color="red")
logo_label.pack(pady=20)

# Sidebar menu
menu_items = ["Home", "TV Shows", "Movies", "New & Popular", "My List"]
for item in menu_items:
    btn = ctk.CTkButton(sidebar, text=item, fg_color="transparent", text_color="white",
                        font=("Arial", 14), anchor="w", command=lambda x=item: print(f"Selected: {x}"))
    btn.pack(fill=tk.X, padx=10, pady=5)

# Main content frame
content_frame = ctk.CTkFrame(root, corner_radius=0)
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Top bar
top_bar = ctk.CTkFrame(content_frame, height=60, corner_radius=0)
top_bar.pack(fill=tk.X)

search_entry = ctk.CTkEntry(top_bar, placeholder_text="Search", width=300)
search_entry.pack(side=tk.LEFT, padx=10, pady=10)

profile_btn = ctk.CTkButton(top_bar, text="Profile", width=100, command=lambda: print("Profile clicked"))
profile_btn.pack(side=tk.RIGHT, padx=10, pady=10)

# Scrollable content area
canvas = tk.Canvas(content_frame, bg="#212121", highlightthickness=0)
scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, corner_radius=0)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Function to load images from URL
def load_image_from_url(url, size=(200, 100)):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img), img
    except Exception as e:
        print(f"Error loading image from {url}: {e}")
        img = Image.new("RGB", size, "gray")
        return ImageTk.PhotoImage(img), img

# Pre-render animation frames with glow within original size
def pre_render_frames(original_img):
    frames = []
    steps = 8
    base_size = (200, 100)
    for i in range(steps + 1):
        scale = 1.0 - (0.1 * i / steps)  # Scale down slightly to fit glow (90% max)
        brightness = 0.8 + (0.4 * i / steps)  # Max 120% brightness
        inner_size = (int(base_size[0] * scale), int(base_size[1] * scale))
        
        # Create base image with brightness
        enhanced_img = ImageEnhance.Brightness(original_img).enhance(brightness)
        resized_img = enhanced_img.resize(inner_size, Image.Resampling.LANCZOS)
        
        # Create glow layer within original size
        glow_img = Image.new("RGBA", base_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(glow_img)
        glow_intensity = int(150 * (i / steps))  # Fade in glow
        draw.rectangle(
            [5, 5, base_size[0] - 5, base_size[1] - 5],
            outline=(255, 0, 0, glow_intensity),
            width=2
        )
        
        # Center the resized image on the glow layer
        offset = ((base_size[0] - inner_size[0]) // 2, (base_size[1] - inner_size[1]) // 2)
        glow_img.paste(resized_img, offset)
        frames.append(ImageTk.PhotoImage(glow_img))
    return frames

# Animation functions
def animate_hover(btn, frames, title_label, enter=True):
    def run_animation():
        if enter:
            for frame in frames:
                btn.configure(image=frame)
                btn.image = frame
                title_label.configure(font=("Arial", 14, "bold"))
                root.update_idletasks()
                time.sleep(0.025)
        else:
            for frame in reversed(frames):
                btn.configure(image=frame)
                btn.image = frame
                title_label.configure(font=("Arial", 12))
                root.update_idletasks()
                time.sleep(0.025)

    def start_animation():
        if not hasattr(btn, "animating") or not btn.animating:
            btn.animating = True
            threading.Thread(target=run_animation, daemon=True).start()
            root.after(200, lambda: setattr(btn, "animating", False))

    start_animation()

def animate_click(btn, original_img):
    def run_animation():
        pressed_size = (180, 90)
        pressed_img = original_img.resize(pressed_size, Image.Resampling.LANCZOS)
        pressed_photo = ImageTk.PhotoImage(pressed_img)
        btn.configure(image=pressed_photo, fg_color="#e50914")
        btn.image = pressed_photo
        root.update_idletasks()
        time.sleep(0.1)

        normal_photo = ImageTk.PhotoImage(original_img)
        btn.configure(image=normal_photo, fg_color="transparent")
        btn.image = normal_photo
        root.update_idletasks()

    threading.Thread(target=run_animation, daemon=True).start()

# Populate content
row = 0
for category, movie_list in movies.items():
    cat_label = ctk.CTkLabel(scrollable_frame, text=category, font=("Arial", 18, "bold"))
    cat_label.grid(row=row, column=0, columnspan=3, pady=(20, 5), sticky="w")
    row += 1
    
    col = 0
    for movie in movie_list:
        photo, pil_img = load_image_from_url(movie["image"])
        animation_frames = pre_render_frames(pil_img)
        btn_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent", width=200, height=120)  # Fixed size frame
        btn_frame.grid(row=row, column=col, padx=5, pady=5)

        btn = ctk.CTkButton(btn_frame, image=photo, text="", fg_color="transparent",
                           width=200, height=100, corner_radius=5,
                           command=lambda m=movie["title"], b=btn, i=pil_img: [print(f"Play: {m}"), animate_click(b, i)])
        btn.image = photo
        btn.pack()

        title_label = ctk.CTkLabel(btn_frame, text=movie["title"], font=("Arial", 12), text_color="white")
        title_label.pack(pady=(2, 0))

        btn.bind("<Enter>", lambda e, b=btn, f=animation_frames, l=title_label: animate_hover(b, f, l, True))
        btn.bind("<Leave>", lambda e, b=btn, f=animation_frames, l=title_label: animate_hover(b, f, l, False))

        col += 1
        if col > 2:
            col = 0
            row += 1
    row += 1

# Mouse wheel scrolling
def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Run the application
root.mainloop()