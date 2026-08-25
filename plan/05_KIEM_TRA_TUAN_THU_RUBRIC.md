# KIỂM TRA TUÂN THỦ RUBRIC — Bài làm thành viên đối chiếu chuẩn

> Nguyên tắc: rubric + bài giảng là chuẩn duy nhất. File này ghi lại từng chỗ nguyên liệu thô của thành viên (đã liệt kê ở `02_NGUYEN_LIEU_THANH_VIEN.md`) **lệch so với yêu cầu chính xác của rubric/lý thuyết** — để khi gộp vào báo cáo chính không copy nguyên xi mà phải sửa đúng chuẩn trước.

## A. Độ phức tạp sơ đồ BPMN (rubric 2.0) — đã tự kiểm tra bằng cách đếm gateway trong file `.bpmn`

Rubric chấm theo số gateway: **>7 gateway = điểm tối đa, >5 = 0.75, >3 = 0.5**, ít hơn nữa gần như không có điểm phần độ phức tạp.

| File `.bpmn` | Quy trình | Số gateway thực tế | Đạt ngưỡng nào |
|---|---|---|---|
| `docs/MoMo.docx` — ảnh nhúng sẵn (6 sơ đồ: Quản trị giá, Quản lý hạng vé, Tìm kiếm..., Mua thêm dịch vụ, Hỗ trợ KH, Xuất hóa đơn) | 6 quy trình đã có Chương 2 đầy đủ | Đếm bằng mắt trên ảnh: mỗi sơ đồ đều có **>10 gateway dạng X (Exclusive)**, ký hiệu đúng chuẩn BPMN | ✅ **>7, đạt điểm tối đa cả 6** — đây là điểm mạnh sẵn có, không cần sửa gì thêm về độ phức tạp |
| `25410206/MoMo_Core01_TimKiem_SoSanhChuyenBay.bpmn` | Tìm kiếm & so sánh chuyến bay | 10 (8 XOR + 2 AND, dùng Parallel Gateway đúng chỗ cho gọi API song song) | ✅ >7 |
| `25410206/MoMo_Core02_LuaChonHanhTrinh_HangBay.bpmn` | Chọn hành trình/hãng bay | 11 (XOR) | ✅ >7 |
| `25410206/MoMo_Core03_ThanhToan_XacNhanDatVe.bpmn` | Thanh toán & xác nhận | 12 (XOR) | ✅ >7 |
| `25410223/MoMo_Core01_...docx` | Tìm kiếm/lựa chọn/thanh toán (bản gộp) | 3 | ❌ dưới ngưỡng >3 thấp nhất |
| `25410223/MoMo_Core02_MuaDichVuBoSung...bpmn` | Mua thêm dịch vụ | 3 | ❌ dưới ngưỡng >3 |
| `25410223/MoMo_Core03_DoiChuyenBay...bpmn` | **Đổi chuyến bay** | 3 | ❌ dưới ngưỡng >3 — **đây là sơ đồ DUY NHẤT có cho quy trình này, cần làm giàu thêm gateway trước khi dùng** |
| `25410237/MoMo_Onboarding_DoiTac.bpmn` | Onboarding đối tác (thuộc "Quản trị danh mục hãng bay") | 3 | ❌ dưới ngưỡng >3 |
| `25410237/MoMo_RaSoat_LoaiBoDoiTac.bpmn` | Rà soát/loại bỏ đối tác (thuộc quy trình trên) | 3 | ❌ dưới ngưỡng >3 |
| `25410237/MoMo_TraSoat_GiaoDichLoi.bpmn` | Tra soát giao dịch lỗi (thuộc "Hỗ trợ KH"/"Quản trị rủi ro") | 2 | ❌ dưới ngưỡng >3 |
| `25410237/MoMo_XuLy_KhieuNaiKH.bpmn` | Xử lý khiếu nại KH | 3 | ❌ dưới ngưỡng >3 |

