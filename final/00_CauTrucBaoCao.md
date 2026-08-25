# KHUNG MỤC LỤC HOÀN CHỈNH — bản đồ ghép nội dung vào `docs/MoMo.docx`

> File này KHÔNG phải nội dung để nộp — là bản đồ nội bộ nhóm dùng để ghép các file trong `final/` và nguyên liệu thành viên vào đúng vị trí trong báo cáo chính thức, giải quyết dứt điểm lỗi trùng số "Chương 3" đang có trong `docs/MoMo.docx` (xem `plan/01_HIEN_TRANG_VA_LOI.md` mục 3).
>
> Quy ước ghi chú mỗi mục: **[XONG]** = đã có nội dung đạt chuẩn trong `docs/MoMo.docx`, không cần sửa nội dung (chỉ cần đánh lại số chương khi ghép). **[DRAFT]** = đã có bản nháp trong `final/` ở phiên này. **[NGUỒN: ...]** = có nguyên liệu sẵn ở thư mục thành viên, cần biên tập trước khi ghép (xem `plan/02_NGUYEN_LIEU_THANH_VIEN.md` và `plan/04_PHAN_CONG_CONG_VIEC.md` để biết ai phụ trách). **[VIẾT MỚI]** = chưa có nguyên liệu, phải viết từ đầu.

---

