# Chương 4: PHÂN TÍCH CÁC QUY TRÌNH

> Đúng 3 quy trình đã chốt phạm vi (`plan/03` mục 1): Tìm kiếm/lựa chọn/thanh toán, Hỗ trợ khách hàng, và Quản trị giá (bonus). Khung mẫu: Phân tích quy trình → Phân tích định tính (VA/BVA/NVA + Lãng phí) → Phân tích các bên liên quan → Phân tích định lượng (Thời gian/Chất lượng/Chi phí).

---

## 4.1. Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé

*(Nguồn: `25410206/MoMo_Core01_TimKiem_va_SoSanhChuyenBay.docx`, đã đạt chuẩn chất lượng cao nhất dự án — giữ nguyên toàn bộ nội dung phân tích, chỉ bổ sung phần chi phí nhân sự theo đúng yêu cầu công thức rubric.)*

### 4.1.1. Phân tích quy trình

Quy trình phục vụ trực tiếp mọi khách hàng có nhu cầu đặt vé máy bay trên MoMo, mang lại giá trị cốt lõi là giúp khách hàng tìm kiếm, so sánh và đặt vé nhanh chóng, minh bạch về giá. Kết quả có thể đạt được: khách hàng chọn được chuyến bay phù hợp và hoàn tất đặt vé; hoặc khách hàng rời bỏ do không tìm được kết quả phù hợp/thời gian phản hồi chậm.

### 4.1.2. Phân tích định tính

**a) Phân tích giá trị gia tăng** — quy trình có **5 hoạt động VA, 8 hoạt động BVA và 3 hoạt động NVA** (bảng chi tiết 16 hoạt động, xem `plan/02` để tra cứu bản gốc đầy đủ — giữ nguyên không đổi). Cả 3 hoạt động NVA (hiển thị cảnh báo dữ liệu không hợp lệ, hiển thị thông báo không có kết quả, thông báo phiên hết hạn) đều là hoạt động sửa lỗi/làm lại, có thể loại bỏ bằng thiết kế (ràng buộc đầu vào tại giao diện, gợi ý chủ động thay vì báo lỗi, làm mới ngầm). Xét theo thời gian, hoạt động VA chiếm 58,2/107,2 giây, tương đương tỷ lệ giá trị gia tăng **54,3%**.

**b) Phân tích lãng phí (Move/Hold/Overdo)** — 6 biểu hiện lãng phí được nhận diện: 1 Move (dữ liệu phải qua 2-4 lượt truyền giữa các hệ thống), 2 Hold (chờ truy vấn nhà cung ứng ~2,1s/phiên; chờ làm mới phiên hết hạn ~8% số phiên), 3 Overdo (truy vấn dư thừa ~20% lượt; khách nhập lại tiêu chí dù đã có lịch sử; lặp lại thao tác lọc trung bình 1,8 lần/phiên). Nhóm Overdo chiếm ưu thế — vấn đề chính không phải chờ đợi mà là làm nhiều hơn mức cần thiết, khắc phục bằng khai thác tốt hơn dữ liệu lịch sử đã có, không cần đầu tư hạ tầng lớn.

**c) Phân tích các bên liên quan** — chọn kỹ thuật **Power-Interest Grid + Fishbone** (Fishbone là kỹ thuật chính thức tính điểm theo rubric; Power-Interest Grid là bổ sung tham khảo, không thay thế). Nhóm "Quản lý chặt chẽ" (quyền lực cao, quan tâm cao): Khách hàng cuối, Đội Sản phẩm Du lịch – Đi lại, Đội Kỹ thuật nền tảng. Mô hình xương cá xác định 3 nhóm nguyên nhân tác động lớn nhất đến tỷ lệ rời bỏ cao: **Máy móc – Hệ thống** (p95 phản hồi API 6,2s, bộ đệm hết hạn sớm), **Dữ liệu** (giá/chỗ trống lệch so với hãng bay), và **Đo lường** (chưa ghi nhận lý do thoát/tỷ lệ chuyển đổi theo bộ lọc) — nhóm Đo lường là nguyên nhân gốc rễ nhất vì ngăn cản xác định các nguyên nhân còn lại.

### 4.1.3. Phân tích định lượng

