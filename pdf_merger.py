# FLEET TIME ENGINEERING PDF MERGER CREATED BY PAUL ADDISON

import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger 2")
        self.root.geometry("400x600")  # Set the window size to 400px wide and 600px tall

        self.file1_path = ""
        self.file2_path = ""

        self.create_widgets()

    def create_widgets(self):
        # Input fields
        self.label_project = tk.Label(self.root, text="Enter Project Number:")
        self.label_project.pack(pady=5)

        self.entry_project = tk.Entry(self.root, width=40)
        self.entry_project.pack(pady=5)

        self.label_activity = tk.Label(self.root, text="Enter Activity Number:")
        self.label_activity.pack(pady=5)

        self.entry_activity = tk.Entry(self.root, width=40)
        self.entry_activity.pack(pady=5)

        self.label_mt = tk.Label(self.root, text="Enter MT Number:")
        self.label_mt.pack(pady=5)

        self.entry_mt = tk.Entry(self.root, width=40)
        self.entry_mt.pack(pady=5)

        self.label_lead_trade = tk.Label(self.root, text="Enter Lead Trade:")
        self.label_lead_trade.pack(pady=5)

        self.entry_lead_trade = tk.Entry(self.root, width=40)
        self.entry_lead_trade.pack(pady=5)

        # File 1
        self.label_file1 = tk.Label(self.root, text="Select first PDF file:")
        self.label_file1.pack(pady=5)

        self.button_browse_file1 = tk.Button(self.root, text="Browse", command=self.browse_file1)
        self.button_browse_file1.pack(pady=5)

        self.label_file1_path = tk.Label(self.root, text="", wraplength=350)
        self.label_file1_path.pack(pady=5)

        # File 2
        self.label_file2 = tk.Label(self.root, text="Select second PDF file:")
        self.label_file2.pack(pady=5)

        self.button_browse_file2 = tk.Button(self.root, text="Browse", command=self.browse_file2)
        self.button_browse_file2.pack(pady=5)

        self.label_file2_path = tk.Label(self.root, text="", wraplength=350)
        self.label_file2_path.pack(pady=5)

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        # Merge button
        self.button_merge = tk.Button(self.buttons_frame, text="Merge PDFs", command=self.merge_pdfs)
        self.button_merge.grid(row=0, column=0, padx=5)

        # Clear button
        self.button_clear = tk.Button(self.buttons_frame, text="Clear", command=self.clear_inputs)
        self.button_clear.grid(row=0, column=1, padx=5)

        # Close button
        self.button_close = tk.Button(self.buttons_frame, text="Close", command=self.root.quit)
        self.button_close.grid(row=0, column=2, padx=5)

    def browse_file1(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file1_path = file_path
            self.label_file1_path.config(text=self.file1_path)

    def browse_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file2_path = file_path
            self.label_file2_path.config(text=self.file2_path)

    def merge_pdfs(self):
        if not self.file1_path or not self.file2_path:
            messagebox.showerror("Error", "Please select both PDF files.")
            return

        project = self.entry_project.get().strip()
        activity = self.entry_activity.get().strip()
        mt = self.entry_mt.get().strip()
        lead_trade = self.entry_lead_trade.get().strip()

        if not project or not activity or not mt or not lead_trade:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        output_filename = f"{project}-{activity}-{mt}-{lead_trade}.pdf"
        output_path = filedialog.asksaveasfilename(initialfile=output_filename, defaultextension=".pdf",
                                                   filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return

        try:
            pdf_writer = PyPDF2.PdfWriter()

            for file_path in [self.file1_path, self.file2_path]:
                pdf_reader = PyPDF2.PdfReader(file_path)
                for page in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page])

            with open(output_path, "wb") as output_file:
                pdf_writer.write(output_file)

            messagebox.showinfo("Success", "PDF files have been merged successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def clear_inputs(self):
        self.entry_project.delete(0, tk.END)
        self.entry_activity.delete(0, tk.END)
        self.entry_mt.delete(0, tk.END)
        self.entry_lead_trade.delete(0, tk.END)
        self.label_file1_path.config(text="")
        self.label_file2_path.config(text="")
        self.file1_path = ""
        self.file2_path = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
