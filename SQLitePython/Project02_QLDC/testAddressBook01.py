
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Hệ thống quản lý địa chỉ")
root.geometry("600x800")

# Kết nối tới db
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# Tao bang de luu tru
try:
    c.execute('''
        CREATE TABLE addresses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode interger
        )
    '''
    )
except Exception as e:
    print(e)

def them():
    print("")

def xoa():
    print("")

def cap_nhat():
    print("")

def truy_van():
    print("")
def chinh_sua():
    print("")


# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
f_name = Entry(input_frame, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(input_frame, width=30)
l_name.grid(row=1, column=1)
address = Entry(input_frame, width=30)
address.grid(row=2, column=1)
city = Entry(input_frame, width=30)
city.grid(row=3, column=1)
state = Entry(input_frame, width=30)
state.grid(row=4, column=1)
zipcode = Entry(input_frame, width=30)
zipcode.grid(row=5, column=1)

# Các nhãn
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=1, column=0)
address_label = Label(input_frame, text="Địa chỉ")
address_label.grid(row=2, column=0)
city_label = Label(input_frame, text="Thành phố")
city_label.grid(row=3, column=0)
state_label = Label(input_frame, text="Tỉnh/Thành")
state_label.grid(row=4, column=0)
zipcode_label = Label(input_frame, text="Mã bưu chính")
zipcode_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

enter_box_label = Label(button_frame, text="Chọn ID")
enter_box_label.grid(row=2, column=0, pady=5)
enter_box = Entry(button_frame, width=30)
enter_box.grid(row=2, column=1, pady=5)

delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("ID", "Họ", "Tên")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.column(col, anchor=CENTER)
    tree.heading(col, text=col)
tree.pack()
# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()