**Kết luận & việc cần làm:**
1. **Tin tốt**: 6 sơ đồ BPMN đã có sẵn trong báo cáo chính (`docs/MoMo.docx`) đều đạt chuẩn độ phức tạp tối đa — không cần vẽ lại, chỉ cần viết thêm phần text "Phương pháp thực hiện" đi kèm (đã ghi ở file 04).
2. **Cần làm thêm**: toàn bộ sơ đồ `.bpmn` riêng của 25410223 và 25410237 đều **quá đơn giản** (2-3 gateway/sơ đồ) so với chuẩn 6 sơ đồ gốc (10-12 gateway). Trước khi dùng cho quy trình "Đổi chuyến bay" (25410223) và "Quản trị danh mục hãng bay" (25410237, có thể gộp 2 sơ đồ Onboarding+RaSoat thành 1 sơ đồ tổng để tăng gateway lên >7), người phụ trách cần **bổ sung thêm nhánh rẽ nhánh** — may mắn là nội dung ngoại lệ đã có sẵn dưới dạng văn xuôi (VD: `cstt.md` của 25410223 mô tả 2-3 kịch bản ngoại lệ cho "Đổi chuyến bay" — như "hết chỗ khi tái phát hành", "hạng vé không hỗ trợ đổi tự động" — nhưng các nhánh này **chưa được vẽ thành gateway** trong file `.bpmn`, chỉ nằm trong mô tả). Việc: chuyển các kịch bản ngoại lệ đã mô tả bằng lời thành gateway thật trong sơ đồ.
3. Toàn bộ 6 sơ đồ gốc dùng đúng ký hiệu **Exclusive Gateway (hình thoi có dấu X)** — không phát hiện lỗi sai ký hiệu (VD: dùng nhầm Parallel cho trường hợp loại trừ lẫn nhau). Khi vẽ thêm cho "Đổi chuyến bay"/"Quản trị danh mục hãng bay", giữ đúng quy tắc chương 3 bài giảng: XOR cho lựa chọn loại trừ, AND/Parallel chỉ dùng khi các nhánh THỰC SỰ chạy đồng thời (như cách 25410206 dùng đúng ở Core01 cho việc gọi API song song nhiều hãng bay).

## B. Phương pháp thực hiện & bộ câu hỏi phỏng vấn (rubric 3.0) — đã kiểm tra xong

**Chuẩn bắt buộc**: mỗi quy trình cần đúng **20 câu hỏi** = 10 định tính (5 có cấu trúc + 5 không cấu trúc) + 10 định lượng (5 có cấu trúc + 5 không cấu trúc), câu định lượng phải hỏi ra **con số thật** (thời lượng/tần suất/%/thang đo), và phải có đủ bằng chứng (sơ đồ tổ chức, kế hoạch làm việc, thuật ngữ, biểu mẫu).

