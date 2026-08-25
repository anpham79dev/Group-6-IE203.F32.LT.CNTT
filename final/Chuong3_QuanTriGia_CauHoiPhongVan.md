# Chương 3.1.2 — Phỏng vấn (Quy trình "Quản trị giá, khuyến mãi và chính sách hiển thị giá")

> Bản sửa cho mục "Phỏng vấn" trong `docs/MoMo.docx` (nằm trong Chương 3 hiện tại, mục "Quản trị giá... → Phương pháp thực hiện"). Đây là **lỗi nghiêm trọng nhất dự án** theo `plan/05_KIEM_TRA_TUAN_THU_RUBRIC.md` mục B: bảng "câu hỏi định lượng" hiện tại copy y hệt bảng "câu hỏi định tính" (0 câu thật sự định lượng), và bảng định tính chỉ có 8 câu (5 có cấu trúc + 3 không cấu trúc) thay vì đúng 10 câu (5+5) theo yêu cầu rubric.
>
> Khung 2×2 dùng làm mẫu: `25410168/Muc3_Phuong_phap_thuc_hien.docx` (đã đạt chuẩn) + 10 câu định lượng gợi ý ở `docs/REVIEW-MoMo.md` mục 1.2 (đã phân loại lại có/không cấu trúc ở đây).

---

## Đoạn dẫn nhập (thay thế đoạn hiện tại)

**Đoạn hiện tại trong `docs/MoMo.docx`** (cần thay, vì khẳng định phỏng vấn thật — nhóm đã xác nhận KHÔNG có phỏng vấn thật MoMo):

> "Nhóm thực hiện đã phối hợp cùng nhân sự nội bộ tại MoMo để tiến hành trao đổi và thu thập thông tin từ các bộ phận liên quan. Mục đích của việc này là nhằm ghi nhận mô tả chi tiết về cách thức làm việc thực tế, từ đó làm cơ sở để xây dựng và vẽ lại các sơ đồ quy trình nghiệp vụ tương ứng."

**Đoạn thay thế:**

> Do đồ án không có điều kiện tiếp cận và phỏng vấn trực tiếp nhân sự nội bộ của M_Service, nhóm xây dựng bộ câu hỏi khảo sát dưới đây theo hình thức **mô phỏng/giả định**: các câu hỏi được thiết kế dựa trên nghiên cứu quy trình nghiệp vụ công khai (trang trợ giúp MoMo, quy định của Ngân hàng Nhà nước về trung gian thanh toán) và suy luận hợp lý về cách các bộ phận nội bộ liên quan (Bộ phận về giá, Marketing, Tài chính/Pháp chế, Growth specialist/Kỹ thuật, CSKH) có thể vận hành quy trình trong thực tế. Bộ câu hỏi đóng vai trò định hướng nội dung phỏng vấn thật nếu nhóm có điều kiện tiếp cận nhân sự MoMo trong tương lai. Các số liệu minh họa được sử dụng ở phần Phân tích định lượng (Chương 4) là **giả định của nhóm**, không phải số liệu thu thập thực tế từ phỏng vấn.

> ⚠️ Áp dụng lại cách diễn đạt này (điều chỉnh cho khớp bộ phận liên quan) cho đoạn dẫn nhập "Phỏng vấn" của **mọi quy trình khác** trong báo cáo — không chỉ riêng "Quản trị giá". Đây là thay đổi áp dụng toàn bài, không phải chỉ chương này.

---

## Câu hỏi định tính (10 câu = 5 có cấu trúc + 5 không cấu trúc)

