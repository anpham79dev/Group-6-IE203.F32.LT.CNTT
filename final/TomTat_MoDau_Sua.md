# Sửa mục TÓM TẮT ĐỒ ÁN và MỞ ĐẦU (`docs/MoMo.docx`)

> Đối chiếu trước/sau, khớp với: (1) cấu trúc 5 chương mới thay vì 4 (`plan/03_CAU_TRUC_MUC_TIEU.md` mục 2), (2) phạm vi 6 quy trình mô hình hóa BPMN sâu + đúng 3 quy trình có chương Phân tích (không phải cả 6, như câu hiện tại đang ngụ ý), (3) bỏ khẳng định phỏng vấn thật MoMo. Câu "phân tích 6 quy trình... hai lăng kính" thực tế nằm ở mục **TÓM TẮT**, không phải MỞ ĐẦU như `docs/REVIEW-MoMo.md` ghi — xem phát hiện đã xác minh lại ở `plan/01_HIEN_TRANG_VA_LOI.md` mục 1.

---

## TÓM TẮT ĐỒ ÁN

**Đoạn 1 — giữ nguyên** (không có lỗi):

> "Ngành thương mại điện tử và dịch vụ du lịch trực tuyến (OTA) tại Việt Nam đang có những bước tiến vượt bậc, đặc biệt là việc tích hợp các dịch vụ này vào các siêu ứng dụng (Super App). Ví điện tử MoMo (thuộc Công ty Cổ phần Dịch vụ Di động Trực tuyến - M_Service) đã tiên phong tích hợp thành công dịch vụ đặt vé máy bay, mang lại trải nghiệm liền mạch cho hàng chục triệu người dùng. Để đạt được điều này, MoMo cần sở hữu một hệ thống quy trình nghiệp vụ phức tạp, từ quản lý đối tác, cấu hình sản phẩm đến xử lý giao dịch và hỗ trợ khách hàng."

> ⚠️ Cụm "hàng chục triệu người dùng" chưa có nguồn xác thực trong tài liệu nhóm — cần dẫn nguồn công khai hoặc đổi thành diễn đạt không có con số cụ thể trước khi nộp (xem `final/Chuong1_TongQuan.md` mục 1.2, cùng loại vấn đề).

**Đoạn 2 — hiện tại:**

> "Đồ án này tập trung nghiên cứu, mô hình hóa và phân tích hệ thống quy trình nghiệp vụ mảng đặt vé máy bay của MoMo. Thông qua việc sử dụng ký hiệu chuẩn BPMN (Business Process Model and Notation), nghiên cứu đã vẽ lại sơ đồ kiến trúc nghiệp vụ và phân tích chi tiết 6 quy trình cốt lõi, quản lý và hỗ trợ. Mỗi quy trình được đánh giá qua hai lăng kính: định tính (phân tích giá trị gia tăng VA/BVA/NVA, nhận diện lãng phí) và định lượng (tính toán thời gian chu kỳ, thời gian xử lý, chi phí nhân sự và hiệu suất). Kết quả của đồ án cung cấp bức tranh toàn cảnh về cách MoMo vận hành mảng vé máy bay, từ đó đề xuất các hướng tối ưu hóa tự động hóa nhằm nâng cao trải nghiệm khách hàng và giảm thiểu chi phí vận hành."

**Vấn đề:** câu "phân tích chi tiết 6 quy trình... Mỗi quy trình được đánh giá qua hai lăng kính [định tính + định lượng]" ngụ ý cả 6 quy trình đều có chương Phân tích đầy đủ — nhưng theo rubric và phạm vi đã chốt, chỉ **3/6** quy trình có chương Phân tích (định tính + định lượng); 6 quy trình chỉ đảm bảo có BPMN + Phương pháp thực hiện.

**Đoạn 2 — sửa thành:**

