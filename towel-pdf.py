import tqdm
import tkinter as tk
from tkinter import filedialog
import pdfplumber
from transformers import pipeline

# Initialize the question answering pipeline
nlp = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

# Initialize a summarization pipeline
summarizer = pipeline("summarization")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(self)
        self.open_button["text"] = "Open File"
        self.open_button["command"] = self.open_file
        self.open_button.pack(side="top")

        self.text_area = tk.Text(self, height=10)
        self.text_area.pack(side="top")

        self.chat_area = tk.Text(self, height=10)
        self.chat_area.pack(side="top")

        self.chat_input = tk.Entry(self)
        self.chat_input.pack(side="left")

        self.send_button = tk.Button(self)
        self.send_button["text"] = "Send"
        self.send_button["command"] = self.send_message
        self.send_button.pack(side="left")

        self.decrement_button = tk.Button(self)
        self.decrement_button["text"] = "<"
        self.decrement_button["command"] = self.decrement
        self.decrement_button.pack(side="left")

        self.chunk_size_label = tk.Label(self, text="Chunk size:")
        self.chunk_size_label.pack(side="left")

        self.chunk_size_value = tk.IntVar()
        self.chunk_size_value.set(150)

        self.chunk_size_input = tk.Label(self, textvariable=self.chunk_size_value)
        self.chunk_size_input.pack(side="left")

        self.increment_button = tk.Button(self)
        self.increment_button["text"] = ">"
        self.increment_button["command"] = self.increment
        self.increment_button.pack(side="left")

        self.summarize_button = tk.Button(self)
        self.summarize_button["text"] = "Summarize"
        self.summarize_button["command"] = self.summarize
        self.summarize_button.pack(side="top")

        self.summary_area = tk.Text(self, height=10)
        self.summary_area.pack(side="top")

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes = (("PDF files","*.pdf"),("all files","*.*")))
        if filename:
            self.display_pdf(filename)

    def display_pdf(self, filename):
        global text
        with pdfplumber.open(filename) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, text)

    def send_message(self):
        question = self.chat_input.get()
        if question:
            answer = nlp({
                'question': question,
                'context': text
            })
            self.chat_area.insert(tk.END, "You: " + question + '\n\n')
            self.chat_area.insert(tk.END, "AI: " + answer['answer'] + '\n\n')
            self.chat_input.delete(0, tk.END)

    def decrement(self):
        self.chunk_size_value.set(max(0, self.chunk_size_value.get() - 10))

    def increment(self):
        self.chunk_size_value.set(self.chunk_size_value.get() + 10)

    def summarize(self):
        # Get the chunk size from the chunk_size_value variable
        chunk_size = self.chunk_size_value.get()

        # Get the text from the text_area widget
        text = self.text_area.get("1.0", tk.END)

        # Split the text into chunks
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

        # Initialize an empty string to hold the summary
        summary = ""

        # Process each chunk
        for chunk in chunks:
            # Set max_length to the chunk size
            max_length = chunk_size

            # Generate the summary for the current chunk
            result = summarizer(chunk, max_length=max_length, min_length=40, do_sample=False)

            # Add the summary of the current chunk to the overall summary
            summary += result[0]['summary_text'] + " "

        # Display the summary in the summary_area widget
        self.summary_area.delete("1.0", tk.END)
        self.summary_area.insert(tk.END, summary)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
