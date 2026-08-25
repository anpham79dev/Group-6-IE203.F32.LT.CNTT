# BẢNG TIÊU CHÍ ĐÁNH GIÁ ĐỒ ÁN MÔN HỌC — HỆ THỐNG QUẢN TRỊ QUY TRÌNH NGHIỆP VỤ

**Đề tài:** TÌM HIỂU VỀ HỆ THỐNG QUY TRÌNH NGHIỆP VỤ MẢNG ĐẶT VÉ MÁY BAY TRÊN ỨNG DỤNG MOMO (THUỘC CÔNG TY CỔ PHẦN DỊCH VỤ DI ĐỘNG TRỰC TUYẾN - M_SERVICE)  
**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung  
**Đơn vị đào tạo:** Trường Đại học Công nghệ Thông tin – Trung tâm Phát triển Công nghệ Thông tin (UIT - ĐHQG-HCM)

---

## PHẦN I: MA TRẬN ĐỐI CHIẾU TIÊU CHÍ RUBRIK VÀ HIỆN TRẠNG ĐỒ ÁN

| STT | Tiêu chí đánh giá theo Rubric | Điểm tối đa | Mức độ đạt chuẩn chi tiết | Hiện trạng báo cáo đồ án nhóm MoMo | Tự đánh giá | Điểm đạt |
|---|---|---|---|---|---|---|
| **1** | **Liệt kê quy trình nghiệp vụ** | **10.0** | **Tối thiểu 10 quy trình (≥3 Quản lý, ≥3 Cốt lõi, ≥3 Hỗ trợ); Nêu đủ: Tác nhân, Các bước bằng lời, Khách hàng, Kết quả đầu ra; Vẽ sơ đồ kiến trúc quy trình** | **Đủ 10 quy trình (4 Quản lý, 3 Cốt lõi, 3 Hỗ trợ); Mô tả chi tiết từng bước, mục tiêu, tác nhân, kết quả; Sơ đồ kiến trúc 3 tầng chuẩn Canvas** | **Đạt tối đa** | **10.0** |
| 1.1 | - Nhóm Quy trình Quản lý (Management) | 3.0 | Ít nhất 3 quy trình quản lý định hướng chiến lược | 4 quy trình: Quản lý hạng vé, Quản trị giá & KM, Quản trị danh mục đối tác NCC, Quản trị rủi ro giao dịch & SLA | Đạt xuất sắc | 3.0 |
| 1.2 | - Nhóm Quy trình Cốt lõi (Core) | 3.0 | Ít nhất 3 quy trình cốt lõi tạo giá trị trực tiếp cho khách hàng | 3 quy trình: Tìm kiếm - đặt chỗ - thanh toán vé, Mua thêm dịch vụ tiện ích sau đặt chỗ, Đổi chuyến bay | Đạt xuất sắc | 3.0 |
| 1.3 | - Nhóm Quy trình Hỗ trợ (Support) | 3.0 | Ít nhất 3 quy trình hỗ trợ vận hành hệ thống | 3 quy trình: Hỗ trợ khách hàng & tiếp nhận phản hồi, Tự động hóa xuất hóa đơn VAT, Quản lý vé đã mua | Đạt xuất sắc | 3.0 |
| 1.4 | - Sơ đồ Kiến trúc quy trình (Canvas) | 1.0 | Sơ đồ phân tầng trực quan chuẩn BPM | Sơ đồ hình mái nhà (House model) phân tầng rõ 3 lớp Management - Core - Support | Đạt chuẩn | 1.0 |
| **2** | **Mô hình hóa quy trình (BPMN 2.0)** | **10.0** | **Mô hình hóa 6 quy trình (2 Quản lý, 2 Cốt lõi, 2 Hỗ trợ); Độ phức tạp cổng điều kiện: >7 gateways (1đ/qt), >5 (0.75đ), >3 (0.5đ); Đúng chuẩn Split-Join & ký hiệu** | **Mô hình hóa đủ 6 quy trình chi tiết; Cả 6 sơ đồ đều đạt 8-19 Gateways (>7 đạt điểm tối đa); Cặp Split-Join tách bạch tường minh, phân làn Swimlane rõ ràng** | **Đạt tối đa** | **10.0** |
| 2.1 | - 2 Quy trình Quản lý chi tiết | 3.0 | 2 quy trình quản lý có độ phức tạp cao (>7 gateways) | Quản trị giá & khuyến mãi (9 gateways), Quản lý hạng vé máy bay (10 gateways) | Đạt tối đa | 3.0 |
| 2.2 | - 2 Quy trình Cốt lõi chi tiết | 3.0 | 2 quy trình cốt lõi có độ phức tạp cao (>7 gateways) | Tìm kiếm & thanh toán đặt vé (19 gateways), Đổi chuyến bay trên MoMo (10 gateways) | Đạt tối đa | 3.0 |
| 2.3 | - 2 Quy trình Hỗ trợ chi tiết | 3.0 | 2 quy trình hỗ trợ có độ phức tạp cao (>7 gateways) | Hỗ trợ CSKH & tra soát ngoại lệ (9 gateways), Tự động hóa xuất hóa đơn VAT (8 gateways) | Đạt tối đa | 3.0 |
| 2.4 | - Kỹ thuật BPMN 2.0 & Tính đúng đắn | 1.0 | Đúng chuẩn cú pháp, không Deadlock, Livelock, phân biệt Sequence Flow và Message Flow | Sơ đồ kiểm tra không lỗi logic, luồng điều khiển liền mạch, xuất file mã nguồn XML chuẩn | Đạt chuẩn | 1.0 |
| **3** | **Phương pháp thực hiện (Discovery)** | **10.0** | **Bằng chứng: Mô tả quy trình, Sơ đồ tổ chức, Kế hoạch làm việc, Thuật ngữ & sổ tay, Biểu mẫu; Phỏng vấn: ≥20 câu hỏi (10 định tính: 5 cấu trúc + 5 phi cấu trúc; 10 định lượng: 5 cấu trúc + 5 phi cấu trúc)** | **Đầy đủ 5 cấu phần bằng chứng cho các quy trình; Bộ phỏng vấn ma trận 2x2 đủ 20 câu hỏi chuẩn xác kèm tuyên bố phương pháp minh bạch, liêm chính** | **Đạt tối đa** | **10.0** |
| 3.1 | - Dựa trên bằng chứng (Evidence-based) | 4.0 | Mô tả quy trình, Sơ đồ tổ chức, Kế hoạch tuần, Thuật ngữ nghiệp vụ, Bộ biểu mẫu tác nghiệp | Mỗi quy trình có đủ 5 cấu phần: mô tả quy trình, bảng phân định trách nhiệm, kế hoạch làm việc theo mốc, bảng thuật ngữ nghiệp vụ hàng không (GDS, PNR, EMD...) và bộ 3-4 biểu mẫu tác nghiệp | Đạt tối đa | 4.0 |
| 3.2 | - Phỏng vấn định tính (10 câu) | 3.0 | 5 câu hỏi có cấu trúc (trắc nghiệm) + 5 câu hỏi không cấu trúc (tự luận mở) | 5 câu trắc nghiệm xác định điểm nghẽn/hình thức test + 5 câu tự luận đào sâu cơ chế phối hợp liên phòng ban | Đạt chuẩn | 3.0 |
| 3.3 | - Phỏng vấn định lượng (10 câu) | 3.0 | 5 câu hỏi có cấu trúc (khoảng số liệu) + 5 câu hỏi không cấu trúc (thu thập số liệu cụ thể) | 5 câu trắc nghiệm khoảng thời gian/tỷ lệ rework + 5 câu thu thập số liệu chi phí, cycle time, CSAT | Đạt chuẩn | 3.0 |
| **4** | **Phân tích quy trình (Process Analysis)** | **10.0** | **Định tính: VA/BVA/NVA (Liệt kê, Mô tả, Khắc phục), Lãng phí (Move/Hold/Overdo); Bên liên quan: Chọn 1 trong 3 (Pareto / Root-cause / Fishbone); Định lượng: Thời gian (công thức rework T/(1-r)), Chi phí, Chất lượng** | **Phân tích chuyên sâu 3 quy trình trọng tâm; Bảng VA đủ 3 cột Liệt kê - Mô tả - Khắc phục; Nhận diện đủ Move-Hold-Overdo; Đầy đủ biểu đồ Pareto 80/20 và Xương cá Fishbone; Công thức định lượng chuẩn xác** | **Đạt tối đa** | **10.0** |
| 4.1 | - Phân tích định tính (VA/BVA/NVA & Lãng phí) | 3.5 | Phân loại hoạt động chi tiết, có giải pháp loại bỏ NVA và tối ưu hóa lãng phí | Bảng VA 16-23 bước cho từng quy trình; phân loại lãng phí Move/Hold/Overdo kèm phương án khắc phục công nghệ | Đạt tối đa | 3.5 |
| 4.2 | - Phân tích bên liên quan (Pareto / Fishbone) | 2.5 | Sử dụng mô hình trực quan xác định nguyên nhân gốc rễ và mức độ ưu tiên | Biểu đồ Pareto 9 nhóm vấn đề hậu mãi (80/20) + Sơ đồ Xương cá (Ishikawa) phân tích tỷ lệ thoát phiên tìm kiếm | Đạt tối đa | 2.5 |
| 4.3 | - Phân tích định lượng (Thời gian, Chi phí, RTY) | 4.0 | Tính thời gian chu kỳ CT (công thức nhánh lặp T/(1-r)), hiệu suất chu kỳ PCE, chi phí theo kịch bản, chất lượng RTY | Tính toán chi tiết Happy path vs Rework path; PCE quy trình Quản trị giá 45,28%, hiệu suất thời gian quy trình Tìm kiếm 95,9%, RTY 39,01%; chi phí nhân sự và chi phí hạ tầng truy vấn | Đạt tối đa | 4.0 |
| **5** | **Trình bày & Báo cáo** | **10.0** | **Báo cáo Word theo mẫu UIT; Mục lục tự động, Danh mục hình/bảng; Label hình ở DƯỚI, label bảng ở TRÊN; Danh mục từ viết tắt; Bảng phân công công việc chi tiết; Tài liệu tham khảo chuẩn** | **Bố cục 5 chương liền mạch, chuẩn font Times New Roman 12pt, dãn dòng 1.25; Đúng quy chuẩn nhãn bảng/hình; Đầy đủ 34 từ viết tắt; Bảng phân công minh bạch 8 thành viên; Tài liệu tham khảo chuẩn học thuật** | **Đạt tối đa** | **10.0** |
| 5.1 | - Quy chuẩn định dạng báo cáo | 4.0 | Font chữ đồng nhất, lề chuẩn 20-25mm, tiêu đề hình/bảng đúng quy ước | Báo cáo trình bày sạch đẹp, phân cấp Heading 1-4 chuẩn mực, bảng biểu định dạng chuyên nghiệp | Đạt chuẩn | 4.0 |
| 5.2 | - Cấu trúc mục lục & Danh mục phụ trợ | 3.0 | Mục lục tự động, Danh mục hình, Danh mục bảng, Danh mục từ viết tắt | Đầy đủ các danh mục mở đầu hỗ trợ tra cứu nhanh | Đạt chuẩn | 3.0 |
| 5.3 | - Bảng phân công & Liêm chính học thuật | 3.0 | Bảng phân công trách nhiệm rõ ràng từng thành viên, trích dẫn tài liệu tham khảo chuẩn | Bảng phân công ghi nhận đóng góp thực tế của 8 thành viên kèm tuyên bố sử dụng dữ liệu giả định minh bạch | Đạt chuẩn | 3.0 |
| **TỔNG CỘNG** | **TỔNG ĐIỂM ĐÁNH GIÁ TOÀN DIỆN ĐỒ ÁN** | **50.0** | **ĐÁNH GIÁ CHUNG: BÁO CÁO VÀ MÔ HÌNH BPMN ĐẠT MỨC XUẤT SẮC** | | **ĐẠT XUẤT SẮC** | **50.0 / 50.0 (10 / 10)** |

