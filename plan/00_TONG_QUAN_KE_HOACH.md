# KẾ HOẠCH HOÀN THIỆN ĐỒ ÁN — MoMo Flight Booking BPM
> Môn: Hệ thống Quản trị Quy trình Nghiệp vụ — IE203.F32.LT.CNTT
> Lập kế hoạch: 25/08/2026 — dựa trên rà soát toàn bộ: Rubric chấm điểm, 8 chương bài giảng, đồ án tham khảo CellPhones.pdf, báo cáo chính `docs/MoMo.docx`, và **toàn bộ bài làm rời rạc trong 7 thư mục thành viên**.

**Đọc các file khác trong thư mục này theo thứ tự:**
1. `01_HIEN_TRANG_VA_LOI.md` — đối chiếu lỗi cũ (REVIEW-MoMo.md) + lỗi mới phát hiện, cây heading hiện tại
2. `02_NGUYEN_LIEU_THANH_VIEN.md` — bài làm sẵn có của từng thành viên, cái nào dùng được
3. `03_CAU_TRUC_MUC_TIEU.md` — cấu trúc báo cáo cuối cùng, đối chiếu rubric + CellPhones.pdf
4. `04_PHAN_CONG_CONG_VIEC.md` — bảng phân công chi tiết, ai làm gì, lấy nguyên liệu từ đâu
5. `05_KIEM_TRA_TUAN_THU_RUBRIC.md` — **kiểm tra tuân thủ**: bài làm thành viên đối chiếu chính xác từng câu chữ rubric/bài giảng, chỉ ra chỗ sai lệch cần sửa trước khi gộp

## ⚠️ Nguyên tắc nguồn tin cậy (quan trọng, áp dụng cho toàn bộ kế hoạch)

**Rubric chấm điểm + tài liệu bài giảng (`docs/Bai_Giang/chap01-08.pdf`) là nguồn chân lý DUY NHẤT.** Bài làm của các thành viên trong 7 thư mục chỉ là **nguyên liệu thô**, không mặc định là đúng chuẩn — nhiều chỗ đã được kiểm tra và phát hiện lệch so với rubric (xem `05_KIEM_TRA_TUAN_THU_RUBRIC.md`), ví dụ: phân loại VA/NVA thiếu nhóm VBA, bảng lãng phí không theo đúng khung Move/Hold/Overdo, bộ câu hỏi phỏng vấn thiếu trục "có cấu trúc/không cấu trúc", một số sơ đồ BPMN quá đơn giản (dưới ngưỡng gateway tối thiểu của rubric).

**Quy tắc thao tác file:**
- **KHÔNG sửa trực tiếp** vào file trong các thư mục thành viên (`25410167/`, `25410168/`, `25410175 - Bao DX/`, `25410195/`, `25410206/`, `25410223/`, `25410237/`) — đó là bài làm gốc của từng người, giữ nguyên để đối chiếu.
- Mọi bản sửa/viết lại được lưu vào `plan/` (dạng ghi chú/bản nháp đã sửa) hoặc `final/` (bản sẵn sàng đưa vào báo cáo chính thức).
- Khi gộp vào `docs/MoMo.docx`, luôn đối chiếu lại với rubric/bài giảng trước, không copy nguyên xi nội dung thành viên dù nhìn "có vẻ đầy đủ".

---

## 1. TIN QUAN TRỌNG NHẤT: nhóm đã có gần đủ nguyên liệu, vấn đề là CHƯA GỘP

Phát hiện lớn nhất của lần rà soát này: `docs/MoMo.docx` (báo cáo chính) chỉ mới hoàn chỉnh **1/10 quy trình** (Quản trị giá, khuyến mãi), còn lại trống hoặc rất mỏng — **NHƯNG** trong 7 thư mục thành viên đã có sẵn:

- **25410206** — 3 báo cáo độc lập chất lượng cao (9 chương/báo cáo, có trích nguồn thật) cho cụm quy trình "Tìm kiếm – Lựa chọn – Thanh toán", **và** một chương Phân tích đầy đủ (VA/NVA, lãng phí, định lượng, stakeholder, Pareto) — hiện đang bị **gắn sai tên quy trình**, cần đổi nhãn rồi dùng.
- **25410237** — 2 báo cáo 8 chương đầy đủ: "Hỗ trợ khách hàng & Xử lý ngoại lệ" và **"Quản trị danh mục hãng bay và đối tác NCC"** (đúng chỗ đang thiếu nhất).
- **25410223** — bộ 3 quy trình (gồm cả **"Đổi chuyến bay"** — quy trình duy nhất trong toàn báo cáo đang trống 100% và cũng là nơi DUY NHẤT có nguyên liệu) + file `cstt.md` mô tả chi tiết, cần dọn vài đoạn lỗi trích dẫn AI còn sót (`[span_226]`...).
- **25410168** — bản phác thảo mỏng cho 2 quy trình (dữ liệu định lượng chỉ là ước lượng minh họa), dùng làm khung sườn.

→ **Chiến lược chủ đạo: KHÔNG viết lại từ đầu.** Việc chính là gộp, biên tập, sửa lỗi logic/format, và chỉ viết mới cho đúng 2-3 mảng thực sự không ai có (xem mục 3).

---

## 2. RUBRIC — 50 điểm, 5 tiêu chí × 10đ (tóm tắt, chi tiết ở file 03)

| # | Tiêu chí | Yêu cầu tối thiểu |
|---|---|---|
| 1.0 | Liệt kê ≥10 quy trình | ≥3 Quản lý + ≥3 Cốt lõi + ≥3 Hỗ trợ, mỗi quy trình có Tác nhân/Mô tả bước/Đối tượng KH/Kết quả + 1 sơ đồ kiến trúc |
| 2.0 | Mô hình hóa BPMN | 2 Quản lý + 2 Cốt lõi + 2 Hỗ trợ được vẽ BPMN đầy đủ; điểm theo **số gateway** (>7 gateway = điểm tối đa) |
| 3.0 | Phương pháp thực hiện | Bằng chứng (sơ đồ tổ chức, kế hoạch, thuật ngữ, biểu mẫu) + **20 câu phỏng vấn** (10 định tính [5 có cấu trúc+5 không] + 10 định lượng [5+5]) |
| 4.0 | Phân tích quy trình | Áp dụng cho **2 quy trình**: VA/BVA/NVA (1đ) + Lãng phí Move/Hold/Overdo (2đ) + Stakeholder qua Pareto/Fishbone/Root-cause (3đ) + Định lượng Thời gian(1đ)/Chất lượng(2đ)/Chi phí(3đ) |
| 5.0 | Trình bày báo cáo | Đúng template UIT, TOC/danh mục hình-bảng-từ viết tắt tự động, caption đúng chuẩn, Tài liệu tham khảo, **hoạt động GitHub liên tục 3 tuần** (bắt buộc, không phải điểm cộng) |

⚠️ **Điểm 3.0 hiện đang hụt nặng nhất so với rubric**: báo cáo hiện tại chỉ có 8 câu hỏi định tính bị copy y hệt thành "định lượng" — thực chất **0 câu định lượng thật**, và tổng chỉ 16/20 câu yêu cầu. Cần viết lại hoàn toàn bộ câu hỏi (đã có sẵn 10 câu định lượng gợi ý trong `REVIEW-MoMo.md`, chỉ cần bổ sung phân loại có/không cấu trúc).

⚠️ **GitHub 3 tuần liên tiếp là điều kiện bắt buộc** (0đ nếu không có) — nhóm cần commit đều đặn ngay từ bây giờ, không dồn vào cuối, kể cả khi merge nội dung từ Word.

---

## 3. KHOẢNG TRỐNG THỰC SỰ KHÔNG CÓ NGUYÊN LIỆU (phải viết mới)