5 câu có cấu trúc **giữ nguyên** từ bảng hiện tại (đã đạt chuẩn, không cần sửa). 5 câu không cấu trúc: giữ 3 câu cũ + bổ sung 2 câu mới (in đậm) để đủ 5.

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Theo Anh/Chị, công đoạn nào trong quy trình này thường phát sinh nhiều khó khăn và mất thời gian nhất? A. Chuẩn hóa dữ liệu giá, thuế, phí. B. Thiết kế cơ chế khuyến mãi. C. Thẩm định hồ sơ điều kiện/ngân sách. D. Cấu hình và kiểm thử hiển thị. | Tất cả các bộ phận tham gia | Xác định điểm nghẽn (bottleneck) trong toàn bộ quy trình. |
| 2 | Có cấu trúc | Khi dữ liệu giá/thuế/phí từ Hãng bay/NCC gửi sang bị thiếu sót, Anh/Chị thường xử lý theo phương án nào? A. Trả lại và yêu cầu Hãng gửi lại toàn bộ. B. Phối hợp với Hãng để bổ sung phần thiếu. C. Tự bổ sung/điều chỉnh dựa trên dữ liệu cũ. D. Báo cáo cấp trên xin ý kiến. | Bộ phận về giá | Đánh giá quy trình xử lý ngoại lệ ở bước đầu vào dữ liệu. |
| 3 | Có cấu trúc | Nguyên nhân phổ biến nhất khiến một hồ sơ khuyến mãi bị từ chối phê duyệt là gì? A. Vượt quá ngân sách cho phép. B. Thiếu chứng từ, hồ sơ hợp lệ. C. Điều kiện áp dụng không rõ ràng, có rủi ro pháp lý. D. Sai đối tượng mục tiêu. | Bộ phận Tài chính/Pháp chế | Đánh giá rủi ro pháp lý, tài chính và mức độ minh bạch của hồ sơ KM. |
| 4 | Có cấu trúc | Khi tiến hành cấu hình hệ thống, khó khăn lớn nhất mà Anh/Chị gặp phải là gì? A. Cơ chế khuyến mãi của Marketing quá phức tạp. B. Thời gian yêu cầu cấu hình quá gấp (SLA ngắn). C. Lỗi từ hệ thống backend. D. Thông tin bàn giao không rõ ràng. | Growth specialist/Kỹ thuật | Đánh giá mức độ phức tạp và tính khả thi trong khâu thiết lập kỹ thuật. |
| 5 | Có cấu trúc | Bước kiểm thử (Test) hiển thị trên App MoMo hiện tại chủ yếu thực hiện theo hình thức nào? A. 100% tự động (Automation Test). B. Chủ yếu là kiểm tra thủ công (Manual Test). C. Kết hợp cả tự động và thủ công. D. Bỏ qua nếu thời gian quá gấp. | Kỹ thuật, Marketing | Xác định mức độ ứng dụng công nghệ trong khâu kiểm soát chất lượng hiển thị. |
| 6 | Không cấu trúc | Theo Anh/Chị, tiêu chuẩn nào hiện đang được sử dụng để chuẩn hóa dữ liệu giá/thuế/phí, và công đoạn này có thể được tự động hóa thêm không? | Bộ phận về giá | Tìm hiểu chi tiết cách thức chuẩn hóa và tiềm năng áp dụng công nghệ tự động hóa. |
| 7 | Không cấu trúc | Trong trường hợp bước "Kiểm tra hiển thị giá/KM" trên App phát hiện lỗi giao diện hoặc sai giá, quy trình yêu cầu chỉnh sửa diễn ra như thế nào và tốn khoảng bao lâu? | Kỹ thuật, Marketing | Đánh giá quy trình xử lý sự cố trước khi công bố (Go-live). |
| 8 | Không cấu trúc | Theo Anh/Chị, để rút ngắn thời gian đưa một chính sách giá/khuyến mãi ra thị trường (Time-to-market), chúng ta nên ưu tiên loại bỏ hoặc thay đổi bước nào trong luồng công việc hiện tại? | Tất cả các bộ phận tham gia | Thu thập ý kiến, sáng kiến cải tiến quy trình thực tế từ người trực tiếp thực hiện. |
| 9 | **Không cấu trúc** | **Theo Anh/Chị, sự phối hợp giữa Marketing và Tài chính/Pháp chế trong khâu thẩm định hồ sơ khuyến mãi hiện có điểm nào chưa ăn khớp, gây chậm trễ?** | Marketing, Tài chính/Pháp chế | Nhận diện điểm nghẽn phối hợp liên phòng ban ở khâu thẩm định. |
| 10 | **Không cấu trúc** | **Anh/Chị nhận thấy rủi ro lớn nhất là gì nếu quy trình duyệt giá/khuyến mãi bị rút ngắn quá mức để kịp tiến độ một chiến dịch gấp?** | Tất cả các bộ phận tham gia | Đánh giá đánh đổi giữa tốc độ và kiểm soát rủi ro trong quy trình. |

## Câu hỏi định lượng (10 câu = 5 có cấu trúc + 5 không cấu trúc) — VIẾT LẠI HOÀN TOÀN

