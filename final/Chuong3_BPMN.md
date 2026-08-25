# Chương 3: MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN

> Đúng 6 quy trình đã chốt phạm vi (2 Quản lý + 2 Cốt lõi + 2 Hỗ trợ, `plan/03` mục 1). Mỗi quy trình theo khung mẫu: **3.X.1 Phương pháp thực hiện** (Dựa trên bằng chứng + Phỏng vấn) → **3.X.2 Mô hình hóa quy trình** (BPMN + diễn giải luồng chính/ngoại lệ).
>
> **Lưu ý áp dụng toàn chương:** nhóm xác nhận **không phỏng vấn thật nhân sự MoMo**. Mọi đoạn dẫn nhập "Phỏng vấn" dưới đây đều diễn đạt là bộ câu hỏi **mô phỏng/giả định**, xây dựng dựa trên nghiên cứu quy trình công khai và suy luận nghiệp vụ hợp lý — không khẳng định đã phỏng vấn thật (theo mẫu đã thống nhất ở `final/Chuong3_QuanTriGia_CauHoiPhongVan.md`).

---

## 3.1. Quản trị giá, khuyến mãi và chính sách hiển thị giá

### 3.1.1. Phương pháp thực hiện

Giữ nguyên toàn bộ nội dung đã đạt chuẩn trong `docs/MoMo.docx` (Sơ đồ tổ chức và trách nhiệm; Kế hoạch làm việc — mục tiêu + bảng công việc theo mốc thời gian; Công nghệ hỗ trợ đề xuất; Rủi ro và giải pháp; Thuật ngữ và sổ tay; 4 Biểu mẫu), đây là mục đã làm tốt nhất bài, dùng làm khung mẫu cho 5 quy trình còn lại. Áp dụng các sửa lỗi nhỏ:

- Sửa định nghĩa **M_Service** trong bảng thuật ngữ: đổi từ "Mã nội bộ chỉ nhóm bộ phận thẩm định rủi ro Tài chính..." (sai, mâu thuẫn với định nghĩa M_Service = Công ty CP Dịch vụ Di động Trực tuyến dùng xuyên suốt báo cáo) sang đúng nghĩa pháp nhân; đổi tên nhóm bộ phận thẩm định thành **"Khối Tài chính/Pháp chế (Finance & Legal)"**.
- Sửa mốc thời gian Kế hoạch làm việc: 3 mốc đầu (T+0–4, T+2–8, T+6–16) đang chồng lấn — bổ sung 1 câu chú thích ngay dưới bảng: *"Các mốc thời gian trên thể hiện khoảng xử lý có thể gối đầu một phần giữa các bộ phận liền kề (VD: Marketing có thể bắt đầu phân tích sơ bộ trong lúc Bộ phận Giá đang hoàn tất chuẩn hóa dữ liệu), không phải các bước tuần tự tuyệt đối."*
- Sửa lỗi chính tả: "tichet" → "Ticketing"; "Developement" → "Development"; "xác đsịnh" → "xác định"; "Group Specialist" → "Growth Specialist"; câu "Bộ phận Giá đóng thực hiện rà soát" → "Bộ phận Giá thực hiện rà soát".
- Sửa "Biểu mẫu 4" — bỏ tab đầu dòng thừa cho đồng nhất với Biểu mẫu 1–3.

**Phỏng vấn:** thay hoàn toàn bộ câu hỏi định tính (8→10 câu, 5+5) và định lượng (viết lại 100%, 5+5) — xem chi tiết đầy đủ tại `final/Chuong3_QuanTriGia_CauHoiPhongVan.md` (đã hoàn thành ở phiên trước).

### 3.1.2. Mô hình hóa quy trình

Giữ nguyên sơ đồ BPMN đã có (đạt chuẩn >10 gateway) và phần diễn giải luồng chính/luồng ngoại lệ đã có trong `docs/MoMo.docx` — đã đạt chuẩn, không cần sửa nội dung, chỉ áp dụng lại đúng số hình `Hình 3.1` khi đánh caption (Giai đoạn 3).

---

## 3.2. Quản trị danh mục hãng bay và đối tác nhà cung ứng

### 3.2.1. Phương pháp thực hiện

**Dựa trên bằng chứng:** vì đây là quy trình nội bộ không được MoMo công bố chi tiết, nhóm xây dựng mô tả dựa trên: (1) trải nghiệm sử dụng thực tế tính năng "Du lịch - Đi lại"; (2) thông tin công bố chính thức từ MoMo (website, hỏi đáp, thông cáo báo chí); (3) đối chiếu thông lệ phổ biến trong quản trị danh mục đối tác của các nền tảng OTA/ví điện tử tương tự; (4) suy luận nghiệp vụ dựa trên cơ cấu tổ chức và quy định pháp lý bắt buộc với tổ chức trung gian thanh toán được NHNN cấp phép. Số liệu định lượng ở mục 4.3 mang tính minh họa, không phải số liệu chính thức MoMo công bố.

