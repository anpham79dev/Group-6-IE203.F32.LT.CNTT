BÁO CÁO PHÂN TÍCH VÀ MÔ HÌNH HÓA QUY TRÌNH NGHIỆP VỤ CỐT LÕI HỆ THỐNG ĐẶT VÉ MÁY BAY MOMO TRAVEL

Hệ thống đặt vé máy bay trên Siêu ứng dụng MoMo (MoMo Travel) vận hành như một đại lý du lịch trực tuyến (Online Travel Agency - OTA) tích hợp sâu vào hạ tầng trung gian thanh toán và ví điện tử. Hệ thống đóng vai trò cầu nối dữ liệu thời gian thực giữa người dùng cuối, nền tảng ví MoMo, các hệ thống phân phối toàn cầu (Global Distribution System - GDS như Amadeus, Sabre, Abacus) và hệ thống đặt giữ chỗ trực tiếp (Computer Reservation System - CRS) của các hãng hàng không nội địa lẫn quốc tế.

Báo cáo này tập trung phân tích chuyên sâu ba luồng nghiệp vụ cốt lõi (Core Processes) thuộc phân hệ MoMo Travel: Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé; Mua thêm dịch vụ bổ sung sau đặt chỗ; và Đổi chuyến bay. Bản mô tả được thiết kế theo các tiêu chuẩn phân tích quy trình nghiệp vụ (BPM), nhằm cung cấp đầy đủ dữ liệu cấu trúc, phân công vai trò (Lanes), logic điều kiện (Gateways), dữ liệu đầu vào/đầu ra và các kịch bản ngoại lệ để phục vụ công tác mô hình hóa chuẩn BPMN 2.0.

CHƯƠNG 1: QUY TRÌNH CỐT LÕI 1 - TÌM KIẾM, LỰA CHỌN HÀNH TRÌNH, THANH TOÁN VÀ XÁC NHẬN ĐẶT VÉ

1.1. Mục tiêu và Phạm vi Luồng Nghiệp vụ

Quy trình cốt lõi này điều phối toàn bộ vòng đời giao dịch ban đầu của khách hàng, bắt đầu từ khi phát sinh nhu cầu di chuyển, tìm kiếm lịch trình, khởi tạo hồ sơ danh sách hành khách (Passenger Name Record - PNR), xử lý thanh toán bất đồng bộ và phát hành vé máy bay điện tử (e-Ticket). Quy trình đảm bảo tính toàn vẹn dữ liệu giữa cổng thanh toán MoMo và hệ thống đặt chỗ của hãng bay trong thời gian thực.

1.2. Phân Định Các Tác Nhân Và Làn Quy Trình (Pools & Swimlanes)

Mô hình quy trình được chia thành năm làn nghiệp vụ (Lanes) chính tương ứng với các chủ thể tham gia xử lý:

⚬ Làn 1: Khách hàng (Customer Lane): Người dùng thao tác trên ứng dụng di động MoMo, thực hiện tìm kiếm, nhập thông tin, lựa chọn dịch vụ và xác thực giao dịch tài chính.

⚬ Làn 2: Giao diện Khách hàng MoMo (MoMo Client App Lane): Phân hệ Frontend chịu trách nhiệm bắt sự kiện thao tác, kiểm tra định dạng dữ liệu (Client-side validation), hiển thị kết quả truy vấn và gửi yêu cầu API.

⚬ Làn 3: Hệ thống Backend MoMo Travel (MoMo Travel Service Lane): Middleware xử lý logic nghiệp vụ, kết nối API nhà cung cấp, áp dụng quy tắc giá, tính toán mã giảm giá (Voucher), quản lý trạng thái đơn hàng và điều phối luồng thanh toán.

⚬ Làn 4: Cổng Thanh toán MoMo (MoMo Payment Gateway Lane): Phân hệ tài chính xử lý trừ tiền tài khoản ví, Ví Trả Sau, thẻ ngân hàng liên kết, thực hiện xác thực sinh trắc học/OTP và hạch toán giao dịch.

⚬ Làn 5: Hệ thống Hãng hàng không / GDS (Airline CRS/GDS Lane): Hệ thống bên ngoài cung cấp dữ liệu lịch bay, giá vé, thực hiện khóa chỗ tạm thời (Seat Hold), nhận lệnh xuất vé (Ticketing) và cấp mã PNR.

1.3. Mô Tả Trình Tự Các Bước Nghiệp Vụ Chi Tiết

Bước 1: Khởi tạo truy vấn tìm kiếm hành trình

