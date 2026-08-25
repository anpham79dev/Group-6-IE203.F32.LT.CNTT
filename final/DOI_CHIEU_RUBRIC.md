# ĐỐI CHIẾU RUBRIC — `final/BaoCao_Final.md` / `.docx`

> Đối chiếu trực tiếp với `docs/Rubik Đánh giá Bài tập Đồ Án.xlsx` (đã dump lại nguyên văn ở phiên này, không dùng lại bản tóm tắt cũ để tránh sai lệch). Tổng 50 điểm, 5 tiêu chí × 10đ. Phương pháp: đối chiếu câu chữ chính xác như đã làm ở `plan/05_KIEM_TRA_TUAN_THU_RUBRIC.md`, không suy đoán có lợi. % ghi dưới dạng khoảng khi phụ thuộc yếu tố nhóm cần tự xác nhận (số liệu thật, render BPMN trực quan).
>
> **Đọc trước khi tin vào %:** đây là ước tính của người tổng hợp dựa trên đối chiếu câu chữ rubric, **không phải điểm số chính thức của giảng viên**. Dùng để nhóm biết chỗ nào cần rà lại trước khi nộp, không dùng để khẳng định chắc chắn sẽ đạt đúng số điểm nêu ra.

---

## Tiêu chí 1.0 — Liệt kê tối thiểu 10 quy trình (10.0đ)

> *Nguyên văn rubric:* "Liệt kê tối thiểu 10 quy trình trong doanh nghiệp phân tích — Mỗi quy trình 1đ." Yêu cầu con: ≥3 Quản lý (Management), ≥3 Cốt lõi (Core), ≥3 Hỗ trợ (Support); mỗi quy trình có Actor, Mô tả quy trình bằng lời (các bước), Đối tượng khách hàng, Liệt kê kết quả có thể xảy ra. Riêng mục "Vẽ kiến trúc quy trình" (tổng 10 quy trình) = 1.0đ.

| Yêu cầu con | Trạng thái trong `BaoCao_Final.md` | % ước tính |
|---|---|---|
| ≥3 quy trình Quản lý | 4 quy trình (Quản lý hạng vé, Quản trị giá, Quản trị danh mục hãng bay, Quản trị rủi ro giao dịch) — Chương 2.2.1 | 100% |
| ≥3 quy trình Cốt lõi | 3 quy trình (Tìm kiếm..., Mua thêm dịch vụ, Đổi chuyến bay) — Chương 2.2.2 | 100% |
| ≥3 quy trình Hỗ trợ | 3 quy trình (Hỗ trợ KH, Xuất hóa đơn, Quản lý vé đã mua) — Chương 2.2.3 | 100% |
| Mỗi quy trình đủ Actor + Mô tả bước + Đối tượng KH + Kết quả | Đủ cả 10/10 quy trình (đã viết mới hoàn chỉnh cho 3 quy trình từng thiếu: Đổi chuyến bay, Quản trị danh mục hãng bay, Quản lý vé đã mua) | 95–100% — riêng "Quản lý vé đã mua" là suy luận của nhóm (không có nguyên liệu thật, đã ghi chú rõ trong bài), giảng viên có thể hỏi sâu hơn |
| Vẽ kiến trúc quy trình (1.0đ) | Giữ nguyên Hình 2.1 gốc — cần đổi lại số caption từ "Hình 1.1" sang "Hình 2.1" (chưa làm, thuộc Giai đoạn 3 trình bày) | 70% — nội dung hình đúng, chỉ thiếu đánh số lại |

**Ước tính tổng: ~9.0–9.5/10.0**

---

## Tiêu chí 2.0 — Mô hình hóa quy trình (10.0đ)

> *Nguyên văn rubric:* "Mô hình hóa 2 quy trình quản lý / 2 quy trình cốt lõi / 2 quy trình hỗ trợ" (3.0đ mỗi nhóm), chấm theo **số cổng điều kiện (gateway)**: >7 = 1đ (tối đa), >5 = 0.75đ, >3 = 0.5đ; trừ điểm nếu sai ký hiệu Split & Join (hệ số 1 → 0.25).

