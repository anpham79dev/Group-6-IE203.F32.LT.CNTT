# BÁO CÁO REVIEW TÀI LIỆU — `MoMo.docx`

> **Đề tài:** Tìm hiểu về hệ thống quy trình nghiệp vụ mảng đặt vé máy bay trên ứng dụng MoMo (M_Service)
> **Môn:** Hệ thống Quản trị Quy trình Nghiệp vụ — IE203.F32.LT.CNTT
> **Ngày review:** 24/08/2026
> **Phạm vi rà soát:** Toàn văn — 578 đoạn, 15 hình, 12 bảng

---

## TÓM TẮT NHANH

| Mức độ | Số lỗi | Ghi chú |
|---|---|---|
| 🔴 Nặng — phải sửa trước khi nộp | 5 nhóm | Trùng số chương, bảng câu hỏi copy, nhiều chương trống |
| 🟠 Logic quy trình | 8 lỗi | Đánh số bước sai, mục tiêu lệch, nhãn gateway sai |
| 🟡 Chính tả / trình bày | 8 lỗi | Ảnh hưởng Mục lục & Danh mục hình tự động |
| 🔵 Rủi ro bị vặn khi bảo vệ | 4 điểm | Số liệu chưa nguồn, tuyên bố phỏng vấn |

**Ba việc cấp bách nhất:**
1. Bảng "Câu hỏi định lượng" bị copy y hệt bảng "Câu hỏi định tính" (8/8 câu giống 100%).
2. Có **hai** chương cùng đánh số "Chương 3".
3. Chương 1, Chương 4 và **toàn bộ chương Phân tích** đang trống — đây là phần chiếm điểm cao nhất.

---

## 🔴 NHÓM 1 — LỖI NẶNG, PHẢI SỬA TRƯỚC KHI NỘP

### 1.1. Trùng số chương: có 2 "Chương 3"

Hiện tại:
- `Chương 3: MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN`
- `Chương 3: PHÂN TÍCH CÁC QUY TRÌNH`

**Cách sửa (chọn 1):**
- **Phương án A:** Đổi thành Chương 4 (Phân tích) và Chương 5 (Kết luận) → cập nhật lại phần Mở đầu thành "5 chương".
- **Phương án B:** Gộp Phân tích thành mục con của Chương 3, giữ nguyên 4 chương như Mở đầu đã cam kết.

---

### 1.2. Bảng "Câu hỏi định lượng" bị copy y hệt bảng "Câu hỏi định tính"

Cả 8 câu ở hai bảng giống nhau **100%** (chỉ khác duy nhất dòng "Đối tượng áp dụng" của câu 3 có thêm chữ "(M_Service)").

Câu định lượng phải thu được **con số**. Gợi ý bộ câu hỏi thay thế:

| STT | Câu hỏi định lượng đề xuất | Đối tượng |
|---|---|---|
| 1 | Trung bình mất bao nhiêu giờ để chuẩn hóa xong 1 bộ dữ liệu giá? (≤2h / 2–4h / 4–8h / >8h) | Bộ phận Giá |
| 2 | Trung bình 1 tuần tiếp nhận bao nhiêu bộ dữ liệu giá từ Hãng bay/NCC? | Bộ phận Giá |
| 3 | Bao nhiêu % bộ dữ liệu bị trả lại yêu cầu bổ sung ở lần gửi đầu tiên? | Bộ phận Giá |
| 4 | Bao nhiêu % hồ sơ khuyến mãi bị Tài chính/Pháp chế từ chối ở lần trình đầu? | Tài chính/Pháp chế |
| 5 | Thời gian trung bình từ lúc nhận hồ sơ đến khi ra quyết định phê duyệt? | Tài chính/Pháp chế |
| 6 | Số lần phải cấu hình lại (rework) trung bình cho 1 chiến dịch KM? | Growth/Kỹ thuật |
| 7 | Thời gian trung bình cho 1 lượt kiểm thử hiển thị trên App? | Kỹ thuật, Marketing |
| 8 | Số ticket khiếu nại liên quan sai giá/sai KM phát sinh mỗi tháng? | CSKH |
| 9 | Tổng thời gian chu kỳ (cycle time) trung bình từ nhận dữ liệu đến công bố? | Tất cả |
| 10 | Số nhân sự tham gia và số giờ công tiêu tốn cho 1 lần chạy quy trình? | Tất cả |

