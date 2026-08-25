# Chương 5: KẾT LUẬN

> Bản nháp tổng hợp (không copy nguyên xi) từ mục Kết luận có sẵn trong 3 báo cáo con chất lượng cao: `25410206/MoMo_Core01_TimKiem_va_SoSanhChuyenBay.docx` (Chương 9), `25410237/MoMo_HauMai_va_XuLyNgoaiLe.docx` (Chương 8), `25410237/MoMo_Quan_tri_danh_muc_hang_bay_va_doi_tac_cung_ung.docx` (Chương 8). Đây là chương hiện đang **TRỐNG 100%**, là dòng cuối cùng của `docs/MoMo.docx` (xem `plan/01_HIEN_TRANG_VA_LOI.md` mục 3). Số liệu cụ thể được giữ lại làm minh họa/dẫn chứng cho lập luận, không phải để copy nguyên bảng.

---

## 5.1. Kết quả đạt được

Đồ án đã xây dựng sơ đồ kiến trúc quy trình nghiệp vụ mảng đặt vé máy bay trên MoMo theo 3 nhóm Quản lý – Cốt lõi – Hỗ trợ (10 quy trình), trong đó mô hình hóa chi tiết bằng BPMN cho 6 quy trình đại diện (2 Quản lý: Quản trị giá – khuyến mãi, Quản trị danh mục hãng bay và đối tác NCC; 2 Cốt lõi: Tìm kiếm – lựa chọn hành trình – thanh toán và xác nhận đặt vé, Đổi chuyến bay; 2 Hỗ trợ: Hỗ trợ khách hàng và tiếp nhận phản hồi, Xuất hóa đơn), và phân tích sâu theo hai lăng kính định tính – định lượng cho 3 trong số 6 quy trình đó (Tìm kiếm..., Hỗ trợ khách hàng..., Quản trị giá...).

Kết quả phân tích ở các quy trình đã hoàn thiện cho thấy một số mẫu hình chung, lặp lại xuyên suốt nhiều quy trình khác nhau của mảng đặt vé máy bay:

- **Giá trị gia tăng tập trung ở khâu xử lý dữ liệu và ra quyết định**, trong khi phần lớn hoạt động không tạo giá trị (NVA) đều là các bước sửa lỗi/rework có thể loại bỏ bằng thiết kế lại quy trình hoặc bổ sung kiểm soát chất lượng đầu vào — ví dụ quy trình Tìm kiếm & so sánh chuyến bay ghi nhận 5 hoạt động VA, 8 hoạt động BVA và 3 hoạt động NVA đều thuộc dạng sửa lỗi.
- **Lãng phí chủ yếu thuộc hai nhóm Hold và Overdo.** Nhóm Hold — thời gian chờ phản hồi/xác minh từ hãng bay hoặc đối tác bên ngoài — xuất hiện lặp lại ở cả quy trình hậu mãi (thời gian chờ xác minh giao dịch lỗi) lẫn quy trình quản trị đối tác (thời gian chờ đối tác phản hồi kế hoạch khắc phục, tối đa 30 ngày). Đây là dạng lãng phí nằm ngoài tầm kiểm soát trực tiếp của MoMo, khác với nhóm Overdo (áp dụng quy trình kiểm soát/thẩm định đầy đủ cho cả những trường hợp đã có tiền lệ xử lý) — vốn hoàn toàn có thể cải thiện bằng nội lực.
- **Hiệu suất thời gian (process time / cycle time) chênh lệch lớn giữa các quy trình phụ thuộc mức độ lệ thuộc vào bên ngoài**: quy trình Tìm kiếm & so sánh chuyến bay (chủ yếu xử lý nội bộ, gọi API song song) đạt hiệu suất thời gian khoảng 95,9%; trong khi các quy trình có bước chờ đối tác phản hồi (tra soát giao dịch lỗi, rà soát đối tác) chỉ đạt hiệu suất khoảng 43–69%. Điều này cho thấy nút thắt lớn nhất của hệ thống không nằm ở năng lực xử lý nội bộ của MoMo mà ở sự phối hợp và tốc độ phản hồi của các đối tác/hãng bay bên ngoài.
- **Nguyên nhân gốc rễ được xác định qua phân tích Pareto và sơ đồ xương cá** đều quy về một số nhóm lặp lại: thiếu chuẩn hóa/tự động hóa trong trao đổi dữ liệu với đối tác, thiếu SLA nội bộ rõ ràng, và hạn chế trong hệ thống đo lường/giám sát vận hành theo thời gian thực.

## 5.2. Hạn chế của đồ án

- Do không tiếp cận được dữ liệu vận hành nội bộ thực tế và không có điều kiện phỏng vấn trực tiếp nhân sự của M_Service, **toàn bộ số liệu định lượng trong báo cáo là số liệu minh họa/giả định của nhóm**, được xây dựng dựa trên bằng chứng gián tiếp (trải nghiệm sử dụng ứng dụng thực tế, tài liệu hướng dẫn công khai của MoMo, quy định của Ngân hàng Nhà nước, và đối chiếu thông lệ ngành thương mại điện tử/OTA) thay vì số liệu vận hành chính thức.
- Mô hình BPMN phản ánh cách nhóm hiểu quy trình dựa trên bằng chứng công khai, có thể khác biệt so với thiết kế thực tế bên trong hệ thống của MoMo — đặc biệt ở các bước kỹ thuật nội bộ (cơ chế bộ đệm dữ liệu giá, cách điều phối truy vấn nhà cung ứng, logic xử lý ngoại lệ chi tiết).
- Tại thời điểm hoàn thiện báo cáo này, một số quy trình trong phạm vi 6 quy trình đầu tư sâu (Đổi chuyến bay, Xuất hóa đơn) vẫn đang trong quá trình hoàn thiện Phương pháp thực hiện — xem tình trạng cập nhật tại `plan/01_HIEN_TRANG_VA_LOI.md` mục 4.

## 5.3. Hướng phát triển

- Nếu có điều kiện tiếp cận phỏng vấn trực tiếp các đội ngũ vận hành liên quan (CSKH, Vận hành Sản phẩm Du lịch, Bộ phận về giá, Tài chính/Pháp chế) của MoMo, nhóm có thể hiệu chỉnh lại số liệu định lượng và mô hình BPMN cho sát với thực tế vận hành hơn, đồng thời xác thực các giả định đã đặt ra trong đồ án.
- Mở rộng phạm vi mô hình hóa và phân tích sâu sang các quy trình còn lại (Quản lý vé đã mua, Quản trị rủi ro giao dịch góc độ SLA/điều khoản) để có bức tranh đầy đủ hơn về toàn bộ mảng đặt vé máy bay.
- Ưu tiên triển khai các đề xuất cải tiến có chi phí thấp và nằm hoàn toàn trong tầm kiểm soát nội bộ của MoMo trước (bổ sung hệ thống đo lường hành vi người dùng, chuẩn hóa checklist/SLA nội bộ), sau đó mới đến các cải tiến phụ thuộc sự phối hợp của hãng bay/đối tác bên ngoài — vì đây là nhóm lãng phí (Hold) khó kiểm soát trực tiếp nhất theo phát hiện xuyên suốt đồ án.