> "Đồ án này tập trung nghiên cứu, mô hình hóa và phân tích hệ thống quy trình nghiệp vụ mảng đặt vé máy bay của MoMo. Thông qua việc sử dụng ký hiệu chuẩn BPMN (Business Process Model and Notation), nghiên cứu đã vẽ lại sơ đồ kiến trúc nghiệp vụ cho 10 quy trình (4 Quản lý, 3 Cốt lõi, 3 Hỗ trợ), trong đó mô hình hóa BPMN chi tiết cho 6 quy trình đại diện (2 Quản lý, 2 Cốt lõi, 2 Hỗ trợ). Trong số đó, 3 quy trình được phân tích chuyên sâu qua hai lăng kính: định tính (phân tích giá trị gia tăng VA/BVA/NVA, nhận diện lãng phí) và định lượng (tính toán thời gian chu kỳ, thời gian xử lý, chi phí nhân sự và hiệu suất). Kết quả của đồ án cung cấp bức tranh toàn cảnh về cách MoMo vận hành mảng vé máy bay, từ đó đề xuất các hướng tối ưu hóa tự động hóa nhằm nâng cao trải nghiệm khách hàng và giảm thiểu chi phí vận hành."

---

## MỞ ĐẦU

**Đoạn 1, 2 — giữ nguyên** (không có lỗi):

> "Trong kỷ nguyên chuyển đổi số, sự ra đời của các 'siêu ứng dụng' đã làm thay đổi hoàn toàn thói quen tiêu dùng. MoMo không chỉ dừng lại ở dịch vụ thanh toán mà đã trở thành nền tảng đáp ứng mọi nhu cầu hàng ngày, trong đó có du lịch - đi lại. Việc bán vé máy bay trực tiếp trên ứng dụng đòi hỏi MoMo phải kết nối hệ thống phức tạp với các hãng hàng không, đại lý vé (NCC), đồng thời quản lý luồng dữ liệu khổng lồ về giá, hạng vé, thông tin khách hàng và giao dịch tài chính.
>
> Mục tiêu của đề tài là ứng dụng lý thuyết Hệ thống quản trị quy trình nghiệp vụ (BPMS) để rà soát lại kiến trúc quy trình của mảng kinh doanh này. Từ đó, xây dựng các mô hình BPMN 'As-Is' (hiện tại) và thực hiện phân tích chuyên sâu nhằm tìm ra các điểm nghẽn (bottlenecks) và các bước không tạo ra giá trị (NVA)."

**Đoạn 3 (danh sách chương) — hiện tại:**

> "Đồ án được chia thành 4 chương:
> Chương 1: Giới thiệu tổng quan về M_Service và dịch vụ đặt vé trên MoMo.
> Chương 2: Sơ đồ kiến trúc hệ thống quy trình nghiệp vụ.
> Chương 3: Mô hình hóa chi tiết bằng BPMN và phân tích (định tính, định lượng) các quy trình.
> Chương 4: Kết luận và đề xuất cải tiến."

**Vấn đề:** vẫn còn cấu trúc 4 chương cũ (gộp BPMN + Phân tích vào 1 chương), trong khi cấu trúc mục tiêu đã chốt là 5 chương tách riêng (khớp đúng 2 tiêu chí rubric tách biệt 2.0 và 4.0 — xem `plan/03_CAU_TRUC_MUC_TIEU.md` mục 2, ghi chú cuối). Ngoài ra Chương 2 hiện tại không chỉ có "sơ đồ kiến trúc" mà còn liệt kê mô tả 10 quy trình.

**Đoạn 3 — sửa thành:**

> "Đồ án được chia thành 5 chương:
> Chương 1: Tổng quan về M_Service và dịch vụ đặt vé máy bay trên MoMo.
> Chương 2: Liệt kê và mô tả các quy trình nghiệp vụ, kèm sơ đồ kiến trúc quy trình.
> Chương 3: Mô hình hóa chi tiết các quy trình bằng BPMN.
> Chương 4: Phân tích các quy trình (định tính và định lượng).
> Chương 5: Kết luận."

---

## Lỗi định dạng liên quan (Giai đoạn 2, ghi chú để không quên)

Heading "Chương 1" trong `docs/MoMo.docx` hiện bị lỗi định dạng — dòng `[Heading 1]` trống rồi mới đến dòng text tiêu đề không có style (xem `plan/01_HIEN_TRANG_VA_LOI.md` phát hiện mới #4). Cần sửa trực tiếp trong Word khi ghép nội dung Chương 1 mới (`final/Chuong1_TongQuan.md`) vào — gán đúng style Heading 1 cho dòng tiêu đề, không thuộc phạm vi sửa bằng văn bản thuần ở đây.