Khách hàng truy cập mục "Du lịch - Đi lại" trên màn hình chính của MoMo, chọn tính năng "Vé máy bay". Tại màn hình tìm kiếm, khách hàng lựa chọn loại hình chuyến bay (Một chiều, Khứ hồi hoặc Nhiều chặng), điểm đi (Origin), điểm đến (Destination), ngày khởi hành, ngày về (nếu có), số lượng hành khách phân loại theo độ tuổi (Người lớn từ 12 tuổi trở lên, Trẻ em từ 2 đến dưới 12 tuổi, Em bé dưới 2 tuổi) và hạng ghế ưu tiên. Khi khách hàng nhấn "Tìm kiếm", ứng dụng MoMo Client gửi yêu cầu truy vấn chứa các tham số này đến MoMo Travel Backend.

Bước 2: Tự động tổng hợp và truy vấn lịch bay real-time

MoMo Travel Backend tiếp nhận yêu cầu, đồng thời khởi tạo các cuộc gọi API song song (Asynchronous REST API Calls) đến hệ thống GDS và hệ thống CRS của các hãng hàng không đối tác như Vietnam Airlines, Vietjet Air, Bamboo Airways, Vietravel Airlines, Pacific Airlines, Sun PhuQuoc Airways và hơn 100 hãng quốc tế. Các hệ thống hãng bay xử lý truy vấn dữ liệu ghế trống (Seat Availability) và giá vé chi tiết (Fare Matrix), trả về danh sách phản hồi.

Bước 3: Lọc dữ liệu, chuẩn hóa giá vé và hiển thị

MoMo Travel Backend tổng hợp dữ liệu thô, thực hiện quy trình chuẩn hóa cấu trúc giá (bao gồm giá cước cơ bản, thuế giá trị gia tăng, phí sân bay, phí quản lý hệ thống và phí dịch vụ MoMo). Hệ thống áp dụng các quy tắc hiển thị giá minh bạch, loại bỏ phí ẩn, và gửi dữ liệu về MoMo Client App. Khách hàng sử dụng bộ lọc linh hoạt để sắp xếp chuyến bay theo các tiêu chí: Giá rẻ nhất, Giờ cất cánh (Sáng sớm, Trưa, Chiều, Tối khuya), Hãng hàng không yêu thích hoặc Thời gian bay ngắn nhất.

Bước 4: Lựa chọn chuyến bay và nhập thông tin hành khách

Khách hàng chọn chuyến bay phù hợp cho từng chiều bay. Tiếp theo, hệ thống chuyển sang màn hình nhập thông tin hành khách. Khách hàng điền chính xác Họ và Tên (viết hoa không dấu theo đúng giấy tờ tùy thân CMND/CCCD/Hộ chiếu), Ngày tháng năm sinh, Giới tính và Thông tin liên hệ gồm Số điện thoại và Email nhận vé. Hệ thống MoMo hỗ trợ tính năng tự động điền (Auto-fill) thông tin cá nhân đã lưu trong tài khoản ví để tối ưu thời gian thao tác.

Bước 5: Mua kèm dịch vụ bổ sung ban đầu và áp dụng ưu đãi

Tại bước này, hệ thống hiển thị tùy chọn mua thêm hành lý ký gửi (các gói từ 15kg đến 40kg hoặc kiện đồ Tết chuyên biệt như mai/đào), chọn chỗ ngồi trước, mua bảo hiểm trễ chuyến bay/bảo hiểm du lịch toàn diện (hợp tác với Bảo Việt) và mã hội viên thân thiết (như dặm Bông Sen Vàng Vietnam Airlines). Khách hàng chọn các thẻ quà tặng (Voucher) khả dụng trong ví MoMo Rewards hoặc nhập mã ưu đãi tại ô khuyến mãi.

Bước 6: Khóa chỗ tạm thời và tạo mã giữ chỗ (PNR)

Sau khi khách hàng kiểm tra lại toàn bộ thông tin và bấm "Tiếp tục", MoMo Travel Backend gửi lệnh đặt chỗ (CreateBooking) đến hệ thống của hãng bay. Hệ thống hãng hàng không xác thực tính hợp lệ của dữ liệu hành khách, thực hiện giữ chỗ tạm thời trong thời hạn định sẵn (Hold Time Limit) và cấp một mã đặt chỗ (Passenger Name Record - PNR) duy nhất gồm 6 ký tự alphanumeric. Mã PNR này được truyền về MoMo kèm theo đồng hồ đếm ngược thời gian thanh toán (thông thường từ 10 đến 15 phút).

Bước 7: Xác nhận phương thức thanh toán và hạch toán tài chính