> 💡 Các câu 9–10 sẽ là **đầu vào bắt buộc** cho phần Phân tích định lượng (thời gian chu kỳ, chi phí nhân sự) ở chương sau.

---

### 1.3. Phần Mở đầu không khớp với thân bài

| Mở đầu tuyên bố | Thực tế trong bài |
|---|---|
| Ch.1: Giới thiệu tổng quan về M_Service và dịch vụ đặt vé trên MoMo | Ch.1 tiêu đề là "TỔNG QUAN LỊCH SỬ HÌNH THÀNH, QUY MÔ LĨNH VỰC VÀ CƠ CẤU TỔ CHỨC" — và **trống hoàn toàn** |
| Ch.2: Sơ đồ kiến trúc hệ thống quy trình nghiệp vụ | Ch.2 tiêu đề là "LIỆT KÊ QUY TRÌNH NGHIỆP VỤ" |
| "Đồ án được chia thành 4 chương" | Thực tế đang có 5 khối chương (do trùng số 3) |
| Tóm tắt: "phân tích chi tiết 6 quy trình… **mỗi quy trình** được đánh giá qua hai lăng kính (định tính + định lượng)" | Chỉ 2/6 quy trình có mục Phân tích, và **cả 2 mục đó đều đang trống** |

**Cách sửa:** thống nhất lại tên chương ở Mở đầu = tên chương thật trong thân bài; sửa câu Tóm tắt cho đúng số quy trình được phân tích thực tế.

---

### 1.4. Các phần chỉ có tiêu đề, chưa có nội dung

Đây là khối lượng công việc còn thiếu lớn nhất — cần chia người làm ngay:

| Vị trí | Tình trạng | Gợi ý phân công |
|---|---|---|
| **Chương 1** (Tổng quan M_Service) | Trống 100% | 1 bạn |
| **Chương 4 — KẾT LUẬN** | Trống 100% | 1 bạn (làm sau cùng) |
| **Chương Phân tích** — VA/BVA/NVA, Phân tích lãng phí, Định lượng (Thời gian / Chất lượng / Chi phí), Stakeholder analysis, Issue register, Biểu đồ Pareto — cho cả 2 quy trình | Trống 100% | 2–3 bạn, **ưu tiên cao nhất** |
| **Chương 3** — mục "Phương pháp thực hiện" của 5 quy trình: Quản lý hạng vé, Đặt vé, Mua thêm dịch vụ, Hỗ trợ KH, Xuất hóa đơn | Chỉ có heading + ảnh BPMN. Duy nhất "Quản trị giá" là làm đầy đủ | Mỗi bạn 1 quy trình, copy cấu trúc của mục "Quản trị giá" |
| **Chương 2** — 3 quy trình chỉ có tên: *Quản trị rủi ro giao dịch*, *Đổi chuyến bay*, *Quản lý vé đã mua* | Thiếu Tác nhân / Mô tả các bước / Đối tượng KH / Kết quả | 1 bạn |
| **Chương 2** — *Quản trị danh mục hãng bay và đối tác NCC* | Có nhưng quá sơ sài (Mô tả các bước chỉ 1 dòng) | Bổ sung theo chuẩn các mục khác |
| MỤC LỤC / DANH MỤC HÌNH VẼ / DANH MỤC BẢNG / DANH MỤC TỪ VIẾT TẮT | Trống — chưa chèn field tự động | Làm sau khi chuẩn hóa heading |
| **TÀI LIỆU THAM KHẢO** | **Không tồn tại mục này** | Bắt buộc bổ sung |
| **Bảng phân công công việc nhóm** | Không có (chỉ có bảng 8 thành viên trên bìa) | Bắt buộc bổ sung |

---

### 1.5. Định nghĩa "M_Service" trong bảng Thuật ngữ bị sai hoàn toàn

Bảng thuật ngữ ghi:

> **M_Service** — "Mã nội bộ (hoặc tên gọi) chỉ nhóm bộ phận đảm nhiệm việc thẩm định rủi ro Tài chính và tuân thủ Pháp chế đối với các chính sách giá/KM trước khi ban hành."

Trong khi **trang bìa và toàn bộ phần còn lại** đều dùng M_Service = **Công ty Cổ phần Dịch vụ Di động Trực tuyến**, tức pháp nhân chủ sở hữu MoMo. Đây là mâu thuẫn nội tại rất dễ bị hỏi khi bảo vệ.

