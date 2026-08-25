# CẤU TRÚC BÁO CÁO MỤC TIÊU

> Đối chiếu giữa: (a) yêu cầu Rubric, (b) khung lý thuyết bài giảng chap01–08, (c) cấu trúc đồ án tham khảo `CellPhones.pdf`, và (d) nguyên liệu thực tế đang có (file 02). Đây là bản thiết kế TOC cuối cùng nhóm nên nhắm tới.

## 1. Quyết định phạm vi — quy trình nào được đầu tư mức nào

Rubric chỉ **bắt buộc**: 6 quy trình có BPMN + Phương pháp thực hiện đầy đủ (2 Quản lý + 2 Cốt lõi + 2 Hỗ trợ), và 2 quy trình có chương Phân tích đầy đủ. Nhóm đã có 10 quy trình được liệt kê (đủ điều kiện rubric 1.0: 4 Quản lý + 3 Cốt lõi + 3 Hỗ trợ). Dựa trên nguyên liệu sẵn có, đề xuất:

| Nhóm | Quy trình chọn đầu tư đầy đủ (BPMN + Phương pháp thực hiện) | Vì sao |
|---|---|---|
| Quản lý (chọn 2/4) | **Quản trị giá, khuyến mãi...** (đã xong) + **Quản trị danh mục hãng bay và đối tác NCC** | Đã có nguyên liệu 8 chương đầy đủ từ 25410237, giải quyết luôn khoảng trống bị review chỉ ra |
| Cốt lõi (chọn 2/3) | **Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé** + **Đổi chuyến bay** | Có nguyên liệu tốt nhất (25410206) + là quy trình duy nhất còn trống 100%, giải quyết dứt điểm |
| Hỗ trợ (chọn 2/3) | **Hỗ trợ khách hàng và tiếp nhận phản hồi** + **Xuất hóa đơn** | 25410237 có sẵn cho Hỗ trợ KH; Xuất hóa đơn đã có mô tả Chương 2 tốt, chỉ cần bổ sung Phương pháp thực hiện theo mẫu |

→ "Mua thêm dịch vụ sau đặt chỗ" và "Quản lý vé đã mua" và "Quản trị rủi ro giao dịch" **vẫn giữ trong danh sách 10 quy trình** (đủ mô tả cơ bản: tác nhân/bước/đối tượng KH/kết quả cho rubric 1.0) nhưng KHÔNG bắt buộc phải đầu tư BPMN + Phương pháp thực hiện sâu — trừ khi nhóm còn dư thời gian (có sẵn nguyên liệu cho "Mua thêm dịch vụ" nên làm thêm nếu kịp, vì gần như miễn phí).

**Chương Phân tích đầy đủ** (định tính + định lượng), chọn tối thiểu 2, đề xuất 3 (rất rẻ vì đã có sẵn):
1. **Tìm kiếm, lựa chọn hành trình...** ← từ 25410206 (3 file Core0X) + 25410223
2. **Hỗ trợ khách hàng...** ← từ 25410237 (HauMai)
3. *(bonus)* **Quản trị giá, khuyến mãi...** ← từ chương Phân tích 25410206 để nhầm tên, chỉ cần đổi nhãn lại đúng quy trình — vì đây là quy trình "mẫu" đã đầy đủ Phương pháp thực hiện, có thêm Phân tích sẽ thành quy trình hoàn chỉnh nhất bài, rất ấn tượng khi bảo vệ

## 2. Cấu trúc chương mục tiêu (đối chiếu CellPhones.pdf + rubric 5.0)

Phần đầu tài liệu (front matter) — theo đúng mẫu CellPhones.pdf, đây là các mục nhóm hiện đang thiếu hoặc để trống:
- Trang bìa (đã có, sửa lại ngày)
- MỤC LỤC (auto field)
- DANH MỤC HÌNH VẼ (auto field)
- DANH MỤC BẢNG (auto field)
- DANH MỤC TỪ VIẾT TẮT (bảng 2 cột thuật ngữ/giải nghĩa — danh sách đã có sẵn trong REVIEW-MoMo.md mục 3.7)
- TÓM TẮT ĐỒ ÁN (đã có, cần sửa số liệu cho khớp)
- MỞ ĐẦU (đã có, cần sửa khớp thân bài — nêu rõ phạm vi: vì sao chỉ 6/10 quy trình được mô hình hóa sâu, giống cách CellPhones.pdf giải thích phạm vi ở phần Mở đầu)

Thân bài — đề xuất đánh lại số chương thành **5 chương** (theo Phương án A trong REVIEW-MoMo.md mục 1.1):

