# 📜 Yeshiva Lessons Uploader (yeshiva_lessons)

This project is a helper script designed to streamline the process of uploading, renaming, and sorting lesson recordings for my Yeshiva's digital database. The main goal is to make the task more **efficient and semi-automated** for the person in charge.

The core script is named **`העלאת שיעורים.py`** (Lesson Upload), chosen to help the understanding of non-programmers people.

---

## 🌐 Designed for Accessibility (Hebrew UI)

This entire project, including the code structure and all user interface (UI) elements (seen in files like `העלאת שיעורים.py`), is written entirely in **Hebrew**. This design choice was made specifically to ensure that the script is **accessible and user-friendly** for individuals who are not professional programmers and whose primary language is Hebrew, allowing them to manage the lessons without needing to navigate an English-only interface.

## 🛠️ Functionality

The script manages the entire workflow through two main classes:
* **`Lesson`**: Defines the properties and file operations for a single lesson recording, treating the file with characteristics of a lesson.
* **`Editor`**: Manages the user interface and coordinates the editing process for multiple files in the edit field directory.

## 🚀 Future Enhancements

The script is a constantly evolving tool. Here are the planned upgrades:

* **Metadata Editing**: Edit the metadata of the `.mp3` file, to facilitate the parsing process of the info.
* **Smarter Indexing**: Implement a smarter indexing process in directories.
* **Automated Uploads**:
    * Upload automatically to the Yeshiva website.
    * Upload automatically to a Drive backup.
    * Upload automatically to Spotify.