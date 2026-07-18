<div align="center">

# 🚩 Hanumanji Line-by-Line Sketch 🚩

### Watch a devotional portrait emerge stroke by stroke with Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF8C00?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![Pillow](https://img.shields.io/badge/Imaging-Pillow-00A86B?style=for-the-badge)](https://pillow.readthedocs.io/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-8A2BE2?style=for-the-badge)](#-installation)
[![Made by DcodeVerse](https://img.shields.io/badge/Made%20by-DcodeVerse-111111?style=for-the-badge)](https://github.com/ayuxhh4you)

**जय हनुमान • JAI HANUMAN**

</div>

---

<div align="center">

## 🖼️ Final Artwork

![Hanumanji final sketch](assets/final_output.png)

*The exact image revealed after the line-by-line animation completes.*

</div>

---

## 📑 Table of contents

- [About the project](#-about-the-project)
- [Features](#-features)
- [Animation flow](#-animation-flow)
- [Installation](#-installation)
- [Controls](#%EF%B8%8F-controls)
- [Customization](#-customize-the-drawing)
- [Project structure](#-project-structure)
- [Technical details](#-technical-details)
- [Troubleshooting](#%EF%B8%8F-troubleshooting)
- [FAQ](#-frequently-asked-questions)

## ✨ About the project

This Python desktop animation recreates a Hanumanji portrait on a clean white fullscreen canvas. It traces prepared artwork paths one batch at a time, layering a soft grey pencil guide beneath crisp black strokes. When every line is complete, the sketch is replaced by the exact high-quality final artwork.

The result combines the feeling of watching a hand-drawn sketch with a clean, accurate final reveal.

## 🔥 Features

- **Line-by-line animation** builds the complete portrait progressively.
- **79 prepared drawing paths** reproduce the artwork accurately.
- **Dual-stroke technique** combines a soft pencil guide with a sharp final line.
- **Smooth rounded paths** use curved joins and rounded caps.
- **Exact final-image reveal** appears after the sketch animation finishes.
- **Fullscreen presentation** automatically fits the current display.
- **Aspect-ratio preservation** prevents the artwork from stretching.
- **High-quality resizing** uses Pillow's LANCZOS resampling.
- **Adjustable speed and stroke widths** are available near the top of the script.
- **Simple keyboard exit** closes the experience with `Esc`.
- **One-click Windows launcher** installs Pillow and starts the app.

### Feature overview

| Category | Implementation |
|---|---|
| Drawing style | Animated pencil-to-ink line sketch |
| Canvas | Fullscreen, borderless white Tkinter canvas |
| Path source | 79 vector-like coordinate paths from JSON |
| Source coordinate space | `1918 × 1078` |
| Guide stroke | Soft grey, width `2` |
| Final stroke | Near-black, width `1` |
| Rendering batch | 3 paths per frame by default |
| Final reveal delay | 900 milliseconds |
| Image scaling | Aspect-ratio-preserving LANCZOS resize |
| Exit control | `Esc` |

## 🎬 Animation flow

```text
Fullscreen white canvas
        ↓
Soft grey pencil guides
        ↓
Clean black sketch lines
        ↓
All 79 paths completed
        ↓
Exact final artwork revealed
```

## 📦 Installation

### Requirements

- Python 3.9 or newer recommended
- Tkinter, normally included with Python on Windows
- Pillow
- A desktop environment capable of opening a Tkinter window

### Clone from GitHub

```bash
git clone https://github.com/ayuxhh4you/hanumanji_line_by_line_final_output_project.git
cd hanumanji_line_by_line_final_output_project
```

### Windows

The easiest option is to double-click `run_windows.bat`. It installs Pillow, launches the animation, and keeps the terminal open after the program closes.

Manual PowerShell setup:

```powershell
py -m pip install -r requirements.txt
py main.py
```

### macOS

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

> Some macOS Python distributions may require a separate Tk-enabled Python installation.

### Linux

Install Tkinter first when it is not already present. On Debian or Ubuntu:

```bash
sudo apt install python3-tk
python3 -m pip install -r requirements.txt
python3 main.py
```

### Generic terminal commands

```bash
pip install -r requirements.txt
python main.py
```

On Windows, you can instead double-click:

```text
run_windows.bat
```

The animation starts automatically after a 500-millisecond preparation delay.

## ⌨️ Control

| Key | Action |
|---|---|
| `Esc` | Close the fullscreen animation |

## 🎨 Customize the drawing

Open `main.py` and adjust the settings near the top:

| Setting | Default | Purpose |
|---|---:|---|
| `PATHS_PER_FRAME` | `3` | Paths drawn during each animation step |
| `FRAME_DELAY` | `1` | Delay between batches in milliseconds |
| `LINE_WIDTH` | `1` | Thickness of the clean black line |
| `GUIDE_WIDTH` | `2` | Thickness of the soft grey guide |

For a slower, more visible sketching process:

```python
PATHS_PER_FRAME = 1
FRAME_DELAY = 8
```

For a faster result:

```python
PATHS_PER_FRAME = 8
FRAME_DELAY = 1
```

## 📁 Project structure

```text
hanumanji_line_by_line_final_output_project/
├── assets/
│   └── final_output.png    # Exact artwork shown after the animation
├── data/
│   └── paths.json         # 79 prepared paths at 1918 × 1078 coordinates
├── main.py                # Tkinter animation and image-reveal logic
├── requirements.txt       # Pillow dependency
├── run_windows.bat        # One-click Windows launcher
└── README.md              # Project documentation
```

> Keep the `assets` and `data` folders in place. The program loads both files relative to `main.py`.

## 🧠 How it works

1. Tkinter creates a borderless fullscreen canvas.
2. Coordinate paths are loaded from `data/paths.json`.
3. Every coordinate is scaled and centered for the current screen.
4. Each path receives a wide grey guide and a narrow black line.
5. Tkinter's `after()` method schedules batches without freezing the interface.
6. Pillow prepares the final image at the largest size that fits the display.
7. After a short pause, the canvas switches to the exact finished artwork.

## ⚙️ Technical details

### Coordinate mapping

The stored paths use the source artwork's `1918 × 1078` coordinate space. At startup, the program calculates independent horizontal and vertical scale factors:

```text
screen point = centered offset + source point × scale factor
```

Because the final image is resized while preserving its aspect ratio, every animated line stays aligned with the final reveal on displays of different sizes.

### Non-blocking animation

The renderer does not use a long blocking loop. Tkinter's `after()` scheduler draws a small batch, returns control to the interface, and schedules the next batch. This keeps the fullscreen window responsive enough to receive the `Esc` key while drawing.

### Two-pass stroke rendering

Every path is rendered twice:

1. A wider `#d6d6d6` line simulates a light pencil guide.
2. A narrow `#050505` line creates the clean final outline.

Both passes use rounded caps, rounded joins, and Tkinter smoothing.

### Final image handling

Pillow loads `assets/final_output.png`, converts it to RGB, and resizes it with LANCZOS resampling. The image is centered without cropping or changing its proportions. Once all paths finish, the canvas is cleared and the prepared image is displayed.

## 🔗 Data format

`data/paths.json` contains:

```json
{
  "width": 1918,
  "height": 1078,
  "paths": [
    [[0, 0], [1, 1]]
  ]
}
```

- `width` and `height` define the original coordinate space.
- `paths` is a collection of point sequences.
- Each point is an `[x, y]` pair.
- Paths with fewer than two points are safely ignored.

The example above only demonstrates the structure; the included file contains the complete 79-path artwork.

## 🛠️ Troubleshooting

**Pillow is missing**  
Run `pip install -r requirements.txt`, or use `py -m pip install pillow` on Windows.

**`python` is not recognized**  
Install Python from [python.org](https://www.python.org/downloads/) and enable **Add Python to PATH**, or use the Windows `py` launcher.

**The data or image file cannot be found**  
Keep `data/paths.json` and `assets/final_output.png` in their original folders beside `main.py`.

**The animation finishes too quickly**  
Set `PATHS_PER_FRAME = 1` and increase `FRAME_DELAY`.

**The window covers the whole screen**  
That is the intended presentation. Press `Esc` to exit.

**The final image looks stretched or cropped**  
The included code preserves its aspect ratio. Make sure you are running the unmodified `main.py` and original asset.

**The sketch and final image do not align**  
Use the included `paths.json` and `final_output.png` together. They were prepared for the same `1918 × 1078` source coordinate space.

## ❓ Frequently asked questions

### Does the program trace the PNG live?

No. The drawing animation uses prepared coordinates from `data/paths.json`. The PNG is loaded separately and shown only during the final reveal.

### Can I replace the final image?

Replacing only the PNG will make the animation and reveal inconsistent. A new image also needs matching path data with the correct source width and height.

### Can I run it in a browser?

Not directly. This is a Python desktop application built with Tkinter. It needs a local Python environment and desktop display.

### Does it need an internet connection?

Only the initial Pillow installation may require internet access. After the dependency is installed, the project runs locally.

### Can I make it windowed instead of fullscreen?

Yes. In `main.py`, replace:

```python
self.root.attributes("-fullscreen", True)
```

with a window size such as:

```python
self.root.geometry("1280x720")
```

### How do I replay the animation?

The current version has no replay key. Close it with `Esc` and launch `main.py` again.

## 🤝 Contributing

Ideas and improvements are welcome. A typical contribution flow is:

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Commit with a clear message.
5. Open a pull request describing the improvement.

Please keep the original artwork paths, final reveal, and fullscreen exit behavior working unless your change intentionally replaces them.

## 📤 Upload this project to GitHub

```powershell
git init
git add -A
git commit -m "Add Hanumanji line-by-line sketch project"
git branch -M main
git remote add origin https://github.com/ayuxhh4you/hanumanji_line_by_line_final_output_project.git
git push -u origin main
```

---

<div align="center">

Created with devotion, Python, Tkinter, and Pillow 🚩

**जय बजरंगबली**

⭐ Star the repository if you enjoy this project!

</div>