Khách hàng lựa chọn nguồn tiền thanh toán trên ứng dụng MoMo: Ví MoMo (tiền mặt trong ví), Tài khoản ngân hàng liên kết, Thẻ nội địa NAPAS, Thẻ quốc tế Visa/Mastercard/JCB, Ví Trả Sau (mở tài khoản hạn mức trước), hoặc Vay Nhanh. Khách hàng kiểm tra tổng chi phí cuối cùng (đã trừ giá trị thẻ quà tặng) và nhấn "Xác nhận thanh toán". MoMo Client yêu cầu xác thực bảo mật thông qua Mật khẩu ví, FaceID hoặc TouchID theo chuẩn bảo mật PCI DSS. Cổng thanh toán MoMo thực hiện trích tiền từ nguồn tiền của người dùng và gửi thông báo xác nhận tiền đã trừ thành công sang MoMo Travel Backend.

Bước 8: Phát hành vé máy bay điện tử (e-Ticket Issuance)

Ngay khi hạch toán thanh toán thành công, MoMo Travel Backend gửi lệnh phát hành vé (IssueTicket) chứa mã PNR và xác nhận thanh toán đến API của hãng hàng không. Hệ thống hãng hàng không chuyển trạng thái PNR từ "Giữ chỗ" (Reserved) sang "Đã xuất vé" (Ticketed), tạo ra số vé điện tử (e-Ticket Number) và trả kết quả về MoMo. MoMo lưu trữ vé vào mục "Quản lý đặt vé" / "Quản lý vé và thông tin hành khách", đồng thời tự động gửi email chứa vé điện tử (định dạng PDF kèm mã QR check-in) và tin nhắn thông báo (Push Notification/SMS) cho khách hàng.

1.4. Bảng Tổng Hợp Luồng Dữ Liệu Và Quy Tắc Nghiệp Vụ Cốt Lõi 1

| Bước Nghiệp Vụ | Dữ Liệu Đầu Vào | Dữ Liệu Đầu Ra | Quy Tắc Nghiệp Vụ & Logic Kiểm Soát |
| :--- | :--- | :--- | :--- |
| 1. Truy vấn lịch bay | Điểm đi, điểm đến, ngày bay, loại vé, số lượng khách. | Yêu cầu API truy vấn (JSON Request). | Điểm đi và điểm đến không được trùng nhau; ngày về phải lớn hơn hoặc bằng ngày đi. |
| 2. Xử lý giá & hiển thị | Khung giá thô từ GDS/CRS hãng bay. | Danh sách chuyến bay kèm tổng giá vé cuối cùng. | Hiển thị giá minh bạch đã bao gồm thuế, phí sân bay và phí quản lý bắt buộc. |
| 3. Nhập thông tin khách | Họ tên, ngày sinh, CCCD/Hộ chiếu, SĐT, Email. | Hồ sơ khách hàng chuẩn hóa. | Họ tên không chứa ký tự đặc biệt hoặc số; số lượng em bé không vượt quá số lượng người lớn. |
| 4. Tạo mã PNR | Hồ sơ khách hàng, thông tin chuyến bay đã chọn. | Mã PNR 6 ký tự, thời hạn giữ chỗ. | Chỗ ngồi bị hủy tự động trên hệ thống hãng nếu hết thời gian giữ chỗ mà chưa hoàn tất thanh toán. |
| 5. Hạch toán tài chính | Nguồn tiền được chọn, mật khẩu/sinh trắc học. | Mã giao dịch tài chính (Transaction ID). | Kiểm tra số dư nguồn tiền; áp dụng mã giảm giá theo đúng điều kiện tối thiểu của đơn hàng. |
| 6. Xuất vé điện tử | Mã PNR, Mã giao dịch tài chính thành công. | Vé điện tử (e-Ticket PDF), Mã QR check-in. | Đồng bộ trạng thái vé tức thì vào cơ sở dữ liệu ứng dụng MoMo và gửi mail tự động trong 60 giây. |

1.5. Xử Lý Luồng Ngoại Lệ Và Sự Cố (Exception Handling)

⚬ Sự cố 1: Hết thời gian giữ chỗ (Payment Timeout): Khách hàng dừng ở bước thanh toán quá thời gian đếm ngược (Hold Time Limit). Cổng thanh toán MoMo tự động hủy lệnh trích tiền; MoMo Travel Backend gửi lệnh hủy giữ chỗ (CancelBooking) sang hãng bay để giải phóng ghế. Hệ thống hiển thị thông báo "Giao dịch hết hạn" và điều hướng khách hàng quay lại màn hình tìm kiếm.

⚬ Sự cố 2: Giữ tiền thành công nhưng hãng không xuất được vé (Issue Ticket Failure): Tiền đã bị trừ trong ví MoMo nhưng API xuất vé của hãng hàng không gặp sự cố đứt gãy kết nối hoặc bị nghẽn hệ thống. MoMo Travel Backend ghi nhận trạng thái giao dịch là "Đang xử lý" (Pending). Hệ thống tự động kích hoạt cơ chế thử lại (Retry Mechanism) trong 15 phút. Nếu vẫn thất bại, giao dịch được chuyển sang phân hệ CSKH; hệ thống tự động hoàn tiền 100% về ví MoMo của khách hàng và gửi thông báo giải thích nguyên nhân.