**Thời gian:** T_ck ≈ **107,2 giây**/phiên (công thức tuần tự=tổng, các bước có nhánh dùng trung bình có trọng số xác suất). T_chờ ≈ 4,42 giây (chờ truy vấn + sửa dữ liệu + làm mới phiên). T_xl = 107,15 − 4,42 ≈ 102,7 giây. **Hiệu suất thời gian ≈ 95,9%.** Kết luận: nút thắt không nằm ở tốc độ hệ thống (chỉ ~5 giây độ trễ) mà ở thời gian thao tác của khách hàng (84,4% thời gian chu kỳ) và tỷ lệ chuyển đổi (38%).

**Chất lượng:** 8 chỉ số đo lường (tỷ lệ có kết quả 96%, tỷ lệ chuyển đổi 38%, thời gian phản hồi 3,5s, p95 6,2s, cache-hit 40%, lệch giá 3,5%, phiên hết hạn 8%, CSAT 4,0/5) — mỗi chỉ số có mức hiện tại/mục tiêu/biện pháp. Chỉ số tổng hợp minh họa: nếu coi mỗi chỉ số đạt mục tiêu = 1 điểm, quy trình hiện đạt **0/8 chỉ số ở mức mục tiêu**, xác nhận còn nhiều dư địa cải thiện đồng đều trên toàn bộ các mặt, không riêng một điểm nghẽn.

**Chi phí:** Vì quy trình này chạy **tự động hoàn toàn** (tác nhân xử lý là "Ứng dụng MoMo"/"Dịch vụ tìm kiếm"/"Hãng bay-GDS", không có nhân sự MoMo trực tiếp thao tác từng bước), công thức chi phí = thời gian × lương nhân sự cho kết quả **≈ 0 đồng/phiên** — không phản ánh đúng bản chất kinh tế của một quy trình tự động hóa. Nhóm bổ sung phép tính này để đúng yêu cầu công thức của rubric, đồng thời giữ mô hình chi phí hạ tầng/truy vấn làm chỉ số kinh tế chính (phù hợp bản chất quy trình): **C = chi phí hạ tầng (6đ) + chi phí vận hành/log (4đ) + 0,60 × chi phí truy vấn song song (24đ) = 24,4 đồng/phiên**; quy mô 100.000 phiên/ngày → **≈2,44 triệu đồng/ngày** (≈890 triệu đồng/năm). Nâng tỷ lệ cache-hit từ 40% lên 65% giảm chi phí 24,6% (~219 triệu đồng/năm).

---

## 4.2. Hỗ trợ khách hàng và tiếp nhận phản hồi

*(Nguồn: `25410237/MoMo_HauMai_va_XuLyNgoaiLe.docx`, chương "Tra soát & xử lý giao dịch lỗi/treo" + "Tiếp nhận & xử lý khiếu nại khách hàng" — bổ sung cột Mô tả + Khắc phục vào bảng VA theo `plan/05` mục C.)*

### 4.2.1. Phân tích quy trình

Quy trình phục vụ khách hàng gặp sự cố giao dịch (treo/lỗi) hoặc có khiếu nại trong quá trình đặt vé. Giá trị mang lại: khôi phục đúng trạng thái vé hoặc hoàn tiền kịp thời, duy trì niềm tin của khách hàng vào nền tảng. Kết quả có thể đạt được: lỗi khắc phục nội bộ thành công; vé cập nhật lại sau xác minh với hãng bay; hoàn tiền do mất chỗ thực sự; khiếu nại được xử lý ngay hoặc sau xác minh; khiếu nại leo thang lên Pháp lý & Tuân thủ.

### 4.2.2. Phân tích định tính

**a) Phân tích giá trị gia tăng — Quy trình 1 (Tra soát giao dịch lỗi/treo):**