- **Sơ đồ tổ chức:** "Nhóm Vận hành & Phát triển Đối tác Du lịch - Đi lại" gồm 4 đội: Đội Phát triển Đối tác (BD), Đội Pháp lý & Tuân thủ, Đội Kỹ thuật/Tích hợp API, Đội Vận hành Sản phẩm Du lịch — đây cũng là 4 tác nhân (swimlane) dùng khi mô hình hóa BPMN.
- **Kế hoạch làm việc** (4 tuần): Tuần 1 — xác định phạm vi, thu thập bằng chứng (cả nhóm); Tuần 2 — xây bộ câu hỏi khảo sát, mô hình hóa BPMN 2 quy trình con (Nhóm BD & Kỹ thuật); Tuần 3 — phân tích định tính/định lượng (Nhóm phân tích); Tuần 4 — phân tích bên liên quan, mô hình xương cá, hoàn thiện báo cáo (cả nhóm).
- **Thuật ngữ và sổ tay:** Onboarding đối tác, SLA, KYB, AML, UAT, CAP, Danh mục đối tác (Partner Catalog), GDS, API, Mini App — bảng đầy đủ giữ nguyên từ nguồn.
- **Biểu mẫu:** (1) Phiếu đánh giá đối tác (Partner Evaluation Scorecard); (2) Checklist hồ sơ onboarding đối tác (giấy phép vận tải/lữ hành, AOC, hồ sơ kỹ thuật API, chính sách giá/hoa hồng, tài khoản thanh toán, cam kết SLA, xác nhận AML/KYB); (3) Biên bản rà soát định kỳ đối tác (tỷ lệ đặt chỗ thành công, thời gian phản hồi API, tỷ lệ khiếu nại/1000 giao dịch, điểm đánh giá khách hàng).

**Phỏng vấn** — đối tượng: Đội Phát triển Đối tác, Đội Pháp lý & Tuân thủ, Đội Kỹ thuật, Đội Vận hành Sản phẩm Du lịch, đại diện đối tác (hãng bay/nhà cung ứng). Bộ câu hỏi mô phỏng/giả định, cơ cấu lại đúng lưới 2×2 từ nguồn 30 câu sẵn có (`25410237/MoMo_Quan_tri_danh_muc...docx`):

**A. Định tính — Có cấu trúc** (dành cho đối tác, câu trả lời cố định)
1. Đánh giá mức độ hài lòng với thời gian phản hồi khi đăng ký hợp tác với MoMo? (Rất hài lòng / Hài lòng / Bình thường / Không hài lòng / Rất không hài lòng)
2. Đối tác có tuân thủ đầy đủ SLA đã cam kết trong kỳ gần nhất không? (Có / Không / Một phần)
3. Mức độ hiển thị của đối tác trên App (vị trí, thứ hạng) có đúng như thỏa thuận không? (Có / Không / Không rõ)
4. Loại hình đối tác thuộc nhóm nào? (Hãng hàng không / Nhà xe - đường sắt / Khách sạn / Nhà cung cấp khác)
5. Có gặp khó khăn kỹ thuật khi tích hợp API với MoMo không? (Không có / Khó khăn nhỏ / Khó khăn lớn)

**B. Định tính — Không cấu trúc**
1. Chia sẻ trải nghiệm tổng thể khi hợp tác với MoMo từ giai đoạn tiếp cận đến khi chính thức lên hệ thống?
2. Điều gì khiến một đối tác quyết định gắn bó lâu dài hay rời bỏ danh mục của MoMo?
3. Mong muốn MoMo cải thiện điều gì nhất trong cách phối hợp vận hành với đối tác?
4. Nếu được đề xuất một thay đổi trong quy trình quản trị danh mục đối tác, sẽ đề xuất điều gì?
5. Nhìn nhận thế nào về vai trò của công nghệ (API, dashboard tự động) trong việc cải thiện quan hệ đối tác - nền tảng?