⚬ Sự cố 3: Thay đổi giá vé thời gian thực (Fare Jump): Trong khoảng thời gian từ lúc khách chọn chuyến bay đến trước khi tạo mã PNR, hãng hàng không thay đổi thang giá. MoMo Travel Backend phát hiện sự chênh lệch giá, lập tức dừng tiến trình khóa chỗ và hiển thị màn hình cảnh báo "Giá vé đã thay đổi", yêu cầu khách hàng xác nhận mức giá mới trước khi tiếp tục.

CHƯƠNG 2: QUY TRÌNH CỐT LÕI 2 - MUA THÊM DỊCH VỤ BỔ SUNG SAU ĐẶT CHỖ (POST-BOOKING ANCILLARY SERVICES)

2.1. Mục tiêu và Phạm vi Luồng Nghiệp vụ

Quy trình này cho phép hành khách đã có vé máy bay hợp lệ (đã được cấp mã PNR) tiến hành mua bổ sung các tiện ích gia tăng trước giờ khởi hành. Dịch vụ bao gồm: Hành lý ký gửi quá cước, chọn vị trí chỗ ngồi ưng ý, đặt suất ăn nóng, bảo hiểm trễ chuyến bay, hoặc các hành lý đặc biệt theo mùa (như vận chuyển cành mai, cành đào dịp Tết).

2.2. Phân Định Các Tác Nhân Và Làn Quy Trình (Pools & Swimlanes)

⚬ Làn 1: Khách hàng (Customer Lane): Khởi chạy tính năng mua dịch vụ bổ sung từ danh mục quản lý vé đã mua trên MoMo.

⚬ Làn 2: Giao diện Khách hàng MoMo (MoMo Client App Lane): Hiển thị sơ đồ khoang máy bay, danh mục hành lý/suất ăn khả dụng tương ứng với PNR.

⚬ Làn 3: Hệ thống Backend MoMo Travel (MoMo Travel Service Lane): Tra cứu dữ liệu PNR từ database, gọi API kiểm tra điều kiện vé từ hãng bay, tính toán chi phí dịch vụ cộng thêm.

⚬ Làn 4: Cổng Thanh toán MoMo (MoMo Payment Gateway Lane): Xử lý thanh toán khoản chi phí mua bổ sung.

⚬ Làn 5: Hệ thống Hãng hàng không (Airline Ancillary API Lane): Cập nhật chứng từ dịch vụ phụ trợ điện tử (Electronic Miscellaneous Document - EMD) vào mã PNR của hành khách.

2.3. Mô Tả Trình Tự Các Bước Nghiệp Vụ Chi Tiết

Bước 1: Tra cứu và truy cập quản lý đặt chỗ

Khách hàng mở ứng dụng MoMo, chuyển sang mục "Du lịch - Đi lại", chọn "Chỗ đã đặt" hoặc vào mục "Tôi" > "Quản lý đặt chỗ" (hoặc "Quản lý vé và thông tin hành khách"). Hệ thống hiển thị danh sách các chuyến bay sắp khởi hành. Khách hàng chọn chuyến bay cần mua thêm dịch vụ, hệ thống hiển thị màn hình "Thông tin vé máy bay". Tại đây, khách hàng nhấn chọn tính năng "Quản lý đặt chỗ" > "Mua hành lý, chỗ ngồi...".

Bước 2: Đồng bộ dữ liệu PNR và truy xuất danh mục dịch vụ phụ trợ

MoMo Travel Backend tiếp nhận mã PNR và hãng bay tương ứng, thực hiện cuộc gọi API GetBookingDetails đến hệ thống hãng hàng không. Hệ thống hãng kiểm tra trạng thái vé (vé phải ở trạng thái "Active" và chưa làm thủ tục check-in tại sân bay) và thời gian còn lại trước giờ cất cánh (thường phải trước từ 3 đến 24 giờ tùy quy định hãng). Hãng trả về danh mục dịch vụ bổ sung khả dụng kèm theo bảng giá niêm yết và sơ đồ chỗ ngồi thời gian thực.

Bước 3: Lựa chọn gói dịch vụ và vị trí

Giao diện ứng dụng hiển thị các phân hệ dịch vụ bổ sung để khách hàng tùy chọn:

⚬ Hành lý ký gửi: Khách hàng chọn gói trọng lượng mong muốn (15kg, 20kg, 23kg, 30kg, 40kg) cho từng hành khách trên từng chặng bay. Đối với các chặng bay dịp Tết, hệ thống cung cấp thêm gói ký gửi cành mai/đào theo tiêu chuẩn kích thước quy định (tối đa 150 x 40 x 40 cm, tối đa 2 cành/bó).