Toàn bộ bảng dưới đây thay thế bảng "câu hỏi định lượng" hiện tại (đang copy y hệt bảng định tính). Mỗi câu đều phải thu được **con số/tỷ lệ/khoảng thời gian thật**, không phải câu hỏi trắc nghiệm ý kiến.

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Trung bình mất bao nhiêu giờ để chuẩn hóa xong 1 bộ dữ liệu giá? A. ≤2 giờ. B. 2–4 giờ. C. 4–8 giờ. D. >8 giờ. | Bộ phận về giá | Đo thời gian xử lý bước chuẩn hóa dữ liệu đầu vào. |
| 2 | Có cấu trúc | Trung bình 1 tuần, bộ phận tiếp nhận khoảng bao nhiêu bộ dữ liệu giá từ Hãng bay/NCC? A. <5 bộ. B. 5–10 bộ. C. 11–20 bộ. D. >20 bộ. | Bộ phận về giá | Đo tần suất/khối lượng công việc đầu vào của quy trình. |
| 3 | Có cấu trúc | Bao nhiêu % hồ sơ khuyến mãi bị Tài chính/Pháp chế từ chối ngay ở lần trình đầu tiên? A. <10%. B. 10–25%. C. 26–50%. D. >50%. | Bộ phận Tài chính/Pháp chế | Đo tỷ lệ rework ở khâu thẩm định pháp lý/tài chính. |
| 4 | Có cấu trúc | Thời gian trung bình từ lúc nhận hồ sơ đến khi ra quyết định phê duyệt là bao lâu? A. <1 ngày. B. 1–2 ngày. C. 3–5 ngày. D. >5 ngày. | Bộ phận Tài chính/Pháp chế | Đo thời gian xử lý bước thẩm định — đầu vào cho tính cycle time. |
| 5 | Có cấu trúc | Trung bình cần bao nhiêu lần cấu hình lại (rework) cho 1 chiến dịch khuyến mãi trước khi đạt yêu cầu hiển thị? A. 0 lần. B. 1 lần. C. 2 lần. D. ≥3 lần. | Growth specialist/Kỹ thuật | Đo tỷ lệ rework ở khâu cấu hình kỹ thuật — đầu vào công thức T/(1-r). |
| 6 | Không cấu trúc | Trung bình 1 lượt kiểm thử (test) hiển thị giá/khuyến mãi trên App mất bao nhiêu phút? | Kỹ thuật, Marketing | Đo thời gian xử lý bước kiểm thử trước khi công bố. |
| 7 | Không cấu trúc | Mỗi tháng phát sinh khoảng bao nhiêu ticket khiếu nại liên quan đến sai giá/sai khuyến mãi hiển thị trên App? | CSKH | Đo chỉ số chất lượng đầu ra của quy trình (tỷ lệ lỗi). |
| 8 | Không cấu trúc | Tổng thời gian chu kỳ (cycle time) trung bình, tính từ lúc nhận dữ liệu giá đến khi chính thức công bố trên App, là khoảng bao lâu? | Tất cả các bộ phận tham gia | Thu thập số liệu cycle time tổng — đầu vào bắt buộc cho phần Phân tích định lượng ở Chương 4. |
| 9 | Không cấu trúc | Trung bình cần bao nhiêu nhân sự và bao nhiêu giờ công để hoàn tất 1 lần chạy toàn bộ quy trình (từ nhận dữ liệu đến công bố)? | Tất cả các bộ phận tham gia | Thu thập số liệu chi phí nhân sự — đầu vào bắt buộc cho phần chi phí (thời gian × lương) ở Chương 4. |
| 10 | Không cấu trúc | Bao nhiêu % bộ dữ liệu giá bị trả lại yêu cầu bổ sung ngay ở lần gửi đầu tiên từ Hãng bay/NCC? | Bộ phận về giá | Đo tỷ lệ lỗi/rework ở bước đầu vào dữ liệu. |

> 💡 Câu 8–9 của bảng định lượng là đầu vào bắt buộc cho phần Phân tích định lượng (thời gian chu kỳ, chi phí nhân sự) nếu sau này nhóm chọn "Quản trị giá" làm quy trình Phân tích thứ 3 (bonus, xem `plan/03` mục 1 và `plan/04` việc #9 của 25410206).

---

## Việc còn lại (ngoài phạm vi Giai đoạn 1)

Bảng trên chỉ áp dụng cho quy trình "Quản trị giá". Việc nhân rộng khung 2×2 này cho các quy trình khác (Quản lý hạng vé, Xuất hóa đơn — theo `plan/04` việc #3 của 25410168) và việc cơ cấu lại bộ câu hỏi đã có sẵn của `25410223`/`25410237` (theo `plan/05` mục B) **chưa nằm trong phạm vi phiên này** — để phiên sau hoặc phân công theo `plan/04`.