**C. Định lượng — Có cấu trúc**
1. Thời gian trung bình hoàn tất 1 hồ sơ onboarding (từ tiếp nhận đến go-live)? A. <10 ngày B. 10–15 ngày C. 16–20 ngày D. >20 ngày
2. Tỷ lệ hồ sơ đối tác bị từ chối ở vòng đánh giá sơ bộ mỗi quý? A. <10% B. 10–25% C. 26–50% D. >50%
3. Trung bình một đối tác cần bao nhiêu lần kiểm thử UAT mới đạt? A. 1 lần B. 2 lần C. 3 lần D. ≥4 lần
4. Tỷ lệ đối tác đạt SLA cam kết mỗi kỳ rà soát? A. <70% B. 70–85% C. 86–95% D. >95%
5. Số đối tác bị đưa vào diện cảnh báo (CAP) trong 12 tháng gần nhất? A. 0 B. 1–3 C. 4–6 D. >6

**D. Định lượng — Không cấu trúc**
1. Tỷ lệ hồ sơ đối tác không đạt thẩm định pháp lý là bao nhiêu %?
2. Chi phí nhân sự trung bình (ngày công) để xử lý 1 hồ sơ onboarding là bao nhiêu?
3. Hiện có bao nhiêu hãng bay và bao nhiêu đối tác cung ứng dịch vụ khác trong danh mục MoMo?
4. Tỷ lệ khiếu nại của khách hàng liên quan đến đối tác trên tổng giao dịch (số/1000 giao dịch)?
5. Thời gian trung bình xử lý 1 trường hợp gỡ đối tác khỏi danh mục là bao nhiêu ngày?

### 3.2.2. Mô hình hóa quy trình

2 sơ đồ BPMN: **Onboarding đối tác** (`MoMo_Onboarding_DoiTac.bpmn`) và **Rà soát/loại bỏ đối tác** (`MoMo_RaSoat_LoaiBoDoiTac.bpmn`), mô tả luồng đầy đủ theo mục 2.2.1 Chương 2. Diễn giải luồng chính và ngoại lệ theo đúng mô tả các bước đã nêu ở Chương 2.

> ⚠️ **Độ phức tạp sơ đồ:** 2 sơ đồ gốc chỉ có 3 gateway/sơ đồ (dưới ngưỡng >7 để đạt điểm tối đa theo rubric 2.0). Xem `final/bpmn/` để biết phương án xử lý cụ thể (Bước 2 của kế hoạch — gộp/bổ sung nhánh).

---

## 3.3. Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé

### 3.3.1. Phương pháp thực hiện

**Dựa trên bằng chứng** *(hợp nhất từ 3 báo cáo `25410206/MoMo_Core01/02/03...docx`, vốn cùng phạm vi và đã được viết để bao quát cả 3 quy trình con gộp thành 1 quy trình này)*: kết hợp 4 nguồn — hướng dẫn công khai của MoMo về cách đặt vé, chính sách hiển thị giá; trải nghiệm sử dụng thực tế của nhóm trên tính năng "Du lịch – Đi lại" (ảnh chụp màn hình từng bước); thông lệ kỹ thuật phổ biến của các nền tảng OTA (bộ đệm dữ liệu giá, truy vấn song song nhiều nhà cung ứng, phiên tìm kiếm có thời hạn); khung lý thuyết BPM và chuẩn BPMN 2.0.

- **Sơ đồ tổ chức:** thể hiện các khối chức năng của M_Service trực tiếp tham gia 3 quy trình con: Đội Sản phẩm Du lịch – Đi lại, Đội Kỹ thuật nền tảng (dịch vụ tìm kiếm/thanh toán), Đội Phát triển Đối tác hàng không, Bộ phận CSKH.
- **Kế hoạch làm việc** (6 tuần, phân công cụ thể theo từng thành viên — xem bảng gốc, giữ nguyên vì đã rất chi tiết): thu thập bằng chứng → xây sơ đồ tổ chức → thiết kế câu hỏi khảo sát → mô hình hóa BPMN → phân tích định tính → phân tích định lượng → phân tích bên liên quan → viết báo cáo.
- **Thuật ngữ và sổ tay:** Bộ đệm (cache) giá & chỗ, Giữ chỗ tạm (hold), Hạng vé (fare class), Khóa giá (price lock), Mã đặt chỗ (PNR), Nguồn tiền, Phiên tìm kiếm, Quy tắc giá hiển thị, Tra soát giao dịch, Xác thực mạnh.
- **Biểu mẫu:** (1) Phiếu ghi nhận phiên tìm kiếm phục vụ đo lường; (2) Phiếu khảo sát trải nghiệm tìm kiếm chuyến bay; (3) Biểu mẫu báo cáo hiệu năng tìm kiếm định kỳ.

**Phỏng vấn** — đối tượng: Đội Sản phẩm Du lịch – Đi lại, Đội Kỹ thuật nền tảng, Đội Phát triển Đối tác hàng không, người dùng cuối đã từng tìm kiếm/đặt vé trên MoMo. Bộ câu hỏi mô phỏng/giả định, đúng lưới 2×2 (đã đạt chuẩn sẵn từ `25410206/MoMo_Core01...docx`):