**Cách sửa:** đổi định nghĩa về đúng nghĩa pháp nhân; nếu muốn giữ khái niệm "bộ phận thẩm định" thì đặt tên riêng, ví dụ *"Khối Tài chính/Pháp chế (Finance & Legal)"*.

---

## 🟠 NHÓM 2 — LỖI LOGIC QUY TRÌNH

### 2.1. Quy trình "Quản trị giá, khuyến mãi và chính sách hiển thị giá" có **hai** "Bước 1"

- `Bước 1: Hãng bay/ Nhà cung cấp cung cấp dữ liệu vé`
- `Bước 1: Tiếp nhận dữ liệu giá từ nhà cung cấp` ← phải là **Bước 2**

→ Quy trình thực chất có **6 bước**, toàn bộ số thứ tự phía sau đang bị lệch 1.

---

### 2.2. Phần "Mục tiêu" bị copy-paste lệch một bước

Cùng quy trình Quản trị giá — mục tiêu ghi ở mỗi bước lại là mục tiêu của bước khác:

| Bước | Mục tiêu đang ghi | Thực ra là mục tiêu của |
|---|---|---|
| B2: *Marketing xây dựng chương trình khuyến mãi* | "Đảm bảo dữ liệu nhận được chính xác và phù hợp với định dạng yêu cầu của hệ thống MoMo trước khi tiến hành cài đặt" | bước **chuẩn hóa dữ liệu** |
| B3: *Tài chính thẩm định rủi ro* | "Thiết lập thông tin hạng vé lên hệ thống máy chủ để chuẩn bị sẵn sàng cho việc mở bán" | bước **cấu hình kỹ thuật** |
| B4: *Kỹ thuật cấu hình giá lên hệ thống* | "Kiểm soát chất lượng, đảm bảo tuyệt đối không có sai sót về giá cả hay điều kiện vé trước khi đưa ra thị trường" | bước **kiểm thử hiển thị** |

**Mục tiêu đúng nên là:**
- B2 → "Thiết kế cơ chế ưu đãi phù hợp tệp khách hàng mục tiêu, đảm bảo hiệu quả ngân sách marketing."
- B3 → "Thẩm định tính khả thi tài chính và tuân thủ pháp lý của chính sách giá/KM trước khi ban hành."
- B4 → "Đưa chính sách đã phê duyệt vào hệ thống dưới dạng tham số cấu hình chính xác."

---

### 2.3. Nhãn nhánh Có/Không bị đảo — Quy trình "Quản lý hạng vé", Bước 4

Văn bản hiện tại:

> "Trường hợp **KHÔNG (Dữ liệu hợp lệ)**: Trả kết quả về cho Ticketing để *Xử lý lỗi và điều chỉnh*…"
> "Trường hợp **CÓ (Dữ liệu hợp lệ)**: Chuyển thông tin cho Ticketing."

Hai nhánh đang mang **cùng một nhãn** "(Dữ liệu hợp lệ)". Phải sửa thành *"KHÔNG hợp lệ"* / *"CÓ hợp lệ"*.

---

### 2.4. Gateway "Có công bố không?" — nhánh KHÔNG đang quay về "Xử lý lỗi"

Nếu quyết định **không công bố** thì lý do có thể là quyết định kinh doanh (chưa đúng thời điểm, hoãn chiến dịch…), chứ không nhất thiết vì lỗi kỹ thuật. Việc bắt buộc quay về "Xử lý lỗi và điều chỉnh" tạo vòng lặp vô nghĩa.

**Cách sửa:** thêm một End Event riêng — *"Tạm hoãn / Hủy công bố hạng vé"*.

---

### 2.5. "Mua thêm dịch vụ sau đặt chỗ" — nhãn nhánh gán sẵn loại vé trước khi kiểm tra

> "Trường hợp tự thao tác trên App **(Vé Nội địa)**: Khách hàng truy cập App và chọn vé đã mua. Hệ thống kiểm tra, **nếu là vé Quốc tế**, App sẽ hiển thị Thông báo liên hệ CSKH."

Nhánh đã dán nhãn "Vé Nội địa" rồi lại kiểm tra ra "Quốc tế" → mâu thuẫn logic. Tương tự ở nhánh CSKH.

**Cách sửa:** nhãn của gateway đầu tiên chỉ nên là **"Qua App"** / **"Qua CSKH"**; việc phân loại nội địa/quốc tế để gateway kế tiếp xử lý.