⚬ Chọn chỗ ngồi: Hệ thống hiển thị sơ đồ khoang hành khách trực quan (Seat Map). Các ghế được phân loại theo màu sắc: Ghế để chân rộng (Extra Legroom), Ghế hàng đầu, Ghế cạnh cửa sổ/lối đi, và Ghế tiêu chuẩn kèm theo mức giá tương ứng. Khách hàng chạm để chọn vị trí mong muốn cho từng người.

⚬ Suất ăn & Tiện ích khác: Khách hàng chọn món ăn nóng, nước uống hoặc dịch vụ đón tiếp ưu tiên (Fast-track) nếu hãng có cung cấp.

⚬ Bảo hiểm: Khách hàng có thể tích chọn bổ sung Bảo hiểm trễ chuyến bay hoặc Bảo hiểm du lịch toàn diện.

Bước 4: Kiểm tra giỏ hàng dịch vụ và áp dụng mã giảm giá

Sau khi chọn xong, MoMo Client App tổng hợp chi phí các dịch vụ bổ sung đã chọn. MoMo Travel Backend kiểm tra các quy tắc cộng dồn giá và áp dụng các thẻ quà tặng áp dụng riêng cho phân hệ tiện ích du lịch. Màn hình hiển thị chi tiết bảng kê tài chính: Giá vé ban đầu, Chi phí dịch vụ mua thêm, Mã giảm giá và Tổng số tiền cần thanh toán bổ sung.

Bước 5: Thanh toán giao dịch dịch vụ bổ sung

Khách hàng nhấn "Xác nhận thanh toán". Quá trình thanh toán diễn ra tương tự như quy trình đặt vé ban đầu: Khách hàng chọn nguồn tiền (Ví MoMo, Thẻ ngân hàng, Ví Trả Sau), nhập mật khẩu hoặc xác thực sinh trắc học. Cổng thanh toán trích tiền và gửi mã giao dịch thành công cho MoMo Travel Backend.

Bước 6: Cập nhật chứng từ EMD và thông báo cho khách hàng

MoMo Travel Backend gửi lệnh API AddAncillary đến hệ thống hãng hàng không. Hệ thống hãng ghi nhận khoản thanh toán, phát hành Chứng từ phụ trợ điện tử (EMD) liên kết trực tiếp với mã PNR hiện tại. Dữ liệu PNR trên hệ thống hãng được cập nhật tự động (ví dụ: bổ sung thêm 20kg hành lý ký gửi hoặc mã số ghế 12A). Hệ thống MoMo hiển thị màn hình Mua dịch vụ bổ sung thành công, đồng thời cập nhật thông tin mới vào "Thông tin vé máy bay" trong ứng dụng và gửi email xác nhận hành trình mới đã cập nhật cho khách hàng.

2.4. Bảng Tổng Hợp Luồng Dữ Liệu Và Quy Tắc Nghiệp Vụ Cốt Lõi 2
2.5. Xử Lý Luồng Ngoại Lệ Và Sự Cố (Exception Handling)

⚬ Sự cố 1: Khách hàng đã Check-in trực tuyến trước khi mua dịch vụ: Hệ thống hãng bay từ chối lệnh AddAncillar[span_226](start_span)[span_226](end_span)[span_239](start_span)[span_239](end_span)y do PNR đã bị khóa sau khi check-in. MoMo Travel Backend sẽ bắt mã lỗi từ hãng và hiển thị thông báo: "Chuyến bay đã thực hiện làm thủ tục. Quý khách vui lòng mua hành lý/dịch vụ trực tiếp tại sân bay".

⚬ Sự cố 2: Trừ tiền thành công nhưng không ghi nhận được chỗ ngồi/hành lý vào PNR: Do lỗi gián đoạn API giữa MoMo và hãng trong khâu ghi nhận EMD. Hệ thống tự động tạo một Ticket chăm sóc khách hàng ưu tiên cao. Nhân viên CSKH MoMo dựa vào mã giao dịch để thực hiện mua bù thủ công trên portal đại lý của hãng hoặc tiến hành hoàn lại tiền dịch vụ bổ sung cho khách hàng trong vòng 24 giờ.

CHƯƠNG 3: QUY TRÌNH CỐT LÕI 3 - ĐỔI CHUYẾN BAY VÀ ĐIỀU CHỈNH LỊCH TRÌNH (FLIGHT CHANGE / RE-ISSUANCE)

3.1. Mục tiêu và Phạm vi Luồng Nghiệp vụ

Quy trình này xử lý các yêu cầu thay đổi ngày bay, giờ bay, hoặc hành trình bay từ phía hành khách sau khi vé đã được xuất thành công. Quy trình đảm bảo tự động hóa hoặc bán tự động việc tính toán điều kiện vé, phí đổi cố định của hãng, phí chênh lệch giá vé thời điểm hiện tại và phí dịch vụ MoMo, sau đó thực hiện đổi chỗ và tái phát hành vé (Re-issue).