**A. Định tính — Có cấu trúc:** (1) Đánh giá mức độ đầy đủ của bộ lọc kết quả tìm kiếm? (2) Nguyên nhân chính khiến khách hàng rời bỏ ở màn hình kết quả? (3) Ưu tiên tốc độ phản hồi hay độ tươi mới dữ liệu giá? (4) Khi kết quả trống, hệ thống xử lý theo hướng nào? (5) Mức độ đồng nhất giữa giá hiển thị lúc tìm kiếm và giá thanh toán thực tế?

**B. Định tính — Không cấu trúc:** (1) Mô tả các bước hệ thống thực hiện từ lúc bấm "Tìm kiếm" đến khi hiển thị kết quả? (2) Cơ chế bộ đệm dữ liệu giá/chỗ trống hiện thiết lập thời hạn bao lâu, vì sao? (3) Khó khăn khi hợp nhất kết quả từ nhiều hãng bay có định dạng khác nhau? (4) Mùa cao điểm, đội ngũ ưu tiên xử lý vấn đề nào trước khi hệ thống quá tải? (5) Nếu được đầu tư thêm nguồn lực, sẽ cải tiến điều gì đầu tiên?

**C. Định lượng — Có cấu trúc:** (1) Trung bình mỗi ngày xử lý bao nhiêu phiên tìm kiếm? (<20.000 / 20.000–50.000 / 50.000–100.000 / >100.000) (2) Tỷ lệ phiên phục vụ từ bộ đệm? (<30% / 30–50% / 50–70% / >70%) (3) Thời gian phản hồi trung bình? (<2s / 2–4s / 4–6s / >6s) (4) Tỷ lệ phiên dẫn tới chọn được chuyến bay? (<20% / 20–35% / 35–50% / >50%) (5) Tỷ lệ phiên hết hạn phải làm mới? (<5% / 5–10% / 10–20% / >20%)

**D. Định lượng — Không cấu trúc:** (1) Chi phí bình quân 1 lượt truy vấn tới hãng bay/GDS, gồm những khoản gì? (2) Thời gian phản hồi p95 của từng nhà cung ứng trong 3 tháng gần nhất? (3) Số lượt tìm kiếm trung bình trước khi khách chọn chuyến bay? (4) Tỷ lệ chênh lệch giữa giá hiển thị và giá thanh toán cuối cùng? (5) Nếu tăng tỷ lệ dùng bộ đệm thêm 20 điểm %, chi phí hạ tầng/truy vấn giảm được bao nhiêu?

### 3.3.2. Mô hình hóa quy trình

Dùng trực tiếp 3 sơ đồ BPMN sẵn có của `25410206` (`MoMo_Core01/02/03...bpmn`, mỗi sơ đồ 10–12 gateway, đã đạt chuẩn tối đa rubric 2.0) — ghép nối tuần tự thành 1 luồng thống nhất khớp với 5 bước đã mô tả ở Chương 2 (Khách hàng nhập & chọn chuyến bay → Giữ chỗ tạm thời → Thanh toán → Trừ tiền & xuất vé → Trả vé điện tử). Diễn giải luồng chính/ngoại lệ theo đúng mô tả Chương 2 (giao dịch Pending, rollback, xuất vé thủ công).

---

## 3.4. Đổi chuyến bay

### 3.4.1. Phương pháp thực hiện

> ⚠️ Quy trình xây gần như từ đầu — nguồn gốc (`25410223/MoMo_Core03...docx`) chỉ có 2 câu hỏi phỏng vấn và không có sơ đồ tổ chức/kế hoạch/thuật ngữ/biểu mẫu. Nội dung dưới đây dựng theo đúng khung mẫu "Quản trị giá", dùng `cstt.md` (mô tả văn xuôi chi tiết, đã dọn sạch artifact `[span_...]`) làm bằng chứng chính.

**Dựa trên bằng chứng:** trải nghiệm sử dụng thực tế tính năng "Quản lý đặt chỗ" trên MoMo; hướng dẫn công khai của MoMo về đổi/hủy vé; đối chiếu chính sách đổi vé phổ biến của các hãng hàng không nội địa (phí đổi cố định theo hạng vé, không hoàn chênh lệch âm); suy luận nghiệp vụ dựa trên kiến trúc hệ thống đặt vé đã mô tả cho quy trình "Tìm kiếm..." (cùng nền tảng Backend MoMo Travel, cùng Cổng thanh toán MoMo).