---

### 2.6. Bảo hiểm du lịch — áp dụng cho nội địa hay cả hai?

> "Trường hợp **Quốc tế**: Khách hàng có thể chuyển thẳng đến các bước **mua bảo hiểm** và xác nhận."
> "Trường hợp **Nội địa**: … và **Chọn bảo hiểm du lịch toàn diện**."

Bảo hiểm xuất hiện ở cả hai nhánh nhưng được mô tả như hai thứ khác nhau. Cần làm rõ: bảo hiểm là bước **chung** sau khi hợp nhất hai nhánh, hay là hai sản phẩm bảo hiểm khác nhau.

---

### 2.7. Mâu thuẫn phân loại nhóm quy trình (Chương 2)

| Vấn đề | Chi tiết |
|---|---|
| Xếp nhóm mâu thuẫn | Phần mô tả xếp *"Xây dựng công bố giá bán cuối cùng"* vào **nhóm Cốt lõi**, nhưng phần Kiến trúc lại đặt *"Quản trị giá, khuyến mãi và chính sách hiển thị giá"* ở **nhóm Quản lý** |
| Mô tả có, danh sách không | Mô tả nhóm Hỗ trợ nhắc *"đối soát tài chính và bảo trì kỹ thuật (API)"* nhưng không có quy trình nào tương ứng trong phần Kiến trúc |
| Danh sách có, mô tả không | *"Quản lý vé đã mua"*, *"Đổi chuyến bay"*, *"Quản trị rủi ro giao dịch"* có trong Kiến trúc nhưng không được nhắc ở phần mô tả nhóm |

**Cách sửa:** lập một bảng đối chiếu 3 nhóm × danh sách quy trình, đảm bảo mô tả và danh sách khớp 1–1.

---

### 2.8. Mốc thời gian trong bảng Kế hoạch làm việc bị chồng lấn

`T+0–4` → `T+2–8` → `T+6–16` → `T+16–20` → `T+20–28` → `T+28–30`

Ba mốc đầu chồng lấn nhau (0–4 vs 2–8 vs 6–16). Nếu là luồng **tuần tự** thì phải liền mạch; nếu cho phép **gối đầu/song song** thì cần thêm một câu giải thích ngay dưới bảng.

---

## 🟡 NHÓM 3 — CHÍNH TẢ, THUẬT NGỮ, TRÌNH BÀY

### 3.1. Lỗi chính tả cần sửa

| Đang viết | Sửa thành |
|---|---|
| "Bộ phận **tichet** cấu hình lên hệ thống" | Bộ phận **Ticketing** |
| "Business **Developement**" | Business **Development** |
| "Hình 1.1. Sơ đồ **kiên** trúc" | Sơ đồ **kiến** trúc |
| "**xác đsịnh** nguyên nhân" | **xác định** nguyên nhân |
| "…từ chối cung cấp thêm dịch vụ**..**" | thừa một dấu chấm |

### 3.2. Tên bộ phận không nhất quán

| Cùng một bộ phận, đang gọi 3 kiểu | Đề xuất chốt |
|---|---|
| "Bộ phận Vé giá" / "Bộ phận về giá" / "Bộ phận quản lý giá" | **Bộ phận Quản lý giá** |
| "Growth specialist" / "**Group** Specialist" (bảng kế hoạch ghi sai) | **Growth Specialist** |
| "Bộ phận Kỹ thuật" / "Growth specialist/Kỹ thuật" | **Bộ phận Growth Specialist / Kỹ thuật** |

> Nên tạo một bảng "quy ước tên tác nhân" ở đầu Chương 2 và dùng thống nhất toàn bài.

### 3.3. Câu tối nghĩa / lặp ý

> "Bộ phận Giá **đóng** thực hiện rà soát." → thừa/sai từ, nên là *"Bộ phận Giá thực hiện rà soát."*

> "Kiểm tra tính đầy đủ của dữ liệu. **Nếu thiếu** sẽ yêu cầu hãng bổ sung **nếu dữ liệu thiếu**." → lặp mệnh đề điều kiện.

### 3.4. Danh sách Tác nhân thiếu so với thân bài

Quy trình "Quản trị giá" liệt kê 5 tác nhân, nhưng thân bài còn có **Pháp chế**, **Growth Specialist**, **Ứng dụng MoMo**. Cần bổ sung cho khớp với swimlane trong BPMN.