| Nhóm | Quy trình | Số gateway | Ngưỡng đạt | Ghi chú |
|---|---|---|---|---|
| Quản lý | Quản trị giá | >10 (đếm bằng mắt trên ảnh gốc) | >7 → tối đa | Không đổi, đã đạt chuẩn từ trước |
| Quản lý | Quản trị danh mục hãng bay | 3 + 3 (2 sơ đồ con, chưa gộp) | >3 → 0.5 | **Chưa gộp** 2 sơ đồ Onboarding+RaSoat thành 1 — việc còn tồn đọng, xem `plan/07` |
| Cốt lõi | Tìm kiếm/lựa chọn/thanh toán | 10–12/sơ đồ (3 sơ đồ con) | >7 → tối đa | Không đổi |
| Cốt lõi | Đổi chuyến bay | **5** (đã thêm 2 gateway ở phiên này: g4, g5) | >3 chắc chắn → 0.5; **chưa chắc >5** (đúng bằng 5, không lớn hơn 5) | Đã verify bằng XML parser (`final/bpmn/Core03_DoiChuyenBay.bpmn`). Nhóm **PHẢI** mở bằng bpmn.io kiểm tra logic/layout trước khi dùng — có thể cân nhắc thêm 1 gateway nữa để chắc chắn vượt ngưỡng >5 |
| Hỗ trợ | Xuất hóa đơn | >10 (ảnh gốc) | >7 → tối đa | Không đổi |
| Hỗ trợ | Hỗ trợ khách hàng | 2 + 3 (2 sơ đồ con, chưa gộp) | >3 → 0.5 (sơ đồ TraSoat chỉ 2 gateway — **dưới cả ngưỡng thấp nhất >3**) | Cần gộp 2 sơ đồ hoặc bổ sung nhánh cho TraSoat — **CHƯA LÀM** |

**Ước tính tổng: ~5.5–7.0/10.0** — đây là tiêu chí có rủi ro thất thoát điểm rõ nhất còn lại, do 3/6 quy trình (Quản trị danh mục hãng bay, Đổi chuyến bay, Hỗ trợ khách hàng) chưa chắc chắn vượt ngưỡng >5. Việc gộp/bổ sung gateway cho 3 sơ đồ còn lại là ưu tiên cao nhất nếu nhóm còn thời gian trước khi nộp.

---

## Tiêu chí 3.0 — Phương pháp thực hiện (10.0đ)

> *Nguyên văn rubric:* "Dựa trên bằng chứng" (Mô tả quy trình hiện có, Sơ đồ tổ chức, Kế hoạch làm việc, Thuật ngữ và sổ tay, Biểu mẫu) + "Phỏng vấn" (10 câu định tính 5 có cấu trúc/5 không cấu trúc + 10 câu định lượng 5/5; tổng số câu chấm theo ngưỡng: <10 câu = 0đ, 10–20 câu = 0.25đ, ≥20 câu = 0.5đ).

| Quy trình | Đủ 5 mục bằng chứng? | Đủ 20 câu hỏi đúng lưới 2×2? |
|---|---|---|
| Quản trị giá | ✅ Đủ (mẫu gốc tốt nhất bài) | ✅ 20 câu (10+10, đã viết lại 100% phần định lượng) |
| Quản trị danh mục hãng bay | ✅ Đủ | ✅ 20 câu (cơ cấu lại từ 30 câu nguồn) |
| Tìm kiếm/lựa chọn/thanh toán | ✅ Đủ | ✅ 20 câu (đã đạt chuẩn từ nguồn gốc) |
| Đổi chuyến bay | ✅ Đủ (viết mới hoàn toàn ở phiên này) | ✅ 20 câu (viết mới hoàn toàn) |
| Hỗ trợ khách hàng | ✅ Đủ | ✅ 20 câu (cơ cấu lại từ 30 câu nguồn) |
| Xuất hóa đơn | ✅ Đủ (viết mới hoàn toàn ở phiên này) | ✅ 20 câu (viết mới hoàn toàn) |

