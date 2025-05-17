# Small-File-Merger
Merge .jpg, .jpeg, and .pdf files into one clean, high-resolution PDF — across Windows, macOS, and Linux

> - Simple yet powerful Python script to combine `.jpg`, `.jpeg`, and `.pdf` files into a single, clean, high-resolution PDF.
> - Works seamlessly across **Windows**, **macOS**, and **Linux**.
> - Preserves the original file structure and ensures accurate file order.
> - Automatically cleans up temporary files after merging.
> - Features a colorful command-line interface for an engaging user experience.
> - Avoids duplicate file processing to keep the merge clean.
> - Ideal for organizing scanned documents, compiling reports, or creating photo albums effortlessly.

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)  


## Features

- ✅ Merge `.jpg`, `.jpeg`, and `.pdf` files into a **single PDF**
- 🎨 Beautiful, colorful CLI using `pyfiglet` and `rich`
- 🧹 Automatically cleans up temporary `.temp.pdf` files
- 🪟 Cross-platform support (macOS, Windows, Linux)
- 📁 Keeps original file structure and order intact


## How to Use

1. Clone this repository or download the `merge_files.py` script.  
   Run:  
   `git clone https://github.com/daniyyell-dev/Small-File-Merger.git`
   
2. Requirements

>  Python 3.7 or newer is required.  
>  Run:  
>  `pip3 install -r requirements.txt`

3. Run the script in your terminal:  
   `python3 /Small-File-Merger/merge_files.py`

4. Follow the on-screen prompts:

- Enter the **full path** to the folder containing your files.
- Enter your desired **output PDF filename**.

The script will:

- Convert all `.jpg` and `.jpeg` files to temporary PDFs
- Merge them with any `.pdf` files found in the folder
- Clean up the temporary `.temp.pdf` files after merging
- Save the combined result as a high-resolution PDF in the same folder

## Troubleshooting

- Ensure you’re using **Python 3.7+**
- Only `.jpg`, `.jpeg`, and `.pdf` files are supported
- Confirm that image files are not corrupted
- Ensure files aren’t being used by another program during execution

## Contributing

Want to make this tool even better? Contributions are welcome!

Ideas for improvement:

- Add support for `.png` and more formats
- Create a GUI version using `tkinter` or `PyQt`
- Add compression options for smaller output size
- Add Docker container support

## To contribute:

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit changes: `git commit -am 'Add feature'`  
4. Push to the branch: `git push origin feature-name`  
5. Open a pull request  