---

## PHẦN II: BẢNG TỔNG HỢP ĐỘ PHỨC TẠP CÁC SƠ ĐỒ BPMN ĐÃ MÔ HÌNH HÓA

| STT | Tên quy trình nghiệp vụ | Nhóm quy trình | Số làn phân quyền (Swimlanes) | Số cổng điều kiện (Gateways) | Tiêu chí Rubric (>7 Gateways) | Đánh giá kỹ thuật BPMN |
|---|---|---|---|---|---|---|
| 1 | **Quản trị giá, khuyến mãi và chính sách hiển thị giá** | Quản lý (Management) | 6 Lanes (Hãng bay/NCC, Bộ phận Giá, Marketing, Tài chính/Pháp chế, Kỹ thuật, App MoMo) | **9 Gateways** | **Đạt tối đa (1.0đ)** | Cặp Split-Join đóng mở chuẩn xác, có nhánh xử lý hồ sơ thiếu, điều chỉnh chiến dịch và sửa lỗi hiển thị |
| 2 | **Quản lý hạng vé máy bay** | Quản lý (Management) | 4 Lanes (Hãng bay/NCC, Business Development, Ticketing, App MoMo) | **10 Gateways** | **Đạt tối đa (1.0đ)** | Phân luồng API quốc tế (giới hạn 2 lần thử lại) và chuẩn hóa dữ liệu nội địa thủ công; tách riêng End Event "tạm hoãn công bố" khỏi nhánh lỗi kỹ thuật |
| 3 | **Tìm kiếm, lựa chọn hành trình, thanh toán và xuất vé** | Cốt lõi (Core) | 4 Lanes (Khách hàng, App MoMo/Core, CSKH, Hãng bay/GDS) | **19 Gateways** | **Đạt tối đa (1.0đ)** | Bao quát toàn bộ luồng khứ hồi/1 chiều, 4 dịch vụ tiện ích bổ sung (mỗi tiện ích có cặp cổng rẽ – cổng gộp riêng) và xử lý ngoại lệ giao dịch Pending/Rollback |
| 4 | **Đổi chuyến bay trên MoMo** | Cốt lõi (Core) | 6 Lanes (Khách hàng, Client App, Backend Travel, Cổng thanh toán, CSKH, Hãng bay) | **10 Gateways** | **Đạt tối đa (1.0đ)** | Kiểm tra điều kiện vé, tình trạng chỗ, đồng thuận mức phí, xác thực bảo mật, kết quả thanh toán, kênh tái phát hành (tự động/thủ công) và xử lý ngoại lệ hết chỗ (hoàn 100% phí đổi) |
| 5 | **Hỗ trợ khách hàng và tiếp nhận phản hồi / tra soát** | Hỗ trợ (Support) | 4 Lanes (Khách hàng, App MoMo, CSKH, Hãng bay/NCC) | **9 Gateways** | **Đạt tối đa (1.0đ)** | Phân loại đa kênh (App/Tổng đài), phân hạng VIP/thường, giải quyết nội bộ hoặc tra soát đối tác |
| 6 | **Tự động hóa xuất hóa đơn điện tử (VAT)** | Hỗ trợ (Support) | 6 Lanes (Khách hàng, App MoMo, Core M_Service, CSKH, Kế toán, Hệ thống hóa đơn điện tử) | **8 Gateways** | **Đạt tối đa (1.0đ)** | Kiểm soát chốt chặn thời hạn, đối soát dữ liệu 3 bên và gọi API phát hành hóa đơn tự động |