```
TRANG BÌA                                          [XONG, cần sửa ngày trên bìa — xem final/TomTat_MoDau_Sua.md ghi chú]
MỤC LỤC / DANH MỤC HÌNH VẼ / DANH MỤC BẢNG / DANH MỤC TỪ VIẾT TẮT   [VIẾT MỚI — chèn field tự động, thuộc Giai đoạn 3]
TÓM TẮT ĐỒ ÁN                                       [DRAFT — final/TomTat_MoDau_Sua.md]
MỞ ĐẦU                                              [DRAFT — final/TomTat_MoDau_Sua.md]

Chương 1: TỔNG QUAN VỀ M_SERVICE VÀ DỊCH VỤ ĐẶT VÉ MÁY BAY TRÊN MOMO   [DRAFT — final/Chuong1_TongQuan.md]
  1.1. Lịch sử hình thành
  1.2. Quy mô và lĩnh vực hoạt động
  1.3. Cơ cấu tổ chức

Chương 2: LIỆT KÊ QUY TRÌNH NGHIỆP VỤ                [XONG phần lớn — giữ nguyên nội dung hiện có trong docs/MoMo.docx]
  2.1. Phân loại quy trình                           [XONG — chỉ sửa câu "quy trình ma" ở nhóm Hỗ trợ, xem plan/01 phát hiện mới #3]
  2.2. Kiến trúc quy trình
    2.2.1. Quy trình quản lý (4 quy trình)
      - Quản lý hạng vé                               [XONG]
      - Quản trị giá, khuyến mãi...                   [XONG]
      - Quản trị danh mục hãng bay và đối tác NCC      [NGUỒN: 25410237/MoMo_Quan_tri_danh_muc... — thay bản 1 dòng hiện tại]
      - Quản trị rủi ro giao dịch, điều khoản và CLDV  [NGUỒN: 25410237/HauMai (phần tra soát lỗi) — thiếu góc độ SLA/điều khoản, xem plan/04 việc 25410195 #4]
    2.2.2. Quy trình cốt lõi (3 quy trình)
      - Tìm kiếm, lựa chọn hành trình, thanh toán...   [XONG]
      - Mua thêm dịch vụ sau đặt chỗ                   [XONG]
      - Đổi chuyến bay                                 [NGUỒN: 25410223/cstt.md + Core03 — TRỐNG 100% hiện tại, ưu tiên cao]
    2.2.3. Quy trình hỗ trợ (3 quy trình)
      - Hỗ trợ khách hàng và tiếp nhận phản hồi         [XONG]
      - Xuất hóa đơn                                    [XONG]
      - Quản lý vé đã mua                               [VIẾT MỚI — không thành viên nào có nguyên liệu]

Chương 3: MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN   (đổi số từ "Chương 3" đầu tiên trong docs/MoMo.docx)
  → Đúng 6 quy trình đã chốt phạm vi (plan/03 mục 1, đã xác nhận với người dùng):
  3.1 Quản trị giá, khuyến mãi và chính sách hiển thị giá
    3.1.1 Phương pháp thực hiện    [XONG khung + DRAFT bảng câu hỏi mới — final/Chuong3_QuanTriGia_CauHoiPhongVan.md]
    3.1.2 Mô hình hóa quy trình    [XONG]
  3.2 Quản trị danh mục hãng bay và đối tác NCC
    3.2.1 Phương pháp thực hiện    [NGUỒN: 25410237 — cần cơ cấu lại lưới câu hỏi 2×2, xem plan/05 mục B]
    3.2.2 Mô hình hóa quy trình    [NGUỒN: 25410237 — cần gộp 2 sơ đồ Onboarding+RaSoat để đạt >7 gateway, xem plan/05 mục A]
  3.3 Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé
    3.3.1 Phương pháp thực hiện    [NGUỒN: 25410206 Core01/02/03 — đã đạt chuẩn 20 câu hỏi, chỉ cần hợp nhất 3 file]
    3.3.2 Mô hình hóa quy trình    [NGUỒN: 25410206 — 3 sơ đồ .bpmn sẵn sàng dùng, đều >10 gateway]
  3.4 Đổi chuyến bay
    3.4.1 Phương pháp thực hiện    [VIẾT MỚI gần như từ đầu — 25410223 hiện chỉ có 2-4 câu hỏi, thiếu toàn bộ bằng chứng, xem plan/05 mục B việc #2]
    3.4.2 Mô hình hóa quy trình    [NGUỒN: 25410223/MoMo_Core03...bpmn — chỉ 3 gateway, cần bổ sung nhánh từ cstt.md để đạt >7]
  3.5 Hỗ trợ khách hàng và tiếp nhận phản hồi
    3.5.1 Phương pháp thực hiện    [NGUỒN: 25410237/HauMai — cần cơ cấu lại lưới câu hỏi 2×2]
    3.5.2 Mô hình hóa quy trình    [NGUỒN: 25410237 — sơ đồ TraSoat/XuLyKhieuNai chỉ 2-3 gateway, cân nhắc gộp]
  3.6 Xuất hóa đơn
    3.6.1 Phương pháp thực hiện    [VIẾT MỚI — không ai có nguyên liệu, Chương 2 mô tả 6 bước đã có sẵn để dựa vào]
    3.6.2 Mô hình hóa quy trình    [XONG — chỉ có ảnh BPMN, cần viết thêm phần diễn giải luồng bằng lời]

Chương 4: PHÂN TÍCH CÁC QUY TRÌNH   (đổi số từ "Chương 3" thứ hai trong docs/MoMo.docx)
  → Đúng 3 quy trình đã chốt phạm vi:
  4.1 Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé
      [NGUỒN: 25410206 Core01/02/03 (đã đạt chuẩn) — cần sửa công thức Chi phí/rework, xem plan/05 mục C]
  4.2 Hỗ trợ khách hàng và tiếp nhận phản hồi
      [NGUỒN: 25410237/HauMai — chỉ cần bổ sung cột mô tả+khắc phục ở bảng VA]
  4.3 (bonus) Quản trị giá, khuyến mãi và chính sách hiển thị giá
      [NGUỒN: 25410206/MoMo.docx (bản riêng) — hiện đang bị gắn NHẦM tên dưới "Tìm kiếm...", cần đổi lại đúng tên quy trình trước khi dùng]

Chương 5: KẾT LUẬN   (đổi số từ "Chương 4" trong docs/MoMo.docx)
  [DRAFT — final/Chuong5_KetLuan.md, tổng hợp từ Kết luận của 25410206 (Core01) + 25410237 (HauMai, Quan_tri_danh_muc)]

TÀI LIỆU THAM KHẢO   [NGUỒN: có sẵn trích dẫn thật trong 25410206 (4 file) + 25410237 (2 file) — nhóm trưởng tổng hợp, loại trùng]

PHỤ LỤC   [tùy chọn — chỉ dùng nếu có bằng chứng phỏng vấn thật; hiện nhóm xác nhận KHÔNG phỏng vấn thật nên có thể bỏ mục này hoặc dùng để lưu bộ câu hỏi mô phỏng đầy đủ]
```

## Ghi chú khi ghép

- Toàn bộ mục đánh **[XONG]** vẫn phải rà lại lỗi logic quy trình (Giai đoạn 2, `plan/01` mục 4 phần 🟠) trước khi coi là hoàn thiện — file này chỉ xử lý lỗi **cấu trúc/khoảng trống**, không phải lỗi logic.
- Số hình/bảng cần đánh lại theo đúng quy ước `Hình <chương>.<số>` / `Bảng <chương>.<số>` sau khi chốt số chương ở trên (`plan/03` mục 3) — việc này làm ở Giai đoạn 3, chưa làm trong file này.
- Việc "Quản lý vé đã mua" và "Xuất hóa đơn — Phương pháp thực hiện" vẫn còn **[VIẾT MỚI]** sau phiên này — chưa nằm trong phạm vi Giai đoạn 1 đã chốt (xem plan cho phiên này), để phiên sau hoặc phân công theo `plan/04`.
