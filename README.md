# 🧠🗞️ TagTheNews

**TagTheNews** is a smart AI-powered web app that classifies news headlines into relevant categories such as **politics**, **technology**, **sports**, **business**, and more — using zero-shot learning with Hugging Face Transformers. The app visualizes confidence levels and provides an elegant Gradio UI for user interaction.

![TagTheNews Screenshot](image/pic2.png)

---

## 🚀 Demo

🖥️ **Live App**: [https://huggingface.co/spaces/Ruusheka/TagTheNews](https://huggingface.co/spaces/Ruusheka/TagTheNews)

---

## 🛠️ Tech Stack

| Tool/Library         | Purpose                                    |
|----------------------|--------------------------------------------|
| 🐍 Python            | Core programming language                  |
| 🤗 Hugging Face Transformers | Zero-shot text classification (`facebook/bart-large-mnli`) |
| 🎨 Gradio            | Interactive frontend with custom CSS       |
| 📊 Matplotlib        | Plotting category confidence               |
| 🧠 Facebook BART     | Pretrained model for classification        |
| 🖼️ Custom CSS        | Beautiful animated frontend                |

---

## ⚙️ How It Works

1. The user inputs a **news headline or sentence**.
2. The app uses the `facebook/bart-large-mnli` model via Hugging Face's `pipeline("zero-shot-classification")` to:
   - Predict the **main category** of the text.
   - Score it against a predefined list of categories.
3. The app returns:
   - Main category and top alternatives with **confidence scores**.
   - A **bar chart** visualizing all category probabilities.
   - Custom HTML layout styled with **animated, glowing UI**.

---

## 📂 Folder Structure

```plaintext
TagTheNews/
├── app.py                  # Main Gradio app
├── requirements.txt        # Dependencies
├── assets/
│   └── pic4.png      # Screenshot of the app
├── README.md               # Project documentation
└── .gitignore
