# NGUYÊN LIỆU SẴN CÓ TỪ CÁC THÀNH VIÊN

> Rà soát toàn bộ 18 file .docx + 1 file .md trong 7 thư mục thành viên (`25410167`, `25410168`, `25410175 - Bao DX`, `25410195`, `25410206`, `25410223`, `25410237`). Mục tiêu: biết chính xác cái gì đã viết sẵn, chất lượng ra sao, và có dùng được ngay không — để **không ai phải viết lại những gì đã có**.

## Tóm tắt 1 dòng mỗi người

| MSSV | Người phụ trách (theo tài liệu) | Đóng góp | Đánh giá |
|---|---|---|---|
| 25410167 | Vũ Thị Nhân Ái | Không có gì (README rỗng) | Cần giao việc mới hoàn toàn |
| 25410168 | Phạm Ngọc Bảo An | Bản nháp mỏng: Phương pháp thực hiện + Phân tích cho 2 quy trình | Dùng làm khung, cần viết lại phần lớn |
| 25410175 | Đinh Xuân Bảo (nhóm trưởng) | Giữ bản chính + đã tự review (REVIEW-MoMo.md) | Vai trò tổng hợp/kiểm soát chất lượng |
| 25410195 | Nguyễn Huỳnh Mỹ Duyên | Không có gì thêm (chỉ bản khung chia sẻ chung) | Cần giao việc mới |
| 25410206 | Nguyễn Đắc Hiển | **3 báo cáo độc lập chất lượng cao nhất dự án** cho cụm Tìm kiếm/Lựa chọn/Thanh toán + 1 chương Phân tích đầy đủ (bị gắn sai tên quy trình) | Nguyên liệu tốt nhất — ưu tiên gộp trước |
| 25410223 | Lê Quốc Hưng | 3 quy trình (bản .docx súc tích + `cstt.md` chi tiết) — **nguồn DUY NHẤT cho "Đổi chuyến bay"** | Rất tốt, cần dọn artifact AI trong cstt.md |
| 25410237 | Nguyễn Mậu An Khương | **2 báo cáo 8 chương đầy đủ**: Hỗ trợ KH & Xử lý ngoại lệ + Quản trị danh mục hãng bay (đúng chỗ đang thiếu) | Nguyên liệu tốt, sẵn sàng gộp |

*(Lưu ý: trang bìa ghi 8 thành viên nhưng chỉ có 7 thư mục — thiếu 1 người, nhóm tự kiểm tra lại.)*

---

## Chi tiết theo từng người

### 25410168 — Phạm Ngọc Bảo An
| File | Nội dung | Mức độ | Khuyến nghị |
|---|---|---|---|
| `Muc3_Phuong_phap_thuc_hien.docx` | Phương pháp thực hiện cho "Tìm kiếm/đặt vé/thanh toán" và "Mua thêm dịch vụ" (bảng bằng chứng, sơ đồ quan hệ ngắn, timeline, thuật ngữ, 20 câu phỏng vấn) | Mỏng hơn nhiều so với mẫu "Quản trị giá" chuẩn (thiếu bảng rủi ro, biểu mẫu, kế hoạch chi tiết theo giờ) | GỘP CÓ VIẾT LẠI — dùng làm khung tham khảo, nên thay bằng nguyên liệu 25410206/25410223 nếu trùng phạm vi |
| `Muc4_Phan_tich_quy_trinh.docx` | VA/NVA, lãng phí (Move/Hold/Overdo), nguyên nhân kiểu Ishikawa (dạng bảng), định lượng thời gian/chất lượng/chi phí — cùng 2 quy trình trên | Cấu trúc ổn nhưng số liệu tự ghi rõ là "ước lượng minh họa" (không phải số thật) | GỘP CÓ VIẾT LẠI |
| (bản full report dùng chung) | Chỉ có đoạn "Lịch sử hình thành" của Chương 1 | 1 đoạn duy nhất | DÙNG NGUYÊN cho Chương 1 |

### 25410175 — Đinh Xuân Bảo (nhóm trưởng)
Giữ bản chính `MoMo.docx` (giống hệt `docs/MoMo.docx`) — không có nguyên liệu bổ sung nào khác ngoài bản review đã có. Vai trò tự nhiên: tổng hợp, merge, và kiểm tra chất lượng cuối cùng.

### 25410195 — Nguyễn Huỳnh Mỹ Duyên
Chỉ có bản khung dùng chung với 25410168/175 (đoạn Lịch sử hình thành, còn lại toàn heading trống). Không có đóng góp riêng.