| Hoạt động | Người thực hiện | Loại giá trị | Mô tả | Khắc phục |
|---|---|---|---|---|
| Ghi nhận ticket tra soát, đánh dấu giao dịch | Đội Vận hành SP Du lịch | BVA | Bước hành chính bắt buộc để kiểm soát xử lý trùng lặp | Tự động tạo ticket khi hệ thống phát hiện bất thường, không cần nhân sự khởi tạo thủ công |
| Kiểm tra log hệ thống nội bộ | Đội Kỹ thuật | VA | Xác định trực tiếp nguyên nhân, quyết định hướng xử lý | Xây dựng dashboard log tự động phân loại lỗi thường gặp |
| Khắc phục & kích hoạt lại luồng xuất vé | Đội Kỹ thuật | VA | Giải quyết trực tiếp vấn đề của khách hàng | Tự động hóa retry cho các lỗi timeout đã có mẫu xử lý |
| Liên hệ đối chiếu với hãng bay | Đội Vận hành SP Du lịch | BVA | Cần thiết để xác minh trạng thái thực tế, khách hàng không thấy | Kênh API tra cứu real-time thay vì liên hệ thủ công |
| Phản hồi trạng thái đặt chỗ thực tế | Hãng bay/Đối tác | BVA | Bước xác nhận bắt buộc từ bên ngoài | Thỏa thuận SLA phản hồi tối đa với từng hãng bay |
| Cập nhật lại vé cho khách | Đội Vận hành SP Du lịch | VA | Khôi phục đúng quyền lợi khách hàng | Tự động đồng bộ vé ngay khi có xác nhận từ hãng |
| Khởi tạo hoàn tiền | Đội Vận hành SP Du lịch | VA | Đảm bảo quyền lợi tài chính khi mất chỗ thực sự | Tự động hóa hoàn tiền ngay khi xác định đủ điều kiện |
| Thông báo kết quả & đóng ticket | Đội Vận hành SP Du lịch | VA | Hoàn tất vòng đời xử lý, thông báo cho khách hàng | Gửi thông báo đa kênh (app/SMS/email) đồng thời |

**a) Phân tích giá trị gia tăng — Quy trình 2 (Xử lý khiếu nại khách hàng):**

| Hoạt động | Người thực hiện | Loại giá trị | Mô tả | Khắc phục |
|---|---|---|---|---|
| Tiếp nhận, phân loại & tạo ticket | CSKH | BVA | Bước phân luồng bắt buộc | Chatbot phân loại sơ bộ trước khi chuyển nhân sự |
| Xử lý trực tiếp & phản hồi khách | CSKH | VA | Giải quyết ngay theo kịch bản chuẩn | Mở rộng danh mục kịch bản xử lý nhanh |
| Liên hệ xác minh với hãng bay/đối tác | Đội Vận hành SP Du lịch | BVA | Cần thiết cho khiếu nại phức tạp, khách hàng không thấy | Ưu tiên kênh xác minh tự động (API) |
| Đề xuất & thực hiện phương án xử lý | Đội Vận hành SP Du lịch | VA | Mang lại quyền lợi thực tế cho khách hàng có căn cứ | Chuẩn hóa khung phương án theo từng loại khiếu nại |
| Soạn phản hồi từ chối | Đội Vận hành SP Du lịch | NVA | Chỉ phát sinh khi khiếu nại không có căn cứ, không tạo giá trị mới | Mẫu phản hồi chuẩn kèm giải thích rõ ràng, giảm thời gian soạn thảo |
| Xem xét theo quy định bảo vệ NTD | Đội Pháp lý & Tuân thủ | VA | Bảo vệ quyền lợi khách hàng ở mức cao nhất khi leo thang | Quy trình leo thang có SLA rõ ràng |
| Đóng ticket & khảo sát hài lòng | CSKH | BVA | Hoàn tất vòng đời, đo lường chất lượng dịch vụ | Khảo sát tự động ngay sau khi đóng ticket |

**b) Phân tích lãng phí (Move/Hold/Overdo)** — cả 2 quy trình con đều có đủ 3 nhóm: **Hold** (chờ hãng bay/đối tác phản hồi xác minh — điểm nghẽn chính, nằm ngoài tầm kiểm soát MoMo), **Move** (trao đổi thông tin ticket thủ công giữa CSKH/Vận hành/Kỹ thuật qua email/điện thoại, dễ sai lệch), **Overdo** (áp dụng quy trình xác minh/chẩn đoán đầy đủ cho cả các trường hợp lặp lại đã có tiền lệ xử lý). Khắc phục chung: hệ thống case-management dùng chung theo thời gian thực, kênh API xác minh tự động với hãng bay, cơ sở tri thức (knowledge base) cho các lỗi/khiếu nại thường gặp.

**c) Phân tích các bên liên quan** — kỹ thuật chính thức được chọn (1 trong 3 theo yêu cầu rubric) là **biểu đồ Pareto**, trình bày ở mục 4.2.3 bên dưới (phân loại 9 nhóm vấn đề hậu mãi theo tần suất). Bảng dưới đây là phân tích bổ sung dạng **Power-Interest Grid** (không thay thế yêu cầu bắt buộc, chỉ làm rõ thêm vai trò từng bên liên quan): Nhóm "Quản lý chặt chẽ, phối hợp thường xuyên": Ban điều hành mảng Du lịch – Đi lại, Đội Vận hành Sản phẩm Du lịch. Nhóm "Giữ hài lòng": Đội Pháp lý & Tuân thủ, NHNN/cơ quan quản lý. Nhóm "Thông tin thường xuyên": CSKH, khách hàng cuối, hãng bay/đối tác.