- **Sơ đồ tổ chức:** Khách hàng ↔ Giao diện MoMo Client App ↔ Backend MoMo Travel ↔ Cổng Thanh toán MoMo ↔ Bộ phận CSKH MoMo Travel ↔ Hệ thống Hãng bay (CRS/GDS Re-issue API).
- **Kế hoạch làm việc:** Tuần 1 — thu thập bằng chứng, xác định công thức tính phí đổi; Tuần 2 — thiết kế câu hỏi khảo sát, mô hình hóa BPMN; Tuần 3 — phân tích định tính/định lượng; Tuần 4 — hoàn thiện báo cáo (tương tự nhịp độ đã áp dụng cho các quy trình khác).
- **Thuật ngữ và sổ tay:** Re-issuance (tái phát hành vé), Fare Rules (quy định điều kiện vé), Hold Time Limit (thời hạn giữ chỗ), Seat Out of Stock (hết chỗ trong lúc xử lý), PNR, EMD.
- **Biểu mẫu:**
  1. *Phiếu tính phí đổi vé* — Mã PNR / Hạng vé cũ / Giá vé cũ / Giá vé mới / Phí đổi cố định Hãng / Chênh lệch giá / Phí dịch vụ MoMo / Tổng phí đổi.
  2. *Phiếu xử lý thủ công qua CSKH* — Mã PNR / Lý do không đổi tự động được / Phí hãng báo qua tổng đài / Link thanh toán đã gửi / Trạng thái tái xuất vé.
  3. *Báo cáo hiệu năng đổi vé định kỳ* — Tổng số ca đổi vé / Tỷ lệ tự động qua API / Tỷ lệ xử lý thủ công / Tỷ lệ hoàn phí do hết chỗ / Thời gian xử lý trung bình mỗi loại.

**Phỏng vấn** — đối tượng: Khách hàng, Backend MoMo Travel, CSKH MoMo Travel, Cổng thanh toán, đối tác Hãng bay/GDS. Bộ câu hỏi mô phỏng/giả định, xây mới đúng lưới 2×2:

**A. Định tính — Có cấu trúc**
1. Đánh giá mức độ minh bạch của bảng phân rã phí đổi vé trên App? (Rất không minh bạch – Không minh bạch – Bình thường – Minh bạch – Rất minh bạch)
2. Bước nào trong quy trình đổi chuyến bay dễ gây khó chịu nhất cho khách hàng? (Tính phí – Chờ CSKH xử lý thủ công – Thanh toán phí chênh lệch – Chờ tái phát hành vé – Khác)
3. Khi hệ thống báo "hạng vé không hỗ trợ đổi tự động", CSKH thường ưu tiên xử lý theo hướng nào? (Gọi ngay hãng bay – Xử lý theo hàng đợi – Báo khách chờ – Khác)
4. Mức độ ưu tiên giữa tốc độ xử lý và độ chính xác tính phí được xếp thế nào? (Ưu tiên tốc độ – Cân bằng – Ưu tiên chính xác)
5. Đánh giá mức độ ổn định của kết nối API tính phí tự động với các hãng bay? (Rất kém – Kém – Trung bình – Tốt – Rất tốt)

**B. Định tính — Không cấu trúc**
1. Mô tả các bước chính từ lúc khách hàng chọn "Đổi chuyến bay" đến khi nhận vé mới?
2. Khó khăn nào phát sinh khi xử lý thủ công các trường hợp hạng vé không hỗ trợ API?
3. Trường hợp khách bị hết chỗ đúng lúc đang trích tiền phí đổi, quy trình hoàn tiền diễn ra thế nào trên thực tế?
4. Tiêu chí nào quyết định một hạng vé được/không được phép đổi tự động qua API?
5. Nếu được đầu tư thêm nguồn lực, sẽ ưu tiên cải tiến điều gì trước trong quy trình đổi chuyến bay?

**C. Định lượng — Có cấu trúc**
1. Trung bình một ca đổi vé tự động qua API mất bao nhiêu phút? A. <1,5 phút B. 1,5–2,5 phút C. 2,5–4 phút D. >4 phút
2. Tỷ lệ ca đổi vé phải chuyển CSKH xử lý thủ công? A. <10% B. 10–25% C. 26–40% D. >40%
3. Một ca xử lý thủ công qua CSKH mất trung bình bao lâu? A. <15 phút B. 15–30 phút C. 30–45 phút D. >45 phút
4. Tỷ lệ giao dịch bị hoàn phí do hết chỗ đúng lúc trích tiền? A. <2% B. 2–5% C. 5–10% D. >10%
5. Phí đổi vé cố định trung bình theo hạng Tiết kiệm? A. <300.000đ B. 300.000–450.000đ C. 450.000–600.000đ D. >600.000đ

