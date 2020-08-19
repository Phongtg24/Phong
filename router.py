 name: dat ip cho loobpack
  hosts: all # tên của thiết bị trong Ansible server( vì ở đây chỉ có router nên có thể để all)
# các tác vụ
  tasks:
    - name: Set loopback IPv4 address # Đặt tên task để quản lý
      ios_l3_interface: # do cấu hình router nên bắt buộc khai báo như vậy
        name_id: "{{item.number}}" # tên cổng
        ipv4: "{{item.ipv4}}" # địa chỉ IP của loopback
        state: present
    with_item:
        - { number: 1, ipv4: "10.0.1.1" }
        - { number: 2, ipv4: "10.0.2.1" }
        - { number: 3, ipv4: "10.0.3.1" }