### 4.2.3. Phân tích định lượng

| Chỉ số | Quy trình 1 (Tra soát) | Quy trình 2 (Khiếu nại) |
|---|---|---|
| Thời gian chu kỳ (T_ck) | ≈ 5,8 giờ | ≈ 4,23 giờ |
| Hiệu suất thời gian | ≈ 69,0% | ≈ 43,3% |
| Chi phí xử lý 1 ca | ≈ 301.000 đồng | ≈ 123.500 đồng |
| Chất lượng | 55% lỗi nội bộ khắc phục ngay; 27% phải hoàn tiền; 80% xong trong SLA 8h | 60% xử lý ngay theo kịch bản; 55% có căn cứ hợp lệ; 5,4% leo thang; CSAT ≈4,1/5 |

Công thức thời gian dùng đúng chuẩn: tuần tự = tổng, nhánh XOR = trung bình có trọng số xác suất (VD Quy trình 2: T_ck = 0,3 + 0,6×0,5 + 0,4×[1 + 6 + 0,55×1 + 0,45×(0,5+0,3×4)] + 0,3 ≈ 4,23 giờ). Hiệu suất thời gian thấp hơn hẳn ở Quy trình 2 (43,3%) xác nhận thời gian chờ hãng bay/đối tác (Hold) là điểm nghẽn nghiêm trọng nhất toàn mảng hậu mãi.

**Phân tích Pareto bổ sung** (9 nhóm vấn đề hậu mãi, 590 ticket/khiếu nại minh họa quý): 4 nhóm đầu (trừ tiền chưa xuất vé 31,5%, chậm hoàn tiền 21,0%, sai lệch thông tin 16,6%, không nhận vé điện tử 10,3%) chiếm ~79,5% — xác nhận đúng nguyên tắc 80/20, đúng hướng ưu tiên cải tiến đã chọn ở trên.

---

## 4.3. Quản trị giá, khuyến mãi và chính sách hiển thị giá *(bonus — quy trình thứ 3 có Phân tích đầy đủ)*

*(Nguồn: `25410206/MoMo.docx` Chương 4 — trước đây bị gắn NHẦM dưới heading "Tìm kiếm, lựa chọn hành trình...", nay đổi đúng tên quy trình. Đã sửa công thức rework theo `plan/05` mục C.)*

### 4.3.1. Phân tích quy trình

Quy trình mang lại giá trị cho cả khách hàng cuối (giá minh bạch, khuyến mãi hấp dẫn) và nội bộ MoMo (kiểm soát rủi ro tài chính/pháp lý trước khi công bố giá). Kết quả có thể đạt được: chính sách giá/KM được phê duyệt và công bố thành công; hoặc bị hủy/từ chối do không đạt thẩm định rủi ro hoặc hồ sơ điều kiện thiếu.

### 4.3.2. Phân tích định tính

**a) Phân tích giá trị gia tăng** — 23 hoạt động được phân loại: **4 VA** (Xây dựng chính sách giá/KM; Thiết kế cơ chế KM; Cấu hình giá lên hệ thống; Công bố giá/KM), **14 BVA**, **5 NVA** (đều là các bước rework: yêu cầu bổ sung dữ liệu, trả lại chuẩn hóa, điều chỉnh mục tiêu campaign, bổ sung hồ sơ pháp lý, sửa cấu hình lỗi). Bảng đầy đủ dưới đây bổ sung 2 cột Mô tả + Khắc phục còn thiếu ở bản gốc:

