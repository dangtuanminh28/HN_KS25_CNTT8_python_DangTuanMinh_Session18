orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]

def view_orders():
    if not orders:
        print("Hệ thống hiện chưa có đơn hàng nào!")
        return
    
    print("-- Danh sách đơn hàng đại lý --")
    print("Mã đơn | Tên đại lý           | Giá trị (VND)  | Trạng thái")
    print("------------------------------------------------------------------")
    for order in orders:
        print(f"{order['id']:<6} | {order['name']:<20} | {order['price']:<14,} | {order['status']}")
    print("------------------------------------------------------------------")

def create_order():
    print("-- Tạo đơn hàng mới --")
    
    while True:
        add_id = input("Nhập mã đơn hàng: ").strip().upper()
        if add_id == '':
            print("Mã đơn hàng không được để trống!")
            continue
        break
        
    for order in orders:
        if add_id == order['id']:
            print("[Lỗi]: Mã đơn này đã tồn tại trong hệ thống! (ERR-01)")
            return

    # Nhậxp tên đại lý
    while True:
        add_name = input("Nhập tên đại lý: ").strip()
        if add_name != '':
            break
        print("Tên đại lý không được để trống!")

    while True:
        try:
            add_price = int(input("Nhập giá trị đơn hàng: "))
            if add_price > 0:
                break
            print("Giá trị đơn hàng phải lớn hơn 0!")
        except ValueError:
            print("Vui lòng nhập giá trị đơn hàng bằng số nguyên hợp lệ!")

    new_order = {
        "id": add_id,
        "name": add_name,
        "price": add_price,
        "status": "Unpaid" 
    }
    orders.append(new_order)
    print("[Thành công]: Đơn hàng tạo thành công!")

def update_payment_status():
    print("-- Cập nhật trạng thái đơn hàng --")
    while True:
        check_id = input("Nhập mã đơn hàng cần cập nhật: ").strip().upper()
        if check_id == '':
            print("Vui lòng nhập mã đơn hàng!")
            continue
        break
        
    for order in orders:
        if check_id == order['id']:
            if order['status'].lower() == 'paid':
                print("[Lỗi]: Đơn hàng này đã thanh toán trước đó! (ERR-04)")
            elif order['status'].lower() == 'unpaid':
                order['status'] = 'Paid'
                print(f"Tìm thấy mã đơn hàng của: {order['name']} (Giá trị: {order['price']:,} VND)")
                print(f"[Thành công]: Đơn hàng {check_id} đã được cập nhật trạng thái ĐÃ THANH TOÁN!")
            return
            
    print(f"[Lỗi]: Không tìm thấy mã đơn hàng có mã {check_id}! (ERR-03)")

def financial_report():
    print("-- Báo cáo tài chính doanh nghiệp --")
    actual_revenue = 0
    
    for order in orders:
        if order['status'].lower() == 'paid':
            actual_revenue += order['price']
            
    if actual_revenue >= 100000000:
        discount_rate = 5
        discount_value = actual_revenue * 0.05
    else:
        discount_rate = 0
        discount_value = 0
        
    print(f"+ Tổng doanh thu thực tế (Đã thanh toán): {actual_revenue:,} VND")
    print(f"+ Tỷ lệ chiết khấu áp dụng: {discount_rate}%")
    print(f"+ Số tiền chiết khấu đại lý nhận lại: {int(discount_value):,} VND")

def main():
    while True:
        print("""
--- QUẢN LÝ ĐƠN HÀNG - AGENT ORDER ---
1. Xem danh sách đơn hàng hiện có
2. Tạo đơn hàng đại lý
3. Cập nhật trạng thái thanh toán
4. Tính toán tổng doanh thu & chiết khẩu
5. Thoát chương trình
""")
        choice = input("Nhập lựa chọn(1-5): ").strip()
        
        if choice == '1':
            view_orders()
        elif choice == '2':
            create_order()
        elif choice == '3':
            update_payment_status()
        elif choice == '4':
            financial_report()
        elif choice == '5':
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại (1-5)!")

if __name__ == "__main__":
    main()