

<!-- ===== FrontMatter_Clean.md ===== -->

# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN

TRUNG TÂM PHÁT TRIỂN CÔNG NGHỆ THÔNG TIN

BÁO CÁO ĐỒ ÁN CUỐI KỲ

HỆ THỐNG QUẢN TRỊ QUY TRÌNH NGHIỆP VỤ

**Đề tài:** TÌM HIỂU VỀ HỆ THỐNG QUY TRÌNH NGHIỆP VỤ MẢNG ĐẶT VÉ MÁY BAY TRÊN ỨNG DỤNG MOMO (THUỘC CÔNG TY CỔ PHẦN DỊCH VỤ DI ĐỘNG TRỰC TUYẾN - M_SERVICE)

**Giảng viên hướng dẫn:** ThS. Hà Lê Hoài Trung

**Nhóm sinh viên thực hiện:**

| STT | MSSV | Họ tên | Vai trò |
|---|---|---|---|
| 1 | 25410175 | Đinh Xuân Bảo | Nhóm trưởng |
| 2 | 25410195 | Nguyễn Huỳnh Mỹ Duyên | Thành viên nhóm |
| 3 | 25410167 | Vũ Thị Nhân Ái | Thành viên nhóm |
| 4 | 25410237 | Nguyễn Mậu An Khương | Thành viên nhóm |
| 5 | 25410168 | Phạm Ngọc Bảo An | Thành viên nhóm |
| 6 | 25410191 | Hồ Nguyễn Bảo Duy | Thành viên nhóm |
| 7 | 25410206 | Nguyễn Đắc Hiển | Thành viên nhóm |
| 8 | 25410223 | Lê Quốc Hưng | Thành viên nhóm |

TP. Hồ Chí Minh, tháng 08 năm 2026

*(⚠️ Nhóm xác nhận lại ngày nộp thật trước khi in — bản gốc ghi "tháng 07", đã tạm sửa thành tháng hiện tại, xem `plan/01` mục 3.8)*

MỤC LỤC *(chèn field tự động trong Word — References → Table of Contents)*

DANH MỤC HÌNH VẼ *(chèn field tự động)*

DANH MỤC BẢNG *(chèn field tự động)*

DANH MỤC TỪ VIẾT TẮT *(xem `final/DanhMucTuVietTat.md`)*

---

## TÓM TẮT ĐỒ ÁN

Ngành thương mại điện tử và dịch vụ du lịch trực tuyến (OTA) tại Việt Nam đang có những bước tiến vượt bậc, đặc biệt là việc tích hợp các dịch vụ này vào các siêu ứng dụng (Super App). Ví điện tử MoMo (thuộc Công ty Cổ phần Dịch vụ Di động Trực tuyến - M_Service) đã tiên phong tích hợp thành công dịch vụ đặt vé máy bay, mang lại trải nghiệm liền mạch cho người dùng. Để đạt được điều này, MoMo cần sở hữu một hệ thống quy trình nghiệp vụ phức tạp, từ quản lý đối tác, cấu hình sản phẩm đến xử lý giao dịch và hỗ trợ khách hàng.

Đồ án này tập trung nghiên cứu, mô hình hóa và phân tích hệ thống quy trình nghiệp vụ mảng đặt vé máy bay của MoMo. Thông qua việc sử dụng ký hiệu chuẩn BPMN (Business Process Model and Notation), nghiên cứu đã vẽ lại sơ đồ kiến trúc nghiệp vụ cho 10 quy trình (4 Quản lý, 3 Cốt lõi, 3 Hỗ trợ), trong đó mô hình hóa BPMN chi tiết cho 6 quy trình đại diện (2 Quản lý, 2 Cốt lõi, 2 Hỗ trợ). Trong số đó, 3 quy trình được phân tích chuyên sâu qua hai lăng kính: định tính (phân tích giá trị gia tăng VA/BVA/NVA, nhận diện lãng phí) và định lượng (tính toán thời gian chu kỳ, thời gian xử lý, chi phí nhân sự và hiệu suất). Kết quả của đồ án cung cấp bức tranh toàn cảnh về cách MoMo vận hành mảng vé máy bay, từ đó đề xuất các hướng tối ưu hóa tự động hóa nhằm nâng cao trải nghiệm khách hàng và giảm thiểu chi phí vận hành.

## MỞ ĐẦU

Trong kỷ nguyên chuyển đổi số, sự ra đời của các "siêu ứng dụng" đã làm thay đổi hoàn toàn thói quen tiêu dùng. MoMo không chỉ dừng lại ở dịch vụ thanh toán mà đã trở thành nền tảng đáp ứng mọi nhu cầu hàng ngày, trong đó có du lịch - đi lại. Việc bán vé máy bay trực tiếp trên ứng dụng đòi hỏi MoMo phải kết nối hệ thống phức tạp với các hãng hàng không, đại lý vé (NCC), đồng thời quản lý luồng dữ liệu khổng lồ về giá, hạng vé, thông tin khách hàng và giao dịch tài chính.

Mục tiêu của đề tài là ứng dụng lý thuyết Hệ thống quản trị quy trình nghiệp vụ (BPMS) để rà soát lại kiến trúc quy trình của mảng kinh doanh này. Từ đó, xây dựng các mô hình BPMN "As-Is" (hiện tại) và thực hiện phân tích chuyên sâu nhằm tìm ra các điểm nghẽn (bottlenecks) và các bước không tạo ra giá trị (NVA).

Đồ án được chia thành 5 chương:

Chương 1: Tổng quan về M_Service và dịch vụ đặt vé máy bay trên MoMo.

Chương 2: Liệt kê và mô tả các quy trình nghiệp vụ, kèm sơ đồ kiến trúc quy trình.

Chương 3: Mô hình hóa chi tiết các quy trình bằng BPMN.

Chương 4: Phân tích các quy trình (định tính và định lượng).

Chương 5: Kết luận.

> ⚠️ Đồ án **không có điều kiện phỏng vấn trực tiếp nhân sự nội bộ MoMo**. Mọi bộ câu hỏi phỏng vấn và số liệu định lượng trình bày trong các chương sau đều mang tính **mô phỏng/giả định**, xây dựng dựa trên nghiên cứu quy trình công khai, trải nghiệm sử dụng thực tế và suy luận nghiệp vụ có căn cứ — không phải số liệu vận hành chính thức do MoMo công bố. Điều này được ghi chú lại ở đầu mỗi phần "Phỏng vấn" trong Chương 3.



<!-- ===== Chuong1_TongQuan.md ===== -->

# Chương 1: TỔNG QUAN VỀ M_SERVICE VÀ DỊCH VỤ ĐẶT VÉ MÁY BAY TRÊN MOMO

> Bản nháp — ghép từ đoạn "Lịch sử hình thành" có sẵn trong bản báo cáo dùng chung của nhóm (`25410168`/`25410195`/`25410175 - Bao DX`, file "TÌM HIỂU VỀ HỆ THỐNG QUY TRÌNH NGHIỆP VỤ...docx") và tổng hợp từ tài liệu kiến trúc quy trình của `25410237` (`MoMo_Kien_truc_quy_trinh_Dat_ve_may_bay.docx`). Đây là chương hiện đang **TRỐNG 100%** trong `docs/MoMo.docx` (xem `plan/01_HIEN_TRANG_VA_LOI.md` mục 3).
>
> ⚠️ Các chỗ đánh dấu **[CẦN NGUỒN THẬT]** là nội dung nhóm chưa có số liệu/tài liệu xác thực — theo đúng nguyên tắc đã thống nhất (`plan/01` mục 4 phần 🔵: "Dẫn nguồn hoặc ghi rõ giả định của nhóm cho các con số chưa có nguồn"), KHÔNG tự bịa số liệu cụ thể (giấy phép, vốn điều lệ, số nhân sự, doanh thu...) — nhóm cần tự bổ sung nguồn công khai đáng tin cậy (website M_Service, thông cáo báo chí, báo cáo Ngân hàng Nhà nước) trước khi nộp.

---

## 1.1. Lịch sử hình thành

Công ty Cổ phần Dịch vụ Di động Trực tuyến (M_Service) chính thức được thành lập vào năm 2007, là đơn vị chủ quản của ví điện tử MoMo. Ban đầu, dịch vụ ra mắt vào năm 2010 dưới dạng ứng dụng trên SIM điện thoại, hợp tác cùng nhà mạng Vinaphone để cung cấp các dịch vụ nạp và chuyển tiền cơ bản. Đến năm 2014, nhóm phát triển quyết định ra mắt ứng dụng trên nền tảng điện thoại thông minh với tên gọi MoMo — viết tắt của cụm từ "Mobile Money" — gửi gắm tham vọng phổ cập dịch vụ tài chính kỹ thuật số, biến chiếc điện thoại thành ví tiền tiện lợi cho mọi người dân Việt Nam.

Qua nhiều năm phát triển, MoMo đã vươn lên trở thành một trong những siêu ứng dụng thanh toán hàng đầu Việt Nam và đạt danh hiệu kỳ lân công nghệ, cạnh tranh trực tiếp với ZaloPay, VNPay, Viettel Money và các nền tảng ví điện tử tích hợp như ShopeePay.

Trong hành trình mở rộng từ một ví điện tử thuần thanh toán sang mô hình "siêu ứng dụng" (Super App), MoMo đã tích hợp thêm nhiều dịch vụ tiện ích ngoài tài chính — trong đó có tính năng "Du lịch - Đi lại", cho phép người dùng tìm kiếm, so sánh và đặt vé máy bay nội địa/quốc tế từ nhiều hãng hàng không (Vietnam Airlines, Vietjet Air, Bamboo Airways...), cùng vé tàu, vé xe khách và đặt phòng khách sạn. Đây chính là phạm vi nghiệp vụ mà đồ án này tập trung mô hình hóa và phân tích.

## 1.2. Quy mô và lĩnh vực hoạt động

M_Service là tổ chức trung gian thanh toán được Ngân hàng Nhà nước Việt Nam cấp phép hoạt động **[CẦN NGUỒN THẬT — số giấy phép, ngày cấp]**. Lĩnh vực hoạt động chính của công ty là cung cấp dịch vụ ví điện tử MoMo, bao gồm các nhóm dịch vụ:

- **Thanh toán & chuyển tiền**: nạp/rút tiền, chuyển tiền, thanh toán hóa đơn, thanh toán tại điểm bán.
- **Dịch vụ tài chính**: ví trả sau, tiết kiệm, bảo hiểm, đầu tư liên kết đối tác.
- **Dịch vụ tiện ích đời sống & du lịch** (Super App): trong đó mảng "Du lịch - Đi lại" — nơi đặt vé máy bay là một hợp phần — là đối tượng nghiên cứu của đồ án này. Vì MoMo không tự vận hành đội bay mà đóng vai trò nền tảng trung gian, mảng đặt vé máy bay là một hệ thống nhiều quy trình phối hợp: từ trải nghiệm tìm kiếm – đặt vé – thanh toán – xuất vé của khách hàng, đến vận hành đối tác phía sau (đồng bộ dữ liệu, đối soát), và các quy trình tuân thủ, bảo mật giao dịch bắt buộc theo quy định của Ngân hàng Nhà nước và ngành hàng không.

Quy mô người dùng, doanh thu và thị phần cụ thể của M_Service **[CẦN NGUỒN THẬT]** — nhóm chưa tiếp cận được số liệu chính thức, đề nghị bổ sung từ báo cáo thường niên hoặc thông cáo báo chí công khai của công ty trước khi hoàn thiện báo cáo.

## 1.3. Cơ cấu tổ chức

Đồ án không tiếp cận được sơ đồ tổ chức chính thức của M_Service **[CẦN NGUỒN THẬT]**. Dựa trên tài liệu kiến trúc quy trình nội bộ nhóm đã tổng hợp (`25410237`, *Tìm hiểu hệ thống quy trình nghiệp vụ mảng đặt vé máy bay trên ứng dụng MoMo — Tài liệu tổng quan kiến trúc quy trình*), nhóm khái quát các bộ phận chức năng có liên quan trực tiếp đến mảng đặt vé máy bay như sau (đây là **bản đồ chức năng do nhóm tổng hợp**, không phải sơ đồ tổ chức chính thức của công ty):

| Nhóm chức năng | Bộ phận liên quan | Vai trò chính trong mảng đặt vé máy bay |
|---|---|---|
| Khách hàng (Front-office) | Bộ phận CSKH | Tiếp nhận, xử lý phản ánh, hoàn/hủy vé, hỗ trợ khách hàng |
| Đối tác & Vận hành | Đội Phát triển Đối tác, Kỹ thuật, Vận hành Sản phẩm Du lịch | Thẩm định/tích hợp hãng bay & NCC, đồng bộ giá vé và lịch bay real-time |
| Đối tác & Vận hành | Đội Vận hành, Tài chính - Kế toán | Đối soát giao dịch, thanh toán hoa hồng với hãng bay/đối tác |
| Tuân thủ & Quản trị rủi ro | Đội Pháp lý & Tuân thủ, Đội Tuân thủ & Quản trị rủi ro | Xác thực giao dịch (eKYC), phòng chống gian lận, xử lý tranh chấp theo pháp luật |
| Hỗ trợ nội bộ | Đội Sản phẩm, Marketing, Growth specialist | Cá nhân hóa ưu đãi/marketing, giám sát chất lượng dịch vụ đối tác (KPI/SLA) |