3.2. Phân Định Các Tác Nhân Và Làn Quy Trình (Pools & Swimlanes)

⚬ Làn 1: Khách hàng (Customer Lane): Khởi tạo yêu cầu đổi chuyến bay, chọn ngày/giờ mới, thanh toán phí chênh lệch.

⚬ Làn 2: Giao diện Khách hàng MoMo (MoMo Client App Lane): Hiển thị màn hình tìm kiếm chuyến bay mới, chi tiết các khoản phí thay đổi.

⚬ Làn 3: Hệ thống Backend MoMo Travel (MoMo Travel Service Lane): Tính toán logic phí đổi theo quy định điều kiện vé (Fare Rules), gửi lệnh đổi chỗ đến hãng.

⚬ Làn 4: Cổng Thanh toán MoMo (MoMo Payment Gateway Lane): Xử lý thanh toán tổng phí chênh lệch đổi vé.

⚬ Làn 5: Bộ phận CSKH MoMo Travel (MoMo CS Operations Lane): Can thiệp hỗ trợ xử lý các hạng vé phức tạp, vé quốc tế hoặc lỗi API hãng.

⚬ Làn 6: Hệ thống Hãng hàng không (Airline CRS/GDS Lane): Kiểm tra điều kiện vé, hủy chỗ cũ, giữ chỗ mới và tái phát hành số vé mới.

3.3. Mô Tả Trình Tự Các Bước Nghiệp Vụ Chi Tiết

Bước 1: Khởi tạo yêu cầu đổi chuyến bay

Khách hàng vào ứng dụng MoMo, truy cập mục "Quản lý đặt chỗ" / "Thông tin vé máy bay", chọn vé máy bay muốn thay đổi. Tại đây, khách hàng nhấn vào nút "Đổi chuyến bay" / "Thay đổi lịch trình". Hệ thống kiểm tra điều kiện vé cơ bản (các hạng vé Siêu tiết kiệm/Economy Saver của một số hãng có thể không cho phép đổi hoặc chỉ cho phép đổi trước giờ bay 24h). Khách hàng chọn thông số muốn đổi: Đổi ngày bay, Đổi giờ bay, hoặc Đổi hành trình (Chặng bay) cho tất cả hoặc một số hành khách trong PNR.

Bước 2: Tìm kiếm lịch bay mới và truy xuất giá vé

MoMo Travel Backend gửi yêu cầu tìm kiếm lịch bay mới sang hệ thống GDS/CRS của hãng hàng không. Hãng trả về danh sách các chuyến bay còn chỗ trong ngày/hành trình mới được chọn. Màn hình hiển thị danh sách các chuyến bay mới kèm theo giá vé chênh lệch ước tính. Khách hàng chọn chuyến bay và giờ bay mới phù hợp với nhu cầu.

Bước 3: Tính toán chi tiết cấu trúc phí đổi (Fare Calculation)

MoMo Travel Backend kết nối với bộ máy tính phí (Fare Rule Engine) của hãng bay để tính toán chính xác tổng số tiền khách hàng phải trả thêm. Công thức tính toán chi phí thay đổi chuyến bay được cấu trúc như sau:

$$\text{Tổng phí đổi} = \text{Phí thay đổi cố định của Hãng} + \text{Chênh lệch giá vé [span_305](start_span)[span_305](end_span)[span_319](start_span)[span_319](end_span)(nếu có)} + \text{Phí dịch vụ đổi vé MoMo}$$

In đó:

⚬ Phí thay đổi cố định của Hãng: Phụ thuộc vào quy định hạng vé đã mua (ví dụ: Hạng Linh hoạt - Miễn phí đổi; Hạng Tiết kiệm - Phí 350.000 VNĐ - 450.000 VNĐ/chặng/hành khách).

⚬ Chênh lệch giá vé: = Giá vé mới tại thời điểm đổi - Giá vé cũ đã trả. (Lưu ý: Nếu giá vé mới thấp hơn giá vé cũ, đa số các hãng hàng không không hoàn lại phần tiền chênh lệch dư theo quy định điều kiện vé nội địa).

⚬ Phí dịch vụ MoMo: Phí xử lý giao dịch đổi vé của nền tảng (nếu có).

Bước 4: Xác nhận chi tiết chi phí và chấp nhận điều kiện đổi

Giao diện ứng dụng MoMo hiển thị chi tiết bảng phân rã chi phí đổi vé. Khách hàng đọc kỹ quy định đổi vé, chi tiết chuyến bay cũ và chuyến bay mới. Nếu đồng ý, khách hàng chọn vào khung "Tôi đã đọc, hiểu và đồng ý với Điều kiện thay đổi vé" và nhấn nút "Thanh toán phí đổi".

