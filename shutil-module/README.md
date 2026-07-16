# 📦 shutil Module Practice

This folder contains practice programs for Python's built-in **`shutil`** module. The programs demonstrate common file and directory operations such as copying, moving, deleting, archiving, and extracting files and folders.

---

## 📚 Topics Covered

- Copying files using `shutil.copy()`
- Copying files with metadata using `shutil.copy2()`
- Moving and renaming files using `shutil.move()`
- Deleting directories using `shutil.rmtree()`
- Checking disk usage using `shutil.disk_usage()`
- Creating ZIP archives using `shutil.make_archive()`
- Extracting ZIP archives using `shutil.unpack_archive()`
- Copying entire directories using `shutil.copytree()`
- Working with file paths using `os.path.join()`
- Listing files using `os.listdir()`
- Creating directories using `os.makedirs()`

---

## 📁 File Structure

```
shutil-module/
│── copy_file.py
│── move_file.py
│── rename_file.py
│── delete_folder.py
│── disk_usage.py
│── create_backup.py
│── extract_archive.py
│── folder_copier.py
│── copy_txt_files.py
│── move_images.py
│── README.md
```

---

## ⚙️ Prerequisites

Some programs require sample files and folders before execution.

Create the following structure (or a similar one) for testing:

```
shutil-module/
│
├── Project/
│   ├── notes.txt
│   ├── report.pdf
│   ├── image1.png
│   ├── image2.jpg
│   └── sample.txt
│
├── Documents/
├── Images/
└── TempFolder/
```

> **Note:** These sample files and folders are **not included** in this repository because they were created only for practice and testing purposes.

---

## 🚀 How to Run

1. Create the required sample files and folders.
2. Open a terminal in the project directory.
3. Run any program using:

```bash
python filename.py
```

Example:

```bash
python copy_file.py
```

---

## 🎯 Key Learnings

- Performed high-level file and directory operations using the `shutil` module.
- Learned the difference between `copy()`, `copy2()`, and `copytree()`.
- Understood how `move()` can also be used for renaming files.
- Created and extracted ZIP archives.
- Checked disk usage programmatically.
- Combined the `os` and `shutil` modules to solve practical file-management tasks.
- Practiced writing platform-independent paths using `os.path.join()`.
- Learned to create directories safely using `os.makedirs()`.

---

## ⚠️ Common Mistakes

- Using `copy()` instead of `copytree()` for directories.
- Forgetting to create the destination folder before moving files.
- Providing incorrect file paths.
- Forgetting the `.zip` extension while extracting archives.
- Assuming `copy()` preserves metadata (use `copy2()` instead).

---

## 📝 Notes

These programs are written for learning and practice purposes. Temporary files and folders used during development have been removed to keep the repository clean. If you wish to execute the programs, create the required sample files and folders as described in the **Prerequisites** section.

---

## 💻 Technologies Used

- Python 3.x
- `shutil` module
- `os` module