Bảng thuật ngữ tên bộ phận ở bảng trên cần được **thống nhất lại** với tên gọi đã dùng trong Chương 2–4 của báo cáo chính (ví dụ "Bộ phận về giá", "Bộ phận Tài chính/Pháp chế", "Growth specialist/Kỹ thuật") — việc thống nhất thuật ngữ toàn bài thuộc Giai đoạn 2 (`plan/00` mục 4, `plan/04` việc #4 của 25410175).



<!-- ===== Chuong2_LietKeQuyTrinh.md ===== -->

# Chương 2: LIỆT KÊ QUY TRÌNH NGHIỆP VỤ

> Bản hợp nhất: giữ nguyên nội dung đã đạt chuẩn của `docs/MoMo.docx` cho 6 quy trình đã đầy đủ (chỉ sửa lỗi logic/chính tả theo `plan/01` mục 4 phần 🟠/🟡), thay thế bản 1 dòng của "Quản trị danh mục hãng bay" bằng nội dung đầy đủ từ `25410237`, và viết mới hoàn toàn cho "Đổi chuyến bay" (từ `25410223/cstt.md`), "Quản lý vé đã mua" (viết mới, không có nguyên liệu thành viên) và bổ sung "Quản trị rủi ro giao dịch, điều khoản và chất lượng dịch vụ" (từ `25410237/HauMai`, phần tra soát giao dịch lỗi — nội dung điều khoản/SLA còn để trống chờ bổ sung).

## 2.1. Phân loại quy trình

Để đảm bảo hoạt động cung cấp dịch vụ đặt vé máy bay diễn ra ổn định và mượt mà, MoMo đã xây dựng một hệ thống quy trình chặt chẽ bao gồm các hoạt động từ quản lý đối tác, vận hành giao dịch cốt lõi đến các hoạt động hỗ trợ khách hàng. Các quy trình được phân thành 3 nhóm chính:

- **Nhóm Quy trình quản lý (Management Process)**: tập trung vào việc điều phối, thiết lập chiến lược và kiểm soát các hoạt động hợp tác với đối tác — từ quản trị danh mục hãng bay và đối tác cung ứng, quản trị giá và chương trình khuyến mãi, cho đến cấu hình và công bố hạng vé lên hệ thống, cùng quản trị rủi ro giao dịch và tuân thủ điều khoản dịch vụ.
- **Nhóm Quy trình cốt lõi (Core Process)**: liên quan trực tiếp đến trải nghiệm giao dịch và chuỗi giá trị dịch vụ cung cấp cho người dùng đầu cuối — tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé; mua thêm dịch vụ tiện ích sau đặt chỗ; và đổi chuyến bay.
- **Nhóm Quy trình hỗ trợ (Support Process)**: đảm bảo nền tảng vận hành trơn tru và duy trì sự hài lòng của người dùng — hỗ trợ khách hàng và tiếp nhận phản hồi, tự động hóa xuất hóa đơn điện tử (VAT), và quản lý vé đã mua.

> ⚠️ Sửa so với bản gốc: câu mô tả nhóm Hỗ trợ trong `docs/MoMo.docx` cũ nhắc tới "đối soát tài chính và bảo trì kỹ thuật (API)" — không có quy trình nào tên như vậy được liệt kê ở bất kỳ đâu trong báo cáo (phát hiện ở `plan/01` mục 2.3). Đã thay bằng đúng 3 quy trình Hỗ trợ thật sự có trong danh sách dưới đây.

*(Hình 2.1. Sơ đồ kiến trúc quy trình nghiệp vụ mảng đặt vé máy bay trên MoMo — giữ nguyên hình đã có trong `docs/MoMo.docx`, chỉ đổi số caption từ "Hình 1.1" thành "Hình 2.1" cho đúng chương.)*

## 2.2. Kiến trúc quy trình

### 2.2.1. Quy trình quản lý (Management Process)

#### Quản lý hạng vé

**Tác nhân:** Hãng bay/NCC, Bộ phận Business Development, Bộ phận Ticketing, Ứng dụng MoMo.

**Mô tả các bước:**

1. **Hãng bay/NCC cung cấp dữ liệu vé.** *Mục tiêu:* đảm bảo dữ liệu gốc từ hãng bay đầy đủ, chính xác và đồng nhất với tiêu chuẩn hệ thống trước khi đưa vào kinh doanh. Khi hãng phát hành hạng vé mới, hãng bay/NCC tiến hành "Tạo/Cập nhật thông tin hạng vé". Tùy loại hãng, hệ thống chia 2 luồng: Quốc tế (dữ liệu real-time qua API) hoặc Nội địa (gửi trực tiếp đến M_Service).
2. **Bộ phận Business Development tiếp nhận và chuẩn hóa thông tin.** *Mục tiêu:* xử lý kết nối hệ thống đối với hãng quốc tế và rà soát, chuẩn hóa dữ liệu thủ công đối với hãng nội địa. Luồng Quốc tế: tích hợp API — nếu thất bại, kiểm tra còn trong số lần cho phép (2 lần) hay không, còn thì sửa lỗi và tích hợp lại, hết thì kết thúc "Không tích hợp được API". Luồng Nội địa: tiếp nhận và kiểm tra dữ liệu đầy đủ/hợp lệ — nếu thiếu, BD gửi yêu cầu chỉnh sửa/bổ sung (tạo vòng lặp với hãng bay); nếu đủ, BD phân tích, đối chiếu và chuẩn hóa dữ liệu rồi chuyển sang Ticketing.
3. **Bộ phận Ticketing cấu hình lên hệ thống.** *Mục tiêu:* thiết lập thông số kỹ thuật và đưa dữ liệu đã chuẩn hóa vào cơ sở dữ liệu MoMo. Ticketing tiếp nhận và kiểm tra dữ liệu đã chuẩn hóa — nếu **chưa** chuẩn hóa đúng yêu cầu, yêu cầu điều chỉnh và trả về BD; nếu **đã** chuẩn hóa đúng, tiến hành cấu hình hạng vé lên hệ thống, lưu vào cơ sở dữ liệu hạng vé, chuyển kiểm tra hiển thị trên MoMo.
4. **Phê duyệt cấu hình hạng vé.** *Mục tiêu:* nghiệm thu giao diện thực tế trên ứng dụng và chốt quyết định công bố. App MoMo kiểm tra hiển thị định dạng và cấu trúc dữ liệu — nếu dữ liệu **KHÔNG hợp lệ**, trả kết quả về Ticketing để xử lý lỗi và điều chỉnh rồi kiểm tra lại; nếu dữ liệu **CÓ hợp lệ**, chuyển cho Ticketing phê duyệt công bố. Nếu Ticketing quyết định **không công bố**, quy trình rẽ sang một End Event riêng "Tạm hoãn/Hủy công bố hạng vé" (không nhất thiết là lỗi kỹ thuật, có thể là quyết định kinh doanh); nếu **có công bố**, chuyển sang bước công bố chính thức.
5. **Giám sát và công bố hạng vé.** *Mục tiêu:* đưa hạng vé ra thị trường và liên tục theo dõi để đảm bảo không có sự cố. Ticketing công bố hạng vé lên App MoMo và bắt đầu giám sát sau công bố — nếu phát hiện lỗi, ghi nhận và quay lại bước xử lý lỗi/điều chỉnh; nếu không có lỗi, quy trình kết thúc, hạng vé hiển thị ổn định và thành công.

**Đối tượng khách hàng:** Nội bộ doanh nghiệp và đối tác Hãng bay.

**Kết quả:** *Thành công* — hạng vé được tích hợp, cấu hình, vượt qua kiểm tra và hiển thị ổn định trên App MoMo. *Thất bại* — kết nối API với hãng bay thất bại (vượt quá 2 lần sửa lỗi cho phép), hệ thống dừng tiếp nhận hạng vé.

> ⚠️ Sửa lỗi so với bản gốc (`plan/01` mục 2.3): 2 nhánh ở Bước 4 trước đây cùng mang nhãn "(Dữ liệu hợp lệ)" cho cả 2 trường hợp Có/Không — đã sửa thành "KHÔNG hợp lệ"/"CÓ hợp lệ" rõ ràng như trên. Đã thêm End Event riêng cho nhánh "không công bố" thay vì bắt buộc quay về "Xử lý lỗi" (`plan/01` mục 2.4).

#### Quản trị giá, khuyến mãi và chính sách hiển thị giá

**Tác nhân:** Hãng bay/Nhà cung cấp, Bộ phận Quản lý giá, Bộ phận Marketing, Bộ phận Tài chính/Pháp chế, Bộ phận Growth Specialist/Kỹ thuật, Ứng dụng MoMo.

**Mô tả các bước:**

1. **Tiếp nhận dữ liệu giá từ nhà cung cấp.** *Mục tiêu:* tiếp nhận thông tin giá và chính sách liên quan đến hạng vé từ Hãng bay/NCC. Hãng bay/NCC gửi dữ liệu giá, thuế, phí và chính sách áp dụng. Bộ phận Quản lý giá tiếp nhận và kiểm tra tính đầy đủ — nếu **không đầy đủ**, gửi yêu cầu điều chỉnh/bổ sung (tạo vòng lặp với hãng); nếu **đầy đủ**, tiến hành chuẩn hóa giá/thuế/phí, kiểm tra lại tính hợp lệ — không hợp lệ thì trả lại để chuẩn hóa lại, hợp lệ thì chuyển sang Marketing.
2. **Marketing xây dựng chương trình khuyến mãi.** *Mục tiêu:* thiết kế cơ chế ưu đãi phù hợp tệp khách hàng mục tiêu, đảm bảo hiệu quả ngân sách marketing. Marketing tiếp nhận dữ liệu đã chuẩn hóa, phân tích khách hàng và mục tiêu chiến dịch, quyết định có áp dụng khuyến mãi hay không — **không** thì đẩy thẳng chính sách giá gốc sang Kỹ thuật; **có** thì xây dựng chính sách, kiểm tra độ phù hợp với khách hàng mục tiêu (không phù hợp thì quay lại điều chỉnh), phù hợp thì thiết kế cơ chế khuyến mãi, bổ sung hồ sơ điều kiện và chuyển sang Tài chính/Pháp chế.
3. **Tài chính/Pháp chế thẩm định rủi ro.** *Mục tiêu:* thẩm định tính khả thi tài chính và tuân thủ pháp lý của chính sách giá/KM trước khi ban hành. Thẩm định chính sách do Marketing đề xuất — **không phê duyệt** thì trả về Marketing điều chỉnh; **có phê duyệt** thì kiểm tra hồ sơ điều kiện — không đầy đủ thì yêu cầu Marketing bổ sung, đầy đủ thì chuyển sang khối Kỹ thuật.
4. **Kỹ thuật cấu hình giá lên hệ thống.** *Mục tiêu:* đưa chính sách đã phê duyệt vào hệ thống dưới dạng tham số cấu hình chính xác. Growth Specialist/Kỹ thuật tiếp nhận chính sách giá (có hoặc không qua khuyến mãi) và tiến hành cấu hình giá, chính sách hiển thị vào cơ sở dữ liệu MoMo.
5. **Hiển thị giá lên App.** *Mục tiêu:* đảm bảo hạng vé hiển thị đúng trên ứng dụng và hệ thống giao dịch vận hành trơn tru. Ứng dụng MoMo truy xuất dữ liệu giá/KM, kiểm tra hiển thị trên giao diện thực tế — hiển thị **không đúng** thì gửi yêu cầu chỉnh sửa cấu hình ngược lại cho Kỹ thuật (lặp lại đến khi đúng); hiển thị **đúng** thì thực hiện công bố giá/KM.

**Đối tượng khách hàng:** Nội bộ hệ thống và người dùng cuối (hiển thị giá cạnh tranh).

**Kết quả:** *Thành công* — mức giá/KM được phê duyệt, cấu hình và công bố chính xác đến người dùng. *Hủy bỏ/Từ chối* — chiến dịch bị hủy do không vượt qua thẩm định rủi ro Tài chính/Pháp chế, hoặc hồ sơ điều kiện không được bổ sung đầy đủ.

> ⚠️ Sửa lỗi so với bản gốc (`plan/01` mục 2.1–2.2): quy trình gốc có **hai** "Bước 1" (đã gộp đánh số lại đúng thành 5 bước như trên); 3 câu "Mục tiêu" ở Bước 2/3/4 gốc bị copy-paste lệch một bước (đã sửa đúng theo bước tương ứng).

#### Quản trị danh mục hãng bay và đối tác nhà cung ứng

**Tác nhân:** Đối tác (hãng bay/nhà cung ứng), Đội Phát triển Đối tác (BD), Đội Pháp lý & Tuân thủ, Đội Kỹ thuật, Đội Vận hành Sản phẩm Du lịch.

**Mô tả các bước:** quy trình gồm 2 quy trình con có quan hệ vòng đời bổ sung nhau:

- **Quy trình con 1 — Thẩm định & Onboarding đối tác mới:** đối tác tiềm năng gửi hồ sơ đề xuất hợp tác (giấy phép kinh doanh vận tải/lữ hành, năng lực cung ứng, năng lực kỹ thuật, chính sách giá) cho Đội BD. BD đánh giá sơ bộ (mức độ phù hợp chiến lược, thị phần, chất lượng dịch vụ, uy tín) — không đạt thì lưu hồ sơ và kết thúc; đạt thì chuyển Đội Pháp lý & Tuân thủ thẩm định (giấy phép, tư cách pháp nhân, AML/KYB) — không đạt thì lưu hồ sơ và kết thúc; đạt thì BD đàm phán và ký thỏa thuận hợp tác (hoa hồng, SLA, chính sách hoàn/hủy). Đội Kỹ thuật tích hợp API (tra cứu giá, đặt chỗ, thanh toán, xuất vé) và kiểm thử UAT — chưa đạt thì phối hợp khắc phục và kiểm thử lại (có thể lặp nhiều vòng); đạt thì Đội Vận hành cấu hình đối tác vào danh mục, chạy pilot nội bộ, rồi go-live chính thức và giám sát KPI/SLA sau ra mắt.
- **Quy trình con 2 — Rà soát, cập nhật và loại bỏ đối tác:** giám sát định kỳ hiệu suất đối tác đã onboarding (tỷ lệ đặt chỗ thành công, thời gian phản hồi API, tỷ lệ khiếu nại/1000 giao dịch), xử lý các trường hợp không đạt SLA bằng kế hoạch hành động khắc phục (CAP), và loại bỏ đối tác vi phạm nghiêm trọng hoặc không cải thiện sau CAP khỏi danh mục.

**Đối tượng khách hàng:** Đội Vận hành Sản phẩm Du lịch (khách hàng nội bộ trực tiếp, tiếp nhận đối tác đã qua duyệt để vận hành danh mục); người dùng cuối MoMo (khách hàng gián tiếp, hưởng lợi từ danh mục hãng bay/đối tác chất lượng).

**Kết quả:** *Onboarding thành công* — đối tác được duyệt, tích hợp, go-live. *Bị từ chối* — ở vòng đánh giá sơ bộ hoặc thẩm định pháp lý, hồ sơ lưu lại xem xét sau. *Rà soát: Đạt, tiếp tục hợp tác / Yêu cầu CAP / Chấm dứt hợp tác.*

*(Nguồn: `25410237/MoMo_Quan_tri_danh_muc_hang_bay_va_doi_tac_cung_ung.docx` — thay thế bản 1 dòng trước đây trong `docs/MoMo.docx`.)*

#### Quản trị rủi ro giao dịch, điều khoản và chất lượng dịch vụ

**Tác nhân:** Khách hàng, Bộ phận CSKH, Bộ phận Tài chính-Kế toán, Hãng bay/NCC.

**Mô tả các bước** *(phần "tra soát giao dịch lỗi/treo" — góc độ "điều khoản và chất lượng dịch vụ (SLA)" hiện chưa có nguyên liệu, cần nhóm bổ sung trước khi nộp)*:

1. **Khách hàng phát hiện và báo cáo giao dịch bất thường.** *Mục tiêu:* ghi nhận kịp thời các trường hợp trừ tiền nhưng chưa xuất vé, giao dịch treo (pending) kéo dài, hoặc sai lệch thông tin thanh toán. Khách hàng liên hệ CSKH qua hotline/app, cung cấp mã giao dịch/mã đặt chỗ liên quan.
2. **CSKH tra soát giao dịch.** *Mục tiêu:* xác minh trạng thái thực tế của giao dịch giữa hệ thống MoMo, cổng thanh toán và hệ thống hãng bay. CSKH tiếp nhận yêu cầu tra soát, đối chiếu dữ liệu giao dịch nội bộ với xác nhận từ hãng bay/đối tác — nếu **có xác nhận khớp** (giao dịch thực tế đã thành công phía hãng), cập nhật lại trạng thái vé cho khách hàng; nếu **không khớp/hãng chưa xác nhận**, chuyển sang quy trình xử lý ngoại lệ (rollback/hoàn tiền hoặc chờ xác nhận thêm từ hãng, có thể kéo dài do phụ thuộc phản hồi bên ngoài).
3. **Xử lý kết quả tra soát.** *Mục tiêu:* khôi phục quyền lợi tài chính hợp lý cho khách hàng. Nếu xác định lỗi thuộc về hệ thống/quy trình MoMo, Bộ phận Tài chính-Kế toán thực hiện hoàn tiền 100% về ví MoMo của khách hàng; nếu giao dịch thực tế đã thành công, cập nhật lại trạng thái vé/dịch vụ và thông báo cho khách hàng.

**Đối tượng khách hàng:** Khách hàng có giao dịch bị lỗi/treo trong quá trình đặt vé, mua dịch vụ hoặc đổi vé.

**Kết quả:** *Giao dịch được khôi phục đúng trạng thái* (vé/dịch vụ hiển thị đúng) hoặc *Hoàn tiền thành công* (nếu xác định lỗi hệ thống). *Chưa giải quyết* — vẫn đang chờ xác nhận từ hãng bay/đối tác bên ngoài (thuộc nhóm lãng phí Hold, nằm ngoài tầm kiểm soát trực tiếp của MoMo).

*(Nguồn: `25410237/MoMo_HauMai_va_XuLyNgoaiLe.docx`, phần tra soát giao dịch lỗi/treo. **Còn thiếu:** SLA/thời gian phản hồi cam kết cụ thể và các điều khoản dịch vụ liên quan — nhóm cần bổ sung trước khi nộp, xem `plan/01` mục 4 phần 🔵.)*

### 2.2.2. Quy trình cốt lõi (Core Process)

#### Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Bộ phận CSKH, Hãng bay/NCC.

**Mô tả các bước:**

1. **Khách hàng nhập và chọn chuyến bay.** *Mục tiêu:* ghi nhận chính xác nhu cầu di chuyển và dịch vụ bổ sung mong muốn. Khách hàng truy cập App MoMo, mục vé máy bay, nhập thông tin tìm kiếm; App hiển thị danh sách chuyến bay/hãng bay. Khách hàng chọn hành trình (khứ hồi: chọn chuyến đi và về; một chiều: chọn chuyến 1 chiều), chọn hạng vé, nhập thông tin khách hàng. Hệ thống phân loại nội địa/quốc tế: **Quốc tế** — chuyển thẳng đến mua bảo hiểm và xác nhận; **Nội địa** — có thể nhập thẻ khách hàng thường xuyên (Vietjet Air), tùy chọn chỗ ngồi/suất ăn/hành lý ký gửi/bảo hiểm du lịch toàn diện (mỗi dịch vụ có nhánh Có/Không riêng).
2. **Ứng dụng thực hiện giữ chỗ tạm thời.** *Mục tiêu:* khóa tạm thời chuyến bay và tiện ích đã chọn, tránh bị mua mất trong lúc khách hàng thanh toán. App hiển thị chi tiết đơn hàng, tạo booking/tạm giữ chỗ. Hệ thống kiểm tra còn thời gian giữ vé — **hết** thì quay lại danh sách chuyến bay để khách thao tác lại; **còn** thì cho phép tiếp tục thanh toán.
3. **Thực hiện thanh toán và hoàn tất giao dịch.** *Mục tiêu:* khách hàng xác nhận đơn và hệ thống xử lý giao dịch tài chính. Khách hàng xác nhận và thanh toán; App xử lý thanh toán và phân luồng theo kết quả: **Thất bại** — thông báo và kết thúc mua vé thất bại; **Thành công** — gửi yêu cầu xuất vé/xác nhận booking đến M_Service (sang Bước 4); **Pending (Treo)** — tạo ticket, chuyển CSKH xử lý ngoại lệ.
4. **Hệ thống trừ tiền và xuất vé.** *Mục tiêu:* xử lý triệt để giao dịch Pending (nếu có), phát hành vé từ hãng và cập nhật dữ liệu vé. Với giao dịch Pending: CSKH tiếp nhận, phân cấp hỗ trợ 24/7 (VIP) hoặc giờ hành chính (thường), liên hệ khách hàng xem còn nhu cầu mua vé — **không còn nhu cầu** thì hỗ trợ hủy đặt vé, rollback tiền, đóng ticket; **còn nhu cầu** thì gửi yêu cầu kiểm tra vé sang hãng bay — vé **đã có** trên hệ thống hãng thì CSKH xuất vé thủ công và chuyển trạng thái thành công; vé **chưa có** thì CSKH giữ vé cho khách, liên hệ hãng xuất vé, nhận mã đặt chỗ/vé điện tử rồi đóng ticket. Từ luồng thành công (trực tiếp hoặc qua xử lý Pending), M_Service cập nhật vé vào hệ thống và cập nhật trạng thái giao dịch thành công.
5. **Trả vé điện tử về cho khách hàng.** *Mục tiêu:* cung cấp chứng từ chuyến bay hợp lệ để khách hàng làm thủ tục tại sân bay. Sau khi M_Service hoàn tất, hệ thống gửi thông báo kết quả cuối cùng; khách hàng nhận thông báo xuất vé thành công trên thiết bị cá nhân. Kết thúc: Mua vé thành công.

**Đối tượng khách hàng:** Hành khách có nhu cầu đặt vé máy bay.

**Kết quả:** *Thành công* — thanh toán hoàn tất, hãng bay trả mã đặt chỗ, vé điện tử được gửi thành công. *Thất bại/Hủy giao dịch* — thanh toán lỗi, hoặc đơn hàng treo (Pending) mà khách hàng không còn nhu cầu và yêu cầu hủy để hoàn tiền (rollback).

*(Nguồn hợp nhất: `docs/MoMo.docx` + 3 báo cáo `25410206/MoMo_Core01/02/03...docx` — cùng phạm vi, đã gộp thành 1 mô tả thống nhất khớp với 8 bước hiện có trong báo cáo chính.)*

#### Mua thêm dịch vụ sau đặt chỗ

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Hãng bay, Nhân viên CSKH.

**Mô tả các bước:**

1. **Tiếp nhận yêu cầu và truy cập thông tin vé.** *Mục tiêu:* xác định đúng đơn hàng/vé cần mua thêm dịch vụ. Khách hàng chọn hình thức liên hệ **Qua App** hoặc **Qua CSKH**. Qua App: truy cập App, chọn vé đã mua — nếu vé Quốc tế, App hiển thị thông báo liên hệ CSKH. Qua CSKH: khách gọi tổng đài, CSKH tiếp nhận, thu thập thông tin và kiểm tra vé — vé không hợp lệ thì thông báo và kết thúc; vé Nội địa thì CSKH hướng dẫn khách tự thao tác trên App.
2. **Chọn mua thêm dịch vụ.** *Mục tiêu:* ghi nhận nhu cầu sử dụng tiện ích bổ sung. Qua App: khách tự chọn hành lý ký gửi (nếu Có → chọn số kg), chỗ ngồi (nếu Có → chọn vị trí), suất ăn (nếu Có → chọn loại). Qua CSKH: nhân viên kiểm tra dịch vụ/báo giá rồi thao tác chọn dịch vụ thay khách hàng.
3. **Gửi yêu cầu và thực hiện thanh toán.** *Mục tiêu:* hoàn tất nghĩa vụ tài chính cho dịch vụ phát sinh. Qua App: khách bấm xác nhận và thanh toán trực tiếp. Qua CSKH: CSKH gửi yêu cầu thanh toán về App của khách, khách kiểm tra và xác nhận thanh toán.
4. **Xử lý giao dịch và đồng bộ với hãng bay.** *Mục tiêu:* ghi nhận trạng thái thanh toán và gửi lệnh xuất dịch vụ sang hãng bay. App xử lý thanh toán, rẽ nhánh theo kết quả: **Thất bại** — thông báo và kết thúc "Mua thêm dịch vụ không thành công"; **Thành công** — M_Service cập nhật dịch vụ mua vào dữ liệu vé, đẩy lệnh sang Hãng bay/NCC; hãng tiếp nhận và trả kết quả đặt thêm dịch vụ.
5. **Gửi thông báo và hiển thị dịch vụ đã mua.** *Mục tiêu:* cập nhật vé điện tử và thông báo kết quả cuối cùng. Sau khi lưu trữ dữ liệu và nhận kết quả từ hãng, hệ thống gửi thông báo cho khách hàng; dịch vụ bổ sung hiển thị trực tiếp trên vé điện tử. Kết thúc: Dịch vụ đã được đặt.

**Đối tượng khách hàng:** Hành khách đã có mã đặt chỗ hợp lệ.

**Kết quả:** *Thành công* — thanh toán hoàn tất, hãng bay chấp nhận, dịch vụ bổ sung được cập nhật vào vé điện tử. *Thất bại* — mã vé không tồn tại/không hợp lệ, giao dịch thanh toán lỗi, hoặc hãng bay từ chối cung cấp thêm dịch vụ.

> ⚠️ Sửa lỗi so với bản gốc (`plan/01` mục 2.5): nhánh gateway đầu tiên trước đây gán sẵn nhãn "(Vé Nội địa)"/"(Vé Quốc tế)" cho lựa chọn kênh liên hệ, rồi lại kiểm tra ra loại vé khác — mâu thuẫn logic. Đã sửa nhãn gateway đầu thành **"Qua App"/"Qua CSKH"**, việc phân loại nội địa/quốc tế được xử lý ở bước kiểm tra kế tiếp.

#### Đổi chuyến bay

**Tác nhân:** Khách hàng, Giao diện MoMo Client App, Backend MoMo Travel, Cổng Thanh toán MoMo, Bộ phận CSKH MoMo Travel, Hệ thống Hãng bay (CRS/GDS).

**Mô tả các bước:**

1. **Khởi tạo yêu cầu đổi chuyến bay.** *Mục tiêu:* ghi nhận đúng vé và nhu cầu thay đổi của khách hàng. Khách hàng vào mục "Quản lý đặt chỗ", chọn vé cần đổi, nhấn "Đổi chuyến bay". Hệ thống kiểm tra điều kiện vé cơ bản (một số hạng vé Tiết kiệm/Economy Saver có thể không cho đổi hoặc chỉ cho đổi trước giờ bay 24h). Khách hàng chọn thông số muốn đổi: ngày bay, giờ bay, hoặc hành trình.
2. **Tìm kiếm lịch bay mới và truy xuất giá vé.** *Mục tiêu:* cung cấp lựa chọn chuyến bay mới phù hợp. Backend gửi yêu cầu tìm kiếm sang GDS/CRS của hãng bay; hãng trả về danh sách chuyến bay còn chỗ kèm giá chênh lệch ước tính. Khách hàng chọn chuyến bay/giờ bay mới.
3. **Tính toán chi tiết cấu trúc phí đổi.** *Mục tiêu:* xác định chính xác tổng số tiền khách hàng phải trả thêm. Công thức: **Tổng phí đổi = Phí đổi cố định của Hãng + Chênh lệch giá vé (giá mới − giá cũ, nếu dương) + Phí dịch vụ MoMo.** Nếu giá vé mới thấp hơn giá cũ, phần chênh lệch âm không được hoàn lại theo quy định phổ biến của các hãng nội địa. Hệ thống kiểm tra: **đổi tự động được qua API?** — **Không** (một số hạng vé quốc tế/vé khuyến mãi đặc biệt không hỗ trợ tính phí tự động) thì tạo Support Ticket chuyển sang CSKH; nhân viên CSKH liên hệ hãng bay kiểm tra phí thủ công, gửi link thanh toán cho khách, sau khi khách thanh toán xong sẽ thao tác tái xuất vé. **Có** thì tiếp tục bước 4 trực tiếp.
4. **Xác nhận chi tiết chi phí và chấp nhận điều kiện đổi.** *Mục tiêu:* đảm bảo khách hàng đồng thuận trước khi trích tiền. Ứng dụng hiển thị bảng phân rã chi phí đổi vé; khách hàng đọc và tick "Tôi đã đọc, hiểu và đồng ý với Điều kiện thay đổi vé", nhấn "Thanh toán phí đổi".
5. **Thanh toán phí chênh lệch đổi chuyến.** *Mục tiêu:* hoàn tất nghĩa vụ tài chính cho khoản phí đổi. Cổng thanh toán MoMo xử lý xác nhận thanh toán, khách hàng chọn nguồn tiền, xác thực bảo mật (mật khẩu/OTP/sinh trắc học).
6. **Tái phát hành vé và cập nhật PNR.** *Mục tiêu:* hoàn tất việc đổi chuyến trên hệ thống hãng bay. Backend gửi lệnh tái phát hành (Re-issue) kèm mã hạch toán sang hãng bay. Hệ thống kiểm tra **Re-issue thành công?** — **Hết chỗ chuyến mới** (khách khác đã mua mất ghế trong lúc thanh toán) thì hủy giao dịch thanh toán phí đổi, hoàn trả 100% phí vừa trích về ví MoMo, giữ nguyên vé cũ, thông báo khách chọn lại chuyến khác; **thành công** thì hãng hủy chỗ chuyến cũ, xác nhận chỗ chuyến mới, thu hồi vé điện tử cũ, cấp vé điện tử mới. App cập nhật lại "Quản lý đặt chỗ", thông báo đổi vé thành công, gửi email/SMS xác nhận hành trình mới.

**Đối tượng khách hàng:** Hành khách đã có vé hợp lệ, có nhu cầu thay đổi lịch trình bay.

**Kết quả:** *Thành công* — vé điện tử mới được cấp dưới cùng/mới mã PNR. *Hủy đổi vé, giữ vé cũ* — hết chỗ trên chuyến mới khi đang trích tiền, hoàn 100% phí đổi. *Xử lý thủ công qua CSKH* — với hạng vé không hỗ trợ tính phí tự động.

*(Nguồn: `25410223/cstt.md` Chương 3 — quy trình duy nhất có nguyên liệu cho mảng này; đây là quy trình đang **trống 100%** trong `docs/MoMo.docx`.)*

### 2.2.3. Quy trình hỗ trợ (Support Process)

#### Hỗ trợ khách hàng và tiếp nhận phản hồi

**Tác nhân:** Khách hàng, Bộ phận CSKH, Hãng bay/Nhà cung cấp.

**Mô tả các bước:**

1. **Khách báo sự cố.** *Mục tiêu:* ghi nhận kịp thời vấn đề/yêu cầu hỗ trợ. Khách hàng liên hệ qua tổng đài hoặc App MoMo; nếu qua App, hệ thống xác thực kiểm tra thông tin.
2. **CSKH tiếp nhận và xác minh.** *Mục tiêu:* ghi nhận thông tin cơ bản, tạo luồng xử lý, phân bổ đúng nhóm nghiệp vụ. CSKH thu thập thông tin, ghi nhận yêu cầu và tạo ticket (lưu vào Dữ liệu hỗ trợ KH), phân loại vấn đề ban đầu và phân công nhóm xử lý. Kiểm tra khách VIP hay thường: VIP → kênh chăm sóc VIP; thường → kênh chăm sóc tiêu chuẩn.
3. **Phân loại lỗi hoặc yêu cầu.** *Mục tiêu:* phân tích chi tiết sự cố để chuẩn bị phương án xử lý. CSKH phân tích yêu cầu — nếu **không đủ thông tin**, yêu cầu khách bổ sung (quay lại phân tích); nếu **đủ thông tin**, xử lý yêu cầu.
4. **Xử lý trực tiếp hoặc chuyển cho bên liên quan.** *Mục tiêu:* giải quyết theo thẩm quyền MoMo hoặc phối hợp đối tác. Đánh giá vấn đề thuộc phạm vi MoMo hay Hãng bay/NCC — **thuộc MoMo** thì CSKH trực tiếp cung cấp hướng dẫn/giải pháp; **thuộc Hãng bay/NCC** thì gửi yêu cầu sang hãng, hãng kiểm tra và xử lý theo chính sách, chấp nhận hoặc từ chối (kèm lý do), CSKH nhận kết quả và ghi nhận vào Dữ liệu hỗ trợ KH.
5. **Phản hồi kết quả cho khách hàng.** *Mục tiêu:* truyền đạt hướng giải quyết cuối cùng và đóng ticket. Tùy hình thức phản hồi: **SMS trên App** — CSKH gửi thông báo qua app, kết thúc "Hoàn tất hỗ trợ"; **Liên hệ trực tiếp** — khách nhận thông báo, nếu **chấp nhận** hướng giải quyết thì CSKH xác nhận hoàn tất, đóng ticket, kết thúc; nếu **không chấp nhận** thì CSKH hướng dẫn khách khiếu nại tiếp theo, đóng ticket, kết thúc.

Ngoài ra, một nhánh nghiệp vụ liên quan trực tiếp là **tra soát giao dịch lỗi/treo** (xem chi tiết ở mục "Quản trị rủi ro giao dịch" phía trên): khi khách hàng phản ánh giao dịch bị trừ tiền nhưng chưa nhận vé/dịch vụ, CSKH phối hợp cùng Bộ phận Tài chính-Kế toán xác minh với hãng bay/đối tác trước khi quyết định cập nhật trạng thái hoặc hoàn tiền.

**Đối tượng khách hàng:** Người dùng gặp sự cố với dịch vụ trên MoMo.

**Kết quả:** *Thành công (đóng ticket)* — sự cố được giải quyết dứt điểm, khách hàng đồng ý phương án xử lý. *Bị từ chối* — hãng bay/NCC từ chối hỗ trợ (kèm lý do). *Không đạt thỏa thuận* — khách không chấp nhận hướng giải quyết, chuyển sang khiếu nại chuyên sâu.

#### Xuất hóa đơn

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Bộ phận CSKH, Bộ phận Kế toán, Hệ thống VACOM.

**Mô tả các bước:**

1. **Khách hàng chọn xuất VAT / Liên hệ CSKH.** *Mục tiêu:* khởi tạo yêu cầu xuất hóa đơn GTGT cho giao dịch đã mua. Qua App: khách truy cập mục Xuất hóa đơn trong chi tiết vé; hệ thống kiểm tra giao dịch đã yêu cầu xuất hóa đơn chưa — **đã yêu cầu** thì hiển thị thông tin hóa đơn đã xuất, kết thúc; **chưa yêu cầu** thì chuyển sang form nhập liệu. Qua CSKH: khách gọi tổng đài, CSKH lấy thông tin yêu cầu.
2. **Nhập thông tin vào form / CSKH thu thập thông tin.** *Mục tiêu:* ghi nhận đầy đủ thông tin xuất hóa đơn. Qua App: khách nhập form, hệ thống kiểm tra dữ liệu — **không hợp lệ** thì yêu cầu nhập lại; **hợp lệ** thì chuyển sang kiểm tra điều kiện. Qua CSKH: CSKH thu thập và đẩy dữ liệu vào hệ thống.
3. **Kiểm tra điều kiện xuất VAT.** *Mục tiêu:* đảm bảo yêu cầu nằm trong thời hạn quy định. M_Service đối chiếu thời hạn 72 giờ (3 ngày) *(⚠️ số liệu chưa có nguồn xác thực, cần dẫn nguồn điều khoản MoMo/quy định thuế hoặc ghi rõ "giả định của nhóm" — xem `plan/01` mục 4 phần 🔵)* — **quá hạn** thì thông báo và kết thúc "Đã quá hạn xuất VAT"; **còn hạn** thì lấy dữ liệu giao dịch/vé/KH để đối soát.
4. **Kiểm tra, đối soát giao dịch.** *Mục tiêu:* đối chiếu tính chính xác giữa dữ liệu giao dịch và yêu cầu xuất hóa đơn. M_Service lấy song song thông tin vé/thanh toán và thông tin KH/hóa đơn, ghép dữ liệu để kiểm tra khớp — **không khớp** thì gửi CSKH kiểm tra/liên hệ khách xác nhận, cập nhật rồi đối chiếu lại; **khớp** thì tạo yêu cầu xuất hóa đơn, chuyển bộ phận kế toán.
5. **Gửi yêu cầu sang VACOM để phát hành hóa đơn điện tử.** *Mục tiêu:* truyền lệnh phát hành hóa đơn sang hệ thống đối tác VACOM *(⚠️ chưa có nguồn xác nhận MoMo dùng nhà cung cấp này — cần dẫn nguồn hoặc ghi rõ giả định)*. Kế toán gọi API tạo hóa đơn — VACOM tiếp nhận **thất bại** thì ghi lỗi, gửi lại hoặc chuyển Kỹ thuật; **thành công** thì VACOM xử lý và phát hành — phát sinh **thất bại** thì cập nhật lỗi, chuyển Kỹ thuật; **thành công** thì hóa đơn được phát hành, chuyển về MoMo.
6. **Trả kết quả và gửi hóa đơn điện tử về cho khách hàng.** *Mục tiêu:* cập nhật trạng thái và cung cấp hóa đơn điện tử cho người dùng. App nhận hóa đơn từ VACOM, đồng thời cập nhật vào Dữ liệu về VAT, cập nhật trạng thái trên App, gửi thông báo cho khách hàng. Khách hàng xem hóa đơn trên thiết bị. Kết thúc: Xuất VAT hoàn tất.

**Đối tượng khách hàng:** Khách hàng cần chứng từ thuế.

**Kết quả:** *Thành công* — dữ liệu đối soát khớp, VACOM phát hành hóa đơn thành công, gửi về App. *Từ chối/Lỗi hệ thống* — quá thời hạn quy định, dữ liệu đối soát không khớp, hoặc hệ thống VACOM lỗi kỹ thuật.

#### Quản lý vé đã mua

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Bộ phận CSKH, Hãng bay.

> ⚠️ Quy trình này **chưa có nguyên liệu từ bất kỳ thành viên nào**. Mô tả dưới đây là suy luận hợp lý của nhóm dựa trên tính năng "Quản lý đặt chỗ"/"Thông tin vé máy bay" đã được nhắc tới nhiều lần trong nguyên liệu của `25410223` và `25410237` (đây là điểm vào chung cho các quy trình "Mua thêm dịch vụ", "Đổi chuyến bay", "Xuất hóa đơn") — **không phải nguyên liệu thu thập/khảo sát thật**, cần nhóm xác nhận và bổ sung chi tiết trước khi nộp.

**Mô tả các bước:**

1. **Truy cập danh sách vé đã mua.** *Mục tiêu:* cho phép khách hàng xem lại toàn bộ vé/hành trình đã đặt. Khách hàng vào mục "Tôi" > "Quản lý đặt chỗ" (hoặc "Vé của tôi") trên App MoMo. Hệ thống truy xuất danh sách vé từ cơ sở dữ liệu vé theo tài khoản khách hàng, phân loại theo trạng thái: Sắp khởi hành / Đã hoàn thành / Đã hủy.
2. **Xem chi tiết vé/hành trình.** *Mục tiêu:* cung cấp đầy đủ thông tin chuyến bay, hành khách và các dịch vụ đã mua kèm. Khách hàng chọn 1 vé để xem chi tiết: mã đặt chỗ (PNR), thông tin hành khách, giờ bay, hạng vé, các dịch vụ bổ sung đã mua (hành lý, chỗ ngồi, suất ăn, bảo hiểm), trạng thái check-in.
3. **Điều hướng sang các tác vụ liên quan.** *Mục tiêu:* làm điểm vào tập trung cho các nhu cầu phát sinh trên vé đã mua. Từ màn hình chi tiết vé, khách hàng có thể chọn: "Mua thêm dịch vụ" (sang quy trình Mua thêm dịch vụ sau đặt chỗ), "Đổi chuyến bay" (sang quy trình Đổi chuyến bay), "Xuất hóa đơn" (sang quy trình Xuất hóa đơn), hoặc "Liên hệ hỗ trợ" (sang quy trình Hỗ trợ khách hàng) nếu gặp sự cố.
4. **Tải/chia sẻ vé điện tử.** *Mục tiêu:* cung cấp chứng từ hợp lệ để khách hàng sử dụng khi ra sân bay. Khách hàng có thể tải vé điện tử (PDF kèm mã QR check-in) hoặc chia sẻ cho người đi cùng qua các ứng dụng khác.

**Đối tượng khách hàng:** Hành khách đã hoàn tất đặt vé, có nhu cầu tra cứu hoặc quản lý vé/hành trình đã mua.

**Kết quả:** *Thành công* — khách hàng xem/tải được vé và điều hướng đúng sang tác vụ cần thực hiện. *Không có dữ liệu* — tài khoản chưa có vé nào đã đặt.



<!-- ===== Chuong3_BPMN.md ===== -->

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

**Phỏng vấn:** do đồ án không có điều kiện phỏng vấn trực tiếp nhân sự nội bộ M_Service, nhóm xây dựng bộ câu hỏi khảo sát dưới đây theo hình thức mô phỏng/giả định — dựa trên nghiên cứu quy trình công khai và suy luận nghiệp vụ hợp lý về cách các bộ phận (Bộ phận về giá, Marketing, Tài chính/Pháp chế, Growth Specialist/Kỹ thuật, CSKH) vận hành. Các số liệu ở Chương 4 là giả định của nhóm, không phải số liệu thu thập thực tế.

*Câu hỏi định tính (10 câu = 5 có cấu trúc + 5 không cấu trúc):*

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Công đoạn nào trong quy trình thường phát sinh nhiều khó khăn và mất thời gian nhất? A. Chuẩn hóa dữ liệu giá, thuế, phí. B. Thiết kế cơ chế khuyến mãi. C. Thẩm định hồ sơ điều kiện/ngân sách. D. Cấu hình và kiểm thử hiển thị. | Tất cả các bộ phận tham gia | Xác định điểm nghẽn (bottleneck) |
| 2 | Có cấu trúc | Khi dữ liệu giá/thuế/phí từ Hãng bay/NCC bị thiếu sót, xử lý theo phương án nào? A. Trả lại yêu cầu gửi lại toàn bộ. B. Phối hợp bổ sung phần thiếu. C. Tự bổ sung dựa trên dữ liệu cũ. D. Báo cáo cấp trên. | Bộ phận về giá | Đánh giá xử lý ngoại lệ đầu vào |
| 3 | Có cấu trúc | Nguyên nhân phổ biến nhất khiến hồ sơ khuyến mãi bị từ chối là gì? A. Vượt ngân sách. B. Thiếu chứng từ hợp lệ. C. Điều kiện áp dụng rủi ro pháp lý. D. Sai đối tượng mục tiêu. | Bộ phận Tài chính/Pháp chế | Đánh giá rủi ro pháp lý/tài chính |
| 4 | Có cấu trúc | Khi cấu hình hệ thống, khó khăn lớn nhất là gì? A. Cơ chế KM phức tạp. B. SLA cấu hình quá gấp. C. Lỗi backend. D. Bàn giao không rõ ràng. | Growth Specialist/Kỹ thuật | Đánh giá độ phức tạp thiết lập |
| 5 | Có cấu trúc | Bước kiểm thử hiển thị hiện chủ yếu theo hình thức nào? A. Tự động 100%. B. Thủ công là chính. C. Kết hợp. D. Bỏ qua nếu gấp. | Kỹ thuật, Marketing | Mức độ ứng dụng công nghệ QA |
| 6 | Không cấu trúc | Tiêu chuẩn nào đang dùng để chuẩn hóa dữ liệu giá/thuế/phí, có thể tự động hóa thêm không? | Bộ phận về giá | Tiềm năng tự động hóa |
| 7 | Không cấu trúc | Khi phát hiện lỗi hiển thị giá/KM, quy trình yêu cầu chỉnh sửa diễn ra thế nào, tốn bao lâu? | Kỹ thuật, Marketing | Xử lý sự cố trước Go-live |
| 8 | Không cấu trúc | Để rút ngắn time-to-market, nên ưu tiên loại bỏ/thay đổi bước nào? | Tất cả các bộ phận tham gia | Ý kiến cải tiến từ người thực hiện |
| 9 | Không cấu trúc | Sự phối hợp giữa Marketing và Tài chính/Pháp chế ở khâu thẩm định hồ sơ KM hiện có điểm nào chưa ăn khớp, gây chậm trễ? | Marketing, Tài chính/Pháp chế | Điểm nghẽn phối hợp liên phòng ban |
| 10 | Không cấu trúc | Rủi ro lớn nhất là gì nếu quy trình duyệt giá/KM bị rút ngắn quá mức để kịp một chiến dịch gấp? | Tất cả các bộ phận tham gia | Đánh đổi tốc độ – kiểm soát rủi ro |

*Câu hỏi định lượng (10 câu = 5 có cấu trúc + 5 không cấu trúc — viết lại hoàn toàn, thay bảng cũ đang copy y hệt bảng định tính):*

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Trung bình mất bao nhiêu giờ để chuẩn hóa xong 1 bộ dữ liệu giá? A. ≤2h. B. 2–4h. C. 4–8h. D. >8h. | Bộ phận về giá | Thời gian xử lý chuẩn hóa |
| 2 | Có cấu trúc | Trung bình 1 tuần tiếp nhận bao nhiêu bộ dữ liệu giá từ Hãng bay/NCC? A. <5. B. 5–10. C. 11–20. D. >20. | Bộ phận về giá | Khối lượng công việc đầu vào |
| 3 | Có cấu trúc | Bao nhiêu % hồ sơ KM bị Tài chính/Pháp chế từ chối ở lần trình đầu? A. <10%. B. 10–25%. C. 26–50%. D. >50%. | Bộ phận Tài chính/Pháp chế | Tỷ lệ rework thẩm định |
| 4 | Có cấu trúc | Thời gian trung bình từ nhận hồ sơ đến khi ra quyết định phê duyệt? A. <1 ngày. B. 1–2 ngày. C. 3–5 ngày. D. >5 ngày. | Bộ phận Tài chính/Pháp chế | Đầu vào tính cycle time |
| 5 | Có cấu trúc | Trung bình cần bao nhiêu lần cấu hình lại (rework) cho 1 chiến dịch KM? A. 0. B. 1. C. 2. D. ≥3. | Growth Specialist/Kỹ thuật | Đầu vào công thức T/(1-r) |
| 6 | Không cấu trúc | Trung bình 1 lượt kiểm thử hiển thị giá/KM mất bao nhiêu phút? | Kỹ thuật, Marketing | Thời gian kiểm thử |
| 7 | Không cấu trúc | Mỗi tháng phát sinh khoảng bao nhiêu ticket khiếu nại liên quan sai giá/sai KM? | CSKH | Chỉ số chất lượng đầu ra |
| 8 | Không cấu trúc | Tổng thời gian chu kỳ trung bình từ nhận dữ liệu đến công bố là bao lâu? | Tất cả các bộ phận tham gia | Cycle time tổng — đầu vào Chương 4 |
| 9 | Không cấu trúc | Trung bình cần bao nhiêu nhân sự và giờ công để hoàn tất 1 lần chạy toàn bộ quy trình? | Tất cả các bộ phận tham gia | Chi phí nhân sự — đầu vào Chương 4 |
| 10 | Không cấu trúc | Bao nhiêu % bộ dữ liệu giá bị trả lại yêu cầu bổ sung ngay lần gửi đầu? | Bộ phận về giá | Tỷ lệ lỗi đầu vào |

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



<!-- ===== Chuong4_PhanTich.md ===== -->

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



<!-- ===== Chuong5_KetLuan.md ===== -->

# Chương 5: KẾT LUẬN

> Bản nháp tổng hợp (không copy nguyên xi) từ mục Kết luận có sẵn trong 3 báo cáo con chất lượng cao: `25410206/MoMo_Core01_TimKiem_va_SoSanhChuyenBay.docx` (Chương 9), `25410237/MoMo_HauMai_va_XuLyNgoaiLe.docx` (Chương 8), `25410237/MoMo_Quan_tri_danh_muc_hang_bay_va_doi_tac_cung_ung.docx` (Chương 8). Đây là chương hiện đang **TRỐNG 100%**, là dòng cuối cùng của `docs/MoMo.docx` (xem `plan/01_HIEN_TRANG_VA_LOI.md` mục 3). Số liệu cụ thể được giữ lại làm minh họa/dẫn chứng cho lập luận, không phải để copy nguyên bảng.

---

## 5.1. Kết quả đạt được

Đồ án đã xây dựng sơ đồ kiến trúc quy trình nghiệp vụ mảng đặt vé máy bay trên MoMo theo 3 nhóm Quản lý – Cốt lõi – Hỗ trợ (10 quy trình), trong đó mô hình hóa chi tiết bằng BPMN cho 6 quy trình đại diện (2 Quản lý: Quản trị giá – khuyến mãi, Quản trị danh mục hãng bay và đối tác NCC; 2 Cốt lõi: Tìm kiếm – lựa chọn hành trình – thanh toán và xác nhận đặt vé, Đổi chuyến bay; 2 Hỗ trợ: Hỗ trợ khách hàng và tiếp nhận phản hồi, Xuất hóa đơn), và phân tích sâu theo hai lăng kính định tính – định lượng cho 3 trong số 6 quy trình đó (Tìm kiếm..., Hỗ trợ khách hàng..., Quản trị giá...).

Kết quả phân tích ở các quy trình đã hoàn thiện cho thấy một số mẫu hình chung, lặp lại xuyên suốt nhiều quy trình khác nhau của mảng đặt vé máy bay:

- **Giá trị gia tăng tập trung ở khâu xử lý dữ liệu và ra quyết định**, trong khi phần lớn hoạt động không tạo giá trị (NVA) đều là các bước sửa lỗi/rework có thể loại bỏ bằng thiết kế lại quy trình hoặc bổ sung kiểm soát chất lượng đầu vào — ví dụ quy trình Tìm kiếm & so sánh chuyến bay ghi nhận 5 hoạt động VA, 8 hoạt động BVA và 3 hoạt động NVA đều thuộc dạng sửa lỗi.
- **Lãng phí chủ yếu thuộc hai nhóm Hold và Overdo.** Nhóm Hold — thời gian chờ phản hồi/xác minh từ hãng bay hoặc đối tác bên ngoài — xuất hiện lặp lại ở cả quy trình hậu mãi (thời gian chờ xác minh giao dịch lỗi) lẫn quy trình quản trị đối tác (thời gian chờ đối tác phản hồi kế hoạch khắc phục, tối đa 30 ngày). Đây là dạng lãng phí nằm ngoài tầm kiểm soát trực tiếp của MoMo, khác với nhóm Overdo (áp dụng quy trình kiểm soát/thẩm định đầy đủ cho cả những trường hợp đã có tiền lệ xử lý) — vốn hoàn toàn có thể cải thiện bằng nội lực.
- **Hiệu suất thời gian (process time / cycle time) chênh lệch lớn giữa các quy trình phụ thuộc mức độ lệ thuộc vào bên ngoài**: quy trình Tìm kiếm & so sánh chuyến bay (chủ yếu xử lý nội bộ, gọi API song song) đạt hiệu suất thời gian khoảng 95,9%; trong khi các quy trình có bước chờ đối tác phản hồi (tra soát giao dịch lỗi, rà soát đối tác) chỉ đạt hiệu suất khoảng 43–69%. Điều này cho thấy nút thắt lớn nhất của hệ thống không nằm ở năng lực xử lý nội bộ của MoMo mà ở sự phối hợp và tốc độ phản hồi của các đối tác/hãng bay bên ngoài.
- **Nguyên nhân gốc rễ được xác định qua phân tích Pareto và sơ đồ xương cá** đều quy về một số nhóm lặp lại: thiếu chuẩn hóa/tự động hóa trong trao đổi dữ liệu với đối tác, thiếu SLA nội bộ rõ ràng, và hạn chế trong hệ thống đo lường/giám sát vận hành theo thời gian thực.

## 5.2. Hạn chế của đồ án

- Do không tiếp cận được dữ liệu vận hành nội bộ thực tế và không có điều kiện phỏng vấn trực tiếp nhân sự của M_Service, **toàn bộ số liệu định lượng trong báo cáo là số liệu minh họa/giả định của nhóm**, được xây dựng dựa trên bằng chứng gián tiếp (trải nghiệm sử dụng ứng dụng thực tế, tài liệu hướng dẫn công khai của MoMo, quy định của Ngân hàng Nhà nước, và đối chiếu thông lệ ngành thương mại điện tử/OTA) thay vì số liệu vận hành chính thức.
- Mô hình BPMN phản ánh cách nhóm hiểu quy trình dựa trên bằng chứng công khai, có thể khác biệt so với thiết kế thực tế bên trong hệ thống của MoMo — đặc biệt ở các bước kỹ thuật nội bộ (cơ chế bộ đệm dữ liệu giá, cách điều phối truy vấn nhà cung ứng, logic xử lý ngoại lệ chi tiết).
- Tại thời điểm hoàn thiện báo cáo này, một số quy trình trong phạm vi 6 quy trình đầu tư sâu (Đổi chuyến bay, Xuất hóa đơn) vẫn đang trong quá trình hoàn thiện Phương pháp thực hiện — xem tình trạng cập nhật tại `plan/01_HIEN_TRANG_VA_LOI.md` mục 4.

## 5.3. Hướng phát triển

- Nếu có điều kiện tiếp cận phỏng vấn trực tiếp các đội ngũ vận hành liên quan (CSKH, Vận hành Sản phẩm Du lịch, Bộ phận về giá, Tài chính/Pháp chế) của MoMo, nhóm có thể hiệu chỉnh lại số liệu định lượng và mô hình BPMN cho sát với thực tế vận hành hơn, đồng thời xác thực các giả định đã đặt ra trong đồ án.
- Mở rộng phạm vi mô hình hóa và phân tích sâu sang các quy trình còn lại (Quản lý vé đã mua, Quản trị rủi ro giao dịch góc độ SLA/điều khoản) để có bức tranh đầy đủ hơn về toàn bộ mảng đặt vé máy bay.
- Ưu tiên triển khai các đề xuất cải tiến có chi phí thấp và nằm hoàn toàn trong tầm kiểm soát nội bộ của MoMo trước (bổ sung hệ thống đo lường hành vi người dùng, chuẩn hóa checklist/SLA nội bộ), sau đó mới đến các cải tiến phụ thuộc sự phối hợp của hãng bay/đối tác bên ngoài — vì đây là nhóm lãng phí (Hold) khó kiểm soát trực tiếp nhất theo phát hiện xuyên suốt đồ án.



<!-- ===== TaiLieuThamKhao.md ===== -->

# TÀI LIỆU THAM KHẢO

> Gộp và loại trùng từ trích dẫn thật có sẵn trong 4 nguồn: `25410206/MoMo_Core01...docx`, `25410237/MoMo_HauMai...docx`, `25410237/MoMo_Quan_tri_danh_muc...docx`, `25410237/MoMo_Kien_truc_quy_trinh...docx`. Định dạng theo kiểu số thứ tự trích dẫn trong ngoặc vuông `[n]`, dùng thống nhất trong toàn báo cáo.

**Nguồn chính thức từ MoMo**

1. MoMo. *5 cách đặt vé máy bay online siêu dễ!* https://www.momo.vn/blog/5-cach-dat-ve-may-bay-online-sieu-de-c116dt1194
2. MoMo. *Cách đặt vé máy bay nhanh chóng qua MoMo?* https://www.momo.vn/hoi-dap/cach-mua-ve-may-bay
3. MoMo. *Đặt vé máy bay trên MoMo với nhiều khuyến mãi hấp dẫn và mức giá rẻ nhất.* https://www.momo.vn/ve-may-bay
4. MoMo. *Bạn cần nhập những thông tin nào khi mua vé máy bay trên MoMo?* https://www.momo.vn/hoi-dap/ban-can-nhap-nhung-thong-tin-nao-khi-mua-ve-may-bay-tren-vi-momo
5. MoMo. *Có thể đặt được vé của những hãng bay nào trên MoMo?* https://www.momo.vn/hoi-dap/co-the-mua-ve-may-bay-cua-cac-hang-nao-tren-momo
6. MoMo. *Sau khi đặt vé thành công, vé của bạn sẽ được gửi qua đâu?* https://www.momo.vn/hoi-dap/sau-khi-dat-ve-thanh-cong-ve-cua-toi-se-duoc-gui-qua-dau
7. MoMo. *Tôi chưa nhận được Mã đặt chỗ.* https://www.momo.vn/hoi-dap/toi-chua-nhan-duoc-ma-dat-cho
8. MoMo. *Mua vé máy bay bằng Ví Trả Sau MoMo — Thanh toán linh hoạt.* https://www.momo.vn/vi-tra-sau/mua-ve-may-bay
9. MoMo. *Sinh trắc học — An toàn bảo mật.* https://www.momo.vn/hoi-dap/an-toan-bao-mat-ctgr8/sinh-trac-hoc
10. MoMo. *Tôi có thể hoàn hủy vé máy bay đã đặt được không?* https://www.momo.vn/hoi-dap/toi-co-the-hoan-huy-ve-may-bay-da-dat-duoc-khong
11. MoMo. *Cách hủy vé máy bay trên MoMo.* https://www.momo.vn/blog/cach-huy-ve-may-bay-tren-momo-c101dt768
12. MoMo. *Hạn mức giao dịch mỗi ngày?* https://www.momo.vn/hoi-dap/han-muc-giao-dich-moi-ngay
13. MoMo. *MoMo nâng cấp bảo mật theo Thông tư 77/2025/TT-NHNN.* https://www.momo.vn/tin-tuc/thong-bao/momo-nang-cap-bao-mat-theo-thong-tu-77-2025-tt-8510

**Báo chí / trang tin thứ ba**

14. Tinh tế. *Dùng thử tính năng "Du lịch – Đi lại" trên Ví MoMo.* https://tinhte.vn/thread/dung-thu-tinh-nang-du-lich-di-lai-tren-vi-momo.3235308/
15. Người Đô Thị. *MoMo ra mắt tính năng "Du lịch - Đi lại" giúp việc mua vé máy bay, vé tàu, xe khách cực dễ.* https://nguoidothi.net.vn/momo-ra-mat-tinh-nang-du-lich-di-lai-giup-viec-mua-ve-may-bay-ve-tau-xe-khach-cuc-de-26496.html
16. Điện Máy Chợ Lớn. *Hướng dẫn cách đặt vé máy bay Vietnam Airlines bằng MoMo.* https://dienmaycholon.com/kinh-nghiem-mua-sam/huong-dan-cach-dat-ve-may-bay-vietnam-airlines-bang-momo-don-gian-de-thuc-hien
17. Thế Giới Di Động. *Cách đặt mua vé máy bay Vietnam Airlines thông qua MoMo cực kỳ tiện lợi.* https://www.thegioididong.com/game-app/cach-dat-mua-ve-may-bay-vietnam-airlines-thong-qua-momo-cuc-ky-tien-loi-1259463
18. Thanh Niên. *MoMo thêm tính năng mua vé tàu xe tết, trả tiền sau.* https://thanhnien.vn/momo-them-tinh-nang-mua-ve-tau-xe-tet-tra-tien-sau-1851414853.htm

**Văn bản pháp luật**

19. Ngân hàng Nhà nước Việt Nam. *Thông tư số 17/2024/TT-NHNN quy định việc mở và sử dụng tài khoản thanh toán tại tổ chức cung ứng dịch vụ thanh toán.*
20. Ngân hàng Nhà nước Việt Nam. *Thông tư số 23/2019/TT-NHNN sửa đổi, bổ sung một số điều của Thông tư số 39/2014/TT-NHNN hướng dẫn về dịch vụ trung gian thanh toán.*

**Tài liệu học thuật / khung lý thuyết**

21. Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of Business Process Management* (2nd ed.). Springer.
22. Object Management Group (OMG). (2013). *Business Process Model and Notation (BPMN), Version 2.0.2.*
23. Ishikawa, K. (1985). *Guide to Quality Control.* Asian Productivity Organization.
24. CellPhoneS. *Tìm hiểu hệ thống quy trình nghiệp vụ của công ty CellphoneS* (tài liệu tham khảo mẫu của giảng viên).

**Tài liệu nội bộ nhóm**

25. Nhóm 9 (IE203.F32.LT.CNTT) — UIT. *Phân tích và mô hình hóa quy trình mảng đặt vé máy bay trên nền tảng MoMo* (các tài liệu con: quản trị danh mục hãng bay và đối tác cung ứng; hoạt động hậu mãi và xử lý ngoại lệ; tìm kiếm — lựa chọn hành trình — thanh toán, 2026).

> ⚠️ Trước khi nộp, đối chiếu lại số thứ tự `[n]` trích dẫn trong thân bài (đặc biệt ở Chương 1, 2, 3) khớp đúng với danh sách này — phần trích dẫn trong thân bài mỗi chương hiện đang đánh số độc lập theo từng báo cáo con gốc, cần đánh số lại thống nhất khi ghép vào 1 file.



<!-- ===== DanhMucTuVietTat.md ===== -->

# DANH MỤC TỪ VIẾT TẮT

> Tổng hợp từ danh sách gốc ở `docs/REVIEW-MoMo.md` mục 3.7 + các thuật ngữ bổ sung xuất hiện trong nội dung đã hợp nhất ở `final/`. Khi ghép vào `docs/MoMo.docx`, dùng Word References → Insert Table of Figures kiểu "Danh mục từ viết tắt" hoặc chèn bảng tĩnh này ngay sau Danh mục bảng.

| Từ viết tắt | Tiếng Anh đầy đủ | Giải nghĩa |
|---|---|---|
| AML | Anti-Money Laundering | Phòng chống rửa tiền |
| API | Application Programming Interface | Giao diện lập trình ứng dụng |
| BD | Business Development | Phát triển kinh doanh/đối tác |
| BI | Business Intelligence | Phân tích dữ liệu kinh doanh |
| BPMN | Business Process Model and Notation | Ký hiệu và mô hình hóa quy trình nghiệp vụ |
| BPMS | Business Process Management System | Hệ thống quản trị quy trình nghiệp vụ |
| BPR | Business Process Reengineering | Tái thiết kế quy trình nghiệp vụ |
| BVA | Business Value Adding | Hoạt động tạo giá trị cho doanh nghiệp (không trực tiếp cho khách hàng) |
| CAP | Corrective Action Plan | Kế hoạch hành động khắc phục |
| CRM | Customer Relationship Management | Quản trị quan hệ khách hàng |
| CRS | Computer Reservation System | Hệ thống đặt giữ chỗ (hãng bay) |
| CSAT | Customer Satisfaction (Score) | Điểm khảo sát mức độ hài lòng khách hàng |
| CSKH | — | Chăm sóc khách hàng |
| DMS | Document Management System | Hệ thống quản lý tài liệu |
| eKYC | electronic Know Your Customer | Định danh khách hàng điện tử |
| EMD | Electronic Miscellaneous Document | Chứng từ phụ trợ điện tử (dịch vụ mua thêm) |
| ETL | Extract – Transform – Load | Trích xuất – biến đổi – nạp dữ liệu |
| GDS | Global Distribution System | Hệ thống phân phối toàn cầu (dữ liệu giá/chỗ ngồi nhiều hãng bay) |
| KM | Khuyến mãi | Chương trình ưu đãi/giảm giá |
| KPI | Key Performance Indicator | Chỉ số hiệu năng chính |
| KYB | Know Your Business | Xác minh thông tin pháp lý/năng lực tổ chức đối tác |
| NCC | — | Nhà cung cấp |
| NHNN | — | Ngân hàng Nhà nước Việt Nam |
| NVA | Non-Value Adding | Hoạt động không tạo giá trị |
| PCE | Process Cycle Efficiency | Hiệu suất chu kỳ quy trình (tỷ lệ thời gian tạo giá trị) |
| PNR | Passenger Name Record | Mã hồ sơ đặt chỗ hành khách |
| RTY | Rolled Throughput Yield | Tỷ lệ chất lượng xuyên suốt quy trình (không lỗi từ đầu đến cuối) |
| SLA | Service Level Agreement | Thỏa thuận mức cam kết dịch vụ |
| T&C | Terms & Conditions | Điều khoản và điều kiện áp dụng |
| UAT | User Acceptance Testing | Kiểm thử nghiệm thu người dùng |
| VA | Value Adding | Hoạt động tạo giá trị trực tiếp cho khách hàng |
| VAT | Value Added Tax | Thuế giá trị gia tăng |
| OTA | Online Travel Agency | Đại lý du lịch trực tuyến |



<!-- ===== BangPhanCong.md ===== -->

# BẢNG PHÂN CÔNG CÔNG VIỆC NHÓM

> Rubric 5.0 yêu cầu bắt buộc mục này. Ghi nhận đúng thực tế: nguyên liệu gốc do từng thành viên xây dựng qua các bài làm riêng (đã kiểm kê chi tiết ở `plan/02_NGUYEN_LIEU_THANH_VIEN.md`); bản báo cáo `BaoCao_Final` này là bản tổng hợp/biên tập cuối cùng do 1 thành viên thực hiện trực tiếp (có dùng công cụ AI hỗ trợ tổng hợp/biên tập) theo yêu cầu rút ngắn tiến độ của nhóm — không phải quá trình 8 người cùng chỉnh sửa như phân công dự kiến ban đầu ở `plan/04_PHAN_CONG_CONG_VIEC.md`.

| STT | MSSV | Họ tên | Vai trò | Đóng góp nguyên liệu gốc |
|---|---|---|---|---|
| 1 | 25410175 | Đinh Xuân Bảo | Nhóm trưởng | Giữ bản báo cáo chính, tự thực hiện review toàn diện (`docs/REVIEW-MoMo.md`) làm cơ sở cho toàn bộ kế hoạch hoàn thiện; 5 sơ đồ BPMN gốc (Quản trị giá, Quản lý hạng vé, Tìm kiếm..., Mua thêm dịch vụ, Xuất hóa đơn) |
| 2 | 25410167 | Vũ Thị Nhân Ái | Thành viên | Chưa có nguyên liệu riêng trong tài liệu thu thập được |
| 3 | 25410168 | Phạm Ngọc Bảo An | Thành viên | Bộ 20 câu hỏi phỏng vấn mẫu đạt chuẩn (Mục 3); khung Phân tích quy trình mẫu (Mục 4); đoạn Lịch sử hình thành công ty (Chương 1) |
| 4 | 25410191 | Hồ Nguyễn Bảo Duy | Thành viên | Có tên trong bảng phân công kế hoạch làm việc của `25410206` (khảo sát/phân tích nguyên nhân), nhưng không có thư mục bài làm riêng trong dự án — ⚠️ cần nhóm xác nhận lại đóng góp thực tế của thành viên này trước khi nộp |
| 5 | 25410195 | Nguyễn Huỳnh Mỹ Duyên | Thành viên | Chưa có nguyên liệu riêng ngoài bản khung dùng chung |
| 6 | 25410206 | Nguyễn Đắc Hiển | Thành viên | 3 báo cáo độc lập chất lượng cao nhất dự án (Tìm kiếm & so sánh; Lựa chọn hành trình & hãng bay; Thanh toán & xác nhận đặt vé) — đầy đủ Phương pháp thực hiện, BPMN, Phân tích định tính/định lượng, trích dẫn nguồn thật; chương Phân tích "Quản trị giá" (bị gắn nhầm tên, đã sửa lại ở bản Final) |
| 7 | 25410223 | Lê Quốc Hưng | Thành viên | Bộ 3 báo cáo súc tích + `cstt.md` mô tả chi tiết cho "Tìm kiếm...", "Mua thêm dịch vụ", "Đổi chuyến bay" — **nguồn DUY NHẤT** cho quy trình "Đổi chuyến bay", vốn trống hoàn toàn trong bản gốc |
| 8 | 25410237 | Nguyễn Mậu An Khương | Thành viên | 2 báo cáo 8 chương đầy đủ: "Hỗ trợ khách hàng & Xử lý ngoại lệ" và "Quản trị danh mục hãng bay và đối tác NCC" — giải quyết trực tiếp 2 khoảng trống lớn nhất của bản gốc; tài liệu tổng quan kiến trúc 13 quy trình |

## Việc tổng hợp bản Final (phiên hoàn thiện gấp rút, theo yêu cầu nhóm trưởng)

| Việc | Người thực hiện | Công cụ hỗ trợ |
|---|---|---|
| Rà soát toàn bộ 18 tài liệu + rubric + bài giảng + đồ án mẫu, lập kế hoạch chi tiết (`plan/00`–`plan/07`) | 1 thành viên (được nhóm ủy quyền) | Claude Code (AI) |
| Biên tập, hợp nhất và viết bổ sung nội dung còn thiếu vào `final/BaoCao_Final.md` | như trên | như trên |
| Sinh bản `.docx` từ nội dung đã biên tập | như trên | Script Python (`python-docx`) |
| Đối chiếu rubric, lập `final/DOI_CHIEU_RUBRIC.md` | như trên | như trên |

> ⚠️ **Trước khi nộp, cả nhóm cần**: (1) đọc lại toàn bộ `final/BaoCao_Final.md`, xác nhận nội dung đúng với hiểu biết thực tế của từng người về phần mình phụ trách; (2) làm rõ đóng góp thực tế của 25410191 (không có thư mục bài làm riêng trong dự án); (3) cân nhắc việc công khai quy trình dùng AI hỗ trợ tổng hợp với giảng viên theo đúng quy định môn học/nhà trường về liêm chính học thuật, nếu có yêu cầu.