| Nguồn | Quy trình | Tổng câu hỏi | Định tính | Định lượng (có thật không?) | Có nhãn có/không cấu trúc? | Bằng chứng (org chart/kế hoạch/thuật ngữ/biểu mẫu) | Kết luận |
|---|---|---|---|---|---|---|---|
| `25410168` Muc3 | Tìm kiếm.../Mua thêm DV (chung) | 20 | 10 (5+5) | 10 (5+5), **đúng chuẩn, có thật** | Có, rõ ràng | Đủ | ✅ ĐẠT CHUẨN |
| `25410206` Core01 | Tìm kiếm & so sánh | 20 | 10 (5+5) | 10 (5+5), có thật | Có | Đủ | ✅ ĐẠT CHUẨN |
| `25410206` Core02 | Lựa chọn hành trình/hãng bay | 20 | 10 (5+5) | 10 (5+5), có thật | Có | Đủ | ✅ ĐẠT CHUẨN |
| `25410206` Core03 | Thanh toán & xác nhận | 20 | 10 (5+5) | 10 (5+5), có thật | Có | Đủ | ✅ ĐẠT CHUẨN |
| `25410223` Core01 | Tìm kiếm/lựa chọn/thanh toán | **4** | 2 | 2 | Không | **Thiếu hoàn toàn** — không có chương Phương pháp thực hiện | ❌ PHẢI VIẾT LẠI TỪ ĐẦU |
| `25410223` Core02 | Mua thêm dịch vụ | **2** | 1 (1 câu bị gắn nhầm nhãn — thực chất hỏi %, tức định lượng nhưng ghi "Định tính") | 1 | Không | Thiếu hoàn toàn | ❌ PHẢI VIẾT LẠI TỪ ĐẦU |
| `25410223` Core03 | Đổi chuyến bay | **2** | 1 | 1 | Không | Thiếu hoàn toàn | ❌ PHẢI VIẾT LẠI TỪ ĐẦU |
| `25410237` HauMai | Hỗ trợ KH/xử lý ngoại lệ | 30 câu nhưng chia 3 danh sách rời rạc (10 định tính phẳng + 10 định lượng phẳng + 5/5 có/không cấu trúc **không gắn với trục định tính/định lượng**) | — | 10 câu ở §4.2 có thật là định lượng | Có nhưng đặt lệch (mục §4.3 riêng, không cross-tag) | Đủ, làm tốt | ❌ CẦN CƠ CẤU LẠI (nội dung tốt, chỉ sai cấu trúc) |
| `25410237` Quan_tri_danh_muc | Quản trị danh mục hãng bay | Giống hệt lỗi cấu trúc ở trên (30 câu, 3 danh sách rời) | — | Có thật | Lệch tương tự | Đủ, làm tốt | ❌ CẦN CƠ CẤU LẠI |
| `docs/MoMo.docx` (báo cáo chính) | Quản trị giá, khuyến mãi | 8 câu duy nhất bị trình bày thành 16 (2 bảng) | 8 (5 có cấu trúc + 3 không — không phải 5/5) | **0 câu định lượng thật** — bảng "định lượng" là **copy y hệt** bảng định tính, cùng STT/cùng nội dung/cùng dạng trắc nghiệm A/B/C/D | Có nhãn nhưng sai tỷ lệ (5/3) và không phải câu định lượng thật | Đủ, làm tốt | ❌ **LỖI NGHIÊM TRỌNG NHẤT DỰ ÁN** — cần thay hoàn toàn bảng định lượng bằng 10 câu mới + bổ sung 2 câu định tính để đạt 5/5 |

**Việc cần làm theo thứ tự ưu tiên:**
1. 🔴 **`docs/MoMo.docx` — bảng câu hỏi "Quản trị giá"**: thay toàn bộ 8 câu "định lượng" giả bằng 10 câu định lượng thật (VD: "Trung bình mất bao nhiêu giờ để xử lý 1 yêu cầu cập nhật giá?", "Bao nhiêu % hồ sơ KM bị từ chối ở lần trình đầu?" — đã có sẵn gợi ý trong `REVIEW-MoMo.md` mục 1.2, chỉ cần bổ sung phân loại 5 có cấu trúc/5 không cấu trúc), đồng thời bổ sung định tính từ 8→10 câu (thêm 2 câu, chia đúng 5/5).
2. 🔴 **`25410223` Core01/02/03**: hiện gần như không có gì (2-4 câu, không có chương Phương pháp thực hiện) — đây là lỗ hổng nặng nhất về khối lượng, người phụ trách (Lê Quốc Hưng) cần viết mới hoàn toàn theo đúng khung mẫu của 25410206 (đã đạt chuẩn), bao gồm cả org chart/kế hoạch/thuật ngữ/biểu mẫu.
3. 🟠 **`25410237` (2 file)**: nội dung câu hỏi thực ra tốt và đã đủ số lượng, chỉ cần **cơ cấu lại** thành đúng lưới 2×2 (định tính×có cấu trúc, định tính×không cấu trúc, định lượng×có cấu trúc, định lượng×không cấu trúc, mỗi ô 5 câu) thay vì 3 danh sách rời rạc hiện tại, đồng thời cắt bớt từ 30 câu dư xuống đúng 20 câu chuẩn.
4. Sửa 1 câu bị gắn nhầm nhãn trong `25410223` Core02 (câu hỏi % bị ghi là "Định tính").