**Ước tính tổng: ~9.0–9.5/10.0** — đây là tiêu chí cải thiện rõ rệt nhất so với bản gốc (trước đây chỉ 1/6 quy trình đạt chuẩn). Điểm trừ nhỏ duy nhất: nội dung "bằng chứng" cho Đổi chuyến bay/Xuất hóa đơn/Quản lý vé đã mua là suy luận/dựng mới, không phải khảo sát thực tế — nếu giám khảo hỏi sâu về nguồn gốc số liệu cụ thể, nhóm cần trả lời trung thực là giả định có căn cứ, không phải thu thập thực địa.

---

## Tiêu chí 4.0 — Phân tích quy trình (10.0đ)

> *Nguyên văn rubric:* áp dụng cho **2 quy trình** (nhóm làm 3, dư 1). Định tính: Phân tích giá trị gia tăng (VA/BVA/NVA, có Liệt kê/Mô tả/Khắc phục), Phân tích lãng phí (Move/Hold/Overdo, có Liệt kê/Mô tả/Khắc phục), Phân tích các bên liên quan (chọn 1/3: Pareto/Root-cause/Fishbone). Định lượng: Thời gian, Chất lượng, Chi phí (đều yêu cầu Tính toán + Khắc phục).

| Quy trình | VA/BVA/NVA đủ cột? | Lãng phí đúng Move/Hold/Overdo? | Bên liên quan (đúng 1/3 kỹ thuật)? | Định lượng có công thức tính? |
|---|---|---|---|---|
| Tìm kiếm/lựa chọn/thanh toán | ✅ Đủ, không đổi | ✅ Đủ, không đổi | ✅ Fishbone (đúng chuẩn) | ✅ Đúng công thức thời gian; **đã bổ sung** phép tính chi phí thời gian×lương (=0, có giải thích vì quy trình tự động hoàn toàn) |
| Hỗ trợ khách hàng | ✅ **Đã bổ sung** cột Mô tả+Khắc phục (bản gốc thiếu) | ✅ Đủ, không đổi | ✅ **Đã sửa nhãn**: Pareto là kỹ thuật chính thức (Power-Interest Grid chỉ bổ sung, không tính điểm thay thế) | ✅ Đúng công thức (T_ck, hiệu suất, chi phí giờ công) |
| Quản trị giá (bonus) | ✅ **Đã bổ sung** cột Mô tả+Khắc phục cho toàn bộ 16 hoạt động | ✅ **Đã cơ cấu lại** đúng Move/Hold/Overdo (bản gốc thiếu nhóm Move) | ✅ Pareto (đúng chuẩn, có tính lũy kế %) | ✅ **Đã sửa công thức rework** từ cộng đơn giản sang đúng T/(1−r); chi phí đã đúng mô hình thời gian×lương từ đầu |

**Ước tính tổng: ~9.0–9.5/10.0** — tiêu chí được nâng cấp mạnh nhất so với bản gốc (trước đây cả 2 mục Phân tích đều **trống 100%**). Rủi ro còn lại: số liệu định lượng là giả định/minh họa (đã ghi rõ trong bài, phù hợp với việc không có dữ liệu vận hành thật) — nếu giảng viên yêu cầu số liệu thật thì đây là giới hạn đã biết trước, không phải lỗi kỹ thuật.

---

## Tiêu chí 5.0 — Trình bày báo cáo (10.0đ)