### 3.5. Chỉ 1/15 hình có caption

- Duy nhất `Hình 1.1. Sơ đồ kiên trúc` có caption; **toàn bộ sơ đồ BPMN không được đánh số/caption** → không thể tạo Danh mục hình vẽ.
- Không bảng nào có caption → không thể tạo Danh mục bảng.
- `Hình 1.1` lại đang nằm trong **Chương 2** → phải đổi thành **Hình 2.1**.

**Việc cần làm:** dùng References → Insert Caption cho toàn bộ hình và bảng, đánh số theo chương (2.1, 2.2, 3.1…).

### 3.6. Heading level lộn xộn (ảnh hưởng trực tiếp đến Mục lục tự động)

| Vị trí | Vấn đề |
|---|---|
| Chương 3, mục *"Tìm kiếm, lựa chọn hành trình…"* | Bản thân là Heading 3, nhưng *"Phương pháp thực hiện"* và *"Mô hình hóa quy trình"* nằm dưới nó **cũng là Heading 3** (các quy trình khác dùng Heading 4) |
| Chương Phân tích | *"Tìm kiếm…"* = Heading 3 nhưng *"Hỗ trợ khách hàng…"* = Heading 2 — hai mục đồng cấp mà khác level |
| Bộ câu hỏi | *"Câu hỏi định tính"* = Heading 6, *"Câu hỏi định lượng"* = Heading 7 — phải cùng cấp |
| Tiêu đề chương | "Chương 2**.**" dùng dấu chấm, các chương khác dùng dấu hai chấm |

### 3.7. Danh mục từ viết tắt đang trống

Các từ viết tắt đã dùng trong bài cần đưa vào bảng: **OTA, BPMN, BPMS, NCC, BD, KM, CSKH, VAT, SLA, UAT, T&C, ETL, CRM, BI, DMS, VA/BVA/NVA, API**.

### 3.8. Ngày trên trang bìa

Bìa ghi *"TP. Hồ Chí Minh, tháng 07 năm 2026"* — kiểm tra lại có đúng tháng nộp không (hiện đã là tháng 08/2026).

---

## 🔵 NHÓM 4 — ĐIỂM DỄ BỊ VẶN KHI BẢO VỆ

### 4.1. Số liệu nghiệp vụ chưa có nguồn

Các con số cụ thể sau đang xuất hiện mà không có trích dẫn:

| Số liệu | Vị trí | Cần làm |
|---|---|---|
| Thời hạn **72 giờ (3 ngày)** để yêu cầu xuất VAT | Quy trình Xuất hóa đơn | Dẫn nguồn (điều khoản MoMo / quy định thuế) hoặc ghi rõ **"giả định của nhóm"** |
| Giới hạn **2 lần** retry tích hợp API | Quy trình Quản lý hạng vé | Như trên |
| Hệ thống hóa đơn điện tử **VACOM** | Quy trình Xuất hóa đơn | Nêu nguồn xác nhận MoMo dùng nhà cung cấp này |

> ⚠️ Nếu là giả định thì **bắt buộc ghi rõ** — giảng viên thường hỏi thẳng "con số này lấy từ đâu".

### 4.2. Tuyên bố "đã phỏng vấn nhân sự nội bộ MoMo"

> "Nhóm thực hiện đã phối hợp cùng nhân sự nội bộ tại MoMo để tiến hành trao đổi và thu thập thông tin từ các bộ phận liên quan."

- **Nếu có phỏng vấn thật:** phải đính kèm biên bản / danh sách người được phỏng vấn / ngày phỏng vấn ở Phụ lục.
- **Nếu chưa phỏng vấn được:** đổi câu thành *"Nhóm đã xây dựng bộ câu hỏi khảo sát dự kiến…"* và ghi rõ mô hình As-Is được **suy luận từ trải nghiệm người dùng thực tế và tài liệu công khai**.

Nếu để nguyên như hiện tại mà không có bằng chứng, toàn bộ mục "Dựa trên bằng chứng" sẽ mất giá trị.

### 4.3. Chưa có SLA cụ thể cho CSKH

Bài chỉ ghi *"phân cấp hỗ trợ 24/7 (nếu là Khách hàng VIP) hoặc hỗ trợ giờ hành chính"*. Cần bổ sung **thời gian phản hồi cam kết** (ví dụ: VIP ≤15 phút, thường ≤4 giờ) — vì chương Phân tích định lượng sẽ cần chính con số này để tính thời gian chu kỳ.

