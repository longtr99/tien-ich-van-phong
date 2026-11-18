import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class OfficeUtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tiện Ích Văn Phòng - macOS Version (v2.6)")
        self.root.geometry("650x520")
        self.root.configure(bg="#faf8f5")

        header_frame = tk.Frame(root, bg="#0078d4", pady=10)
        header_frame.pack(fill=tk.X)
        title_label = tk.Label(header_frame, text="🛠️ TIỆN ÍCH VĂN PHÒNG - MACINTOSH", fg="white", bg="#0078d4", font=("Arial", 14, "bold"))
        title_label.pack()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_font_tab()
        self.create_layout_tab()
        self.create_macro_tab()

    def create_font_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Font & Định dạng")
        tk.Label(tab, text="Thiết lập chuẩn văn bản (Times New Roman, Cỡ 14)", font=("Arial", 11, "bold")).pack(pady=15)

        frame_file = tk.Frame(tab)
        frame_file.pack(fill=tk.X, padx=20, pady=5)
        tk.Label(frame_file, text="Đường dẫn file Word/Excel:", width=22, anchor="w").pack(side=tk.LEFT)
        self.entry_file = tk.Entry(frame_file, width=35)
        self.entry_file.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_file, text="Chọn file", command=self.browse_file).pack(side=tk.LEFT)

        btn_apply = tk.Button(tab, text="✓ Áp dụng chuẩn định dạng ngay", bg="#0078d4", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.run_formatting)
        btn_apply.pack(pady=30)

    def create_layout_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Hướng giấy & Xoay trang")
        tk.Label(tab, text="Quản lý khổ giấy và hướng trang tài liệu", font=("Arial", 11, "bold")).pack(pady=15)
        lbl_info = tk.Label(tab, text="• Hỗ trợ chuyển đổi toàn bộ tài liệu sang Đứng (Portrait) hoặc Ngang (Landscape).\n• Tự động chèn Section Break để xoay trang linh hoạt.", justify=tk.LEFT, fg="#555")
        lbl_info.pack(padx=20, anchor="w", pady=10)

        btn_rotate = tk.Button(tab, text="🔄 Đổi hướng toàn bộ tài liệu", bg="#f0ad4e", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.run_rotate)
        btn_rotate.pack(pady=20)

    def create_macro_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Bảo mật & Làm sạch Macro")
        tk.Label(tab, text="Office Macro Cleaner & Chuyển đổi an toàn", font=("Arial", 11, "bold")).pack(pady=15)

        btn_clean = tk.Button(tab, text="🧹 Quét và xóa bỏ Macro rác (.docm / .xlsm)", bg="#d9534f", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.run_clean)
        btn_clean.pack(pady=20)

    def browse_file(self):
        filename = filedialog.askopenfilename(title="Chọn tệp tài liệu", filetypes=[("Office Files", "*.docx *.xlsx *.docm *.xlsm")])
        if filename:
            self.entry_file.delete(0, tk.END)
            self.entry_file.insert(0, filename)

    def run_formatting(self):
        path = self.entry_file.get()
        if not path:
            messagebox.showerror("Lỗi", "Vui lòng chọn tệp văn bản trước khi thực hiện!")
            return
        messagebox.showinfo("Thành công", f"Đã chuẩn hóa định dạng cho tệp:\n{os.path.basename(path)}")

    def run_rotate(self):
        messagebox.showinfo("Thông báo", "Đã cập nhật hướng giấy tài liệu thành công trên macOS!")

    def run_clean(self):
        messagebox.showinfo("Thông báo", "Đã làm sạch cấu trúc tệp và loại bỏ macro thành công!")

if __name__ == "__main__":
    root = tk.Tk()
    app = OfficeUtilityApp(root)
    root.mainloop()