### 25410206 — Nguyễn Đắc Hiển ⭐ nguyên liệu tốt nhất dự án
| File | Nội dung | Mức độ | Khuyến nghị |
|---|---|---|---|
| `MoMo_Core01_TimKiem_va_SoSanhChuyenBay.docx` | Tìm kiếm & so sánh chuyến bay — báo cáo độc lập 9 chương đầy đủ (giới thiệu, định vị, phương pháp có biểu mẫu + ngân hàng câu hỏi phỏng vấn, phân tích cấu trúc BPMN, VA/NVA, lãng phí, định lượng thời gian/chi phí/chất lượng, stakeholder + root-cause kiểu fishbone, kết luận + đề xuất TO-BE, **có trích dẫn nguồn thật** từ trang trợ giúp MoMo) | Xuất sắc — có giả định rõ ràng, tính toán mạch lạc (PCE, cycle time, cost/session) | GỘP CÓ VIẾT LẠI (cần thu gọn/hợp nhất vì báo cáo chính gộp chung 3 bước này thành 1 quy trình "Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé") |
| `MoMo_Core02_LuaChonHanhTrinh_va_HangBay.docx` | Chọn hành trình/hãng bay (giữ chỗ, tạo PNR) — cùng cấu trúc 9 chương, cùng chất lượng | Xuất sắc | GỘP CÓ VIẾT LẠI |
| `MoMo_Core03_ThanhToan_va_XacNhanDatVe.docx` | Thanh toán & xác nhận đặt vé — cùng cấu trúc 9 chương | Xuất sắc | GỘP CÓ VIẾT LẠI |
| `MoMo.docx` (bản riêng) | Chương 4 "Phân tích các quy trình" đầy đủ: VA, lãng phí, định lượng (có PCE/RTY), stakeholder, issue register, biểu đồ Pareto | Đầy đủ, chặt chẽ — **NHƯNG đang bị gắn nhầm tên**: nội dung thực chất phân tích quy trình "Quản trị giá, khuyến mãi" nhưng lại để dưới heading "Tìm kiếm, lựa chọn hành trình..." | GỘP CÓ VIẾT LẠI — **việc đầu tiên là đổi lại đúng tên quy trình**, sau đó có thể dùng làm chương Phân tích thứ 2 hoặc thứ 3 (bổ sung cho "Quản trị giá" — quy trình vốn đã có Phương pháp thực hiện đầy đủ nhưng chưa có Phân tích) |
| File `.bpmn`/`.png` đi kèm mỗi Core0X | Sơ đồ BPMN | Sẵn sàng dùng | Dùng trực tiếp, chỉ cần kiểm tra khớp với văn bản sau khi hợp nhất |

### 25410223 — Lê Quốc Hưng
| File | Nội dung | Mức độ | Khuyến nghị |
|---|---|---|---|
| `MoMo_Core01_...TimKiem_LuaChon_ThanhToan_XacNhanDatVe.docx` | Cùng phạm vi với quy trình gộp chính thức | Khung 9 chương súc tích (dạng gạch đầu dòng), đúng nhưng nông hơn bản 25410206 | GỘP CÓ VIẾT LẠI (bản 25410206 chi tiết hơn — có thể dùng 25410223 để đối chiếu/bổ sung ý còn thiếu) |
| `MoMo_Core02_MuaDichVuBoSung_SauDatCho.docx` | Mua thêm dịch vụ sau đặt chỗ | Khung 9 chương súc tích, đầy đủ | GỘP CÓ VIẾT LẠI |
| `MoMo_Core03_DoiChuyenBay_DieuChinhLichTrinh.docx` | **Đổi chuyến bay** — quy trình đang TRỐNG 100% trong báo cáo chính | Khung 9 chương súc tích, có công thức tính phí đổi vé, xử lý ngoại lệ, đề xuất TO-BE | GỘP CÓ VIẾT LẠI — **nguồn DUY NHẤT cho quy trình này, ưu tiên cao** |
| `cstt.md` | Cùng 3 quy trình trên nhưng viết văn xuôi chi tiết hơn nhiều (mô tả từng bước 7-8 bước, bảng luồng dữ liệu, 2-3 kịch bản ngoại lệ mỗi quy trình với cách xử lý đầy đủ), có cả Chương 5 phân tích định lượng cycle-time + đề xuất TO-BE | Chất lượng mô tả văn xuôi tốt nhất dự án | GỘP CÓ VIẾT LẠI — **NHƯNG phải dọn trước**: còn sót artifact trích dẫn AI kiểu `[span_226]...[span_226]` ngay trong câu văn (VD: "AddAncillar[span_226]...y", "phí đổi vé[span_305]...(nếu có)") — phải xóa sạch các đoạn `[span_...]` trước khi đưa vào báo cáo chính thức. Thiếu các mục VA/NVA, lãng phí, stakeholder, fishbone (có ở bản .docx song song) |