### 4.4. Bộ Biểu mẫu / Thuật ngữ / Rủi ro chỉ làm cho 1 quy trình

Hiện chỉ quy trình *"Quản trị giá"* có đủ: Sơ đồ tổ chức & trách nhiệm, Kế hoạch làm việc, Công nghệ hỗ trợ, Rủi ro & giải pháp, Thuật ngữ, 4 Biểu mẫu, Bộ câu hỏi.

**Chọn 1 trong 2:**
- Làm đủ cho cả 6 quy trình (khối lượng lớn), **hoặc**
- Thêm một câu giới hạn phạm vi: *"Nhóm chọn quy trình Quản trị giá làm mẫu trình bày đầy đủ phương pháp; 5 quy trình còn lại áp dụng cùng cấu trúc và được tóm lược."*

---

## ✅ CHECKLIST THỨ TỰ THỰC HIỆN

| # | Việc | Ưu tiên | Người phụ trách |
|---|---|---|---|
| 1 | Sửa trùng số chương + viết **Chương 1** và **Chương 4 (Kết luận)** | 🔴 Cao nhất | |
| 2 | Viết lại **bảng Câu hỏi định lượng** | 🔴 Cao nhất | |
| 3 | Điền **chương Phân tích**: VA/BVA/NVA, Lãng phí, Thời gian–Chất lượng–Chi phí, Stakeholder, Issue register, Pareto | 🔴 Cao nhất | |
| 4 | Sửa lỗi logic quy trình (mục 2.1 → 2.8) | 🟠 Cao | |
| 5 | Sửa định nghĩa **M_Service** + thống nhất tên bộ phận toàn bài | 🟠 Cao | |
| 6 | Bổ sung "Phương pháp thực hiện" cho 5 quy trình còn lại (Ch.3) | 🟠 Cao | |
| 7 | Bổ sung mô tả cho 3 quy trình còn trống ở Ch.2 | 🟡 TB | |
| 8 | Chuẩn hóa heading level → chèn Mục lục / Danh mục hình / Danh mục bảng tự động | 🟡 TB | |
| 9 | Đánh caption toàn bộ hình & bảng | 🟡 TB | |
| 10 | Bổ sung **Danh mục từ viết tắt**, **Tài liệu tham khảo**, **Bảng phân công công việc** | 🟡 TB | |
| 11 | Rà lại chính tả (mục 3.1) + ngày trên bìa | 🟡 Thấp | |
| 12 | Dẫn nguồn cho số liệu 72h / 2 lần retry / VACOM; làm rõ tuyên bố phỏng vấn | 🔵 Trước buổi bảo vệ | |

---

## PHỤ LỤC — NHỮNG PHẦN ĐÃ LÀM TỐT

Để nhóm biết đâu là phần nên giữ nguyên và nhân rộng:

- **Quy trình "Quản trị giá, khuyến mãi và chính sách hiển thị giá"** ở Chương 3 là mẫu trình bày tốt — có đủ Sơ đồ tổ chức & trách nhiệm, Kế hoạch làm việc (mục tiêu + bảng công việc), Bảng công nghệ hỗ trợ đề xuất, Bảng rủi ro & giải pháp, Bảng thuật ngữ, 4 biểu mẫu kèm mục đích/người sử dụng, và phần Diễn giải luồng tách rõ **Luồng chính** vs **Luồng ngoại lệ**. → **Dùng đúng cấu trúc này cho 5 quy trình còn lại.**
- **Bảng Công nghệ hỗ trợ đề xuất** (API+ETL, Rule Engine, CRM+BI, BPM, DMS, Backend API, Automated Testing, API Gateway) ánh xạ đúng theo từng giai đoạn — rất hợp với yêu cầu môn học.
- **Bảng Rủi ro & giải pháp** gắn được từng rủi ro với đúng gateway trong BPMN — cách làm này thể hiện là nhóm hiểu mô hình chứ không chỉ vẽ.
- **Phần mô tả luồng ngoại lệ** của các quy trình cốt lõi (xử lý giao dịch Pending, rollback tiền, xuất vé thủ công) khá chi tiết và sát thực tế.

---

*Báo cáo review được lập tự động từ rà soát toàn văn `MoMo.docx`.*