**D. Định lượng — Không cấu trúc**
1. Mỗi tháng có trung bình bao nhiêu yêu cầu đổi chuyến bay được tiếp nhận?
2. Trong số đó, bao nhiêu % là vé quốc tế cần xử lý thủ công qua CSKH?
3. Thời gian phản hồi trung bình của hãng bay khi CSKH liên hệ kiểm tra phí thủ công?
4. Chi phí nhân sự CSKH trung bình (giờ công) để xử lý 1 ca đổi vé thủ công?
5. Số lần trung bình một khách hàng phải chọn lại chuyến mới do hết chỗ trong lúc đổi vé?

### 3.4.2. Mô hình hóa quy trình

Dùng sơ đồ `25410223/MoMo_Core03_DoiChuyenBay...bpmn` (6 lane: Khách hàng, MoMo Client App, Backend MoMo Travel, Cổng Thanh toán MoMo, CSKH MoMo Travel, Hệ thống Hãng bay) làm nền, đã bổ sung thêm gateway — xem `final/bpmn/Core03_DoiChuyenBay.bpmn` và mô tả cụ thể ở phần Bước 2 của kế hoạch thực hiện.

**Luồng chính (Happy path):** Khởi tạo yêu cầu → Tìm chuyến mới → Tính phí (đổi tự động API) → Xác nhận phí → Thanh toán → Tái phát hành vé thành công → Kết thúc.

**Luồng ngoại lệ:**
- *Hạng vé không hỗ trợ đổi tự động:* rẽ sang Support Ticket → CSKH liên hệ hãng bay kiểm tra phí thủ công → gửi link thanh toán → tái xuất vé thủ công.
- *Hết chỗ khi đang trích tiền (Re-issue thất bại):* hủy giao dịch thanh toán, hoàn 100% phí đổi, giữ nguyên vé cũ, thông báo khách chọn lại chuyến khác.

---

## 3.5. Hỗ trợ khách hàng và tiếp nhận phản hồi

### 3.5.1. Phương pháp thực hiện

**Dựa trên bằng chứng** *(từ `25410237/MoMo_HauMai_va_XuLyNgoaiLe.docx`)*: trải nghiệm sử dụng thực tế và hướng dẫn công khai của MoMo về hủy/hoàn vé, hạn mức giao dịch, xử lý sự cố; thông tin công bố chính thức (hỏi đáp, thông báo bảo mật, chính sách hoàn/hủy); đối chiếu thông lệ xử lý khiếu nại/tra soát của các nền tảng OTA/ví điện tử tương tự; suy luận dựa trên quy định pháp lý bắt buộc với tổ chức trung gian thanh toán được NHNN cấp phép.

- **Sơ đồ tổ chức:** tính liên phòng ban rõ rệt — Khối Vận hành & Tuân thủ (CSKH), Khối Sản phẩm (Đội Vận hành Sản phẩm Du lịch, Đội Kỹ thuật), Đội Pháp lý & Tuân thủ (khi khiếu nại leo thang), hãng bay/đối tác (xác minh thông tin đặt chỗ).
- **Kế hoạch làm việc** (4 tuần): thu thập bằng chứng tình huống ngoại lệ → xây câu hỏi khảo sát + mô hình hóa BPMN → phân tích định tính/định lượng + biểu đồ Pareto → phân tích bên liên quan, hoàn thiện báo cáo.
- **Thuật ngữ và sổ tay:** Ticket tra soát, Giao dịch treo, Lỗi đồng bộ, SLA, Leo thang (Escalation), Hoàn tiền (Refund), CAP, Log hệ thống, Khảo sát hài lòng (CSAT).
- **Biểu mẫu:** (1) Phiếu ghi nhận & xử lý ticket tra soát giao dịch; (2) Phiếu tiếp nhận & xử lý khiếu nại khách hàng; (3) Báo cáo tổng hợp hậu mãi định kỳ.

**Phỏng vấn** — đối tượng: nhân viên/trưởng nhóm CSKH, Đội Vận hành Sản phẩm Du lịch, Đội Kỹ thuật, Đội Pháp lý & Tuân thủ, khách hàng từng gặp sự cố/khiếu nại. Bộ câu hỏi mô phỏng/giả định, đúng lưới 2×2:

**A. Định tính — Có cấu trúc:** (1) Đánh giá mức độ hài lòng với thời gian xử lý khiếu nại/tra soát? (2) Vấn đề gặp phải thuộc nhóm nào? (Giao dịch treo/Chậm hoàn tiền/Sai lệch thông tin/Chưa nhận vé/Khác) (3) Có nhận thông báo cập nhật tiến độ xử lý không? (4) Kênh liên hệ đã sử dụng là gì? (5) Có phải liên hệ lại nhiều lần để được giải quyết dứt điểm không?