**Phát hiện hệ thống (áp dụng toàn dự án):** trục "có cấu trúc/không cấu trúc" là điểm yếu nhất — chỉ 4/10 nguồn (đều của 25410168 và 25410206) làm đúng lưới 2×2 với định tính/định lượng. Đây nên là việc chuẩn hóa ưu tiên hàng đầu khi viết lại bộ câu hỏi cho các quy trình còn lại.

## C. Nội dung Phân tích quy trình (rubric 4.0) — đã kiểm tra xong

**Chuẩn bắt buộc**: VA/BVA/NVA đủ 3 nhóm (không phải VA/NVA 2 nhóm) với cột "khắc phục"; lãng phí đúng khung Move/Hold/Overdo; bên liên quan chọn đúng 1/3 kỹ thuật (Pareto/Root-cause/Fishbone 6M: Measurement/Material/Machine/Milieu/Man/Method) và trình bày đủ; định lượng thời gian dùng đúng công thức (tuần tự=tổng, XOR=trung bình có trọng số xác suất, AND=max, rework=T/(1-r)) + hiệu suất = xử lý/chu kỳ; chi phí = thời gian×lương theo từng tác nhân; chất lượng phải có tính toán, không chỉ nêu số.

| Nguồn | VA/BVA/NVA (3 nhóm)? | Lãng phí Move/Hold/Overdo? | Kỹ thuật bên liên quan | Công thức định lượng đúng chuẩn? | Cột khắc phục? | Kết luận |
|---|---|---|---|---|---|---|
| `25410168` Muc4 | ✅ Đủ 3 nhóm, đủ cột (ghi "VBA" thay vì "BVA" — chỉnh chính tả) | ✅ Đúng Move/Hold/Overdo | ⚠️ Chọn Fishbone nhưng chỉ 5 nhóm nguyên nhân, thiếu đủ 6M | ❌ Thời gian/Chất lượng/Chi phí đều là khoảng ước lượng, **không có công thức tính** | ✅ Có | NEEDS FIX — thêm công thức định lượng thật, bổ sung đủ 6M |
| `25410206` MoMo.docx (Chương 4, thực chất là "Quản trị giá") | ⚠️ Đúng khái niệm nhưng bảng thiếu cột mô tả+khắc phục | ⚠️ Thiếu hẳn nhóm "Move", Over-processing/Defect không gộp đúng "Overdo" | ✅ Có chọn Pareto đúng chuẩn, tính cumulative % | ⚠️ Thời gian đúng công thức tuần tự; **rework dùng cộng xác suất×thời gian thay vì T/(1-r)**; Chi phí/Chất lượng có tính toán (PCE, RTY) | ⚠️ Thiếu ở bảng VA | NEEDS FIX — còn 1 quy trình con "Hỗ trợ KH" trong file này **hoàn toàn trống** (chỉ có heading) |
| `25410206` Core01/02/03 (3 file) | ✅ Đủ 3 nhóm, đủ cột | ✅ Đúng Move/Hold/Overdo | ✅ Mỗi file chọn đúng 1/3 kỹ thuật khác nhau (Fishbone/Root-cause/Pareto), có giải thích lý do chọn | ✅ Thời gian đúng công thức XOR-trọng số, có tính hiệu suất chu kỳ. ❌ **Chi phí dùng mô hình giá hạ tầng/giao dịch, KHÔNG dùng thời gian×lương như yêu cầu**. ⚠️ Chất lượng chỉ nêu số hiện tại/mục tiêu, không có phép tính | ✅ Có | NEEDS FIX — chỉ cần sửa lại công thức Chi phí theo đúng mô hình thời gian×lương, và bổ sung phép tính cho Chất lượng |
| `25410223` Core01/02/03 (3 file) + `cstt.md` | ❌ Dùng nhầm "CVA" thay "VA", chỉ liệt kê 3-4 hoạt động mẫu (không đủ), không có cột khắc phục | ❌ **Không có mục lãng phí nào cả** (Core02/03), hoặc chỉ 2 gạch đầu dòng không theo khung (Core01) | ⚠️ Gắn nhãn "Fishbone" nhưng chỉ 1 câu liệt kê nguyên nhân, không có bảng 6M | ❌ Chỉ có khoảng thời gian ước lượng, **không công thức**; **hoàn toàn không có mục Chất lượng và Chi phí** ở cả 3 file | ❌ Thiếu | **NEEDS FIX NẶNG NHẤT** — thực chất chưa có chương Phân tích đúng nghĩa, phải xây mới theo đúng khung của 25410206 |
| `25410237` HauMai + Quan_tri_danh_muc (2 file) | ⚠️ Phân loại đúng cho mọi hoạt động nhưng bảng chỉ 3 cột (thiếu mô tả+khắc phục) | ✅ Đúng Move/Hold/Overdo, đủ 4 cột | ✅ HauMai chọn Pareto đúng chuẩn; Quan_tri_danh_muc chọn Fishbone với **đủ 6 nhóm nguyên nhân** (không đúng tên 6M gốc nhưng đủ cấu trúc) | ✅ **Công thức định lượng tốt nhất dự án** — có công thức lồng tuần tự+XOR-trọng số, tính hiệu suất chu kỳ, Chi phí = Σ(thời gian×lương) đúng chuẩn, Chất lượng có phép tính rõ ràng (VD: 0,45×0,6=27%) | ⚠️ Thiếu ở bảng VA | NEEDS FIX NHẸ — chỉ cần bổ sung cột mô tả+khắc phục cho bảng VA, đây là nguồn tốt nhất để làm mẫu chuẩn |

