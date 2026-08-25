# HIỆN TRẠNG BÁO CÁO CHÍNH (`docs/MoMo.docx`) — Đối chiếu & Bổ sung

> File `docs/REVIEW-MoMo.md` (đã có sẵn trong dự án) là review gốc, liệt kê 25 lỗi cụ thể theo 4 nhóm mức độ. File này **xác minh lại toàn bộ 25 lỗi đó** trên bản dump text mới nhất, chỉ ra vài chỗ review gốc mô tả chưa chính xác 100%, và bổ sung phát hiện mới. Dùng file này song song với `REVIEW-MoMo.md` — không thay thế.

## 1. Kết quả xác minh 25 lỗi của REVIEW-MoMo.md

**Xác nhận đúng gần như tuyệt đối (23/25)** — chi tiết dòng cụ thể trong dump đối chiếu khớp với mô tả gốc. Đáng chú ý 2 điểm review gốc mô tả **hơi khác thực tế**:

- **Lỗi #1.2 (bảng câu hỏi định lượng trùng định tính):** Không phải trùng **100% cả 8/8 câu** như review gốc nói — câu 3 có khác 1 cụm từ nhỏ ("(M_Service)"). Nhưng bản chất vấn đề còn **nghiêm trọng hơn** review gốc nêu: cả 8 câu trong bảng "định lượng" đều là câu hỏi trắc nghiệm/mở kiểu định tính — **không có câu nào hỏi ra con số, thời lượng, tần suất, hay thang đo** cả. Tức bộ câu hỏi định lượng thực chất KHÔNG TỒN TẠI, chứ không chỉ là bị copy nhầm.
- **Lỗi #1.4 (câu tuyên bố "phân tích 6 quy trình... hai lăng kính"):** review gốc ghi câu này nằm ở "Mở đầu" — thực tế câu đó nằm ở mục **TÓM TẮT ĐỒ ÁN**, còn Mở đầu là đoạn khác (về số chương). Không đổi bản chất vấn đề, chỉ đổi vị trí cần sửa.

## 2. Phát hiện MỚI (chưa có trong REVIEW-MoMo.md)

1. **Bảng "câu hỏi định lượng" không hề định lượng** — xem trên. → khi viết lại 20 câu hỏi (10 định tính + 10 định lượng theo yêu cầu rubric), phải làm từ đầu, không sửa nhẹ bảng cũ.
2. **Số bảng thực tế trong dump là 11, không phải 12** như review gốc ghi ("12 bảng") — chênh lệch nhỏ, có thể do 1 bảng bị mất khi trích xuất text; cần kiểm tra lại trực tiếp trong Word khi thao tác thật.
3. **Nhóm Hỗ trợ được nhắc tới một quy trình "ma"**: mục mô tả nhóm Hỗ trợ (dòng ~47) có câu "...đối soát tài chính và bảo trì kỹ thuật (API)" nhưng **không có quy trình nào tên như vậy** được liệt kê hay mô hình hóa ở bất kỳ đâu trong tài liệu — chỉ là câu văn mô tả suông. Cần xóa câu này hoặc thay bằng mô tả đúng 3 quy trình Hỗ trợ thật sự có (Hỗ trợ KH, Xuất hóa đơn, Quản lý vé đã mua).
4. **Heading Chương 1 có dấu hiệu bị lỗi định dạng** — dòng Heading 1 của "Chương 1" xuất hiện trống rồi mới tới dòng text tiêu đề không có style — gợi ý có xuống dòng thừa trong Word. Cần kiểm tra trực tiếp khi mở file.
5. **Lỗi định dạng nhỏ:** "Biểu mẫu 4" có tab đầu dòng thừa, không giống Biểu mẫu 1–3 — sửa cho đồng nhất.
6. **Lỗi heading-level giống hệt lặp lại ở CHƯƠNG 3 (Phân tích) chứ không chỉ Chương 3 (BPMN)** — mục "Tìm kiếm, lựa chọn hành trình..." là Heading 3 nhưng "Hỗ trợ khách hàng và tiếp nhận phản hồi" lại là Heading 2, hai mục ngang hàng nhưng khác cấp — **lỗi y hệt đã xảy ra 2 lần ở 2 chương khác nhau**, cần sửa đồng bộ cả hai chỗ.
7. **Thuật ngữ "Đối tượng khách hàng" dùng cho đối tác nội bộ/B2B** (VD: "Đối tượng khách hàng: Nội bộ doanh nghiệp và đối tác Hãng bay") — không sai nhưng dễ gây hiểu lầm khi bảo vệ, nên có định nghĩa rõ trong bảng thuật ngữ.

