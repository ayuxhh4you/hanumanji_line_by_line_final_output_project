import os
import json
import tkinter as tk
from PIL import Image, ImageTk

# ============================================================
# Hanumanji Line-by-Line Sketch Making Project
# DcodeVerse fixed version
#
# Flow:
# 1. White canvas opens
# 2. Sketch draws line-by-line from the final output image
# 3. Final clean output image appears exactly at the end
#
# Run:
#   pip install pillow
#   python main.py
#
# Press ESC to exit
# ============================================================

PATH_FILE = "data/paths.json"
FINAL_IMAGE = "assets/final_output.png"

# Speed controls
PATHS_PER_FRAME = 3      # higher = faster
FRAME_DELAY = 1          # milliseconds
LINE_WIDTH = 1           # final line thickness
GUIDE_WIDTH = 2          # soft grey first stroke

class LineByLineSketch:
    def __init__(self, root):
        self.root = root
        self.root.title("Hanumanji Python Sketch - DcodeVerse")
        self.root.configure(bg="white")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()

        self.canvas = tk.Canvas(root, width=self.sw, height=self.sh, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        base = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(base, PATH_FILE), "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.img = Image.open(os.path.join(base, FINAL_IMAGE)).convert("RGB")
        self.display = self.fit_image(self.img, self.sw, self.sh)
        self.final_photo = ImageTk.PhotoImage(self.display)

        self.src_w = self.data["width"]
        self.src_h = self.data["height"]
        self.dst_w, self.dst_h = self.display.size
        self.scale_x = self.dst_w / self.src_w
        self.scale_y = self.dst_h / self.src_h
        self.x0 = (self.sw - self.dst_w) / 2
        self.y0 = (self.sh - self.dst_h) / 2

        self.paths = self.data["paths"]
        self.index = 0

        self.root.after(500, self.draw_batch)

    def fit_image(self, img, max_w, max_h):
        scale = min(max_w / img.width, max_h / img.height)
        return img.resize((int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS)

    def map_point(self, p):
        x, y = p
        return self.x0 + x * self.scale_x, self.y0 + y * self.scale_y

    def draw_one_path(self, path):
        if len(path) < 2:
            return

        coords = []
        for p in path:
            coords.extend(self.map_point(p))

        # grey pencil guide
        self.canvas.create_line(
            *coords,
            fill="#d6d6d6",
            width=GUIDE_WIDTH,
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND,
            smooth=True
        )

        # clean black line
        self.canvas.create_line(
            *coords,
            fill="#050505",
            width=LINE_WIDTH,
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND,
            smooth=True
        )

    def draw_batch(self):
        end = min(self.index + PATHS_PER_FRAME, len(self.paths))

        for i in range(self.index, end):
            self.draw_one_path(self.paths[i])

        self.index = end

        if self.index < len(self.paths):
            self.root.after(FRAME_DELAY, self.draw_batch)
        else:
            self.root.after(900, self.final_reveal)

    def final_reveal(self):
        # exact final image appears
        self.canvas.delete("all")
        self.canvas.create_image(self.sw // 2, self.sh // 2, image=self.final_photo, anchor="center")
        print("Hanumanji line-by-line sketch completed.")

def main():
    root = tk.Tk()
    LineByLineSketch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