**B. Định tính — Không cấu trúc:** (1) Chia sẻ trải nghiệm cụ thể lần gần nhất gặp sự cố và cách được hỗ trợ? (2) Điều gì khiến khách hàng cảm thấy được tôn trọng khi gặp sự cố dù chưa có kết quả ngay? (3) Mong muốn MoMo cải thiện điều gì nhất trong cách thông báo tiến độ? (4) Đề xuất thay đổi gì trong quy trình xử lý ngoại lệ? (5) Vai trò của tự động hóa (chatbot, dashboard) trong rút ngắn thời gian xử lý?

**C. Định lượng — Có cấu trúc** *(chuyển 5 câu định lượng phù hợp nhất sang dạng có khoảng lựa chọn)*: (1) Thời gian trung bình đóng 1 ticket tra soát? (<2h / 2–6h / 6–24h / >24h) (2) Tỷ lệ giao dịch treo do lỗi nội bộ so với lỗi hãng bay/đối tác? (<30% / 30–50% / 50–70% / >70% là lỗi nội bộ) (3) Thời gian trung bình hoàn tất 1 yêu cầu hoàn tiền? (<1 ngày / 1–3 ngày / 3–7 ngày / >7 ngày) (4) Tỷ lệ khiếu nại xử lý ngay theo kịch bản chuẩn? (<50% / 50–70% / 70–90% / >90%) (5) Tỷ lệ khiếu nại bị leo thang lần 2? (<5% / 5–10% / 10–20% / >20%)

**D. Định lượng — Không cấu trúc:** (1) Mỗi tháng trung bình bao nhiêu ticket tra soát và bao nhiêu khiếu nại được tiếp nhận? (2) Tỷ lệ khiếu nại có căn cứ hợp lệ sau khi xác minh với hãng bay/đối tác? (3) Chi phí nhân sự trung bình (giờ công) để xử lý 1 ticket/khiếu nại? (4) Điểm khảo sát hài lòng (CSAT) trung bình sau khi ticket được đóng (thang 5)? (5) Nhóm vấn đề nào chiếm tỷ trọng lớn nhất theo phân loại Pareto?

### 3.5.2. Mô hình hóa quy trình

2 sơ đồ BPMN: **Tra soát giao dịch lỗi** (`MoMo_TraSoat_GiaoDichLoi.bpmn`) và **Xử lý khiếu nại khách hàng** (`MoMo_XuLy_KhieuNaiKH.bpmn`), mô tả theo đúng luồng đã nêu ở Chương 2 (mục Hỗ trợ khách hàng + Quản trị rủi ro giao dịch).

> ⚠️ **Độ phức tạp sơ đồ:** `MoMo_TraSoat_GiaoDichLoi.bpmn` chỉ có 2 gateway, `MoMo_XuLy_KhieuNaiKH.bpmn` có 3 gateway (dưới ngưỡng >7 để đạt điểm tối đa rubric 2.0) — cân nhắc gộp 2 sơ đồ thành 1 sơ đồ tổng "Hỗ trợ khách hàng & xử lý ngoại lệ" nếu cấu trúc lane tương thích (xem Bước 2 kế hoạch).

---

## 3.6. Xuất hóa đơn

### 3.6.1. Phương pháp thực hiện

> ⚠️ Quy trình chưa có nguyên liệu Phương pháp thực hiện từ bất kỳ thành viên nào. Nội dung dưới đây viết mới, dùng mô tả 6 bước đã có sẵn ở Chương 2 làm cơ sở, theo đúng khung mẫu "Quản trị giá".

**Dựa trên bằng chứng:** hướng dẫn công khai của MoMo về xuất hóa đơn VAT cho giao dịch mua vé/dịch vụ; quy định pháp luật về thời hạn xuất hóa đơn điện tử đối với giao dịch thương mại điện tử; suy luận nghiệp vụ dựa trên việc MoMo là tổ chức trung gian thanh toán phải tuân thủ quy định về hóa đơn, chứng từ.