| Hoạt động | Người thực hiện | Loại | Mô tả | Khắc phục |
|---|---|---|---|---|
| Gửi/Tiếp nhận/Kiểm tra dữ liệu giá gốc | Hãng bay–NCC / Bộ phận Giá | BVA | Đầu vào bắt buộc, chưa tạo giá trị trực tiếp cho khách | Chuẩn hóa định dạng dữ liệu đầu vào bắt buộc từ hãng bay |
| Yêu cầu bổ sung dữ liệu (nếu thiếu) | Bộ phận Giá | NVA | Phát sinh do dữ liệu đầu vào không đạt chuẩn ngay từ đầu | Web portal cho hãng bay tự validate trước khi gửi |
| Chuẩn hóa giá/thuế/phí + kiểm tra | Bộ phận Giá | BVA | Đảm bảo dữ liệu đồng nhất trước khi dùng | Rule Engine tự động chuẩn hóa theo công thức thuế chuẩn |
| Trả lại điều chỉnh chuẩn hóa (nếu sai) | Bộ phận Giá | NVA | Rework do sai công thức tính | Kiểm tra chéo (Maker-Checker) trước khi chuyển tiếp |
| Phân tích tệp KH & mục tiêu chiến dịch | Marketing | BVA | Chuẩn bị cơ sở cho quyết định KM, KH chưa thấy | CRM/BI hỗ trợ phân tích tự động |
| Xây dựng chính sách giá/KM | Marketing | VA | Tạo ra ưu đãi cụ thể mang lại giá trị cho khách | Thư viện mẫu cơ chế KM đã duyệt sẵn |
| Thiết kế cơ chế KM & điều kiện | Marketing | VA | Hoàn thiện sản phẩm ưu đãi cuối cùng | Template hồ sơ điều kiện chuẩn hóa |
| Điều chỉnh đối tượng/mục tiêu (nếu không phù hợp) | Marketing | NVA | Rework do đánh giá sai tệp khách hàng ban đầu | Kiểm tra độ phù hợp bằng dữ liệu hành vi trước khi thiết kế |
| Thẩm định tài chính + kiểm tra hồ sơ | Tài chính/Pháp chế | BVA | Kiểm soát rủi ro, khách hàng không thấy trực tiếp | Checklist pháp lý chuẩn cho Marketing tự rà trước |
| Yêu cầu bổ sung hồ sơ (nếu thiếu) | Tài chính/Pháp chế | NVA | Rework do hồ sơ Marketing gửi chưa đủ | Template hồ sơ điều kiện đã duyệt sẵn (như trên) |
| Cấu hình thuật toán giá/hiển thị | Kỹ thuật | VA | Đưa chính sách vào vận hành thực tế | Unit test tự động trước khi lên môi trường thật |
| Ghi nhận/lưu trữ dữ liệu | App MoMo | BVA | Bước kỹ thuật nền tảng | Tự động hóa hoàn toàn, không cần can thiệp thủ công |
| Kiểm tra hiển thị (UAT) | Kỹ thuật/App | BVA | Đảm bảo chất lượng trước khi ra mắt | Automation testing quét UI/UX |
| Yêu cầu chỉnh sửa cấu hình (nếu lỗi) | Kỹ thuật | NVA | Rework do lỗi cấu hình/hiển thị | Unit test + kiểm thử tự động (như trên) |
| Công bố giá/KM chính thức | Kỹ thuật | VA | Đưa giá trị đến tay người dùng cuối | — (bước cuối, đã tối ưu) |
| Hiển thị thành công đến người dùng | App MoMo | VA | Hoàn tất giá trị cốt lõi của quy trình | Giám sát tự động, cảnh báo sớm nếu lỗi hiển thị |

**b) Phân tích lãng phí** — cơ cấu lại đúng khung **Move/Hold/Overdo** (bản gốc dùng "Hold/Over-processing/Defect", thiếu hẳn nhóm Move — đã bổ sung):

| Nhóm | Liệt kê | Mô tả | Khắc phục |
|---|---|---|---|
| **Move** | Hồ sơ giá/KM luân chuyển qua 5 khâu thủ công: Hãng bay → Bộ phận Giá → Marketing → Tài chính/Pháp chế → Kỹ thuật | Mỗi lần bàn giao đều qua email/file rời rạc, dễ thất lạc hoặc sai phiên bản, không có hệ thống theo dõi trạng thái tập trung | Nền tảng quản lý luồng phê duyệt (BPM Software) dùng chung, hiển thị trạng thái real-time cho mọi bên |
| **Hold** | Chờ Hãng bay gửi lại dữ liệu bổ sung; chờ Marketing sửa cơ chế KM khi bị từ chối; chờ Kỹ thuật rà soát khi test lỗi | Tăng đáng kể cycle time, có thể bỏ lỡ thời điểm vàng (time-to-market) của chiến dịch | SLA phản hồi nội bộ/đối tác rõ ràng; cảnh báo tự động khi ticket quá hạn |
| **Overdo** | Chuẩn hóa thuế/phí thủ công lặp lại cho từng hãng bay; soạn lại hồ sơ điều kiện KM từ đầu dù format tương tự | Tốn thời gian nhân sự cho tác vụ lặp, tăng nguy cơ sai sót con người | ETL tự động chuẩn hóa cấu trúc giá; Template Library cho các loại hình KM chuẩn |
| **Overdo** | Cấu hình sai tham số dẫn đến phải sửa lại; hồ sơ pháp lý thiếu chặt chẽ bị bác | Lãng phí toàn bộ nỗ lực các bước trước, đe dọa doanh thu/uy tín nếu lọt ra production | Maker-Checker bắt buộc; Automation Testing rà soát UI/UX trước nghiệm thu |