## 3. Cây heading hiện tại của `docs/MoMo.docx` (để đối chiếu khi chỉnh sửa)

```
MỤC LỤC / DANH MỤC HÌNH VẼ / DANH MỤC BẢNG / DANH MỤC TỪ VIẾT TẮT  — đều trống (chưa chèn field)
TÓM TẮT ĐỒ ÁN — có nội dung
MỞ ĐẦU — có nội dung nhưng không khớp thân bài

Chương 1: TỔNG QUAN...  → TRỐNG 100%

Chương 2. LIỆT KÊ QUY TRÌNH NGHIỆP VỤ
  PHÂN LOẠI QUY TRÌNH — có nội dung + Hình 1.1 (đánh số sai chương)
  KIẾN TRÚC QUY TRÌNH
    Quy trình quản lý:
      Quản lý hạng vé — ĐẦY ĐỦ
      Quản trị giá, khuyến mãi... — ĐẦY ĐỦ
      Quản trị danh mục hãng bay và đối tác NCC — MỎNG (1 dòng)
      Quản trị rủi ro giao dịch, điều khoản và chất lượng dịch vụ — TRỐNG
    Quy trình cốt lõi:
      Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé — ĐẦY ĐỦ
      Mua thêm dịch vụ sau đặt chỗ — ĐẦY ĐỦ
      Đổi chuyến bay — TRỐNG
    Quy trình hỗ trợ:
      Hỗ trợ khách hàng và tiếp nhận phản hồi — ĐẦY ĐỦ
      Xuất hóa đơn — ĐẦY ĐỦ (6 bước)
      Quản lý vé đã mua — TRỐNG

Chương 3: MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN   ⚠️ trùng số với chương dưới
  Quản trị giá, khuyến mãi... → Phương pháp thực hiện (ĐẦY ĐỦ: sơ đồ tổ chức, kế hoạch, công nghệ, rủi ro,
                                  thuật ngữ, 4 biểu mẫu, phỏng vấn) + Mô hình hóa quy trình (ĐẦY ĐỦ)
  Quản lý hạng vé → Phương pháp thực hiện TRỐNG / Mô hình hóa TRỐNG (chỉ có ảnh BPMN, không có text)
  Tìm kiếm, lựa chọn... → 2 mục con lại bị đặt SAI CẤP (H3 thay vì H4) / cả hai TRỐNG
  Mua thêm dịch vụ sau đặt chỗ → TRỐNG / TRỐNG
  Hỗ trợ khách hàng... → TRỐNG / TRỐNG
  Xuất hóa đơn → TRỐNG / TRỐNG

Chương 3: PHÂN TÍCH CÁC QUY TRÌNH   ⚠️ trùng số với chương trên
  Tìm kiếm, lựa chọn... → VA/lãng phí/định lượng(TG-CL-CP)/stakeholder+Pareto — TẤT CẢ TRỐNG
  Hỗ trợ khách hàng...  (bị đặt sai cấp H2 thay vì H3) → cấu trúc y hệt — TẤT CẢ TRỐNG

Chương 4: KẾT LUẬN → TRỐNG 100%, là dòng cuối cùng của tài liệu
```

**Tỷ trọng nội dung hiện tại:** trong ~565 đoạn văn của toàn tài liệu, khoảng 51% nằm ở Chương 2 (phần mô tả cơ bản, đã tương đối ổn), còn Chương 3 (BPMN) có tới hơn 90% nội dung chỉ tập trung ở **một** quy trình duy nhất (Quản trị giá). Chương 1, Chương 4, toàn bộ Chương 3-Phân tích, và 5/6 mục "Phương pháp thực hiện" còn lại đang trống hoàn toàn.

## 4. Danh sách lỗi cần sửa (gộp từ REVIEW-MoMo.md + phát hiện mới, để tick khi làm)