```
Chương 1: TỔNG QUAN VỀ M_SERVICE VÀ DỊCH VỤ ĐẶT VÉ MÁY BAY TRÊN MOMO
  1.1. Lịch sử hình thành
  1.2. Quy mô và lĩnh vực hoạt động
  1.3. Cơ cấu tổ chức

Chương 2: LIỆT KÊ QUY TRÌNH NGHIỆP VỤ  (giữ nguyên, chỉ vá 4 khoảng trống + sửa nhóm mâu thuẫn)
  2.1. Phân loại quy trình
  2.2. Kiến trúc quy trình  (sơ đồ kiến trúc — bắt buộc rubric 1.4)
    2.2.1. Quy trình quản lý (4 quy trình)
    2.2.2. Quy trình cốt lõi (3 quy trình)
    2.2.3. Quy trình hỗ trợ (3 quy trình)

Chương 3: MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN  (6 quy trình theo mục 1, mỗi quy trình theo mẫu "Quản trị giá":
  Phương pháp thực hiện [bằng chứng + phỏng vấn] → Mô hình hóa quy trình)

Chương 4: PHÂN TÍCH CÁC QUY TRÌNH  (2-3 quy trình theo mục 1, mỗi quy trình theo mẫu CellPhones.pdf:
  Phân tích định tính [VA/BVA/NVA + Lãng phí] → Phân tích các bên liên quan [Stakeholder + Pareto/Fishbone/Root-cause]
  → Phân tích định lượng [Thời gian + Chất lượng + Chi phí])

Chương 5: KẾT LUẬN

TÀI LIỆU THAM KHẢO  (mục hiện đang không tồn tại — bắt buộc bổ sung, đã có nguồn thật từ 25410206)

PHỤ LỤC (tùy chọn — nếu có bằng chứng phỏng vấn thật thì để ở đây)
```

> Lưu ý: đổi 4→5 chương là lựa chọn rõ ràng hơn Phương án B (gộp Phân tích làm mục con của Chương 3) vì Phân tích và Mô hình hóa BPMN là 2 tiêu chí rubric **tách biệt** (2.0 và 4.0) — tách thành 2 chương riêng giúp giám khảo dễ đối chiếu điểm hơn.

## 3. Quy ước đánh số hình/bảng (theo mẫu CellPhones.pdf)

- `Hình <số chương>.<số thứ tự>` — VD: `Hình 3.1`, `Hình 3.2`... mỗi chương đếm lại từ 1.
- `Bảng <số chương>.<số thứ tự>` — tương tự.
- Caption hình đặt **dưới** hình, caption bảng đặt **trên** bảng (đúng yêu cầu rubric 5.0: "label hình nằm dưới, label bảng nằm trên").
- Dùng Word References → Insert Caption để tự động đánh số và tự động đồng bộ vào Danh mục hình/Danh mục bảng.

## 4. Khung mẫu áp dụng cho MỖI quy trình được mô hình hóa đầy đủ ở Chương 3 (giữ nguyên mẫu "Quản trị giá" đã làm tốt, theo đúng nhận xét trong REVIEW-MoMo.md phần "Phụ lục — những phần đã làm tốt")

```
X.1 Phương pháp thực hiện
  X.1.1 Dựa trên bằng chứng
    - Sơ đồ tổ chức và trách nhiệm
    - Kế hoạch làm việc (mục tiêu + bảng công việc theo mốc thời gian không chồng lấn)
    - Công nghệ hỗ trợ đề xuất
    - Rủi ro và giải pháp (gắn với từng gateway trong BPMN)
    - Thuật ngữ và sổ tay
    - Biểu mẫu (kèm mục đích + người sử dụng)
  X.1.2 Phỏng vấn
    - Câu hỏi định tính (5 có cấu trúc + 5 không cấu trúc)
    - Câu hỏi định lượng (5 có cấu trúc + 5 không cấu trúc) — PHẢI hỏi ra con số thật
X.2 Mô hình hóa quy trình
  - Sơ đồ BPMN (đủ độ phức tạp — nên có >5 gateway để đạt điểm cao ở rubric 2.0)
  - Diễn giải luồng chính (Happy path)
  - Diễn giải luồng ngoại lệ (Exception flows)
```

## 5. Khung mẫu áp dụng cho MỖI quy trình có chương Phân tích (theo mẫu CellPhones.pdf, khớp rubric 4.0 + lý thuyết chap05)

```
X.1 Phân tích quy trình (actors / khách hàng của quy trình / giá trị mang lại / kết quả có thể đạt được)
X.2 Phân tích định tính
  X.2.1 Phân tích giá trị gia tăng — bảng: Bước | Người thực hiện | Phân loại (VA/BVA/NVA) | Mô tả | Khắc phục
  X.2.2 Phân tích lãng phí — bảng theo 3 nhóm Move/Hold/Overdo (dùng đúng taxonomy 7 lãng phí trong chap05):
        liệt kê | mô tả | khắc phục
X.3 Phân tích các bên liên quan
  - Chọn 1 trong 3: biểu đồ Pareto / phân tích nguyên nhân-kết quả (5 Whys) / sơ đồ xương cá (Fishbone)
  - Issue Register: Tên vấn đề | Giải thích | Giả định | Tác động định tính | Tác động định lượng
X.4 Phân tích định lượng
  X.4.1 Thời gian — công thức cycle time theo chap05 (tuần tự=tổng, XOR=trung bình có trọng số xác suất,
        AND=max, rework=T/(1-r)) + hiệu suất thời gian (%)
  X.4.2 Chất lượng — chỉ số lỗi/tỷ lệ rework, ví dụ PCE/RTY nếu có sẵn số liệu (25410206 đã tính sẵn)
  X.4.3 Chi phí — theo đầu người + mức lương, tổng chi phí/chu kỳ + hiệu suất chi phí (%)
  → Mỗi mục đều cần cột "khắc phục" — dùng đúng thuật ngữ 9 heuristic (H1-H9) hoặc 5 nguyên tắc BPR
    trong chap06 để đề xuất có cơ sở lý thuyết, không chỉ nói chung chung
```
