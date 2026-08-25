# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN

TRUNG TÂM PHÁT TRIỂN CÔNG NGHỆ THÔNG TIN

BÁO CÁO ĐỒ ÁN CUỐI KỲ

HỆ THỐNG QUẢN TRỊ QUY TRÌNH NGHIỆP VỤ

**Đề tài:** TÌM HIỂU VỀ HỆ THỐNG QUY TRÌNH NGHIỆP VỤ MẢNG ĐẶT VÉ MÁY BAY TRÊN ỨNG DỤNG MOMO (THUỘC CÔNG TY CỔ PHẦN DỊCH VỤ DI ĐỘNG TRỰC TUYẾN - M_SERVICE)

**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung

**Nhóm sinh viên thực hiện:**

| STT | MSSV | Họ tên | Vai trò |
|---|---|---|---|
| 1 | 25410175 | Đinh Xuân Bảo | Nhóm trưởng |
| 2 | 25410195 | Nguyễn Huỳnh Mỹ Duyên | Thành viên nhóm |
| 3 | 25410167 | Vũ Thị Nhân Ái | Thành viên nhóm |
| 4 | 25410237 | Nguyễn Mậu An Khương | Thành viên nhóm |
| 5 | 25410168 | Phạm Ngọc Bảo An | Thành viên nhóm |
| 6 | 25410191 | Hồ Nguyễn Bảo Duy | Thành viên nhóm |
| 7 | 25410206 | Nguyễn Đắc Hiển | Thành viên nhóm |
| 8 | 25410223 | Lê Quốc Hưng | Thành viên nhóm |

TP. Hồ Chí Minh, tháng 08 năm 2026

*(⚠️ Nhóm xác nhận lại ngày nộp thật trước khi in — bản gốc ghi "tháng 07", đã tạm sửa thành tháng hiện tại, xem `plan/01` mục 3.8)*

MỤC LỤC *(chèn field tự động trong Word — References → Table of Contents)*

DANH MỤC HÌNH VẼ *(chèn field tự động)*

DANH MỤC BẢNG *(chèn field tự động)*

DANH MỤC TỪ VIẾT TẮT *(xem `final/DanhMucTuVietTat.md`)*

---

## TÓM TẮT ĐỒ ÁN

Ngành thương mại điện tử và dịch vụ du lịch trực tuyến (OTA) tại Việt Nam đang có những bước tiến vượt bậc, đặc biệt là việc tích hợp các dịch vụ này vào các siêu ứng dụng (Super App). Ví điện tử MoMo (thuộc Công ty Cổ phần Dịch vụ Di động Trực tuyến - M_Service) đã tiên phong tích hợp thành công dịch vụ đặt vé máy bay, mang lại trải nghiệm liền mạch cho người dùng. Để đạt được điều này, MoMo cần sở hữu một hệ thống quy trình nghiệp vụ phức tạp, từ quản lý đối tác, cấu hình sản phẩm đến xử lý giao dịch và hỗ trợ khách hàng.

Đồ án này tập trung nghiên cứu, mô hình hóa và phân tích hệ thống quy trình nghiệp vụ mảng đặt vé máy bay của MoMo. Thông qua việc sử dụng ký hiệu chuẩn BPMN (Business Process Model and Notation), nghiên cứu đã vẽ lại sơ đồ kiến trúc nghiệp vụ cho 10 quy trình (4 Quản lý, 3 Cốt lõi, 3 Hỗ trợ), trong đó mô hình hóa BPMN chi tiết cho 6 quy trình đại diện (2 Quản lý, 2 Cốt lõi, 2 Hỗ trợ). Trong số đó, 3 quy trình được phân tích chuyên sâu qua hai lăng kính: định tính (phân tích giá trị gia tăng VA/BVA/NVA, nhận diện lãng phí) và định lượng (tính toán thời gian chu kỳ, thời gian xử lý, chi phí nhân sự và hiệu suất). Kết quả của đồ án cung cấp bức tranh toàn cảnh về cách MoMo vận hành mảng vé máy bay, từ đó đề xuất các hướng tối ưu hóa tự động hóa nhằm nâng cao trải nghiệm khách hàng và giảm thiểu chi phí vận hành.

## MỞ ĐẦU

Trong kỷ nguyên chuyển đổi số, sự ra đời của các "siêu ứng dụng" đã làm thay đổi hoàn toàn thói quen tiêu dùng. MoMo không chỉ dừng lại ở dịch vụ thanh toán mà đã trở thành nền tảng đáp ứng mọi nhu cầu hàng ngày, trong đó có du lịch - đi lại. Việc bán vé máy bay trực tiếp trên ứng dụng đòi hỏi MoMo phải kết nối hệ thống phức tạp với các hãng hàng không, đại lý vé (NCC), đồng thời quản lý luồng dữ liệu khổng lồ về giá, hạng vé, thông tin khách hàng và giao dịch tài chính.

Mục tiêu của đề tài là ứng dụng lý thuyết Hệ thống quản trị quy trình nghiệp vụ (BPMS) để rà soát lại kiến trúc quy trình của mảng kinh doanh này. Từ đó, xây dựng các mô hình BPMN "As-Is" (hiện tại) và thực hiện phân tích chuyên sâu nhằm tìm ra các điểm nghẽn (bottlenecks) và các bước không tạo ra giá trị (NVA).

Đồ án được chia thành 5 chương:

Chương 1: Tổng quan về M_Service và dịch vụ đặt vé máy bay trên MoMo.

Chương 2: Liệt kê và mô tả các quy trình nghiệp vụ, kèm sơ đồ kiến trúc quy trình.

Chương 3: Mô hình hóa chi tiết các quy trình bằng BPMN.

Chương 4: Phân tích các quy trình (định tính và định lượng).

Chương 5: Kết luận.

> ⚠️ Đồ án **không có điều kiện phỏng vấn trực tiếp nhân sự nội bộ MoMo**. Mọi bộ câu hỏi phỏng vấn và số liệu định lượng trình bày trong các chương sau đều mang tính **mô phỏng/giả định**, xây dựng dựa trên nghiên cứu quy trình công khai, trải nghiệm sử dụng thực tế và suy luận nghiệp vụ có căn cứ — không phải số liệu vận hành chính thức do MoMo công bố. Điều này được ghi chú lại ở đầu mỗi phần "Phỏng vấn" trong Chương 3.