### 25410237 — Nguyễn Mậu An Khương ⭐ đúng trọng tâm khoảng trống
| File | Nội dung | Mức độ | Khuyến nghị |
|---|---|---|---|
| `MoMo_HauMai_va_XuLyNgoaiLe.docx` | Hỗ trợ KH/khiếu nại + tra soát giao dịch lỗi/treo (liên quan "Quản trị rủi ro giao dịch") | Báo cáo 8 chương đầy đủ: phương pháp, biểu mẫu, >20 câu phỏng vấn, BPMN, VA/NVA, lãng phí, định lượng, stakeholder, Pareto/root-cause, kết luận | GỘP CÓ VIẾT LẠI — dùng cho quy trình "Hỗ trợ khách hàng và tiếp nhận phản hồi" (đã có sẵn Chương 2), và phần tra soát giao dịch lỗi có thể bổ sung cho "Quản trị rủi ro giao dịch" (đang trống) |
| `MoMo_Quan_tri_danh_muc_hang_bay_va_doi_tac_cung_ung.docx` | **Quản trị danh mục hãng bay và đối tác NCC** — đúng quy trình đang mỏng nhất (1 dòng) trong báo cáo chính | Báo cáo 8 chương đầy đủ: quy trình con "Onboarding đối tác" + "Rà soát/loại bỏ đối tác", biểu mẫu, fishbone root-cause | GỘP CÓ VIẾT LẠI — **ưu tiên cao, giải quyết trực tiếp 1 khoảng trống được review gốc chỉ ra** |
| `MoMo_Kien_truc_quy_trinh_Dat_ve_may_bay.docx` | Tổng quan kiến trúc: liệt kê 13 quy trình theo 4 nhóm (Khách hàng/Đối tác-Vận hành/Tuân thủ-Rủi ro/Hỗ trợ nội bộ) — khác cách chia 3 nhóm (Quản lý/Cốt lõi/Hỗ trợ) của báo cáo chính | Tài liệu tham chiếu gọn, có thông tin công ty (thành lập 2007, giấy phép 16/GP-NHNN, sơ đồ tổ chức) | GỘP CÓ VIẾT LẠI — dùng phần thông tin công ty cho Chương 1; **không dùng cách chia 4 nhóm** vì phải khớp khung Quản lý/Cốt lõi/Hỗ trợ mà bài giảng chap01/02 và rubric yêu cầu |
| `Nhom-6.docx` | Quy trình xác thực tài khoản eKYC — quy trình ví MoMo nói chung, **KHÔNG thuộc phạm vi đặt vé máy bay** | Viết tốt nhưng lạc đề (có thể là bản nháp từ giai đoạn nhóm còn cân nhắc chủ đề) | KHÔNG DÙNG — loại khỏi báo cáo cuối |
| File `.bpmn` (4 file: Onboarding, RaSoat, TraSoat, XuLyKhieuNai) | Sơ đồ BPMN tương ứng | Sẵn sàng dùng | Dùng trực tiếp |

---

## Bảng đối chiếu: khoảng trống ↔ nguyên liệu sẵn có

| Khoảng trống trong `docs/MoMo.docx` | Có nguyên liệu? | Lấy từ đâu |
|---|---|---|
| Chương 1 — Tổng quan công ty | Một phần | Đoạn Lịch sử hình thành (25410168/195/175) + org chart/giấy phép (25410237 Kiến trúc) |
| Chương 4 — Kết luận | Gián tiếp | Tổng hợp từ mục Kết luận của 25410206 + 25410237 (không copy nguyên, phải viết lại tổng hợp) |
| Phân tích — Tìm kiếm/lựa chọn/thanh toán | **Có, rất tốt** | 25410206 (3 file Core0X) + 25410223 (Core01 + cstt.md) |
| Phân tích — Mua thêm dịch vụ | **Có, tốt** | 25410223 (Core02) + cstt.md + 25410168 (Muc4, mỏng hơn) |
| Phân tích — Hỗ trợ khách hàng | **Có, rất tốt** | 25410237 (HauMai_va_XuLyNgoaiLe) |
| Phương pháp thực hiện — 5 quy trình mỏng | Có cho 3/5 (Tìm kiếm, Mua thêm dịch vụ, Hỗ trợ KH) | Như trên |
| Phương pháp thực hiện — Quản lý hạng vé | **Không có** | Phải viết mới theo mẫu "Quản trị giá" |
| Phương pháp thực hiện — Xuất hóa đơn | **Không có** | Phải viết mới theo mẫu "Quản trị giá" |
| Chương 2 — Đổi chuyến bay (trống 100%) | **Có, nguồn duy nhất** | 25410223 (Core03 + cstt.md) |
| Chương 2 — Quản lý vé đã mua (trống 100%) | **Không có** | Phải viết mới hoàn toàn |
| Chương 2 — Quản trị rủi ro giao dịch | Một phần (chỉ khía cạnh tra soát lỗi) | 25410237 (HauMai, quy trình 1) — thiếu góc độ điều khoản/SLA |
| Quản trị danh mục hãng bay (đang mỏng) | **Có, rất tốt** | 25410237 (Quan_tri_danh_muc...) |
| Tài liệu tham khảo | **Có nguồn thật** | 25410206 (trích dẫn trang trợ giúp MoMo trong 3 báo cáo Core0X) |
