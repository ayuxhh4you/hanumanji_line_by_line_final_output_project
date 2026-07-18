<div align="center">

# 🚩 Hanumanji Line-by-Line Sketch 🚩

### Watch a devotional portrait emerge stroke by stroke with Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF8C00?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![Pillow](https://img.shields.io/badge/Imaging-Pillow-00A86B?style=for-the-badge)](https://pillow.readthedocs.io/)

**जय हनुमान • JAI HANUMAN**

</div>

---

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

## 🚀 Quick start

### Requirements

- Python 3.x
- Tkinter, normally included with Python on Windows
- Pillow

### Clone from GitHub

```bash
git clone https://github.com/ayuxhh4you/hanumanji_line_by_line_final_output_project.git
cd hanumanji_line_by_line_final_output_project
```

### Install the dependency

```bash
pip install -r requirements.txt
```

### Start the animation

```bash
python main.py
```

On Windows, you can instead double-click:

```text
run_windows.bat
```

If `python` is not recognized on Windows, use:

```powershell
py -m pip install -r requirements.txt
py main.py
```

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

---

<div align="center">

Created with devotion, Python, Tkinter, and Pillow 🚩

**जय बजरंगबली**

⭐ Star the repository if you enjoy this project!

</div>