Bước 5: Thanh toán phí chênh lệch đổi chuyến

Cổng thanh toán MoMo khởi chạy màn hình xác nhận thanh toán khoản phí chênh lệch. Khách hàng chọn nguồn tiền, thực hiện xác thực bảo mật (Mật khẩu/OTP/Sinh trắc học). Sau khi tài khoản bị trích tiền thành công, mã hạch toán được gửi về MoMo Travel Backend.

Bước 6: Tái phát hành vé (Re-issuance) và cập nhật PNR

MoMo Travel Backend gửi lệnh tái phát hành vé (ReissueTicket) kèm mã hạch toán phí đổi sang API hãng hàng không. Hệ thống hãng hàng không hủy chỗ trên chuyến bay cũ, xác nhận chỗ trên chuyến bay mới, thu hồi vé điện tử cũ và phát hành vé điện tử mới (Số vé điện tử mới) dưới cùng mã PNR hoặc mã PNR mới. Hệ thống MoMo cập nhật lại thông tin vé trong mục "Quản lý đặt chỗ", hủy thông tin vé cũ, hiển thị thông báo đổi vé thành công và gửi Email/SMS xác nhận hành trình mới cho khách hàng.

3.4. Bảng Tổng Hợp Luồng Dữ Liệu Và Quy Tắc Nghiệp Vụ Cốt Lõi 3

Bước Nghiệp Vụ	Dữ Liệu Đầu Vào	Dữ Liệu Đầu Ra	Quy Tắc Nghiệp Vụ & Logic Kiểm Soát
1. Kiểm tra điều kiện đổi	Mã PNR, Điều kiện hạng vé cũ.	Trạng thái cho phép đổi (Eligible/Ineligible).	Vé phải còn hiệu lực đổi theo quy định điều kiện vé của hãng; phải thực hiện trước giờ bay tối thiểu từ 3 - 24 tiếng.
2. Bảng tính phí đổi	Giá vé cũ, Giá vé mới, Quy tắc phí hãng.	Bảng kê chi tiết phí đổi vé.	Nếu vé mới rẻ hơn vé cũ, tiền chênh lệch âm không được hoàn lại; chỉ thu thêm nếu vé mới cao giá hơn.
3. Thanh toán phí chênh lệch	Xác nhận chấp nhận phí, Nguồn tiền thanh toán.	Mã giao dịch đổi vé.	Khóa giữ chỗ trên chuyến bay mới trong thời gian thanh toán phí đổi (thường là 10 phút).
4. Tái phát hành vé mới	Mã PNR, Mã thanh toán phí chênh lệch.	Vé điện tử mới (New e-Ticket/Itinerary).	Cập nhật số vé mới, tự động vô hiệu hóa số vé điện tử cũ trên hệ thống.

3.5. Xử Lý Luồng Ngoại Lệ Và Sự Cố (Exception Handling)

⚬ Sự cố 1: Hạng vé không hỗ trợ đổi tự động qua API (Ngoại lệ xử lý thủ công): Một số hãng hàng không quốc tế hoặc các vé mua trong chương trình khuyến mãi đặc biệt không cho phép tự động tính phí đổi qua API. Hệ thống MoMo Travel hiển thị thông báo: "Yêu cầu đổi vé của Quý khách cần xử lý trực tiếp". Hệ thống tạo một Yêu cầu hỗ trợ (Support Ticket) chuyển thẳng sang Luồng CSKH. Nhân viên CSKH MoMo liên hệ tổng đài hãng bay để kiểm tra phí thủ công, gửi đường link thanh toán khoản phí chênh lệch cho khách hàng qua ứng dụng MoMo, sau khi khách thanh toán xong nhân viên sẽ thao tác tái xuất vé.

⚬ Sự cố 2: Đã trích phí đổi vé nhưng hãng báo hết chỗ cất cánh (Seat Out of Stock during Re-issue): Trong quá trình khách hàng thực hiện thanh toán phí đổi, số ghế trống trên chuyến bay mới đã bị khách hàng khác mua mất. Lệnh ReissueTicket bị hãng từ chối. MoMo Travel Backend lập tức hủy giao dịch thanh toán phí đổi, hoàn trả 100% tiền phí đổi vừa trích về ví MoMo, đồng thời giữ nguyên trạng thái vé và chuyến bay cũ của khách hàng, kèm thông báo "Chuyến bay mới đã hết chỗ, vui lòng chọn lại chuyến bay khác".

CHƯƠNG 4: BẢNG TỔNG HỢP MÃ HÓA NGUYÊN LIỆU ĐỂ VẼ SƠ ĐỒ BPMN 2.0

