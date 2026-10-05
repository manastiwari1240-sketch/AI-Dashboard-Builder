import tkinter as tk
from tkinter import filedialog, messagebox
import csv


def upload_csv():
    file = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file:
        return

    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            data = list(csv.reader(f))

        if not data:
            messagebox.showerror("Error", "CSV file is empty.")
            return

        headers = data[0]
        rows = data[1:]

        result.delete("1.0", tk.END)

        result.insert(tk.END, "🤖 AI DASHBOARD ANALYSIS\n")
        result.insert(tk.END, "=" * 45 + "\n\n")

        result.insert(tk.END, f"📊 Total Records : {len(rows)}\n")
        result.insert(tk.END, f"📁 Total Columns : {len(headers)}\n\n")

        result.insert(tk.END, "📌 Columns:\n")

        for column in headers:
            result.insert(tk.END, f"   • {column}\n")

        result.insert(tk.END, "\n📈 Numeric Analysis:\n")

        for i, column in enumerate(headers):

            values = []

            for row in rows:
                if i < len(row):
                    try:
                        values.append(float(row[i]))
                    except ValueError:
                        pass

            if values:
                average = sum(values) / len(values)

                result.insert(
                    tk.END,
                    f"\n{column}\n"
                    f"   Average : {average:.2f}\n"
                    f"   Minimum : {min(values)}\n"
                    f"   Maximum : {max(values)}\n"
                )

        result.insert(tk.END, "\n\n✅ Analysis completed successfully!")

    except Exception as error:
        messagebox.showerror("Error", str(error))


root = tk.Tk()

root.title("AI Dashboard Builder")
root.geometry("800x600")

title = tk.Label(
    root,
    text="🤖 AI Dashboard Builder",
    font=("Arial", 24, "bold")
)

title.pack(pady=25)

subtitle = tk.Label(
    root,
    text="Upload CSV → Analyze Data → Generate Insights",
    font=("Arial", 12)
)

subtitle.pack(pady=5)

button = tk.Button(
    root,
    text="📂 Upload CSV Dataset",
    font=("Arial", 14, "bold"),
    command=upload_csv,
    padx=20,
    pady=10
)

button.pack(pady=20)

result = tk.Text(
    root,
    font=("Consolas", 12),
    width=80,
    height=22
)

result.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)

root.mainloop()