- **Sơ đồ tổ chức:** Khách hàng ↔ Ứng dụng MoMo ↔ Bộ phận CSKH ↔ Bộ phận Kế toán (M_Service) ↔ Hệ thống VACOM (đối tác cung cấp hóa đơn điện tử).
- **Kế hoạch làm việc:** Tuần 1 — thu thập bằng chứng, xác định điều kiện/thời hạn xuất VAT; Tuần 2 — thiết kế câu hỏi khảo sát, mô hình hóa BPMN; Tuần 3 — phân tích định tính/định lượng; Tuần 4 — hoàn thiện báo cáo.
- **Thuật ngữ và sổ tay:** VAT (Value Added Tax — thuế giá trị gia tăng), Hóa đơn điện tử, VACOM (hệ thống đối tác phát hành hóa đơn — *cần nhóm xác nhận nguồn thật, xem ghi chú ở Chương 2*), Đối soát giao dịch.
- **Biểu mẫu:**
  1. *Phiếu yêu cầu xuất VAT* — Mã giao dịch/vé / Thông tin công ty (MST, tên, địa chỉ) / Kênh yêu cầu (App/CSKH) / Thời điểm yêu cầu.
  2. *Phiếu đối soát dữ liệu xuất hóa đơn* — Mã giao dịch / Kết quả đối chiếu (Khớp/Không khớp) / Người xử lý / Thời gian xử lý.
  3. *Báo cáo hiệu năng xuất hóa đơn định kỳ* — Tổng số yêu cầu / Tỷ lệ xuất thành công lần đầu / Tỷ lệ quá hạn 72 giờ / Tỷ lệ lỗi từ VACOM / Thời gian xử lý trung bình.

**Phỏng vấn** — đối tượng: Bộ phận CSKH, Bộ phận Kế toán, Bộ phận Kỹ thuật (tích hợp VACOM), khách hàng đã yêu cầu xuất hóa đơn. Bộ câu hỏi mô phỏng/giả định:

**A. Định tính — Có cấu trúc:** (1) Đánh giá mức độ dễ sử dụng của form yêu cầu xuất VAT trên App? (2) Nguyên nhân phổ biến nhất khiến yêu cầu xuất hóa đơn bị từ chối là gì? (Quá hạn 72h / Dữ liệu không khớp / Lỗi hệ thống VACOM / Khác) (3) Kênh yêu cầu xuất hóa đơn khách hàng dùng nhiều nhất? (Qua App / Qua CSKH) (4) Mức độ ổn định của kết nối API với hệ thống VACOM? (Rất kém – Kém – Trung bình – Tốt – Rất tốt) (5) Mức độ hài lòng với thời gian nhận được hóa đơn điện tử sau khi yêu cầu?

**B. Định tính — Không cấu trúc:** (1) Mô tả các bước xử lý một yêu cầu xuất hóa đơn từ lúc tiếp nhận đến khi gửi hóa đơn cho khách? (2) Khó khăn nào phát sinh khi dữ liệu giao dịch và dữ liệu xuất hóa đơn không khớp? (3) Vì sao thời hạn xuất VAT lại giới hạn ở 72 giờ, cơ sở nào để chọn mốc này? (4) Khi hệ thống VACOM gặp lỗi, đội kỹ thuật ưu tiên xử lý theo hướng nào? (5) Nếu được cải tiến, sẽ ưu tiên thay đổi điều gì trước trong quy trình xuất hóa đơn?

**C. Định lượng — Có cấu trúc:** (1) Tỷ lệ yêu cầu xuất hóa đơn thành công ngay lần đầu? A. <70% B. 70–85% C. 86–95% D. >95% (2) Tỷ lệ yêu cầu bị từ chối do quá hạn 72 giờ? A. <5% B. 5–10% C. 10–20% D. >20% (3) Thời gian trung bình từ lúc yêu cầu đến khi nhận hóa đơn điện tử? A. <10 phút B. 10–30 phút C. 30–60 phút D. >60 phút (4) Tỷ lệ lỗi phát sinh từ phía hệ thống VACOM? A. <2% B. 2–5% C. 5–10% D. >10% (5) Tỷ lệ yêu cầu qua kênh CSKH so với qua App? A. <10% B. 10–25% C. 25–50% D. >50%

**D. Định lượng — Không cấu trúc:** (1) Mỗi tháng có trung bình bao nhiêu yêu cầu xuất hóa đơn VAT? (2) Chi phí vận hành trung bình (nhân sự + phí dịch vụ VACOM) cho mỗi hóa đơn xuất thành công là bao nhiêu? (3) Thời gian trung bình để CSKH xử lý 1 trường hợp dữ liệu đối soát không khớp là bao lâu? (4) Tỷ lệ khách hàng phải liên hệ lại CSKH sau khi yêu cầu xuất VAT qua App không thành công? (5) Số lượng khiếu nại liên quan đến xuất hóa đơn phát sinh mỗi tháng?

### 3.6.2. Mô hình hóa quy trình

Dùng ảnh BPMN sẵn có trong `docs/MoMo.docx` (chỉ có ảnh, chưa có text diễn giải). Diễn giải luồng chính/ngoại lệ theo đúng 6 bước đã mô tả ở Chương 2 (kiểm tra điều kiện 72 giờ, đối soát giao dịch, gửi VACOM, trả kết quả).