| Mảng thiếu | Ai chưa có ai viết | Ghi chú |
|---|---|---|
| "Quản lý vé đã mua" (Chương 2 + có thể cả Chương 3) | Không có thành viên nào | Quy trình hỗ trợ, mức độ ưu tiên thấp hơn — chỉ bắt buộc ở mức mô tả (rubric 1.0), KHÔNG bắt buộc phải vẽ BPMN đầy đủ nếu nhóm đã đủ 2 quy trình hỗ trợ khác |
| "Phương pháp thực hiện" của "Xuất hóa đơn" | Không có | Chương 2 (mô tả 6 bước) đã có sẵn, chỉ thiếu phần org chart/kế hoạch/rủi ro/biểu mẫu kiểu "Quản trị giá" |
| "Phương pháp thực hiện" của "Quản lý hạng vé" | Không có | Tương tự — Chương 2 đã đầy đủ |
| Góc độ SLA/điều khoản của "Quản trị rủi ro giao dịch, điều khoản và chất lượng dịch vụ" | Chỉ có một phần (xử lý giao dịch lỗi trong tài liệu 25410237) | Cần bổ sung phần "điều khoản và chất lượng dịch vụ" |
| Chương 4 — KẾT LUẬN | Không ai viết riêng, nhưng mỗi báo cáo con (25410206, 25410237) đều có mục Kết luận riêng có thể tổng hợp | Cần 1 người tổng hợp, không phải viết từ số 0 |

Tất cả các mảng khác đã có nguyên liệu — xem chi tiết bảng đối chiếu ở `02_NGUYEN_LIEU_THANH_VIEN.md`.

---

## 4. THỨ TỰ ƯU TIÊN THỰC HIỆN (4 giai đoạn)

**Giai đoạn 0 — Quyết định phạm vi (làm trong 1 buổi họp nhóm):**
- Chốt đúng 2 quy trình Quản lý + 2 Cốt lõi + 2 Hỗ trợ sẽ được đầu tư đầy đủ (BPMN + Phương pháp thực hiện) — đề xuất cụ thể ở `03_CAU_TRUC_MUC_TIEU.md`.
- Chốt đúng 2-3 quy trình sẽ có chương Phân tích đầy đủ (định tính + định lượng).
- Phân công theo `04_PHAN_CONG_CONG_VIEC.md` (có thể điều chỉnh theo người).

**Giai đoạn 1 — Sửa lỗi cấu trúc & gộp nguyên liệu (ưu tiên 🔴 cao nhất):**
- Sửa trùng "Chương 3", viết Chương 1 + Chương 4.
- Gộp nguyên liệu từ các thư mục thành viên vào đúng vị trí (xem file 04).
- Viết lại hoàn toàn bộ câu hỏi phỏng vấn (20 câu, đúng phân loại).

**Giai đoạn 2 — Sửa lỗi logic quy trình & thuật ngữ (🟠):**
- Áp dụng toàn bộ 8 lỗi logic trong `01_HIEN_TRANG_VA_LOI.md` (off-by-one bước, nhãn gateway sai, mục tiêu copy sai chỗ, định nghĩa M_Service...).
- Thống nhất tên bộ phận, thuật ngữ toàn bài.

**Giai đoạn 3 — Trình bày & hoàn thiện (🟡):**
- Chuẩn hóa heading level → TOC/Danh mục hình/bảng/từ viết tắt tự động.
- Caption toàn bộ hình/bảng theo đúng số chương (theo mẫu CellPhones.pdf: `Hình 3.1`, `Bảng 3.1`...).
- Viết mục Tài liệu tham khảo (đã có sẵn nguồn thật từ báo cáo 25410206).
- Bổ sung bảng phân công công việc nhóm, sửa ngày trên bìa.

**Giai đoạn 4 — Trước bảo vệ (🔵):**
- Dẫn nguồn hoặc ghi rõ "giả định của nhóm" cho các con số chưa có nguồn.
- Làm rõ tuyên bố phỏng vấn nội bộ MoMo (thật hay không).
- Chạy thử buổi bảo vệ, kiểm tra thời lượng slide.

---

## 5. NGUYÊN TẮC LÀM VIỆC

- Toàn bộ file trung gian (dump text, ghi chú) đã lưu ở scratchpad — không ảnh hưởng thư mục dự án.
- Khi bắt đầu chỉnh sửa thật, **làm việc trên file trong `final/`**, không sửa trực tiếp `docs/MoMo.docx` cho đến khi nhóm duyệt nội dung — giữ bản gốc để so sánh.
- Vì Word không tiện thao tác qua công cụ dòng lệnh, đề xuất: xuất nội dung cần chỉnh sang bản nháp có cấu trúc rõ ràng trước, nhóm review, sau đó mới paste ngược vào file .docx theo template UIT chính thức (rubric 5.0 yêu cầu đúng template — bắt buộc tải từ httt.uit.edu.vn/cac-bieu-mau).