**c) Phân tích các bên liên quan (Stakeholder analysis)** — 6 bên liên quan: Khách hàng (mong giá minh bạch, mã KM dễ hiểu — rủi ro churn nếu giá "độn" lúc thanh toán), Hãng bay/NCC (mong chính sách giá được tuân thủ đúng — rủi ro tranh chấp nếu bán sai giá gốc), Bộ phận Giá (áp lực xử lý khối lượng dữ liệu lớn, dễ human error), Marketing (mong phê duyệt nhanh — hay xung đột với Pháp chế), Tài chính/Pháp chế (kiểm soát ngân sách/pháp lý — dễ thành bottleneck), Kỹ thuật/Growth (mong ticket rõ ràng — rủi ro bug ẩn khi kết hợp nhiều chính sách).

**Issue Register (5 vấn đề)** + **Biểu đồ Pareto** (85 điểm ghi nhận): Hồ sơ pháp lý/điều kiện KM không chặt chẽ (29,41%, lũy kế 29,41%) → Dữ liệu đầu vào thiếu sót (23,53%, lũy kế 52,94%) → Lỗi cấu hình kỹ thuật (17,65%, lũy kế 70,59%) → Mâu thuẫn cơ chế KM (17,65%, lũy kế 88,24%) → Sai chuẩn hóa cấu trúc giá (11,76%, lũy kế 100%). Áp dụng 80/20: 3 nhóm đầu (70,59%) là ưu tiên cải tiến hàng đầu.

### 4.3.3. Phân tích định lượng

**Thời gian** — Happy Path = 940 phút (~15,6 giờ). **Sửa công thức rework** (bản gốc dùng cộng đơn giản xác suất×thời gian; sửa đúng theo công thức rework **CT = T/(1−r)** cho từng nhánh làm lại):

| Nhánh rework | p (xác suất) | T (phút) | Công thức cũ (p×T) | Công thức đúng: p×T/(1−p) |
|---|---|---|---|---|
| Bổ sung dữ liệu Hãng bay | 20% | 60 | 12,0 | **15,0** |
| Sai chuẩn hóa | 10% | 45 | 4,5 | **5,0** |
| Sai mục tiêu Marketing | 15% | 120 | 18,0 | **21,18** |
| Thiếu hồ sơ pháp lý | 25% | 90 | 22,5 | **30,0** |
| Lỗi cấu hình phải sửa | 15% | 90 | 13,5 | **15,88** |
| **Tổng thời gian trễ (Delayed Time)** | | | 70,5 | **≈ 87,06** |

Thời gian chu kỳ trung bình (đã sửa) = 940 + 87,06 ≈ **1.027,06 phút** (≈17,1 giờ). Thời gian VA (không đổi) = 465 phút. **PCE = 465/1.027,06 × 100% ≈ 45,28%** (bản gốc ghi 46,01% — chênh lệch nhỏ do áp dụng đúng công thức rework, không thay đổi kết luận: hơn một nửa thời gian quy trình bị tiêu tốn cho kiểm duyệt/chuẩn hóa/chờ đợi).

**Chất lượng** — RTY (Rolled Throughput Yield) = 80% × 90% × 85% × 75% × 85% ≈ **39,01%** — chỉ ~39% chiến dịch được thiết lập hoàn hảo ngay lần đầu. Khắc phục: nâng chất lượng đầu vào (80%→95%) bằng validation tự động; nâng chất lượng hồ sơ pháp lý (75%→95%) bằng checklist bắt buộc; nâng chất lượng cấu hình (85%→98%) bằng unit test tự động.

**Chi phí** — đã đúng mô hình thời gian×lương từ đầu (không cần sửa): chi phí nhân công Happy Path ≈ 1.413.600 đồng/chiến dịch. Chi phí VA = Marketing (300p×1.440đ) + Kỹ thuật (160p×2.000đ) = 752.000 đồng. **Hiệu suất chi phí = 752.000/1.413.600 × 100% ≈ 53,19%** — gần một nửa chi phí nhân sự chi cho kiểm tra/rà soát/đối chiếu, chưa kể chi phí cơ hội do thời gian trễ.
