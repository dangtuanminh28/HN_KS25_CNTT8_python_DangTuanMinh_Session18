products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    if products_list == []:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
        return

    print("-- DANH SÁCH SẢN PHẨM --")
    print("ID   | Tên sản phẩm      | Giá bán")
    for prod in products_list:
        print(f"{prod['id']} | {prod['name']} | {prod['price']}")
    print("--------------------------------------")

def add_product(products_list):
    input_id = input("Nhập mã sản phẩm(ID): ").strip().upper()
    if input_id == '':
        print("Mã không được để trống!")
        return

    for prod in products_list:
        if input_id == prod['id']:
            print("Mã tồn tại!")
            return

    add_name = input("Nhập tên sản phẩm: ").strip()
    if add_name == '':
        print("Tên sản phẩm ko được để trống!")
        return

    add_price_str = input("Nhập giá sản phẩm: ").strip()
    if add_price_str == '':
        print("Giá sản phẩm không được để trống!")
        return
    if not add_price_str.isdigit():
        print("Giá sản phẩm phải nhập là số!")
        return
    
    add_price = int(add_price_str)
    if add_price <= 0:
        print("Giá bán phải lớn hơn 0!")
        return

    new_products = {
        'id': input_id,
        'name': add_name,
        'price': add_price,
    }
    products_list.append(new_products)
    print("Thêm sản phẩm thành công!")

def update_price(products_list):
    input_id = input("Nhập mã sản phẩm cần cập nhật (ID): ").strip().upper()
    if input_id == '':
        print("Mã không được để trống!")
        return

    for prod in products_list:
        if input_id == prod['id']:
            add_price_str = input("Nhập giá sản phẩm cần sửa giá: ").strip()
            if add_price_str == '':
                print("Giá sản phẩm không được để trống!")
                return
            if not add_price_str.isdigit():
                print("Giá sản phẩm phải nhập là số!")
                return

            add_price = int(add_price_str)
            if add_price <= 0:
                print("Giá bán phải lớn hơn 0!")
                return
            
            prod['price'] = add_price
            print("Cập nhật giá cho sản phẩm thành công!")
            return
    else:
        print(f"Không tìm thấy sản phẩm có mã [{input_id}]!")

while True:
    print("""
======================================
     QUẢN LÝ CỬA HÀNG - MINI STORE 
======================================
1. Xem dánh sách sản phẩm hiện có
2. Thêm mới một sản phẩm
3. Cập nhật giá sản phẩm theo id
4. Thoát chương trình
======================================
""")
    choice = input("Nhập chức năng(1-4): ").strip()
    if choice == '1':
        show_products(products)
    elif choice == '2':
        add_product(products)
    elif choice == '3':
        update_price(products)
    elif choice == '4':
        print("Thoát chương trình")
        break
    else:
        print("Vui lòng nhập lại(1-4)!")