**Việc cần làm theo thứ tự ưu tiên:**
1. 🔴 **25410223 (Core01/02/03)**: đây là điểm yếu nặng nhất — thực chất KHÔNG có phân tích lãng phí, không có mục Chất lượng/Chi phí ở cả 3 quy trình, phân loại giá trị dùng sai thuật ngữ "CVA". Không thể chỉ "biên tập nhẹ" như dự kiến ban đầu ở file 04 — cần xây dựng lại gần như từ đầu theo đúng khung mẫu của 25410206 (là mẫu chuẩn nhất). Ưu tiên cao vì đây cũng là nguồn duy nhất cho quy trình "Đổi chuyến bay".
2. 🟠 **25410206 (cả MoMo.docx Chương 4 và 3 file Core0X)**: sửa công thức Chi phí — đổi từ mô hình giá hạ tầng/giao dịch sang đúng mô hình **thời gian × mức lương theo từng tác nhân** (rubric yêu cầu rõ). Sửa công thức rework từ "cộng xác suất×thời gian" sang đúng **T/(1-r)**. Bổ sung phép tính cho mục Chất lượng (hiện chỉ nêu số, không tính).
3. 🟠 **25410237 (2 file)**: chỉ cần bổ sung 2 cột (mô tả, khắc phục) vào bảng VA — việc nhỏ, nhanh.
4. 🟡 **25410168**: thêm công thức định lượng thật cho Thời gian/Chất lượng/Chi phí (hiện toàn số ước lượng không tính toán); bổ sung đủ 6 nhóm cho Fishbone.
5. 🟡 Tất cả các nguồn: chuẩn hóa lại bảng VA thành đúng 3 cột `liệt kê | mô tả | khắc phục` — đây là lỗi lặp lại nhiều nơi nhất.
6. Viết nội dung cho quy trình "Hỗ trợ khách hàng" đang bị bỏ trống hoàn toàn trong file `25410206/MoMo.docx` (chỉ có heading, không có nội dung) — may mắn đã có nguồn thay thế tốt hơn từ `25410237/HauMai`.

**Phát hiện hệ thống:** nhiều báo cáo (2, 3, 4, 5, 10, 11) đều làm thêm một bảng "Power-Interest Grid" trước khi chọn kỹ thuật chính thức — đây KHÔNG phải 1 trong 3 kỹ thuật rubric yêu cầu, nên không tính điểm cho phần đó, chỉ phần Pareto/Root-cause/Fishbone được chọn chính thức mới tính. Không cần xóa Power-Interest Grid (vẫn là nội dung hay) nhưng đừng nhầm rằng nó thay thế được yêu cầu bắt buộc.