### 🔴 Cấu trúc (làm trước tiên)
- [x] Đổi số 1 trong 2 "Chương 3" thành Chương 4/5, dồn "KẾT LUẬN" xuống đúng số cuối cùng — bản nháp khung mục lục ở `final/00_CauTrucBaoCao.md` (chưa ghép vào file .docx thật, chờ nhóm duyệt)
- [x] Viết Chương 1 (dùng nguyên liệu ở file 02) — bản nháp `final/Chuong1_TongQuan.md` (mục 1.2/1.3 còn thiếu số liệu thật, đã đánh dấu [CẦN NGUỒN THẬT])
- [x] Viết Chương 4 → **Chương 5** Kết luận (tổng hợp từ các bản Kết luận sẵn có) — bản nháp `final/Chuong5_KetLuan.md`
- [x] Viết lại hoàn toàn bảng câu hỏi phỏng vấn cho quy trình "Quản trị giá": 10 định tính (5 có cấu trúc + 5 không) + 10 định lượng (5+5) — bản nháp `final/Chuong3_QuanTriGia_CauHoiPhongVan.md`. **Còn dở**: chưa nhân rộng cho các quy trình khác (Quản lý hạng vé, Xuất hóa đơn — 25410168 việc #3) và chưa cơ cấu lại bộ câu hỏi có sẵn của 25410223/25410237 (plan/05 mục B)
- [x] Sửa câu Tóm tắt/Mở đầu cho khớp số chương và số quy trình thực tế được phân tích — bản đối chiếu trước/sau ở `final/TomTat_MoDau_Sua.md`

### 🟠 Logic quy trình (theo đúng thứ tự trong REVIEW-MoMo.md mục 2.1 → 2.8)
- [ ] 2.1 Sửa 2 "Bước 1" ở quy trình Quản trị giá → đánh lại số 1–6
- [ ] 2.2 Sửa 3 câu "Mục tiêu" bị lệch (B2/B3/B4) — dùng câu đề xuất sẵn trong REVIEW-MoMo.md
- [ ] 2.3 Sửa nhãn 2 nhánh "(Dữ liệu hợp lệ)" → "KHÔNG hợp lệ"/"CÓ hợp lệ" (Quản lý hạng vé, Bước 4)
- [ ] 2.4 Thêm End Event riêng cho nhánh "KHÔNG công bố" (không quay về Xử lý lỗi)
- [ ] 2.5 Sửa nhãn gateway "(Vé Nội địa)" mâu thuẫn với kiểm tra "Quốc tế" (Mua thêm dịch vụ)
- [ ] 2.6 Làm rõ bảo hiểm du lịch là bước chung hay 2 sản phẩm khác nhau
- [ ] 2.7 Sửa mâu thuẫn phân nhóm quy trình + xóa câu "quy trình ma" (phát hiện mới #3)
- [ ] 2.8 Sửa mốc thời gian chồng lấn trong Kế hoạch làm việc (T+0–4 / T+2–8 / T+6–16)
- [ ] Sửa định nghĩa M_Service trong bảng thuật ngữ (đang định nghĩa nhầm thành "bộ phận thẩm định")

### 🟡 Trình bày (sau khi nội dung đã đủ)
- [ ] Sửa lỗi chính tả: tichet, Developement, kiên trúc, xác đsịnh (REVIEW-MoMo.md mục 3.1)
- [ ] Thống nhất tên bộ phận: "Bộ phận Quản lý giá", "Growth Specialist" (mục 3.2)
- [ ] Chuẩn hóa heading level (cả 2 chỗ bị lỗi — Chương 3-BPMN và Chương 3-Phân tích, phát hiện mới #6)
- [ ] Chèn Mục lục / Danh mục hình / Danh mục bảng / Danh mục từ viết tắt dạng field tự động
- [ ] Caption toàn bộ hình + bảng theo mẫu CellPhones.pdf: `Hình <chương>.<số>`, `Bảng <chương>.<số>`, đăng ký vào danh mục
- [ ] Viết mục Tài liệu tham khảo (có sẵn nguồn thật trong báo cáo 25410206 — xem file 02)
- [ ] Bổ sung bảng phân công công việc nhóm
- [ ] Sửa tab thừa ở "Biểu mẫu 4" (phát hiện mới #5)
- [ ] Kiểm tra lại ngày trên bìa (đang ghi tháng 07/2026)

### 🔵 Trước buổi bảo vệ
- [ ] Dẫn nguồn hoặc ghi "giả định của nhóm" cho: 72 giờ VAT, 2 lần retry API, VACOM
- [ ] Làm rõ tuyên bố "đã phỏng vấn nhân sự nội bộ MoMo" — có bằng chứng thật thì đính kèm phụ lục, không thì đổi câu chữ
- [ ] Bổ sung SLA cụ thể cho CSKH (số phút/giờ phản hồi cam kết)