Để phục vụ công tác vẽ sơ đồ quy trình nghiệp vụ chuẩn BPMN 2.0 cho cả 3 quy trình cốt lõi trên các phần mềm chuyên dụng (như Camunda, Draw.io, Lucidchart, Bizagi), bảng dưới đây tổng hợp mã hóa chi tiết các phần tử BPMN bao gồm: Tiến trình (Process/Pool), Làn (Lane), Sự kiện bắt đầu/ket thúc (Events), Cổng quyết định (Gateways), và các Tác vụ (Tasks).

CHƯƠNG 5: ĐÁNH GIÁ ĐỊNH LƯỢNG VÀ ĐỀ XUẤT CẢI TIẾN QUY TRÌNH (TO-BE RECOMMENDATIONS)

5.1. Phân Tích Định Lượng Thời Gian Xử Lý (Cycle Time Analysis)

Dựa trên dữ liệu vận hành thực tế của các hệ thống OTA tích hợp Ví điện tử, tổng thời gian xử lý trung bình của từng luồng quy trình được tổng hợp như sau:

Quy trình 1 (Tìm kiếm, Đặt vé và Thanh toán):

⚬ Thời gian tìm kiếm và trả kết quả API: ‭$3 - 5$‬ giây.

⚬ Thời gian thao tác của khách hàng (Lựa chọn, nhập thông tin, mua dịch vụ): ‭$120 - 180$‬ giây.

⚬ Thời gian tạo PNR và giữ chỗ tạm thời: ‭$2 - 4$‬ giây.

⚬ Thời gian xác thực thanh toán tài chính (Sinh trắc học/OTP): ‭$5 - 10$‬ giây.

⚬ Thời gian xuất vé điện tử từ Hãng: ‭$5 - 15$‬ giây.

⚬ $$\text{Tổng thời gian chu kỳ cơ bản (Success Flow)} \approx 2,5 - 3,5 \text{ phút}$$

Quy trình 2 (Mua thêm dịch vụ bổ sung):

⚬ Truy xuất PNR và sơ đồ ghế: ‭$2 - 4$‬ giây.

⚬ Thao tác chọn gói dịch vụ/ghế: ‭$45 - 60$‬ giây.

⚬ Thanh toán và ghi nhận EMD: ‭$10 - 20$‬ giây.

⚬ $$\text{Tổng thời gian chu k[span_377](start_span)[span_377](end_span)[span_379](start_span)[span_379](end_span)ỳ} \approx 1 - 1,5 \text{ phút}$$

Quy trình 3 (Đổi chuyến bay):

⚬ Kiểm tra điều kiện vé và tính phí chênh lệch tự động: ‭$5 - 8$‬ giây.

⚬ Thao tác chọn chuyến mới và xác nhận phí: ‭$60 - 90$‬ giây.

⚬ Thanh toán và tái phát hành vé (Re-issue): ‭$15 - 30$‬ giây.

⚬ $$\text{Tổng thời gian chu kỳ tự động (Auto Re-issue)} \approx 1,5 - 2,5 \text{ phút}$$

⚬ (Trường hợp ngoại lệ xử lý qua CSKH thủ công: ‭$15 - 45$‬ phút tùy thuộc thời gian phản hồi của Hãng hàng không).

5.2. Đề Xuất Cải Tiến Mô Hình TO-BE

Nhằm tối ưu hóa hiệu năng hệ thống, giảm tỷ lệ hủy đơn (Drop-off rate) và hạn chế lỗi ngoại lệ, các giải pháp số hóa sau cần được tích hợp vào mô hình quy trình TO-BE:

1. Tự động hóa luồng Đổi vé 100% qua API (Full Automated Self-service Re-issuance): Xây dựng bộ quy tắc Fare Rule Engine thông minh cho tất cả các hãng hàng không kết nối, loại bỏ hoàn toàn việc chuyển Ticket sang CSKH xử lý thủ công đối với các vé nội địa.

2. Cơ chế khóa chỗ thông minh (Smart Lock Payment): Khi khách hàng chọn phương thức thanh toán, hệ thống tự động giữ giữ chỗ (PNR Hold) và khóa mức giá trong 15 phút, ngăn chặn tuyệt đối tình trạng tăng giá vé đột ngột (Fare Jump) trong quá trình người dùng nhập OTP thanh toán.

3. **Tích hợp trợ lý AI nhắc lịch và gợi ý mua bổ sung (AI-driven Ancillary Upselling): Sử dụng thuật toán học máy dựa trên lịch sử chuyến bay để dự đoán nhu cầu hành lý/suất ăn, tự động gửi gợi ý mua kèm hành lý ký gửi giá ưu đãi trước giờ bay 24h qua Push Notification, giúp tăng doanh thu dịch vụ phụ trợ (Ancillary Revenue).