> *Nguyên văn rubric:* Slide (chính tả, font/size/màu/bullet, mục lục trang/hình/bảng, trình bày, đúng giờ, bật cam) + Word (chính tả, font, mục lục trang/hình/bảng, **đúng mẫu báo cáo của trường** https://httt.uit.edu.vn/cac-bieu-mau/, tiêu đề bảng/hình đúng vị trí — label hình dưới, label bảng trên, Tài liệu tham khảo, mục lục/mục lục hình/mục lục bảng/bảng viết tắt) + Github (hoạt động 3 tuần liên tiếp — **0đ nếu không có**, là điều kiện bắt buộc chứ không phải điểm cộng).

| Yêu cầu con | Trạng thái | % ước tính |
|---|---|---|
| Nội dung Word đầy đủ, chính tả | `BaoCao_Final.md`/`.docx` đã có đủ nội dung, đã sửa các lỗi chính tả đã biết (tichet, Developement, xác đsịnh...) | 90% |
| Đúng mẫu báo cáo chính thức của trường | **CHƯA làm** — dự án không có file template gốc từ httt.uit.edu.vn/cac-bieu-mau, `BaoCao_Final.docx` chỉ dùng Heading style chuẩn Word, KHÔNG đảm bảo khớp margin/font/bìa của mẫu trường | **0–30%** — đây là rủi ro lớn nhất còn lại, **bắt buộc nhóm tự tải mẫu thật và format lại** trước khi nộp |
| Mục lục / Danh mục hình / Danh mục bảng / Danh mục từ viết tắt tự động | Chưa chèn field tự động (phải làm trực tiếp trong Word, không làm được qua nội dung Markdown); đã có `final/DanhMucTuVietTat.md` làm nội dung sẵn để dán vào | 20% — nội dung sẵn sàng, thao tác chèn field còn thiếu |
| Caption hình/bảng đúng vị trí (hình dưới, bảng trên), đúng số chương | Chưa đánh lại (thuộc Giai đoạn 3, chưa làm ở phiên này) | 10% |
| Tài liệu tham khảo | ✅ Đã có, gộp từ nguồn thật (`final/TaiLieuThamKhao.md`) | 85% — cần đối chiếu lại số `[n]` trích dẫn trong thân bài cho khớp |
| Github hoạt động 3 tuần liên tiếp | **Chưa xác nhận** — phụ thuộc hoàn toàn vào lịch sử commit thật của nhóm, không đánh giá được qua nội dung báo cáo | **Không đánh giá được ở đây — 0đ nếu chưa có, nhóm phải tự kiểm tra ngay** |

**Ước tính tổng: ~4.0–5.5/10.0** — đây là tiêu chí **kém nhất trong 5 tiêu chí**, vì phần lớn công việc còn lại (template chính thức, field tự động, caption, Github) là thao tác thủ công trong Word/GitHub mà một phiên tổng hợp nội dung không thể thay thế được. **Đây là việc nhóm bắt buộc phải tự làm sau khi nhận bản `BaoCao_Final.docx`.**

---

## TỔNG HỢP

| Tiêu chí | Điểm tối đa | Ước tính đạt được | Việc còn lại quan trọng nhất |
|---|---|---|---|
| 1.0 Liệt kê ≥10 quy trình | 10.0 | ~9.0–9.5 | Đánh lại số caption Hình 2.1 |
| 2.0 Mô hình hóa BPMN | 10.0 | ~5.5–7.0 | Gộp/bổ sung gateway cho 3 sơ đồ dưới ngưỡng (Quản trị danh mục, Đổi chuyến bay, Hỗ trợ KH) |
| 3.0 Phương pháp thực hiện | 10.0 | ~9.0–9.5 | Không còn việc lớn, chỉ rà soát lại câu chữ |
| 4.0 Phân tích quy trình | 10.0 | ~9.0–9.5 | Không còn việc lớn, chỉ rà soát lại số liệu |
| 5.0 Trình bày báo cáo | 10.0 | ~4.0–5.5 | Tải template thật của trường + format lại toàn bộ trong Word + xác nhận GitHub 3 tuần |
| **TỔNG** | **50.0** | **~36.5–41.0 (73–82%)** | |

> ⚠️ Con số tổng chỉ mang tính định hướng — sai số lớn nhất nằm ở Tiêu chí 5.0 (phụ thuộc hoàn toàn vào việc nhóm tự format Word + tình trạng Github thật, không thể đánh giá qua nội dung văn bản) và Tiêu chí 2.0 (phụ thuộc việc nhóm có làm thêm sơ đồ BPMN hay không). **Nếu nhóm hoàn tất 2 việc này, điểm ước tính có thể lên tới ~44–46/50 (88–92%).**