---

## PHẦN III: BẢNG PHÂN CÔNG VÀ ĐÓNG GÓP THỰC TẾ THÀNH VIÊN NHÓM

| STT | MSSV | Họ và tên | Vai trò trong nhóm | Nhiệm vụ & Đóng góp nội dung cụ thể vào đồ án |
|---|---|---|---|---|
| 1 | 25410175 | Đinh Xuân Bảo | Nhóm trưởng | Quản lý tiến độ đồ án, tổng hợp và biên tập báo cáo chính, rà soát toàn diện, xây dựng 5 sơ đồ BPMN gốc (Quản trị giá, Quản lý hạng vé, Tìm kiếm vé, Mua thêm dịch vụ, Xuất hóa đơn) |
| 2 | 25410167 | Vũ Thị Nhân Ái | Thành viên nhóm | Thu thập tài liệu quy định pháp lý (Thông tư NHNN về ví điện tử), rà soát thuật ngữ chuyên ngành và chính sách thuế VAT trong thương mại điện tử |
| 3 | 25410168 | Phạm Ngọc Bảo An | Thành viên nhóm | Thiết kế khung câu hỏi phỏng vấn chuẩn 2x2, xây dựng khung phân tích giá trị gia tăng (VA/BVA/NVA) và nghiên cứu lịch sử hình thành MoMo |
| 4 | 25410191 | Hồ Nguyễn Bảo Duy | Thành viên nhóm | Khảo sát thực tế tính năng đặt vé trên ứng dụng MoMo, thu thập bằng chứng giao diện, biên bản kiểm thử và luồng thanh toán |
| 5 | 25410195 | Nguyễn Huỳnh Mỹ Duyên | Thành viên nhóm | Rà soát cấu trúc báo cáo theo mẫu chuẩn UIT, kiểm tra tính đồng bộ danh mục từ viết tắt và định dạng bảng biểu, hình vẽ |
| 6 | 25410206 | Nguyễn Đắc Hiển | Thành viên nhóm | Xây dựng 3 báo cáo chuyên sâu mảng Tìm kiếm & Thanh toán vé, thiết kế mô hình BPMN Core01/02/03, tính toán định lượng thời gian chu kỳ ($CT$) và chi phí vận hành |
| 7 | 25410223 | Lê Quốc Hưng | Thành viên nhóm | Phân tích và mô hình hóa quy trình Đổi chuyến bay, mô tả chi tiết chính sách phí đổi, cấu trúc phí chênh lệch và tái phát hành vé (Re-issue) |
| 8 | 25410237 | Nguyễn Mậu An Khương | Thành viên nhóm | Xây dựng báo cáo Hỗ trợ khách hàng & Tra soát lỗi, quy trình Quản trị danh mục đối tác NCC, phân tích biểu đồ Pareto (80/20) và kiến trúc 10 quy trình |
