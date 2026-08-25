# Chương 1: TỔNG QUAN VỀ M_SERVICE VÀ DỊCH VỤ ĐẶT VÉ MÁY BAY TRÊN MOMO

> Bản nháp — ghép từ đoạn "Lịch sử hình thành" có sẵn trong bản báo cáo dùng chung của nhóm (`25410168`/`25410195`/`25410175 - Bao DX`, file "TÌM HIỂU VỀ HỆ THỐNG QUY TRÌNH NGHIỆP VỤ...docx") và tổng hợp từ tài liệu kiến trúc quy trình của `25410237` (`MoMo_Kien_truc_quy_trinh_Dat_ve_may_bay.docx`). Đây là chương hiện đang **TRỐNG 100%** trong `docs/MoMo.docx` (xem `plan/01_HIEN_TRANG_VA_LOI.md` mục 3).
>
> ⚠️ Các chỗ đánh dấu **[CẦN NGUỒN THẬT]** là nội dung nhóm chưa có số liệu/tài liệu xác thực — theo đúng nguyên tắc đã thống nhất (`plan/01` mục 4 phần 🔵: "Dẫn nguồn hoặc ghi rõ giả định của nhóm cho các con số chưa có nguồn"), KHÔNG tự bịa số liệu cụ thể (giấy phép, vốn điều lệ, số nhân sự, doanh thu...) — nhóm cần tự bổ sung nguồn công khai đáng tin cậy (website M_Service, thông cáo báo chí, báo cáo Ngân hàng Nhà nước) trước khi nộp.

---

## 1.1. Lịch sử hình thành

Công ty Cổ phần Dịch vụ Di động Trực tuyến (M_Service) chính thức được thành lập vào năm 2007, là đơn vị chủ quản của ví điện tử MoMo. Ban đầu, dịch vụ ra mắt vào năm 2010 dưới dạng ứng dụng trên SIM điện thoại, hợp tác cùng nhà mạng Vinaphone để cung cấp các dịch vụ nạp và chuyển tiền cơ bản. Đến năm 2014, nhóm phát triển quyết định ra mắt ứng dụng trên nền tảng điện thoại thông minh với tên gọi MoMo — viết tắt của cụm từ "Mobile Money" — gửi gắm tham vọng phổ cập dịch vụ tài chính kỹ thuật số, biến chiếc điện thoại thành ví tiền tiện lợi cho mọi người dân Việt Nam.

Qua nhiều năm phát triển, MoMo đã vươn lên trở thành một trong những siêu ứng dụng thanh toán hàng đầu Việt Nam và đạt danh hiệu kỳ lân công nghệ, cạnh tranh trực tiếp với ZaloPay, VNPay, Viettel Money và các nền tảng ví điện tử tích hợp như ShopeePay.

Trong hành trình mở rộng từ một ví điện tử thuần thanh toán sang mô hình "siêu ứng dụng" (Super App), MoMo đã tích hợp thêm nhiều dịch vụ tiện ích ngoài tài chính — trong đó có tính năng "Du lịch - Đi lại", cho phép người dùng tìm kiếm, so sánh và đặt vé máy bay nội địa/quốc tế từ nhiều hãng hàng không (Vietnam Airlines, Vietjet Air, Bamboo Airways...), cùng vé tàu, vé xe khách và đặt phòng khách sạn. Đây chính là phạm vi nghiệp vụ mà đồ án này tập trung mô hình hóa và phân tích.

## 1.2. Quy mô và lĩnh vực hoạt động

M_Service là tổ chức trung gian thanh toán được Ngân hàng Nhà nước Việt Nam cấp phép hoạt động **[CẦN NGUỒN THẬT — số giấy phép, ngày cấp]**. Lĩnh vực hoạt động chính của công ty là cung cấp dịch vụ ví điện tử MoMo, bao gồm các nhóm dịch vụ:

- **Thanh toán & chuyển tiền**: nạp/rút tiền, chuyển tiền, thanh toán hóa đơn, thanh toán tại điểm bán.
- **Dịch vụ tài chính**: ví trả sau, tiết kiệm, bảo hiểm, đầu tư liên kết đối tác.
- **Dịch vụ tiện ích đời sống & du lịch** (Super App): trong đó mảng "Du lịch - Đi lại" — nơi đặt vé máy bay là một hợp phần — là đối tượng nghiên cứu của đồ án này. Vì MoMo không tự vận hành đội bay mà đóng vai trò nền tảng trung gian, mảng đặt vé máy bay là một hệ thống nhiều quy trình phối hợp: từ trải nghiệm tìm kiếm – đặt vé – thanh toán – xuất vé của khách hàng, đến vận hành đối tác phía sau (đồng bộ dữ liệu, đối soát), và các quy trình tuân thủ, bảo mật giao dịch bắt buộc theo quy định của Ngân hàng Nhà nước và ngành hàng không.

Quy mô người dùng, doanh thu và thị phần cụ thể của M_Service **[CẦN NGUỒN THẬT]** — nhóm chưa tiếp cận được số liệu chính thức, đề nghị bổ sung từ báo cáo thường niên hoặc thông cáo báo chí công khai của công ty trước khi hoàn thiện báo cáo.

## 1.3. Cơ cấu tổ chức

Đồ án không tiếp cận được sơ đồ tổ chức chính thức của M_Service **[CẦN NGUỒN THẬT]**. Dựa trên tài liệu kiến trúc quy trình nội bộ nhóm đã tổng hợp (`25410237`, *Tìm hiểu hệ thống quy trình nghiệp vụ mảng đặt vé máy bay trên ứng dụng MoMo — Tài liệu tổng quan kiến trúc quy trình*), nhóm khái quát các bộ phận chức năng có liên quan trực tiếp đến mảng đặt vé máy bay như sau (đây là **bản đồ chức năng do nhóm tổng hợp**, không phải sơ đồ tổ chức chính thức của công ty):

| Nhóm chức năng | Bộ phận liên quan | Vai trò chính trong mảng đặt vé máy bay |
|---|---|---|
| Khách hàng (Front-office) | Bộ phận CSKH | Tiếp nhận, xử lý phản ánh, hoàn/hủy vé, hỗ trợ khách hàng |
| Đối tác & Vận hành | Đội Phát triển Đối tác, Kỹ thuật, Vận hành Sản phẩm Du lịch | Thẩm định/tích hợp hãng bay & NCC, đồng bộ giá vé và lịch bay real-time |
| Đối tác & Vận hành | Đội Vận hành, Tài chính - Kế toán | Đối soát giao dịch, thanh toán hoa hồng với hãng bay/đối tác |
| Tuân thủ & Quản trị rủi ro | Đội Pháp lý & Tuân thủ, Đội Tuân thủ & Quản trị rủi ro | Xác thực giao dịch (eKYC), phòng chống gian lận, xử lý tranh chấp theo pháp luật |
| Hỗ trợ nội bộ | Đội Sản phẩm, Marketing, Growth specialist | Cá nhân hóa ưu đãi/marketing, giám sát chất lượng dịch vụ đối tác (KPI/SLA) |

Bảng thuật ngữ tên bộ phận ở bảng trên cần được **thống nhất lại** với tên gọi đã dùng trong Chương 2–4 của báo cáo chính (ví dụ "Bộ phận về giá", "Bộ phận Tài chính/Pháp chế", "Growth specialist/Kỹ thuật") — việc thống nhất thuật ngữ toàn bài thuộc Giai đoạn 2 (`plan/00` mục 4, `plan/04` việc #4 của 25410175).
