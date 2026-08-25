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

MỤC LỤC

DANH MỤC HÌNH VẼ

DANH MỤC BẢNG

DANH MỤC TỪ VIẾT TẮT

---

## TÓM TẮT ĐỒ ÁN

Ngành thương mại điện tử và dịch vụ du lịch trực tuyến (OTA) tại Việt Nam đang có những bước tiến vượt bậc, đặc biệt là việc tích hợp các dịch vụ này vào các siêu ứng dụng (Super App). Ví điện tử MoMo (thuộc Công ty Cổ phần Dịch vụ Di động Trực tuyến - M_Service) đã tiên phong tích hợp thành công dịch vụ đặt vé máy bay, mang lại trải nghiệm liền mạch cho người dùng [3][15]. Để đạt được điều này, MoMo cần sở hữu một hệ thống quy trình nghiệp vụ phức tạp, từ quản lý đối tác, cấu hình sản phẩm đến xử lý giao dịch và hỗ trợ khách hàng.

Đồ án này tập trung nghiên cứu, mô hình hóa và phân tích hệ thống quy trình nghiệp vụ mảng đặt vé máy bay của MoMo. Thông qua việc sử dụng ký hiệu chuẩn BPMN (Business Process Model and Notation) [22], nghiên cứu đã vẽ lại sơ đồ kiến trúc nghiệp vụ cho 10 quy trình (4 Quản lý, 3 Cốt lõi, 3 Hỗ trợ), trong đó mô hình hóa BPMN chi tiết cho 6 quy trình đại diện (2 Quản lý, 2 Cốt lõi, 2 Hỗ trợ). Trong số đó, 3 quy trình được phân tích chuyên sâu qua hai lăng kính: định tính (phân tích giá trị gia tăng VA/BVA/NVA, nhận diện lãng phí) và định lượng (tính toán thời gian chu kỳ, thời gian xử lý, chi phí nhân sự và hiệu suất) theo khung lý thuyết quản trị quy trình nghiệp vụ [21]. Kết quả của đồ án cung cấp bức tranh toàn cảnh về cách MoMo vận hành mảng vé máy bay, từ đó đề xuất các hướng tối ưu hóa tự động hóa nhằm nâng cao trải nghiệm khách hàng và giảm thiểu chi phí vận hành.

## MỞ ĐẦU

Trong kỷ nguyên chuyển đổi số, sự ra đời của các "siêu ứng dụng" đã làm thay đổi hoàn toàn thói quen tiêu dùng. MoMo không chỉ dừng lại ở dịch vụ thanh toán mà đã trở thành nền tảng đáp ứng mọi nhu cầu hàng ngày, trong đó có du lịch - đi lại [14][15]. Việc bán vé máy bay trực tiếp trên ứng dụng đòi hỏi MoMo phải kết nối hệ thống phức tạp với các hãng hàng không, đại lý vé (NCC), đồng thời quản lý luồng dữ liệu khổng lồ về giá, hạng vé, thông tin khách hàng và giao dịch tài chính.

Mục tiêu của đề tài là ứng dụng lý thuyết Hệ thống quản trị quy trình nghiệp vụ (BPMS) để rà soát lại kiến trúc quy trình của mảng kinh doanh này. Từ đó, xây dựng các mô hình BPMN "As-Is" (hiện tại) và thực hiện phân tích chuyên sâu nhằm tìm ra các điểm nghẽn (bottlenecks) và các bước không tạo ra giá trị (NVA).

Đồ án được chia thành 5 chương:

Chương 1: Tổng quan về M_Service và dịch vụ đặt vé máy bay trên MoMo.

Chương 2: Liệt kê và mô tả các quy trình nghiệp vụ, kèm sơ đồ kiến trúc quy trình.

Chương 3: Mô hình hóa chi tiết các quy trình bằng BPMN.

Chương 4: Phân tích các quy trình (định tính và định lượng).

Chương 5: Kết luận.

**Tuyên bố về phương pháp và phạm vi dữ liệu.** Đồ án được thực hiện hoàn toàn từ nguồn thông tin công khai; nhóm không có điều kiện phỏng vấn trực tiếp nhân sự nội bộ của M_Service và không tiếp cận được dữ liệu vận hành thực tế của doanh nghiệp. Vì vậy, toàn bộ bộ câu hỏi phỏng vấn trình bày ở Chương 3 là **bộ công cụ khảo sát được thiết kế sẵn** (chưa triển khai thực tế), và toàn bộ số liệu định lượng ở Chương 4 là **số liệu giả định mang tính minh họa** do nhóm tự xây dựng dựa trên nghiên cứu quy trình công khai, trải nghiệm sử dụng ứng dụng thực tế và suy luận nghiệp vụ có căn cứ. Các con số này phục vụ mục đích minh họa phương pháp tính toán theo khung lý thuyết BPM, không phải số liệu vận hành chính thức do MoMo công bố. Nội dung này được nhắc lại ở đầu mỗi phần liên quan để bảo đảm tính minh bạch.

---

# Chương 1: TỔNG QUAN VỀ M_SERVICE VÀ DỊCH VỤ ĐẶT VÉ MÁY BAY TRÊN MOMO

## 1.1. Lịch sử hình thành

Công ty Cổ phần Dịch vụ Di động Trực tuyến (M_Service) chính thức được thành lập vào năm 2007, là đơn vị chủ quản của ví điện tử MoMo. Ban đầu, dịch vụ ra mắt vào năm 2010 dưới dạng ứng dụng trên SIM điện thoại, hợp tác cùng nhà mạng Vinaphone để cung cấp các dịch vụ nạp và chuyển tiền cơ bản. Đến năm 2014, nhóm phát triển quyết định ra mắt ứng dụng trên nền tảng điện thoại thông minh với tên gọi MoMo — viết tắt của cụm từ "Mobile Money" — gửi gắm tham vọng phổ cập dịch vụ tài chính kỹ thuật số, biến chiếc điện thoại thành ví tiền tiện lợi cho mọi người dân Việt Nam.

Qua nhiều năm phát triển, MoMo đã vươn lên trở thành một trong những siêu ứng dụng thanh toán hàng đầu Việt Nam và đạt danh hiệu kỳ lân công nghệ, cạnh tranh trực tiếp với ZaloPay, VNPay, Viettel Money và các nền tảng ví điện tử tích hợp như ShopeePay.

Trong hành trình mở rộng từ một ví điện tử thuần thanh toán sang mô hình "siêu ứng dụng" (Super App), MoMo đã tích hợp thêm nhiều dịch vụ tiện ích ngoài tài chính — trong đó có tính năng "Du lịch - Đi lại" [14][15][18], cho phép người dùng tìm kiếm, so sánh và đặt vé máy bay nội địa/quốc tế từ nhiều hãng hàng không (Vietnam Airlines, Vietjet Air, Bamboo Airways...) [5], cùng vé tàu, vé xe khách và đặt phòng khách sạn. Đây chính là phạm vi nghiệp vụ mà đồ án này tập trung mô hình hóa và phân tích.

## 1.2. Quy mô và lĩnh vực hoạt động

M_Service hoạt động với tư cách tổ chức cung ứng dịch vụ trung gian thanh toán, chịu sự điều chỉnh của khung pháp lý do Ngân hàng Nhà nước Việt Nam ban hành đối với dịch vụ trung gian thanh toán và tài khoản thanh toán [19][20]. Việc tuân thủ khung pháp lý này thể hiện trực tiếp trong các quy trình nghiệp vụ của doanh nghiệp, ví dụ yêu cầu xác thực sinh trắc học và nâng cấp biện pháp bảo mật giao dịch theo quy định mới của Ngân hàng Nhà nước [9][13].

Lĩnh vực hoạt động chính của công ty là cung cấp dịch vụ ví điện tử MoMo, bao gồm các nhóm dịch vụ:

- **Thanh toán & chuyển tiền**: nạp/rút tiền, chuyển tiền, thanh toán hóa đơn, thanh toán tại điểm bán. Hoạt động này chịu ràng buộc về hạn mức giao dịch theo chính sách công bố của MoMo [12].
- **Dịch vụ tài chính**: ví trả sau, tiết kiệm, bảo hiểm, đầu tư liên kết đối tác. Riêng với mảng vé máy bay, MoMo cho phép thanh toán bằng Ví Trả Sau [8].
- **Dịch vụ tiện ích đời sống & du lịch** (Super App): trong đó mảng "Du lịch - Đi lại" — nơi đặt vé máy bay là một hợp phần — là đối tượng nghiên cứu của đồ án này. Vì MoMo không tự vận hành đội bay mà đóng vai trò nền tảng trung gian, mảng đặt vé máy bay là một hệ thống nhiều quy trình phối hợp: từ trải nghiệm tìm kiếm – đặt vé – thanh toán – xuất vé của khách hàng [1][2][4], đến vận hành đối tác phía sau (đồng bộ dữ liệu, đối soát), và các quy trình tuân thủ, bảo mật giao dịch bắt buộc theo quy định của Ngân hàng Nhà nước và ngành hàng không.

Do M_Service là công ty cổ phần chưa niêm yết và không công bố báo cáo tài chính thường niên ra công chúng, đồ án không đưa ra các con số cụ thể về quy mô người dùng, doanh thu hay thị phần. Phạm vi phân tích của đồ án vì vậy tập trung vào **cấu trúc và logic vận hành của quy trình nghiệp vụ**, là phần có thể quan sát và kiểm chứng được qua tài liệu công khai cùng trải nghiệm sử dụng thực tế, thay vì các chỉ tiêu tài chính doanh nghiệp.

## 1.3. Cơ cấu tổ chức

M_Service không công bố sơ đồ tổ chức chính thức ra bên ngoài. Do đó, thay vì mô tả sơ đồ tổ chức của toàn doanh nghiệp, nhóm xây dựng một **bản đồ chức năng** khái quát các bộ phận có liên quan trực tiếp đến mảng đặt vé máy bay. Bản đồ này được suy luận từ vai trò các tác nhân xuất hiện trong chính các quy trình nghiệp vụ mà đồ án mô hình hóa ở Chương 3, đối chiếu với thông lệ tổ chức phổ biến của các nền tảng OTA và ví điện tử [21]. Đây là cách tiếp cận "từ quy trình suy ra chức năng", phù hợp khi không tiếp cận được tài liệu tổ chức nội bộ.

*Bảng 1.1. Bản đồ chức năng các bộ phận liên quan đến mảng đặt vé máy bay*

| Nhóm chức năng | Bộ phận liên quan | Vai trò chính trong mảng đặt vé máy bay |
|---|---|---|
| Khách hàng (Front-office) | Bộ phận CSKH | Tiếp nhận, xử lý phản ánh, hoàn/hủy vé, hỗ trợ khách hàng |
| Đối tác & Vận hành | Bộ phận Business Development (BD), Bộ phận Ticketing, Đội Kỹ thuật | Thẩm định/tích hợp hãng bay & NCC, chuẩn hóa và cấu hình hạng vé, đồng bộ giá vé và lịch bay real-time |
| Đối tác & Vận hành | Đội Vận hành Sản phẩm Du lịch, Bộ phận Tài chính - Kế toán | Đối soát giao dịch, thanh toán hoa hồng với hãng bay/đối tác, xử lý hoàn tiền |
| Tuân thủ & Quản trị rủi ro | Bộ phận Tài chính/Pháp chế (Finance & Legal) | Thẩm định chính sách giá/khuyến mãi, xác thực giao dịch (eKYC), phòng chống gian lận, xử lý tranh chấp theo pháp luật |
| Hỗ trợ nội bộ | Bộ phận Quản lý Giá, Marketing, Growth Specialist | Xây dựng chính sách giá và ưu đãi, cá nhân hóa khuyến mãi, giám sát chất lượng dịch vụ đối tác (KPI/SLA) |

Tên gọi các bộ phận trong bảng trên được sử dụng thống nhất xuyên suốt các Chương 2, 3 và 4 của báo cáo, đồng thời tương ứng với tên các làn (swimlane) trong những sơ đồ BPMN được trình bày ở Chương 3.

---

# Chương 2: LIỆT KÊ QUY TRÌNH NGHIỆP VỤ

## 2.1. Phân loại quy trình

Để đảm bảo hoạt động cung cấp dịch vụ đặt vé máy bay diễn ra ổn định và mượt mà, MoMo đã xây dựng một hệ thống quy trình chặt chẽ bao gồm các hoạt động từ quản lý đối tác, vận hành giao dịch cốt lõi đến các hoạt động hỗ trợ khách hàng. Theo khung phân loại quy trình nghiệp vụ của Dumas và cộng sự [21], và tham khảo cách phân tầng kiến trúc quy trình trong tài liệu mẫu của môn học [24], các quy trình được phân thành 3 nhóm chính:

- **Nhóm Quy trình quản lý (Management Process)**: tập trung vào việc điều phối, thiết lập chiến lược và kiểm soát các hoạt động hợp tác với đối tác — từ quản lý hạng vé, quản trị giá và chương trình khuyến mãi, quản trị danh mục hãng bay và đối tác cung ứng, cho đến quản trị rủi ro giao dịch và tuân thủ điều khoản dịch vụ.
- **Nhóm Quy trình cốt lõi (Core Process)**: liên quan trực tiếp đến trải nghiệm giao dịch và chuỗi giá trị dịch vụ cung cấp cho người dùng đầu cuối — tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé; mua thêm dịch vụ tiện ích sau đặt chỗ; và đổi chuyến bay.
- **Nhóm Quy trình hỗ trợ (Support Process)**: đảm bảo nền tảng vận hành trơn tru và duy trì sự hài lòng của người dùng — hỗ trợ khách hàng và tiếp nhận phản hồi, tự động hóa xuất hóa đơn điện tử (VAT), và quản lý vé đã mua.

Sơ đồ kiến trúc quy trình dưới đây thể hiện đầy đủ 10 quy trình được phân thành ba tầng Quản lý – Cốt lõi – Hỗ trợ.

![](BPMN/PNG/00_KienTrucQuyTrinh.png)

*Hình 2.1. Sơ đồ kiến trúc quy trình nghiệp vụ mảng đặt vé máy bay trên MoMo*

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

**Kết quả:** *Thành công* — hạng vé được tích hợp, cấu hình, vượt qua kiểm tra và hiển thị ổn định trên App MoMo. *Thất bại* — kết nối API với hãng bay thất bại (vượt quá 2 lần sửa lỗi cho phép), hệ thống dừng tiếp nhận hạng vé. *Tạm hoãn* — dữ liệu hợp lệ nhưng Ticketing quyết định chưa công bố vì lý do kinh doanh.

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

#### Quản trị danh mục hãng bay và đối tác nhà cung ứng

**Tác nhân:** Đối tác (hãng bay/nhà cung ứng), Đội Phát triển Đối tác (BD), Bộ phận Tài chính/Pháp chế, Đội Kỹ thuật, Đội Vận hành Sản phẩm Du lịch.

**Mô tả các bước:** quy trình gồm 2 quy trình con có quan hệ vòng đời bổ sung nhau:

- **Quy trình con 1 — Thẩm định & Onboarding đối tác mới:** đối tác tiềm năng gửi hồ sơ đề xuất hợp tác (giấy phép kinh doanh vận tải/lữ hành, năng lực cung ứng, năng lực kỹ thuật, chính sách giá) cho Đội BD. BD đánh giá sơ bộ (mức độ phù hợp chiến lược, thị phần, chất lượng dịch vụ, uy tín) — không đạt thì lưu hồ sơ và kết thúc; đạt thì chuyển Bộ phận Tài chính/Pháp chế thẩm định (giấy phép, tư cách pháp nhân, AML/KYB) — không đạt thì lưu hồ sơ và kết thúc; đạt thì BD đàm phán và ký thỏa thuận hợp tác (hoa hồng, SLA, chính sách hoàn/hủy). Đội Kỹ thuật tích hợp API (tra cứu giá, đặt chỗ, thanh toán, xuất vé) và kiểm thử UAT — chưa đạt thì phối hợp khắc phục và kiểm thử lại (có thể lặp nhiều vòng); đạt thì Đội Vận hành cấu hình đối tác vào danh mục, chạy pilot nội bộ, rồi go-live chính thức và giám sát KPI/SLA sau ra mắt.
- **Quy trình con 2 — Rà soát, cập nhật và loại bỏ đối tác:** giám sát định kỳ hiệu suất đối tác đã onboarding (tỷ lệ đặt chỗ thành công, thời gian phản hồi API, tỷ lệ khiếu nại/1000 giao dịch), xử lý các trường hợp không đạt SLA bằng kế hoạch hành động khắc phục (CAP) với thời hạn ấn định, và loại bỏ đối tác vi phạm nghiêm trọng hoặc không cải thiện sau CAP khỏi danh mục.

**Đối tượng khách hàng:** Đội Vận hành Sản phẩm Du lịch (khách hàng nội bộ trực tiếp, tiếp nhận đối tác đã qua duyệt để vận hành danh mục); người dùng cuối MoMo (khách hàng gián tiếp, hưởng lợi từ danh mục hãng bay/đối tác chất lượng).

**Kết quả:** *Onboarding thành công* — đối tác được duyệt, tích hợp, go-live. *Bị từ chối* — ở vòng đánh giá sơ bộ hoặc thẩm định pháp lý, hồ sơ lưu lại xem xét sau. *Rà soát: Đạt, tiếp tục hợp tác / Yêu cầu CAP / Chấm dứt hợp tác.*

#### Quản trị rủi ro giao dịch, điều khoản và chất lượng dịch vụ

**Tác nhân:** Khách hàng, Bộ phận CSKH, Bộ phận Tài chính-Kế toán, Hãng bay/NCC.

**Mô tả các bước:**

1. **Khách hàng phát hiện và báo cáo giao dịch bất thường.** *Mục tiêu:* ghi nhận kịp thời các trường hợp trừ tiền nhưng chưa xuất vé, giao dịch treo (pending) kéo dài, hoặc sai lệch thông tin thanh toán. Khách hàng liên hệ CSKH qua hotline/app, cung cấp mã giao dịch/mã đặt chỗ liên quan [7].
2. **CSKH tra soát giao dịch.** *Mục tiêu:* xác minh trạng thái thực tế của giao dịch giữa hệ thống MoMo, cổng thanh toán và hệ thống hãng bay. CSKH tiếp nhận yêu cầu tra soát, đối chiếu dữ liệu giao dịch nội bộ với xác nhận từ hãng bay/đối tác — nếu **có xác nhận khớp** (giao dịch thực tế đã thành công phía hãng), cập nhật lại trạng thái vé cho khách hàng; nếu **không khớp/hãng chưa xác nhận**, chuyển sang quy trình xử lý ngoại lệ (rollback/hoàn tiền hoặc chờ xác nhận thêm từ hãng, có thể kéo dài do phụ thuộc phản hồi bên ngoài).
3. **Xử lý kết quả tra soát.** *Mục tiêu:* khôi phục quyền lợi tài chính hợp lý cho khách hàng. Nếu xác định lỗi thuộc về hệ thống/quy trình MoMo, Bộ phận Tài chính-Kế toán thực hiện hoàn tiền 100% về ví MoMo của khách hàng; nếu giao dịch thực tế đã thành công, cập nhật lại trạng thái vé/dịch vụ và thông báo cho khách hàng.
4. **Quản trị điều khoản và cam kết chất lượng dịch vụ.** *Mục tiêu:* thiết lập và duy trì các ràng buộc dịch vụ làm căn cứ xử lý tranh chấp. MoMo công bố công khai các điều khoản áp dụng cho từng nhóm nghiệp vụ — điều kiện và phạm vi hoàn/hủy vé [10][11], hạn mức giao dịch theo ngày [12], và yêu cầu xác thực bảo mật bắt buộc theo quy định của Ngân hàng Nhà nước [9][13]. Các điều khoản này vừa là cam kết với khách hàng, vừa là tham chiếu để CSKH quyết định hướng xử lý khi phát sinh khiếu nại. Song song, MoMo ràng buộc SLA với hãng bay/đối tác trong thỏa thuận hợp tác (xem quy trình *Quản trị danh mục hãng bay*), làm cơ sở quy trách nhiệm khi sự cố bắt nguồn từ phía đối tác.

**Đối tượng khách hàng:** Khách hàng có giao dịch bị lỗi/treo trong quá trình đặt vé, mua dịch vụ hoặc đổi vé.

**Kết quả:** *Giao dịch được khôi phục đúng trạng thái* (vé/dịch vụ hiển thị đúng) hoặc *Hoàn tiền thành công* (nếu xác định lỗi hệ thống). *Chưa giải quyết* — vẫn đang chờ xác nhận từ hãng bay/đối tác bên ngoài (thuộc nhóm lãng phí Hold, nằm ngoài tầm kiểm soát trực tiếp của MoMo).

### 2.2.2. Quy trình cốt lõi (Core Process)

#### Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Bộ phận CSKH, Hãng bay/NCC.

**Mô tả các bước:**

1. **Khách hàng nhập và chọn chuyến bay.** *Mục tiêu:* ghi nhận chính xác nhu cầu di chuyển và dịch vụ bổ sung mong muốn. Khách hàng truy cập App MoMo, mục vé máy bay, nhập thông tin tìm kiếm [1][2][16][17]; App hiển thị danh sách chuyến bay/hãng bay. Khách hàng chọn hành trình (khứ hồi: chọn chuyến đi và về; một chiều: chọn chuyến 1 chiều), chọn hạng vé, nhập thông tin khách hàng [4]. Hệ thống phân loại nội địa/quốc tế: **Quốc tế** — chuyển thẳng đến mua bảo hiểm và xác nhận; **Nội địa** — có thể nhập thẻ khách hàng thường xuyên (Vietjet Air), tùy chọn chỗ ngồi/suất ăn/hành lý ký gửi/bảo hiểm du lịch toàn diện (mỗi dịch vụ có nhánh Có/Không riêng).
2. **Ứng dụng thực hiện giữ chỗ tạm thời.** *Mục tiêu:* khóa tạm thời chuyến bay và tiện ích đã chọn, tránh bị mua mất trong lúc khách hàng thanh toán. App hiển thị chi tiết đơn hàng, tạo booking/tạm giữ chỗ. Hệ thống kiểm tra còn thời gian giữ vé — **hết** thì quay lại danh sách chuyến bay để khách thao tác lại; **còn** thì cho phép tiếp tục thanh toán.
3. **Thực hiện thanh toán và hoàn tất giao dịch.** *Mục tiêu:* khách hàng xác nhận đơn và hệ thống xử lý giao dịch tài chính. Khách hàng xác nhận và thanh toán (có thể dùng số dư ví hoặc Ví Trả Sau [8], xác thực bằng sinh trắc học/OTP theo quy định bảo mật [9][13]); App xử lý thanh toán và phân luồng theo kết quả: **Thất bại** — thông báo và kết thúc mua vé thất bại; **Thành công** — gửi yêu cầu xuất vé/xác nhận booking đến M_Service (sang Bước 4); **Pending (Treo)** — tạo ticket, chuyển CSKH xử lý ngoại lệ.
4. **Hệ thống trừ tiền và xuất vé.** *Mục tiêu:* xử lý triệt để giao dịch Pending (nếu có), phát hành vé từ hãng và cập nhật dữ liệu vé. Với giao dịch Pending: CSKH tiếp nhận, phân cấp hỗ trợ 24/7 (VIP) hoặc giờ hành chính (thường), liên hệ khách hàng xem còn nhu cầu mua vé — **không còn nhu cầu** thì hỗ trợ hủy đặt vé, rollback tiền, đóng ticket; **còn nhu cầu** thì gửi yêu cầu kiểm tra vé sang hãng bay — vé **đã có** trên hệ thống hãng thì CSKH xuất vé thủ công và chuyển trạng thái thành công; vé **chưa có** thì CSKH giữ vé cho khách, liên hệ hãng xuất vé, nhận mã đặt chỗ/vé điện tử rồi đóng ticket [7]. Từ luồng thành công (trực tiếp hoặc qua xử lý Pending), M_Service cập nhật vé vào hệ thống và cập nhật trạng thái giao dịch thành công.
5. **Trả vé điện tử về cho khách hàng.** *Mục tiêu:* cung cấp chứng từ chuyến bay hợp lệ để khách hàng làm thủ tục tại sân bay. Sau khi M_Service hoàn tất, hệ thống gửi thông báo kết quả cuối cùng; khách hàng nhận thông báo xuất vé thành công trên thiết bị cá nhân, vé điện tử được gửi qua kênh đã đăng ký [6]. Kết thúc: Mua vé thành công.

**Đối tượng khách hàng:** Hành khách có nhu cầu đặt vé máy bay.

**Kết quả:** *Thành công* — thanh toán hoàn tất, hãng bay trả mã đặt chỗ, vé điện tử được gửi thành công. *Thất bại/Hủy giao dịch* — thanh toán lỗi, hoặc đơn hàng treo (Pending) mà khách hàng không còn nhu cầu và yêu cầu hủy để hoàn tiền (rollback).

#### Mua thêm dịch vụ sau đặt chỗ

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Hãng bay, Nhân viên CSKH.

**Mô tả các bước:**

1. **Tiếp nhận yêu cầu và truy cập thông tin vé.** *Mục tiêu:* xác định đúng đơn hàng/vé cần mua thêm dịch vụ. Khách hàng chọn hình thức liên hệ **Qua App** hoặc **Qua CSKH**. Qua App: truy cập App, chọn vé đã mua — nếu vé Quốc tế, App hiển thị thông báo liên hệ CSKH. Qua CSKH: khách gọi tổng đài, CSKH tiếp nhận, thu thập thông tin và kiểm tra vé — vé không hợp lệ thì thông báo và kết thúc; vé Nội địa thì CSKH hướng dẫn khách tự thao tác trên App.
2. **Chọn mua thêm dịch vụ.** *Mục tiêu:* ghi nhận nhu cầu sử dụng tiện ích bổ sung. Qua App: khách tự chọn hành lý ký gửi (nếu Có → chọn số kg), chỗ ngồi (nếu Có → chọn vị trí), suất ăn (nếu Có → chọn loại). Qua CSKH: nhân viên kiểm tra dịch vụ/báo giá rồi thao tác chọn dịch vụ thay khách hàng.
3. **Gửi yêu cầu và thực hiện thanh toán.** *Mục tiêu:* hoàn tất nghĩa vụ tài chính cho dịch vụ phát sinh. Qua App: khách bấm xác nhận và thanh toán trực tiếp. Qua CSKH: CSKH gửi yêu cầu thanh toán về App của khách, khách kiểm tra và xác nhận thanh toán.
4. **Xử lý giao dịch và đồng bộ với hãng bay.** *Mục tiêu:* ghi nhận trạng thái thanh toán và gửi lệnh xuất dịch vụ sang hãng bay. App xử lý thanh toán, rẽ nhánh theo kết quả: **Thất bại** — thông báo và kết thúc "Mua thêm dịch vụ không thành công"; **Thành công** — M_Service cập nhật dịch vụ mua vào dữ liệu vé, đẩy lệnh sang Hãng bay/NCC; hãng tiếp nhận và trả kết quả đặt thêm dịch vụ (thường được ghi nhận dưới dạng chứng từ phụ trợ điện tử EMD).
5. **Gửi thông báo và hiển thị dịch vụ đã mua.** *Mục tiêu:* cập nhật vé điện tử và thông báo kết quả cuối cùng. Sau khi lưu trữ dữ liệu và nhận kết quả từ hãng, hệ thống gửi thông báo cho khách hàng; dịch vụ bổ sung hiển thị trực tiếp trên vé điện tử. Kết thúc: Dịch vụ đã được đặt.

**Đối tượng khách hàng:** Hành khách đã có mã đặt chỗ hợp lệ.

**Kết quả:** *Thành công* — thanh toán hoàn tất, hãng bay chấp nhận, dịch vụ bổ sung được cập nhật vào vé điện tử. *Thất bại* — mã vé không tồn tại/không hợp lệ, giao dịch thanh toán lỗi, hoặc hãng bay từ chối cung cấp thêm dịch vụ.

#### Đổi chuyến bay

**Tác nhân:** Khách hàng, Giao diện MoMo Client App, Backend MoMo Travel, Cổng Thanh toán MoMo, Bộ phận CSKH MoMo Travel, Hệ thống Hãng bay (CRS/GDS).

**Mô tả các bước:**

1. **Khởi tạo yêu cầu đổi chuyến bay.** *Mục tiêu:* ghi nhận đúng vé và nhu cầu thay đổi của khách hàng. Khách hàng vào mục "Quản lý đặt chỗ", chọn vé cần đổi, nhấn "Đổi chuyến bay". Hệ thống kiểm tra điều kiện vé cơ bản (một số hạng vé Tiết kiệm/Economy Saver có thể không cho đổi hoặc chỉ cho đổi trước giờ bay 24h) theo chính sách hoàn/đổi được công bố [10][11]. Khách hàng chọn thông số muốn đổi: ngày bay, giờ bay, hoặc hành trình.
2. **Tìm kiếm lịch bay mới và truy xuất giá vé.** *Mục tiêu:* cung cấp lựa chọn chuyến bay mới phù hợp. Backend gửi yêu cầu tìm kiếm sang GDS/CRS của hãng bay; hãng trả về danh sách chuyến bay còn chỗ kèm giá chênh lệch ước tính. Hệ thống kiểm tra **có chuyến bay phù hợp còn chỗ hay không** — nếu không, thông báo và kết thúc, giữ nguyên vé cũ; nếu có, hiển thị để khách hàng chọn chuyến bay/giờ bay mới.
3. **Tính toán chi tiết cấu trúc phí đổi.** *Mục tiêu:* xác định chính xác tổng số tiền khách hàng phải trả thêm. Công thức: **Tổng phí đổi = Phí đổi cố định của Hãng + Chênh lệch giá vé (giá mới − giá cũ, nếu dương) + Phí dịch vụ MoMo.** Nếu giá vé mới thấp hơn giá cũ, phần chênh lệch âm không được hoàn lại theo quy định phổ biến của các hãng nội địa. Hệ thống kiểm tra: **đổi tự động được qua API?** — **Không** (một số hạng vé quốc tế/vé khuyến mãi đặc biệt không hỗ trợ tính phí tự động) thì tạo Support Ticket chuyển sang CSKH; nhân viên CSKH liên hệ hãng bay kiểm tra phí thủ công và gửi yêu cầu thanh toán cho khách. **Có** thì tiếp tục bước 4 trực tiếp.
4. **Xác nhận chi tiết chi phí và chấp nhận điều kiện đổi.** *Mục tiêu:* đảm bảo khách hàng đồng thuận trước khi trích tiền. Ứng dụng hiển thị bảng phân rã chi phí đổi vé. Hệ thống kiểm tra **khách hàng có đồng ý mức phí đổi hay không** — không đồng ý thì kết thúc, giữ nguyên vé cũ; đồng ý thì khách hàng tick "Tôi đã đọc, hiểu và đồng ý với Điều kiện thay đổi vé" và nhấn "Thanh toán phí đổi".
5. **Thanh toán phí chênh lệch đổi chuyến.** *Mục tiêu:* hoàn tất nghĩa vụ tài chính cho khoản phí đổi. Khách hàng chọn nguồn tiền và thực hiện xác thực bảo mật (mật khẩu/OTP/sinh trắc học) theo quy định [9][13]. Hệ thống kiểm tra **xác thực có thành công không** — thất bại thì hủy yêu cầu đổi vé; thành công thì Cổng thanh toán MoMo xử lý trích tiền. Tiếp tục kiểm tra **thanh toán thành công?** — thất bại thì kết thúc "Đổi vé thất bại do lỗi thanh toán"; thành công thì chuyển sang tái phát hành vé.
6. **Tái phát hành vé và cập nhật PNR.** *Mục tiêu:* hoàn tất việc đổi chuyến trên hệ thống hãng bay. Hệ thống xác định **kênh tái phát hành**: **tự động qua API** thì Backend gửi lệnh Re-issue kèm mã hạch toán sang hãng bay; **thủ công qua CSKH** thì nhân viên CSKH thao tác tái xuất vé trực tiếp với hãng. Cả hai nhánh hội tụ tại bước hãng bay xử lý. Hệ thống kiểm tra **Re-issue thành công?** — **Hết chỗ chuyến mới** (khách khác đã mua mất ghế trong lúc thanh toán) thì hủy giao dịch thanh toán phí đổi, hoàn trả 100% phí vừa trích về ví MoMo, giữ nguyên vé cũ, thông báo khách chọn lại chuyến khác; **thành công** thì hãng hủy chỗ chuyến cũ, xác nhận chỗ chuyến mới, thu hồi vé điện tử cũ, cấp vé điện tử mới. App cập nhật lại "Quản lý đặt chỗ", thông báo đổi vé thành công, gửi email/SMS xác nhận hành trình mới.

**Đối tượng khách hàng:** Hành khách đã có vé hợp lệ, có nhu cầu thay đổi lịch trình bay.

**Kết quả:** *Thành công* — vé điện tử mới được cấp kèm mã đặt chỗ (PNR) mới, vé cũ bị thu hồi. *Hủy đổi vé, giữ vé cũ* — không có chuyến phù hợp, khách không đồng ý mức phí, hoặc hết chỗ trên chuyến mới khi đang trích tiền (trường hợp này hoàn 100% phí đổi). *Thất bại* — xác thực bảo mật hoặc thanh toán phí đổi không thành công.

### 2.2.3. Quy trình hỗ trợ (Support Process)

#### Hỗ trợ khách hàng và tiếp nhận phản hồi

**Tác nhân:** Khách hàng, Bộ phận CSKH, Hãng bay/Nhà cung cấp.

**Mô tả các bước:**

1. **Khách báo sự cố.** *Mục tiêu:* ghi nhận kịp thời vấn đề/yêu cầu hỗ trợ. Khách hàng liên hệ qua tổng đài hoặc App MoMo; nếu qua App, hệ thống xác thực kiểm tra thông tin.
2. **CSKH tiếp nhận và xác minh.** *Mục tiêu:* ghi nhận thông tin cơ bản, tạo luồng xử lý, phân bổ đúng nhóm nghiệp vụ. CSKH thu thập thông tin, ghi nhận yêu cầu và tạo ticket (lưu vào Dữ liệu hỗ trợ KH), phân loại vấn đề ban đầu và phân công nhóm xử lý. Kiểm tra khách VIP hay thường: VIP → kênh chăm sóc VIP; thường → kênh chăm sóc tiêu chuẩn.
3. **Phân loại lỗi hoặc yêu cầu.** *Mục tiêu:* phân tích chi tiết sự cố để chuẩn bị phương án xử lý. CSKH phân tích yêu cầu — nếu **không đủ thông tin**, yêu cầu khách bổ sung (quay lại phân tích); nếu **đủ thông tin**, xử lý yêu cầu.
4. **Xử lý trực tiếp hoặc chuyển cho bên liên quan.** *Mục tiêu:* giải quyết theo thẩm quyền MoMo hoặc phối hợp đối tác. Đánh giá vấn đề thuộc phạm vi MoMo hay Hãng bay/NCC — **thuộc MoMo** thì CSKH trực tiếp cung cấp hướng dẫn/giải pháp; **thuộc Hãng bay/NCC** thì gửi yêu cầu sang hãng, hãng kiểm tra và xử lý theo chính sách, chấp nhận hoặc từ chối (kèm lý do), CSKH nhận kết quả và ghi nhận vào Dữ liệu hỗ trợ KH.
5. **Phản hồi kết quả cho khách hàng.** *Mục tiêu:* truyền đạt hướng giải quyết cuối cùng và đóng ticket. Tùy hình thức phản hồi: **Thông báo trên App** — CSKH gửi thông báo qua app, kết thúc "Hoàn tất hỗ trợ"; **Liên hệ trực tiếp** — khách nhận thông báo, nếu **chấp nhận** hướng giải quyết thì CSKH xác nhận hoàn tất, đóng ticket, kết thúc; nếu **không chấp nhận** thì CSKH hướng dẫn khách khiếu nại lên cấp cao hơn (Pháp chế), đóng ticket, kết thúc.

Ngoài ra, một nhánh nghiệp vụ liên quan trực tiếp là **tra soát giao dịch lỗi/treo** (xem chi tiết ở mục *Quản trị rủi ro giao dịch* phía trên): khi khách hàng phản ánh giao dịch bị trừ tiền nhưng chưa nhận vé/dịch vụ [7], CSKH phối hợp cùng Bộ phận Tài chính-Kế toán xác minh với hãng bay/đối tác trước khi quyết định cập nhật trạng thái hoặc hoàn tiền.

**Đối tượng khách hàng:** Người dùng gặp sự cố với dịch vụ trên MoMo.

**Kết quả:** *Thành công (đóng ticket)* — sự cố được giải quyết dứt điểm, khách hàng đồng ý phương án xử lý. *Bị từ chối* — hãng bay/NCC từ chối hỗ trợ (kèm lý do). *Không đạt thỏa thuận* — khách không chấp nhận hướng giải quyết, chuyển sang khiếu nại chuyên sâu.

#### Xuất hóa đơn

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Bộ phận CSKH, Bộ phận Kế toán, Hệ thống hóa đơn điện tử của đối tác.

**Mô tả các bước:**

1. **Khách hàng chọn xuất VAT / Liên hệ CSKH.** *Mục tiêu:* khởi tạo yêu cầu xuất hóa đơn GTGT cho giao dịch đã mua. Qua App: khách truy cập mục Xuất hóa đơn trong chi tiết vé; hệ thống kiểm tra giao dịch đã yêu cầu xuất hóa đơn chưa — **đã yêu cầu** thì hiển thị thông tin hóa đơn đã xuất, kết thúc; **chưa yêu cầu** thì chuyển sang form nhập liệu. Qua CSKH: khách gọi tổng đài, CSKH lấy thông tin yêu cầu.
2. **Nhập thông tin vào form / CSKH thu thập thông tin.** *Mục tiêu:* ghi nhận đầy đủ thông tin xuất hóa đơn. Qua App: khách nhập form (mã số thuế, tên công ty, địa chỉ, email), hệ thống kiểm tra dữ liệu — **không hợp lệ** thì yêu cầu nhập lại; **hợp lệ** thì chuyển sang kiểm tra điều kiện. Qua CSKH: CSKH thu thập và đẩy dữ liệu vào hệ thống.
3. **Kiểm tra điều kiện xuất VAT.** *Mục tiêu:* đảm bảo yêu cầu nằm trong thời hạn quy định. M_Service đối chiếu thời hạn tiếp nhận yêu cầu xuất hóa đơn (trong mô hình này nhóm giả định mốc 72 giờ kể từ thời điểm giao dịch, tương ứng thông lệ phổ biến của các nền tảng thương mại điện tử) — **quá hạn** thì thông báo và kết thúc "Đã quá hạn xuất VAT"; **còn hạn** thì lấy dữ liệu giao dịch/vé/KH để đối soát.
4. **Kiểm tra, đối soát giao dịch.** *Mục tiêu:* đối chiếu tính chính xác giữa dữ liệu giao dịch và yêu cầu xuất hóa đơn. M_Service lấy song song thông tin vé/thanh toán và thông tin KH/hóa đơn, ghép dữ liệu để kiểm tra khớp — **không khớp** thì gửi CSKH kiểm tra/liên hệ khách xác nhận, cập nhật rồi đối chiếu lại; **khớp** thì tạo yêu cầu xuất hóa đơn, chuyển bộ phận kế toán.
5. **Gửi yêu cầu sang hệ thống hóa đơn điện tử để phát hành.** *Mục tiêu:* truyền lệnh phát hành hóa đơn sang hệ thống của đơn vị cung cấp dịch vụ hóa đơn điện tử. Kế toán gọi API tạo hóa đơn — hệ thống đối tác tiếp nhận **thất bại** thì ghi lỗi, gửi lại hoặc chuyển Kỹ thuật; **thành công** thì đối tác xử lý dữ liệu, ký số và phát hành — nếu **phát hành thất bại** thì cập nhật trạng thái lỗi, báo Kỹ thuật và kết thúc nhánh này; **thành công** thì hóa đơn được phát hành và truyền file (XML/PDF) về MoMo.
6. **Trả kết quả và gửi hóa đơn điện tử về cho khách hàng.** *Mục tiêu:* cập nhật trạng thái và cung cấp hóa đơn điện tử cho người dùng. App nhận hóa đơn, đồng thời cập nhật vào Dữ liệu về VAT, cập nhật trạng thái trên App, gửi thông báo cho khách hàng. Khách hàng xem/tải hóa đơn trên thiết bị. Kết thúc: Xuất VAT hoàn tất.

**Đối tượng khách hàng:** Khách hàng cần chứng từ thuế.

**Kết quả:** *Thành công* — dữ liệu đối soát khớp, hóa đơn được phát hành và gửi về App. *Từ chối/Lỗi hệ thống* — quá thời hạn quy định, dữ liệu đối soát không khớp, hoặc hệ thống hóa đơn điện tử gặp lỗi kỹ thuật.

#### Quản lý vé đã mua

**Tác nhân:** Khách hàng, Ứng dụng MoMo, Bộ phận CSKH, Hãng bay.

**Mô tả các bước:**

1. **Truy cập danh sách vé đã mua.** *Mục tiêu:* cho phép khách hàng xem lại toàn bộ vé/hành trình đã đặt. Khách hàng vào mục "Tôi" > "Quản lý đặt chỗ" (hoặc "Vé của tôi") trên App MoMo. Hệ thống truy xuất danh sách vé từ cơ sở dữ liệu vé theo tài khoản khách hàng, phân loại theo trạng thái: Sắp khởi hành / Đã hoàn thành / Đã hủy.
2. **Xem chi tiết vé/hành trình.** *Mục tiêu:* cung cấp đầy đủ thông tin chuyến bay, hành khách và các dịch vụ đã mua kèm. Khách hàng chọn 1 vé để xem chi tiết: mã đặt chỗ (PNR), thông tin hành khách, giờ bay, hạng vé, các dịch vụ bổ sung đã mua (hành lý, chỗ ngồi, suất ăn, bảo hiểm), trạng thái check-in.
3. **Điều hướng sang các tác vụ liên quan.** *Mục tiêu:* làm điểm vào tập trung cho các nhu cầu phát sinh trên vé đã mua. Từ màn hình chi tiết vé, khách hàng có thể chọn: "Mua thêm dịch vụ" (sang quy trình *Mua thêm dịch vụ sau đặt chỗ*), "Đổi chuyến bay" (sang quy trình *Đổi chuyến bay*), "Xuất hóa đơn" (sang quy trình *Xuất hóa đơn*), hoặc "Liên hệ hỗ trợ" (sang quy trình *Hỗ trợ khách hàng*) nếu gặp sự cố.
4. **Tải/chia sẻ vé điện tử.** *Mục tiêu:* cung cấp chứng từ hợp lệ để khách hàng sử dụng khi ra sân bay. Khách hàng có thể tải vé điện tử (PDF kèm mã QR check-in) hoặc chia sẻ cho người đi cùng qua các ứng dụng khác. Vé điện tử cũng được gửi tới khách hàng qua kênh đã đăng ký ngay khi đặt thành công [6].

**Đối tượng khách hàng:** Hành khách đã hoàn tất đặt vé, có nhu cầu tra cứu hoặc quản lý vé/hành trình đã mua.

**Kết quả:** *Thành công* — khách hàng xem/tải được vé và điều hướng đúng sang tác vụ cần thực hiện. *Không có dữ liệu* — tài khoản chưa có vé nào đã đặt.

---

# Chương 3: MÔ HÌNH HÓA CHI TIẾT CÁC QUY TRÌNH BẰNG BPMN

Chương này trình bày 6 quy trình đại diện được chọn mô hình hóa chi tiết, đúng cơ cấu 2 Quản lý – 2 Cốt lõi – 2 Hỗ trợ. Mỗi quy trình theo khung thống nhất: **3.X.1 Phương pháp thực hiện** (Dựa trên bằng chứng + Bộ câu hỏi phỏng vấn) → **3.X.2 Mô hình hóa quy trình** (sơ đồ BPMN kèm diễn giải luồng chính và luồng ngoại lệ).

**Lưu ý áp dụng cho toàn chương.** Như đã nêu ở phần Mở đầu, nhóm không phỏng vấn trực tiếp nhân sự M_Service. Các bộ câu hỏi dưới đây là **công cụ khảo sát do nhóm thiết kế** theo đúng lưới 2×2 mà phương pháp discovery yêu cầu (định tính/định lượng × có cấu trúc/không cấu trúc), thể hiện cách nhóm sẽ thu thập dữ liệu nếu được tiếp cận doanh nghiệp — không phải biên bản phỏng vấn đã thực hiện.

---

## 3.1. Quản trị giá, khuyến mãi và chính sách hiển thị giá

### 3.1.1. Phương pháp thực hiện

**a) Mô tả quy trình hiện có.** Quy trình được tái dựng từ bốn nguồn bằng chứng: (1) chính sách hiển thị giá và khuyến mãi công bố công khai trên trang vé máy bay của MoMo [3]; (2) quan sát trực tiếp cách giá, thuế, phí và mã ưu đãi hiển thị trên ứng dụng qua nhiều phiên đặt vé thử ở các khung giờ khác nhau; (3) thông lệ vận hành giá của các nền tảng OTA (tách giá gốc – thuế/phí – ưu đãi thành các lớp cấu hình độc lập); (4) ràng buộc pháp lý về minh bạch giá đối với tổ chức trung gian thanh toán [19][20]. Diễn giải chi tiết 5 bước của quy trình đã trình bày ở mục 2.2.1.

**b) Sơ đồ tổ chức và trách nhiệm.** Sáu tác nhân tham gia, tương ứng 6 làn trong sơ đồ BPMN ở mục 3.1.2:

*Bảng 3.1. Phân định trách nhiệm quy trình Quản trị giá và khuyến mãi*

| Tác nhân | Trách nhiệm chính | Đầu ra bàn giao |
|---|---|---|
| Hãng bay / NCC | Cung cấp dữ liệu giá, thuế, phí và chính sách áp dụng | Bộ dữ liệu giá gốc |
| Bộ phận Quản lý Giá | Tiếp nhận, kiểm tra tính đầy đủ, chuẩn hóa cấu trúc giá/thuế/phí | Bộ dữ liệu giá đã chuẩn hóa |
| Bộ phận Marketing | Phân tích tệp khách hàng, thiết kế cơ chế khuyến mãi và hồ sơ điều kiện | Đề xuất chính sách giá/KM |
| Bộ phận Tài chính / Pháp chế | Thẩm định khả thi tài chính, rủi ro pháp lý, kiểm tra hồ sơ điều kiện | Quyết định phê duyệt/từ chối |
| Growth Specialist / Kỹ thuật | Cấu hình tham số giá và quy tắc hiển thị lên hệ thống | Cấu hình đã triển khai |
| Ứng dụng MoMo | Truy xuất, kiểm tra và hiển thị giá/KM tới người dùng cuối | Giá/KM hiển thị chính thức |

**c) Kế hoạch làm việc.** Nhóm thực hiện nghiên cứu quy trình này theo 4 mốc:

*Bảng 3.2. Kế hoạch làm việc nghiên cứu quy trình Quản trị giá*

| Mốc | Công việc | Bộ phận là đối tượng nghiên cứu |
|---|---|---|
| T+0 – T+4 | Thu thập bằng chứng công khai, quan sát hiển thị giá trên App | Hãng bay/NCC, Bộ phận Giá |
| T+2 – T+8 | Dựng mô tả quy trình, thiết kế bộ câu hỏi khảo sát | Marketing, Tài chính/Pháp chế |
| T+6 – T+16 | Mô hình hóa BPMN, đối chiếu logic rẽ nhánh | Kỹ thuật, Ứng dụng MoMo |
| T+16 – T+20 | Phân tích định tính/định lượng, hoàn thiện báo cáo | Toàn bộ tác nhân |

Các mốc thời gian trên có thể gối đầu một phần giữa các giai đoạn liền kề (ví dụ việc thiết kế câu hỏi khảo sát có thể bắt đầu khi phần thu thập bằng chứng chưa kết thúc), không phải các bước tuần tự tuyệt đối.

**d) Thuật ngữ và sổ tay.**

*Bảng 3.3. Thuật ngữ nghiệp vụ quy trình Quản trị giá*

| Thuật ngữ | Giải nghĩa |
|---|---|
| M_Service | Công ty Cổ phần Dịch vụ Di động Trực tuyến — pháp nhân chủ quản ví điện tử MoMo |
| Khối Tài chính/Pháp chế (Finance & Legal) | Bộ phận thẩm định rủi ro tài chính và tuân thủ pháp lý của chính sách giá/khuyến mãi |
| Giá gốc (base fare) | Giá vé do hãng bay công bố, chưa gồm thuế và phụ phí |
| Chuẩn hóa giá | Việc quy đổi dữ liệu giá/thuế/phí từ nhiều hãng về một cấu trúc thống nhất của hệ thống |
| Hồ sơ điều kiện | Tập tài liệu quy định phạm vi, đối tượng, thời hạn và ngân sách áp dụng của một chương trình khuyến mãi |
| Quy tắc hiển thị giá | Tập tham số quyết định cách giá và ưu đãi được trình bày trên giao diện người dùng |
| Growth Specialist | Vai trò kỹ thuật – tăng trưởng, chịu trách nhiệm cấu hình và kiểm thử chính sách giá trên hệ thống |
| Time-to-market | Khoảng thời gian từ khi có ý tưởng chiến dịch đến khi ưu đãi hiển thị tới người dùng |

**e) Biểu mẫu tác nghiệp.**

1. *Phiếu tiếp nhận dữ liệu giá* — Mã hãng bay / Kỳ áp dụng / Số hạng vé / Trạng thái kiểm tra đầy đủ / Người tiếp nhận / Thời điểm tiếp nhận.
2. *Phiếu đề xuất chương trình khuyến mãi* — Tên chiến dịch / Tệp khách hàng mục tiêu / Cơ chế ưu đãi / Ngân sách dự kiến / Thời hạn áp dụng / Người đề xuất.
3. *Phiếu thẩm định Tài chính – Pháp chế* — Mã đề xuất / Kết quả thẩm định tài chính / Kết quả thẩm định pháp lý / Tình trạng hồ sơ điều kiện / Kết luận phê duyệt.
4. *Biên bản nghiệm thu hiển thị giá* — Mã cấu hình / Kết quả kiểm tra hiển thị / Số lần yêu cầu chỉnh sửa / Thời điểm công bố chính thức.

**f) Bộ câu hỏi phỏng vấn.** Đối tượng dự kiến: Bộ phận Quản lý Giá, Marketing, Tài chính/Pháp chế, Growth Specialist/Kỹ thuật, CSKH.

*Bảng 3.4. Câu hỏi định tính — quy trình Quản trị giá (5 có cấu trúc + 5 không cấu trúc)*

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Công đoạn nào trong quy trình thường phát sinh nhiều khó khăn và mất thời gian nhất? A. Chuẩn hóa dữ liệu giá, thuế, phí. B. Thiết kế cơ chế khuyến mãi. C. Thẩm định hồ sơ điều kiện/ngân sách. D. Cấu hình và kiểm thử hiển thị. | Tất cả các bộ phận tham gia | Xác định điểm nghẽn (bottleneck) |
| 2 | Có cấu trúc | Khi dữ liệu giá/thuế/phí từ Hãng bay/NCC bị thiếu sót, xử lý theo phương án nào? A. Trả lại yêu cầu gửi lại toàn bộ. B. Phối hợp bổ sung phần thiếu. C. Tự bổ sung dựa trên dữ liệu cũ. D. Báo cáo cấp trên. | Bộ phận Quản lý Giá | Đánh giá xử lý ngoại lệ đầu vào |
| 3 | Có cấu trúc | Nguyên nhân phổ biến nhất khiến hồ sơ khuyến mãi bị từ chối là gì? A. Vượt ngân sách. B. Thiếu chứng từ hợp lệ. C. Điều kiện áp dụng rủi ro pháp lý. D. Sai đối tượng mục tiêu. | Tài chính/Pháp chế | Đánh giá rủi ro pháp lý/tài chính |
| 4 | Có cấu trúc | Khi cấu hình hệ thống, khó khăn lớn nhất là gì? A. Cơ chế KM phức tạp. B. SLA cấu hình quá gấp. C. Lỗi backend. D. Bàn giao không rõ ràng. | Growth Specialist/Kỹ thuật | Đánh giá độ phức tạp thiết lập |
| 5 | Có cấu trúc | Bước kiểm thử hiển thị hiện chủ yếu theo hình thức nào? A. Tự động 100%. B. Thủ công là chính. C. Kết hợp. D. Bỏ qua nếu gấp. | Kỹ thuật, Marketing | Mức độ ứng dụng công nghệ QA |
| 6 | Không cấu trúc | Tiêu chuẩn nào đang dùng để chuẩn hóa dữ liệu giá/thuế/phí, có thể tự động hóa thêm không? | Bộ phận Quản lý Giá | Tiềm năng tự động hóa |
| 7 | Không cấu trúc | Khi phát hiện lỗi hiển thị giá/KM, quy trình yêu cầu chỉnh sửa diễn ra thế nào, tốn bao lâu? | Kỹ thuật, Marketing | Xử lý sự cố trước Go-live |
| 8 | Không cấu trúc | Để rút ngắn time-to-market, nên ưu tiên loại bỏ hoặc thay đổi bước nào? | Tất cả các bộ phận tham gia | Ý kiến cải tiến từ người thực hiện |
| 9 | Không cấu trúc | Sự phối hợp giữa Marketing và Tài chính/Pháp chế ở khâu thẩm định hồ sơ KM hiện có điểm nào chưa ăn khớp, gây chậm trễ? | Marketing, Tài chính/Pháp chế | Điểm nghẽn phối hợp liên phòng ban |
| 10 | Không cấu trúc | Rủi ro lớn nhất là gì nếu quy trình duyệt giá/KM bị rút ngắn quá mức để kịp một chiến dịch gấp? | Tất cả các bộ phận tham gia | Đánh đổi tốc độ – kiểm soát rủi ro |

*Bảng 3.5. Câu hỏi định lượng — quy trình Quản trị giá (5 có cấu trúc + 5 không cấu trúc)*

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Trung bình mất bao nhiêu giờ để chuẩn hóa xong 1 bộ dữ liệu giá? A. ≤2h. B. 2–4h. C. 4–8h. D. >8h. | Bộ phận Quản lý Giá | Thời gian xử lý chuẩn hóa |
| 2 | Có cấu trúc | Trung bình 1 tuần tiếp nhận bao nhiêu bộ dữ liệu giá từ Hãng bay/NCC? A. <5. B. 5–10. C. 11–20. D. >20. | Bộ phận Quản lý Giá | Khối lượng công việc đầu vào |
| 3 | Có cấu trúc | Bao nhiêu % hồ sơ KM bị Tài chính/Pháp chế từ chối ở lần trình đầu? A. <10%. B. 10–25%. C. 26–50%. D. >50%. | Tài chính/Pháp chế | Tỷ lệ rework thẩm định |
| 4 | Có cấu trúc | Thời gian trung bình từ nhận hồ sơ đến khi ra quyết định phê duyệt? A. <1 ngày. B. 1–2 ngày. C. 3–5 ngày. D. >5 ngày. | Tài chính/Pháp chế | Đầu vào tính thời gian chu kỳ |
| 5 | Có cấu trúc | Trung bình cần bao nhiêu lần cấu hình lại (rework) cho 1 chiến dịch KM? A. 0. B. 1. C. 2. D. ≥3. | Growth Specialist/Kỹ thuật | Đầu vào công thức thời gian trễ do rework |
| 6 | Không cấu trúc | Trung bình 1 lượt kiểm thử hiển thị giá/KM mất bao nhiêu phút? | Kỹ thuật, Marketing | Thời gian kiểm thử |
| 7 | Không cấu trúc | Mỗi tháng phát sinh khoảng bao nhiêu ticket khiếu nại liên quan sai giá/sai KM? | CSKH | Chỉ số chất lượng đầu ra |
| 8 | Không cấu trúc | Tổng thời gian chu kỳ trung bình từ nhận dữ liệu đến công bố là bao lâu? | Tất cả các bộ phận tham gia | Thời gian chu kỳ tổng — đầu vào Chương 4 |
| 9 | Không cấu trúc | Trung bình cần bao nhiêu nhân sự và giờ công để hoàn tất 1 lần chạy toàn bộ quy trình? | Tất cả các bộ phận tham gia | Chi phí nhân sự — đầu vào Chương 4 |
| 10 | Không cấu trúc | Bao nhiêu % bộ dữ liệu giá bị trả lại yêu cầu bổ sung ngay lần gửi đầu? | Bộ phận Quản lý Giá | Tỷ lệ lỗi đầu vào |

### 3.1.2. Mô hình hóa quy trình

![](BPMN/PNG/01_Management_QuanTriGia_KhuyenMai.png)

*Hình 3.1. Sơ đồ BPMN quy trình Quản trị giá, khuyến mãi và chính sách hiển thị giá (6 làn, 9 cổng điều kiện)*

**Luồng chính:** Hãng bay/NCC gửi dữ liệu giá → Bộ phận Giá tiếp nhận, kiểm tra đầy đủ và chuẩn hóa → Marketing phân tích tệp khách hàng và xây dựng cơ chế khuyến mãi → Tài chính/Pháp chế thẩm định và phê duyệt → Kỹ thuật cấu hình lên hệ thống → App kiểm tra hiển thị → Công bố giá/KM thành công.

**Luồng ngoại lệ:**
- *Dữ liệu giá không đầy đủ:* quay lại yêu cầu hãng bay bổ sung, tạo vòng lặp cho tới khi dữ liệu hợp lệ.
- *Chuẩn hóa sai:* trả lại Bộ phận Giá điều chỉnh trước khi chuyển tiếp.
- *Không áp dụng khuyến mãi:* bỏ qua toàn bộ nhánh Marketing – Pháp chế, đẩy thẳng chính sách giá gốc sang Kỹ thuật (hai nhánh hội tụ tại cổng gộp trước bước cấu hình).
- *Chính sách không được phê duyệt hoặc không phù hợp tệp khách hàng:* trả về Marketing điều chỉnh mục tiêu chiến dịch.
- *Hồ sơ điều kiện thiếu:* quay lại bước bổ sung hồ sơ.
- *Hiển thị sai trên App:* quay ngược về cổng gộp trước bước cấu hình để Kỹ thuật sửa và kiểm thử lại.

---

## 3.2. Quản lý hạng vé máy bay

### 3.2.1. Phương pháp thực hiện

**a) Mô tả quy trình hiện có.** Bằng chứng gồm: (1) danh sách hãng hàng không và các hạng vé thực tế bán trên MoMo, đối chiếu qua nhiều lượt tra cứu trên ứng dụng [5]; (2) sự khác biệt quan sát được giữa hãng nội địa và hãng quốc tế về mức độ chi tiết và độ trễ cập nhật dữ liệu hạng vé, cho thấy tồn tại hai luồng tiếp nhận khác nhau; (3) thông tin công khai về việc MoMo mở rộng danh mục vé và đối tác vận chuyển [15][18]; (4) thông lệ kỹ thuật của các nền tảng phân phối vé về chuẩn hóa fare class trước khi đưa lên kênh bán. Diễn giải 5 bước đã trình bày ở mục 2.2.1.

**b) Sơ đồ tổ chức và trách nhiệm.** Bốn tác nhân, tương ứng 4 làn trong sơ đồ BPMN ở mục 3.2.2:

*Bảng 3.6. Phân định trách nhiệm quy trình Quản lý hạng vé*

| Tác nhân | Trách nhiệm chính | Đầu ra bàn giao |
|---|---|---|
| Hãng bay / NCC | Tạo và cập nhật thông tin hạng vé; cung cấp qua API (quốc tế) hoặc gửi trực tiếp (nội địa) | Dữ liệu hạng vé gốc |
| Bộ phận Business Development (BD) | Tích hợp API, kiểm tra tính đầy đủ, phân tích đối chiếu và chuẩn hóa dữ liệu | Dữ liệu hạng vé đã chuẩn hóa |
| Bộ phận Ticketing (M_Service) | Kiểm tra dữ liệu chuẩn hóa, cấu hình hạng vé lên hệ thống, phê duyệt và công bố, giám sát sau công bố | Hạng vé đã công bố |
| Ứng dụng MoMo | Kiểm tra hiển thị định dạng và cấu trúc dữ liệu hạng vé trên giao diện | Kết quả nghiệm thu hiển thị |

**c) Kế hoạch làm việc.**

*Bảng 3.7. Kế hoạch làm việc nghiên cứu quy trình Quản lý hạng vé*

| Tuần | Công việc | Bộ phận là đối tượng nghiên cứu |
|---|---|---|
| Tuần 1 | Khảo sát danh mục hãng bay và hạng vé hiển thị trên App; xác định phạm vi | Hãng bay/NCC |
| Tuần 2 | Thiết kế bộ câu hỏi khảo sát; dựng mô hình BPMN sơ bộ | BD, Ticketing |
| Tuần 3 | Đối chiếu logic hai luồng quốc tế/nội địa và cơ chế giới hạn số lần thử API | BD, Kỹ thuật |
| Tuần 4 | Rà soát cơ chế phê duyệt – công bố – giám sát; hoàn thiện báo cáo | Ticketing, Ứng dụng MoMo |

**d) Thuật ngữ và sổ tay.**

*Bảng 3.8. Thuật ngữ nghiệp vụ quy trình Quản lý hạng vé*

| Thuật ngữ | Giải nghĩa |
|---|---|
| Hạng vé (fare class) | Nhóm điều kiện giá – quyền lợi – quy định đổi/hoàn gắn với một mức giá của hãng bay |
| Ticketing | Bộ phận chịu trách nhiệm cấu hình, phê duyệt và công bố hạng vé lên hệ thống bán |
| Business Development (BD) | Bộ phận phát triển đối tác, đầu mối tiếp nhận và chuẩn hóa dữ liệu từ hãng bay |
| Tích hợp API | Việc kết nối kỹ thuật để nhận dữ liệu hạng vé real-time từ hệ thống hãng bay |
| Chuẩn hóa dữ liệu hạng vé | Quy đổi thông tin hạng vé từ định dạng riêng của từng hãng về cấu trúc chung của MoMo |
| Giám sát sau công bố | Hoạt động theo dõi hiển thị và giao dịch thực tế sau khi hạng vé đã lên App |
| Tạm hoãn công bố | Quyết định kinh doanh chưa đưa hạng vé ra thị trường dù dữ liệu đã hợp lệ |

**e) Biểu mẫu tác nghiệp.**

1. *Phiếu tiếp nhận hạng vé mới* — Mã hãng / Loại hãng (quốc tế – nội địa) / Số hạng vé / Kênh tiếp nhận / Trạng thái kiểm tra đầy đủ.
2. *Nhật ký tích hợp API* — Mã hãng / Lần thử / Kết quả / Mô tả lỗi / Người xử lý / Trạng thái kết thúc.
3. *Phiếu chuẩn hóa và đối chiếu dữ liệu hạng vé* — Mã hạng vé gốc / Mã hạng vé sau chuẩn hóa / Kết quả đối chiếu / Người thực hiện.
4. *Biên bản phê duyệt công bố hạng vé* — Mã cấu hình / Kết quả kiểm tra hiển thị / Quyết định công bố (Có/Tạm hoãn) / Lý do / Thời điểm công bố.

**f) Bộ câu hỏi phỏng vấn.** Đối tượng dự kiến: Bộ phận BD, Bộ phận Ticketing, Đội Kỹ thuật tích hợp, đại diện hãng bay/NCC.

*Bảng 3.9. Câu hỏi định tính — quy trình Quản lý hạng vé (5 có cấu trúc + 5 không cấu trúc)*

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Nguyên nhân phổ biến nhất khiến tích hợp API với hãng quốc tế thất bại? A. Sai định dạng dữ liệu. B. Xác thực/bảo mật. C. Hạ tầng hãng không ổn định. D. Tài liệu API thiếu. | BD, Kỹ thuật | Nhận diện lỗi tích hợp chủ đạo |
| 2 | Có cấu trúc | Với hãng nội địa, thông tin hạng vé thường thiếu ở hạng mục nào nhất? A. Điều kiện đổi/hoàn. B. Quy định hành lý. C. Mức giá theo giai đoạn. D. Mã hạng vé chuẩn. | BD | Xác định lỗ hổng dữ liệu đầu vào |
| 3 | Có cấu trúc | Giới hạn 2 lần thử lại khi tích hợp API được đánh giá thế nào? A. Quá ít. B. Hợp lý. C. Quá nhiều. D. Nên bỏ giới hạn cứng. | BD, Kỹ thuật | Đánh giá tính phù hợp của quy tắc dừng |
| 4 | Có cấu trúc | Lý do thường gặp nhất khiến Ticketing trả dữ liệu về BD để chuẩn hóa lại? A. Sai mã hạng vé. B. Thiếu điều kiện vé. C. Sai cấu trúc giá. D. Trùng lặp dữ liệu. | Ticketing | Nguyên nhân rework nội bộ |
| 5 | Có cấu trúc | Trường hợp "tạm hoãn công bố" thường xuất phát từ đâu? A. Quyết định kinh doanh. B. Chờ hãng xác nhận lại. C. Rủi ro hiển thị. D. Trùng chiến dịch khác. | Ticketing | Phân biệt dừng kỹ thuật và dừng kinh doanh |
| 6 | Không cấu trúc | Mô tả các bước từ khi hãng phát hành hạng vé mới đến khi hạng vé hiển thị trên App? | BD, Ticketing | Xác thực lại luồng quy trình |
| 7 | Không cấu trúc | Khác biệt lớn nhất về cách làm việc giữa luồng hãng quốc tế và hãng nội địa là gì? | BD | Cơ sở tách hai nhánh trong mô hình |
| 8 | Không cấu trúc | Việc giám sát sau công bố hiện được thực hiện thủ công hay tự động, phát hiện lỗi nhờ đâu? | Ticketing, Kỹ thuật | Mức độ tự động hóa khâu giám sát |
| 9 | Không cấu trúc | Khi phát hiện lỗi hạng vé đã lên App, quy trình xử lý khẩn diễn ra thế nào? | Ticketing | Năng lực phản ứng sự cố |
| 10 | Không cấu trúc | Nếu được cải tiến một khâu duy nhất trong quy trình này, sẽ chọn khâu nào và vì sao? | Tất cả các bộ phận tham gia | Ý kiến cải tiến từ người thực hiện |

*Bảng 3.10. Câu hỏi định lượng — quy trình Quản lý hạng vé (5 có cấu trúc + 5 không cấu trúc)*

| STT | Loại câu hỏi | Câu hỏi cụ thể | Đối tượng áp dụng | Mục tiêu thu thập |
|---|---|---|---|---|
| 1 | Có cấu trúc | Trung bình mỗi tháng tiếp nhận bao nhiêu hạng vé mới/cập nhật? A. <10. B. 10–30. C. 31–60. D. >60. | BD | Khối lượng đầu vào |
| 2 | Có cấu trúc | Tỷ lệ tích hợp API thành công ngay lần đầu? A. <50%. B. 50–70%. C. 71–90%. D. >90%. | BD, Kỹ thuật | Chất lượng tích hợp |
| 3 | Có cấu trúc | Thời gian trung bình từ khi nhận dữ liệu đến khi công bố hạng vé? A. <1 ngày. B. 1–3 ngày. C. 4–7 ngày. D. >7 ngày. | Ticketing | Thời gian chu kỳ tổng |
| 4 | Có cấu trúc | Tỷ lệ hồ sơ hạng vé bị trả về BD để chuẩn hóa lại? A. <10%. B. 10–25%. C. 26–40%. D. >40%. | Ticketing | Tỷ lệ rework |
| 5 | Có cấu trúc | Tỷ lệ hạng vé phát sinh lỗi trong giai đoạn giám sát sau công bố? A. <2%. B. 2–5%. C. 5–10%. D. >10%. | Ticketing | Chất lượng đầu ra |
| 6 | Không cấu trúc | Trung bình mất bao nhiêu giờ công để chuẩn hóa xong dữ liệu của một hãng nội địa? | BD | Chi phí nhân sự khâu chuẩn hóa |
| 7 | Không cấu trúc | Chi phí kỹ thuật ước tính cho một lần tích hợp API với hãng mới là bao nhiêu? | Kỹ thuật | Chi phí đầu tư tích hợp |
| 8 | Không cấu trúc | Trong 12 tháng gần nhất, bao nhiêu trường hợp phải kết thúc vì không tích hợp được API? | BD | Tần suất thất bại tuyệt đối |
| 9 | Không cấu trúc | Bao nhiêu % quyết định "tạm hoãn công bố" cuối cùng vẫn được công bố sau đó? | Ticketing | Tính chất tạm thời của quyết định hoãn |
| 10 | Không cấu trúc | Mỗi tháng phát sinh bao nhiêu khiếu nại của khách hàng liên quan sai thông tin hạng vé? | CSKH | Tác động tới khách hàng cuối |

### 3.2.2. Mô hình hóa quy trình

![](BPMN/PNG/02_Management_QuanLyHangVe.png)

*Hình 3.2. Sơ đồ BPMN quy trình Quản lý hạng vé máy bay (4 làn, 10 cổng điều kiện)*

**Luồng chính:** Hãng phát hành hạng vé mới → phân luồng theo loại hãng → (quốc tế) tích hợp API thành công / (nội địa) BD kiểm tra, phân tích đối chiếu và chuẩn hóa → hai nhánh hội tụ tại cổng gộp → Ticketing kiểm tra dữ liệu chuẩn hóa → cấu hình hạng vé lên hệ thống → App kiểm tra hiển thị hợp lệ → Ticketing phê duyệt và công bố → giám sát sau công bố không phát sinh lỗi → hạng vé hiển thị ổn định.

**Luồng ngoại lệ:**
- *Tích hợp API thất bại:* kiểm tra còn trong giới hạn 2 lần thử — còn thì sửa lỗi và tích hợp lại (vòng lặp), hết thì kết thúc "Không tích hợp được API".
- *Dữ liệu nội địa không đầy đủ:* trả hãng bay chỉnh sửa/bổ sung rồi gửi lại.
- *Dữ liệu chưa chuẩn hóa đúng yêu cầu:* Ticketing trả về BD phân tích đối chiếu lại.
- *Hiển thị không hợp lệ trên App:* rẽ vào cổng gộp xử lý lỗi → Ticketing xử lý và điều chỉnh → kiểm tra hiển thị lại.
- *Quyết định không công bố:* kết thúc ở End Event riêng "Tạm hoãn/Hủy công bố hạng vé", phân biệt rõ với kết thúc do lỗi kỹ thuật.
- *Phát sinh lỗi sau công bố:* quay lại cổng gộp xử lý lỗi, dùng chung nhánh khắc phục với lỗi hiển thị.

---

## 3.3. Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé

### 3.3.1. Phương pháp thực hiện

**a) Mô tả quy trình hiện có.** Kết hợp bốn nguồn: hướng dẫn công khai của MoMo về cách đặt vé và các thông tin cần nhập [1][2][4]; trải nghiệm sử dụng thực tế của nhóm trên tính năng "Du lịch – Đi lại" (ảnh chụp màn hình từng bước) [14]; thông lệ kỹ thuật phổ biến của các nền tảng OTA (bộ đệm dữ liệu giá, truy vấn song song nhiều nhà cung ứng, phiên tìm kiếm có thời hạn); và khung lý thuyết BPM cùng chuẩn BPMN 2.0 [21][22]. Diễn giải 5 bước đã trình bày ở mục 2.2.2.

**b) Sơ đồ tổ chức.** Bốn khối chức năng trực tiếp tham gia, tương ứng 4 làn trong sơ đồ: Khách hàng; Ứng dụng MoMo / Nền tảng Core (dịch vụ tìm kiếm và thanh toán); Bộ phận CSKH / Xử lý ngoại lệ; Hãng bay / GDS.

**c) Kế hoạch làm việc** (6 tuần): thu thập bằng chứng → xây sơ đồ tổ chức → thiết kế câu hỏi khảo sát → mô hình hóa BPMN → phân tích định tính → phân tích định lượng và hoàn thiện báo cáo.

**d) Thuật ngữ và sổ tay:** Bộ đệm (cache) giá & chỗ, Giữ chỗ tạm (hold), Hạng vé (fare class), Khóa giá (price lock), Mã đặt chỗ (PNR), Nguồn tiền, Phiên tìm kiếm, Quy tắc giá hiển thị, Tra soát giao dịch, Xác thực mạnh.

**e) Biểu mẫu:** (1) Phiếu ghi nhận phiên tìm kiếm phục vụ đo lường; (2) Phiếu khảo sát trải nghiệm tìm kiếm chuyến bay; (3) Biểu mẫu báo cáo hiệu năng tìm kiếm định kỳ.

**f) Bộ câu hỏi phỏng vấn.** Đối tượng dự kiến: Đội Sản phẩm Du lịch – Đi lại, Đội Kỹ thuật nền tảng, Đội Phát triển Đối tác hàng không, người dùng cuối đã từng đặt vé trên MoMo.

**A. Định tính — Có cấu trúc:** (1) Đánh giá mức độ đầy đủ của bộ lọc kết quả tìm kiếm? (2) Nguyên nhân chính khiến khách hàng rời bỏ ở màn hình kết quả? (3) Ưu tiên tốc độ phản hồi hay độ tươi mới dữ liệu giá? (4) Khi kết quả trống, hệ thống xử lý theo hướng nào? (5) Mức độ đồng nhất giữa giá hiển thị lúc tìm kiếm và giá thanh toán thực tế?

**B. Định tính — Không cấu trúc:** (1) Mô tả các bước hệ thống thực hiện từ lúc bấm "Tìm kiếm" đến khi hiển thị kết quả? (2) Cơ chế bộ đệm dữ liệu giá/chỗ trống hiện thiết lập thời hạn bao lâu, vì sao? (3) Khó khăn khi hợp nhất kết quả từ nhiều hãng bay có định dạng khác nhau? (4) Mùa cao điểm, đội ngũ ưu tiên xử lý vấn đề nào trước khi hệ thống quá tải? (5) Nếu được đầu tư thêm nguồn lực, sẽ cải tiến điều gì đầu tiên?

**C. Định lượng — Có cấu trúc:** (1) Trung bình mỗi ngày xử lý bao nhiêu phiên tìm kiếm? (<20.000 / 20.000–50.000 / 50.000–100.000 / >100.000) (2) Tỷ lệ phiên phục vụ từ bộ đệm? (<30% / 30–50% / 50–70% / >70%) (3) Thời gian phản hồi trung bình? (<2s / 2–4s / 4–6s / >6s) (4) Tỷ lệ phiên dẫn tới chọn được chuyến bay? (<20% / 20–35% / 35–50% / >50%) (5) Tỷ lệ phiên hết hạn phải làm mới? (<5% / 5–10% / 10–20% / >20%)

**D. Định lượng — Không cấu trúc:** (1) Chi phí bình quân 1 lượt truy vấn tới hãng bay/GDS, gồm những khoản gì? (2) Thời gian phản hồi p95 của từng nhà cung ứng trong 3 tháng gần nhất? (3) Số lượt tìm kiếm trung bình trước khi khách chọn chuyến bay? (4) Tỷ lệ chênh lệch giữa giá hiển thị và giá thanh toán cuối cùng? (5) Nếu tăng tỷ lệ dùng bộ đệm thêm 20 điểm %, chi phí hạ tầng/truy vấn giảm được bao nhiêu?

### 3.3.2. Mô hình hóa quy trình

![](BPMN/PNG/03_Core_TimKiem_DatVe_ThanhToan.png)

*Hình 3.3. Sơ đồ BPMN quy trình Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé (4 làn, 19 cổng điều kiện)*

**Luồng chính:** Khách hàng nhập thông tin tìm kiếm → App truy vấn và hiển thị danh sách chuyến bay → chọn hành trình (khứ hồi/một chiều) → chọn hạng vé và nhập thông tin hành khách → phân luồng nội địa/quốc tế → chọn các tiện ích bổ sung → tạo booking giữ chỗ → còn thời gian giữ vé → xác nhận và thanh toán → thanh toán thành công → M_Service cập nhật vé → gửi vé điện tử → Mua vé thành công.

**Luồng ngoại lệ:**
- *Hết thời gian giữ chỗ:* quay lại bước nhập thông tin tìm kiếm để khách thao tác lại từ đầu.
- *Thanh toán thất bại:* kết thúc "Mua vé thất bại".
- *Giao dịch Pending (treo):* tạo ticket chuyển CSKH → phân cấp VIP (24/7) hoặc thường (giờ hành chính) → liên hệ khách xác nhận còn nhu cầu — không còn thì rollback hoàn tiền và kết thúc "Hủy đơn hàng"; còn nhu cầu thì kiểm tra vé phía hãng bay — vé đã có sẵn thì CSKH xuất vé thủ công, vé chưa có thì giữ chỗ và liên hệ hãng phát hành, sau đó nhập lại luồng thành công.
- *Chuỗi tiện ích bổ sung:* mỗi tiện ích (chỗ ngồi, suất ăn, hành lý, bảo hiểm) là một cặp cổng rẽ – cổng gộp độc lập, cho phép khách chọn hoặc bỏ qua từng dịch vụ mà vẫn hội tụ đúng về một luồng chung trước khi tạo booking. Vé quốc tế đi tắt trực tiếp tới nhánh bảo hiểm.

---

## 3.4. Đổi chuyến bay

### 3.4.1. Phương pháp thực hiện

**a) Mô tả quy trình hiện có.** Bằng chứng gồm: trải nghiệm sử dụng thực tế tính năng "Quản lý đặt chỗ" trên MoMo; hướng dẫn và chính sách công khai của MoMo về hoàn/hủy/đổi vé [10][11]; đối chiếu chính sách đổi vé phổ biến của các hãng hàng không nội địa (phí đổi cố định theo hạng vé, không hoàn phần chênh lệch âm); và suy luận nghiệp vụ dựa trên kiến trúc hệ thống đã mô tả ở quy trình 3.3 (cùng nền tảng Backend MoMo Travel, cùng Cổng thanh toán MoMo, cùng yêu cầu xác thực mạnh [9][13]). Diễn giải 6 bước đã trình bày ở mục 2.2.2.

**b) Sơ đồ tổ chức.** Sáu tác nhân, tương ứng 6 làn: Khách hàng ↔ Giao diện MoMo Client App ↔ Backend MoMo Travel ↔ Cổng Thanh toán MoMo ↔ Bộ phận CSKH MoMo Travel ↔ Hệ thống Hãng bay (CRS/GDS Re-issue API).

**c) Kế hoạch làm việc:** Tuần 1 — thu thập bằng chứng, xác định công thức tính phí đổi; Tuần 2 — thiết kế câu hỏi khảo sát, mô hình hóa BPMN; Tuần 3 — phân tích định tính/định lượng; Tuần 4 — hoàn thiện báo cáo.

**d) Thuật ngữ và sổ tay:** Re-issuance (tái phát hành vé), Fare Rules (quy định điều kiện vé), Hold Time Limit (thời hạn giữ chỗ), Seat Out of Stock (hết chỗ trong lúc xử lý), PNR, EMD.

**e) Biểu mẫu:**
1. *Phiếu tính phí đổi vé* — Mã PNR / Hạng vé cũ / Giá vé cũ / Giá vé mới / Phí đổi cố định Hãng / Chênh lệch giá / Phí dịch vụ MoMo / Tổng phí đổi.
2. *Phiếu xử lý thủ công qua CSKH* — Mã PNR / Lý do không đổi tự động được / Phí hãng báo qua tổng đài / Yêu cầu thanh toán đã gửi / Trạng thái tái xuất vé.
3. *Báo cáo hiệu năng đổi vé định kỳ* — Tổng số ca đổi vé / Tỷ lệ tự động qua API / Tỷ lệ xử lý thủ công / Tỷ lệ hoàn phí do hết chỗ / Thời gian xử lý trung bình mỗi loại.

**f) Bộ câu hỏi phỏng vấn.** Đối tượng dự kiến: Khách hàng, Backend MoMo Travel, CSKH MoMo Travel, Cổng thanh toán, đối tác Hãng bay/GDS.

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
4. Tiêu chí nào quyết định một hạng vé được hoặc không được phép đổi tự động qua API?
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

![](BPMN/PNG/04_Core_DoiChuyenBay.png)

*Hình 3.4. Sơ đồ BPMN quy trình Đổi chuyến bay trên MoMo (6 làn, 10 cổng điều kiện)*

**Luồng chính:** Khách hàng chọn "Đổi chuyến bay" → Backend kiểm tra điều kiện hạng vé gốc → vé được phép đổi → truy vấn lịch bay mới sang GDS → có chuyến phù hợp còn chỗ → khách chọn chuyến mới → tính phí đổi → hỗ trợ đổi tự động qua API → hiển thị bảng phân rã phí → khách đồng ý mức phí → xác nhận điều kiện đổi → xác thực sinh trắc học/OTP thành công → trích tiền phí đổi thành công → tái phát hành tự động qua API → hãng bay hủy chỗ cũ, cấp vé điện tử mới → cập nhật Quản lý đặt chỗ → thông báo và gửi vé mới → Đổi chuyến bay thành công.

**Luồng ngoại lệ:**
- *Vé không được phép đổi:* kết thúc ngay, giữ nguyên vé cũ.
- *Không có chuyến bay phù hợp còn chỗ:* thông báo và kết thúc, giữ nguyên vé cũ.
- *Hạng vé không hỗ trợ đổi tự động:* tạo Support Ticket → CSKH liên hệ hãng kiểm tra phí thủ công và gửi yêu cầu thanh toán → hội tụ trở lại luồng chính tại cổng gộp sau khâu kiểm tra phí.
- *Khách không đồng ý mức phí:* kết thúc "Khách hủy yêu cầu đổi", giữ nguyên vé cũ.
- *Xác thực bảo mật thất bại:* kết thúc "Xác thực thất bại — hủy yêu cầu đổi vé".
- *Trích tiền thất bại:* kết thúc "Đổi vé thất bại do lỗi thanh toán".
- *Kênh tái phát hành thủ công:* sau khi thanh toán thành công, CSKH thao tác tái xuất vé trực tiếp với hãng, rồi hội tụ về cùng bước xử lý của hãng bay như nhánh tự động.
- *Hết chỗ chuyến mới khi đang xử lý Re-issue:* hủy giao dịch thanh toán, hoàn 100% phí đổi về Ví, thông báo giữ nguyên vé cũ và mời khách chọn lại chuyến khác.

---

## 3.5. Hỗ trợ khách hàng và tiếp nhận phản hồi

### 3.5.1. Phương pháp thực hiện

**a) Mô tả quy trình hiện có.** Bằng chứng gồm: hướng dẫn công khai của MoMo về hoàn/hủy vé [10][11], hạn mức giao dịch [12] và xử lý trường hợp chưa nhận được mã đặt chỗ [7]; thông báo chính thức về nâng cấp bảo mật [13]; đối chiếu thông lệ xử lý khiếu nại và tra soát của các nền tảng OTA/ví điện tử; và suy luận dựa trên nghĩa vụ pháp lý của tổ chức trung gian thanh toán [19][20]. Diễn giải 5 bước đã trình bày ở mục 2.2.3.

**b) Sơ đồ tổ chức.** Tính liên phòng ban rõ rệt — Bộ phận CSKH (đầu mối tiếp nhận), Đội Vận hành Sản phẩm Du lịch và Đội Kỹ thuật (xử lý chuyên môn), Bộ phận Tài chính/Pháp chế (khi khiếu nại leo thang), Hãng bay/đối tác (xác minh thông tin đặt chỗ). Sơ đồ BPMN thể hiện 4 làn: Khách hàng, Ứng dụng MoMo, CSKH, Hãng bay/NCC.

**c) Kế hoạch làm việc** (4 tuần): thu thập bằng chứng tình huống ngoại lệ → xây câu hỏi khảo sát và mô hình hóa BPMN → phân tích định tính/định lượng kèm biểu đồ Pareto → phân tích bên liên quan và hoàn thiện báo cáo.

**d) Thuật ngữ và sổ tay:** Ticket tra soát, Giao dịch treo, Lỗi đồng bộ, SLA, Leo thang (Escalation), Hoàn tiền (Refund), CAP, Log hệ thống, Khảo sát hài lòng (CSAT).

**e) Biểu mẫu:** (1) Phiếu ghi nhận và xử lý ticket tra soát giao dịch; (2) Phiếu tiếp nhận và xử lý khiếu nại khách hàng; (3) Báo cáo tổng hợp hậu mãi định kỳ.

**f) Bộ câu hỏi phỏng vấn.** Đối tượng dự kiến: nhân viên/trưởng nhóm CSKH, Đội Vận hành Sản phẩm Du lịch, Đội Kỹ thuật, Bộ phận Tài chính/Pháp chế, khách hàng từng gặp sự cố.

**A. Định tính — Có cấu trúc:** (1) Đánh giá mức độ hài lòng với thời gian xử lý khiếu nại/tra soát? (2) Vấn đề gặp phải thuộc nhóm nào? (Giao dịch treo/Chậm hoàn tiền/Sai lệch thông tin/Chưa nhận vé/Khác) (3) Có nhận thông báo cập nhật tiến độ xử lý không? (4) Kênh liên hệ đã sử dụng là gì? (5) Có phải liên hệ lại nhiều lần để được giải quyết dứt điểm không?

**B. Định tính — Không cấu trúc:** (1) Chia sẻ trải nghiệm cụ thể lần gần nhất gặp sự cố và cách được hỗ trợ? (2) Điều gì khiến khách hàng cảm thấy được tôn trọng khi gặp sự cố dù chưa có kết quả ngay? (3) Mong muốn MoMo cải thiện điều gì nhất trong cách thông báo tiến độ? (4) Đề xuất thay đổi gì trong quy trình xử lý ngoại lệ? (5) Vai trò của tự động hóa (chatbot, dashboard) trong rút ngắn thời gian xử lý?

**C. Định lượng — Có cấu trúc:** (1) Thời gian trung bình đóng 1 ticket tra soát? (<2h / 2–6h / 6–24h / >24h) (2) Tỷ lệ giao dịch treo do lỗi nội bộ so với lỗi hãng bay/đối tác? (<30% / 30–50% / 50–70% / >70% là lỗi nội bộ) (3) Thời gian trung bình hoàn tất 1 yêu cầu hoàn tiền? (<1 ngày / 1–3 ngày / 3–7 ngày / >7 ngày) (4) Tỷ lệ khiếu nại xử lý ngay theo kịch bản chuẩn? (<50% / 50–70% / 70–90% / >90%) (5) Tỷ lệ khiếu nại bị leo thang lần 2? (<5% / 5–10% / 10–20% / >20%)

**D. Định lượng — Không cấu trúc:** (1) Mỗi tháng trung bình bao nhiêu ticket tra soát và bao nhiêu khiếu nại được tiếp nhận? (2) Tỷ lệ khiếu nại có căn cứ hợp lệ sau khi xác minh với hãng bay/đối tác? (3) Chi phí nhân sự trung bình (giờ công) để xử lý 1 ticket/khiếu nại? (4) Điểm khảo sát hài lòng (CSAT) trung bình sau khi ticket được đóng (thang 5)? (5) Nhóm vấn đề nào chiếm tỷ trọng lớn nhất theo phân loại Pareto?

### 3.5.2. Mô hình hóa quy trình

![](BPMN/PNG/05_Support_HoTro_CSKH_TraSoat.png)

*Hình 3.5. Sơ đồ BPMN quy trình Hỗ trợ khách hàng, tiếp nhận phản hồi và tra soát giao dịch (4 làn, 9 cổng điều kiện)*

**Luồng chính:** Khách hàng liên hệ qua tổng đài hoặc App → CSKH tiếp nhận, xác minh và tạo ticket → phân hạng khách VIP/thường → phân tích yêu cầu đủ thông tin → đánh giá phạm vi trách nhiệm → thuộc MoMo thì CSKH xử lý và cung cấp giải pháp trực tiếp → phản hồi khách hàng → khách chấp nhận → đóng ticket, hoàn tất hỗ trợ.

**Luồng ngoại lệ:**
- *Không đủ thông tin:* yêu cầu khách bổ sung, quay lại bước phân tích.
- *Vấn đề thuộc hãng bay/NCC:* chuyển yêu cầu sang hãng → hãng kiểm tra và quyết định chấp nhận hoặc từ chối (kèm lý do) → CSKH ghi nhận kết quả và phản hồi khách.
- *Khách không chấp nhận hướng giải quyết:* CSKH hướng dẫn khiếu nại lên cấp cao hơn, kết thúc "Chuyển sang khiếu nại cấp cao (Pháp chế)".
- *Nhánh tra soát giao dịch lỗi/treo:* đối chiếu dữ liệu nội bộ với xác nhận từ hãng — khớp thì cập nhật lại trạng thái vé; không khớp thì chuyển hướng hoàn tiền hoặc tiếp tục chờ xác nhận từ đối tác.

---

## 3.6. Xuất hóa đơn điện tử (VAT)

### 3.6.1. Phương pháp thực hiện

**a) Mô tả quy trình hiện có.** Bằng chứng gồm: chức năng xuất hóa đơn hiển thị trong chi tiết giao dịch trên ứng dụng; quy định pháp luật về hóa đơn điện tử áp dụng cho giao dịch thương mại điện tử; và nghĩa vụ về hóa đơn, chứng từ của tổ chức trung gian thanh toán [19][20]. Diễn giải 6 bước đã trình bày ở mục 2.2.3.

> **Giả định của nhóm cần lưu ý.** Mốc thời hạn 72 giờ để yêu cầu xuất hóa đơn và việc sử dụng một hệ thống hóa đơn điện tử của đối tác thứ ba là **giả định do nhóm đặt ra** nhằm mô hình hóa đầy đủ các nhánh nghiệp vụ; MoMo không công bố công khai hai thông tin này. Trong sơ đồ BPMN, đối tác phát hành hóa đơn được đặt tên minh họa là "Hệ thống Hóa đơn điện tử". Nếu triển khai thực tế, hai tham số này cần được xác nhận lại với doanh nghiệp.

**b) Sơ đồ tổ chức.** Sáu tác nhân, tương ứng 6 làn: Khách hàng ↔ Ứng dụng MoMo ↔ Hệ thống Core M_Service ↔ Bộ phận CSKH ↔ Bộ phận Kế toán (M_Service) ↔ Hệ thống Hóa đơn điện tử của đối tác.

**c) Kế hoạch làm việc:** Tuần 1 — thu thập bằng chứng, xác định điều kiện/thời hạn xuất VAT; Tuần 2 — thiết kế câu hỏi khảo sát, mô hình hóa BPMN; Tuần 3 — phân tích định tính/định lượng; Tuần 4 — hoàn thiện báo cáo.

**d) Thuật ngữ và sổ tay:** VAT (thuế giá trị gia tăng), Hóa đơn điện tử, Ký số hóa đơn, Đối soát giao dịch, Mã số thuế (MST).

**e) Biểu mẫu:**
1. *Phiếu yêu cầu xuất VAT* — Mã giao dịch/vé / Thông tin công ty (MST, tên, địa chỉ) / Kênh yêu cầu (App/CSKH) / Thời điểm yêu cầu.
2. *Phiếu đối soát dữ liệu xuất hóa đơn* — Mã giao dịch / Kết quả đối chiếu (Khớp/Không khớp) / Người xử lý / Thời gian xử lý.
3. *Báo cáo hiệu năng xuất hóa đơn định kỳ* — Tổng số yêu cầu / Tỷ lệ xuất thành công lần đầu / Tỷ lệ quá hạn / Tỷ lệ lỗi từ hệ thống đối tác / Thời gian xử lý trung bình.

**f) Bộ câu hỏi phỏng vấn.** Đối tượng dự kiến: Bộ phận CSKH, Bộ phận Kế toán, Bộ phận Kỹ thuật (tích hợp hóa đơn điện tử), khách hàng đã yêu cầu xuất hóa đơn.

**A. Định tính — Có cấu trúc:** (1) Đánh giá mức độ dễ sử dụng của form yêu cầu xuất VAT trên App? (2) Nguyên nhân phổ biến nhất khiến yêu cầu xuất hóa đơn bị từ chối? (Quá hạn / Dữ liệu không khớp / Lỗi hệ thống đối tác / Khác) (3) Kênh yêu cầu xuất hóa đơn khách hàng dùng nhiều nhất? (Qua App / Qua CSKH) (4) Mức độ ổn định của kết nối API với hệ thống hóa đơn điện tử? (Rất kém – Kém – Trung bình – Tốt – Rất tốt) (5) Mức độ hài lòng với thời gian nhận được hóa đơn điện tử sau khi yêu cầu?

**B. Định tính — Không cấu trúc:** (1) Mô tả các bước xử lý một yêu cầu xuất hóa đơn từ lúc tiếp nhận đến khi gửi hóa đơn cho khách? (2) Khó khăn nào phát sinh khi dữ liệu giao dịch và dữ liệu xuất hóa đơn không khớp? (3) Cơ sở nào để ấn định thời hạn tiếp nhận yêu cầu xuất VAT? (4) Khi hệ thống hóa đơn điện tử gặp lỗi, đội kỹ thuật ưu tiên xử lý theo hướng nào? (5) Nếu được cải tiến, sẽ ưu tiên thay đổi điều gì trước trong quy trình xuất hóa đơn?

**C. Định lượng — Có cấu trúc:** (1) Tỷ lệ yêu cầu xuất hóa đơn thành công ngay lần đầu? A. <70% B. 70–85% C. 86–95% D. >95% (2) Tỷ lệ yêu cầu bị từ chối do quá hạn? A. <5% B. 5–10% C. 10–20% D. >20% (3) Thời gian trung bình từ lúc yêu cầu đến khi nhận hóa đơn điện tử? A. <10 phút B. 10–30 phút C. 30–60 phút D. >60 phút (4) Tỷ lệ lỗi phát sinh từ phía hệ thống hóa đơn điện tử? A. <2% B. 2–5% C. 5–10% D. >10% (5) Tỷ lệ yêu cầu qua kênh CSKH so với qua App? A. <10% B. 10–25% C. 25–50% D. >50%

**D. Định lượng — Không cấu trúc:** (1) Mỗi tháng có trung bình bao nhiêu yêu cầu xuất hóa đơn VAT? (2) Chi phí vận hành trung bình (nhân sự + phí dịch vụ hóa đơn điện tử) cho mỗi hóa đơn xuất thành công? (3) Thời gian trung bình để CSKH xử lý 1 trường hợp dữ liệu đối soát không khớp? (4) Tỷ lệ khách hàng phải liên hệ lại CSKH sau khi yêu cầu xuất VAT qua App không thành công? (5) Số lượng khiếu nại liên quan đến xuất hóa đơn phát sinh mỗi tháng?

### 3.6.2. Mô hình hóa quy trình

![](BPMN/PNG/06_Support_XuatHoaDon.png)

*Hình 3.6. Sơ đồ BPMN quy trình Tự động hóa xuất hóa đơn điện tử (VAT) (6 làn, 8 cổng điều kiện)*

**Luồng chính:** Khách hàng yêu cầu xuất VAT qua App → hệ thống kiểm tra giao dịch chưa từng yêu cầu → hiển thị form → khách nhập MST, tên công ty, địa chỉ, email → thông tin hợp lệ → Core M_Service kiểm tra còn trong thời hạn → đối soát vé, thanh toán và thông tin hóa đơn khớp → tạo yêu cầu chuyển Kế toán → Kế toán gọi API sang hệ thống hóa đơn điện tử → đối tác tiếp nhận và phát hành thành công → truyền file hóa đơn về MoMo → cập nhật CSDL, App và gửi email → khách hàng xem/tải hóa đơn → Xuất hóa đơn VAT hoàn tất.

**Luồng ngoại lệ:**
- *Giao dịch đã yêu cầu xuất VAT trước đó:* hiển thị thông tin hóa đơn đã xuất và kết thúc.
- *Thông tin nhập không hợp lệ:* quay lại form để khách nhập lại.
- *Kênh tổng đài:* CSKH tiếp nhận và nhập thông tin thay khách, sau đó hội tụ vào luồng chung tại cổng gộp nguồn yêu cầu.
- *Quá thời hạn:* kết thúc "Từ chối do quá thời hạn".
- *Dữ liệu đối soát không khớp:* chuyển CSKH kiểm tra và liên hệ khách xác nhận, cập nhật rồi đối soát lại (vòng lặp).
- *Đối tác tiếp nhận API thất bại:* ghi nhận lỗi, gửi lại hoặc chuyển Kỹ thuật (vòng lặp thử lại).
- *Phát hành hóa đơn thất bại:* cập nhật trạng thái lỗi và báo Kỹ thuật, kết thúc "Xuất VAT thất bại — chuyển Kỹ thuật xử lý".

---

# Chương 4: PHÂN TÍCH CÁC QUY TRÌNH

Chương này phân tích chuyên sâu 3 quy trình (vượt yêu cầu tối thiểu 2 quy trình của đề bài), theo khung: Phân tích quy trình → Phân tích định tính (giá trị gia tăng VA/BVA/NVA + Lãng phí Move/Hold/Overdo) → Phân tích các bên liên quan → Phân tích định lượng (Thời gian / Chất lượng / Chi phí).

**Về nguồn số liệu.** Toàn bộ số liệu định lượng trong chương này là **số liệu giả định mang tính minh họa** do nhóm xây dựng, không phải dữ liệu vận hành do M_Service công bố (xem Tuyên bố về phương pháp ở phần Mở đầu). Mục đích là minh họa cách vận dụng các công thức phân tích quy trình theo khung lý thuyết BPM [21] trên một tình huống nghiệp vụ thực tế.

---

## 4.1. Tìm kiếm, lựa chọn hành trình, thanh toán và xác nhận đặt vé

### 4.1.1. Phân tích quy trình

Quy trình phục vụ trực tiếp mọi khách hàng có nhu cầu đặt vé máy bay trên MoMo, mang lại giá trị cốt lõi là giúp khách hàng tìm kiếm, so sánh và đặt vé nhanh chóng, minh bạch về giá. Kết quả có thể đạt được: khách hàng chọn được chuyến bay phù hợp và hoàn tất đặt vé; hoặc khách hàng rời bỏ do không tìm được kết quả phù hợp hoặc thời gian phản hồi chậm.

### 4.1.2. Phân tích định tính

**a) Phân tích giá trị gia tăng (VA/BVA/NVA)**

*Bảng 4.1. Phân loại giá trị gia tăng 16 hoạt động của quy trình Tìm kiếm – đặt vé*

| # | Hoạt động | Người thực hiện | Loại | Thời gian (giây) | Mô tả | Khắc phục |
|---|---|---|---|---|---|---|
| 1 | Nhập thông tin tìm kiếm hành trình | Khách hàng | VA | 21,5 | Ghi nhận trực tiếp nhu cầu di chuyển — giá trị khách hàng sẵn sàng trả tiền | Ghi nhớ hành trình gần đây, gợi ý tự động điền |
| 2 | So sánh và lọc kết quả tìm kiếm | Khách hàng | BVA | 20,1 | Cần thiết để ra quyết định nhưng bản thân thao tác lọc không tạo giá trị mới | Sắp xếp mặc định theo hành vi lịch sử, giảm số lần lọc thủ công |
| 3 | Chọn hành trình (khứ hồi / một chiều) | Khách hàng | VA | 11,8 | Quyết định cốt lõi của khách hàng | Hiển thị so sánh giá theo ngày lân cận ngay tại bước chọn |
| 4 | Chọn hạng vé | Khách hàng | VA | 8,4 | Xác định quyền lợi và điều kiện vé | Bảng so sánh quyền lợi hạng vé trực quan |
| 5 | Nhập thông tin hành khách | Khách hàng | VA | 14,6 | Dữ liệu bắt buộc để phát hành vé hợp lệ | Lưu hồ sơ hành khách thường dùng, điền tự động |
| 6 | Chọn tiện ích bổ sung (chỗ ngồi, suất ăn, hành lý, bảo hiểm) | Khách hàng | BVA | 12,2 | Tăng doanh thu phụ trợ, nhưng không bắt buộc với giá trị cốt lõi là tấm vé | Gộp thành một màn hình tổng hợp thay vì 4 bước rẽ nhánh liên tiếp |
| 7 | Xác nhận chi tiết đơn hàng | Khách hàng | VA | 1,9 | Chốt giao dịch — bước tạo giá trị cuối cùng phía khách hàng | Tóm tắt đơn hàng rõ ràng, giảm thao tác cuộn |
| 8 | Kiểm tra tính hợp lệ dữ liệu đầu vào | Ứng dụng MoMo | BVA | 0,4 | Kiểm soát chất lượng dữ liệu, khách hàng không nhìn thấy | Ràng buộc đầu vào ngay tại giao diện thay vì kiểm tra sau |
| 9 | Truy vấn song song tới hãng bay / GDS | Nền tảng Core | BVA | 3,5 | Bắt buộc về mặt kỹ thuật để có dữ liệu giá và chỗ trống | Tăng tỷ lệ phục vụ từ bộ đệm, giảm số truy vấn dư thừa |
| 10 | Hợp nhất và chuẩn hóa kết quả từ nhiều nguồn | Nền tảng Core | BVA | 1,8 | Cần thiết vì mỗi hãng trả dữ liệu theo định dạng riêng | Chuẩn hóa định dạng ngay tại lớp tích hợp đối tác |
| 11 | Áp quy tắc giá hiển thị | Nền tảng Core | BVA | 0,9 | Đảm bảo giá hiển thị đúng chính sách đã duyệt | Cache quy tắc giá, chỉ tính lại khi chính sách thay đổi |
| 12 | Tạo booking / giữ chỗ tạm | Nền tảng Core | BVA | 3,2 | Khóa chỗ tránh mất trong lúc thanh toán | Kéo dài hợp lý thời hạn giữ chỗ để giảm phiên hết hạn |
| 13 | Đồng bộ trạng thái giữ chỗ với hãng bay | Nền tảng Core | BVA | 2,6 | Bắt buộc để chỗ được ghi nhận phía hãng | Đồng bộ bất đồng bộ, không chặn luồng người dùng |
| 14 | Hiển thị cảnh báo dữ liệu nhập không hợp lệ | Ứng dụng MoMo | NVA | 1,2 | Chỉ phát sinh khi khách nhập sai — hoạt động sửa lỗi | Ràng buộc định dạng ngay khi gõ, loại bỏ hoàn toàn bước này |
| 15 | Hiển thị thông báo không có kết quả phù hợp | Ứng dụng MoMo | NVA | 0,9 | Ngõ cụt trải nghiệm, không đưa khách tiến gần hơn tới việc đặt vé | Gợi ý chủ động ngày/sân bay lân cận thay vì báo trống |
| 16 | Thông báo phiên giữ chỗ hết hạn, yêu cầu tìm lại | Ứng dụng MoMo | NVA | 2,2 | Buộc khách làm lại toàn bộ thao tác đã thực hiện | Làm mới phiên ngầm, giữ lại tiêu chí tìm kiếm đã nhập |

**Tổng hợp:** quy trình có **5 hoạt động VA (58,2 giây), 8 hoạt động BVA (44,7 giây) và 3 hoạt động NVA (4,3 giây)**, tổng thời gian chu kỳ 107,2 giây. Tỷ lệ giá trị gia tăng theo thời gian = 58,2/107,2 ≈ **54,3%**.

Điểm đáng chú ý: cả 3 hoạt động NVA đều thuộc dạng **sửa lỗi hoặc làm lại**, tức hoàn toàn có thể loại bỏ bằng thiết kế chứ không cần đầu tư hạ tầng — ràng buộc đầu vào tại giao diện, gợi ý chủ động thay vì báo lỗi, và làm mới phiên ngầm.

**b) Phân tích lãng phí (Move/Hold/Overdo)**

*Bảng 4.2. Nhận diện lãng phí quy trình Tìm kiếm – đặt vé*

| Nhóm | Biểu hiện lãng phí | Mức độ | Khắc phục đề xuất |
|---|---|---|---|
| **Move** | Dữ liệu một phiên tìm kiếm phải đi qua 2–4 lượt truyền giữa App → Core → nhà cung ứng → Core → App | ~2–4 lượt/phiên | Gộp truy vấn, giảm số chặng trung gian bằng lớp tổng hợp dữ liệu duy nhất |
| **Hold** | Chờ nhà cung ứng phản hồi truy vấn chuyến bay | ~2,1 giây/phiên | Tăng tỷ lệ phục vụ từ bộ đệm, đặt ngưỡng timeout theo từng nhà cung ứng |
| **Hold** | Chờ làm mới sau khi phiên giữ chỗ hết hạn | ~8% số phiên | Kéo dài thời hạn giữ chỗ; làm mới ngầm giữ nguyên tiêu chí đã nhập |
| **Overdo** | Truy vấn dư thừa tới nhà cung ứng dù dữ liệu trong bộ đệm còn hiệu lực | ~20% số lượt truy vấn | Tinh chỉnh chính sách hết hạn bộ đệm theo tuyến bay và khung giờ |
| **Overdo** | Khách phải nhập lại tiêu chí tìm kiếm dù hệ thống đã có lịch sử hành vi | Mỗi phiên mới | Tự động điền từ hành trình gần nhất |
| **Overdo** | Lặp lại thao tác lọc/sắp xếp nhiều lần trong cùng một phiên | ~1,8 lần/phiên | Sắp xếp mặc định thông minh theo tệp khách hàng |

Nhóm **Overdo chiếm ưu thế** (3/6 biểu hiện): vấn đề chính của quy trình không phải chờ đợi mà là **làm nhiều hơn mức cần thiết**. Điều này thuận lợi cho cải tiến, vì khắc phục chủ yếu nằm ở việc khai thác tốt hơn dữ liệu lịch sử đã có, không đòi hỏi đầu tư hạ tầng lớn.

**c) Phân tích các bên liên quan**

Kỹ thuật chính thức được chọn theo yêu cầu là **sơ đồ xương cá (Fishbone/Ishikawa)** [23], nhằm truy nguyên nguyên nhân gốc rễ của tỷ lệ rời bỏ cao ở màn hình kết quả tìm kiếm. Ba nhóm nguyên nhân tác động lớn nhất:

- **Máy móc – Hệ thống:** thời gian phản hồi p95 lên tới 6,2 giây; bộ đệm hết hạn sớm khiến nhiều phiên phải truy vấn lại từ đầu.
- **Dữ liệu:** giá và tình trạng chỗ trống lệch so với hệ thống hãng bay, dẫn tới chênh lệch giữa giá hiển thị và giá thanh toán.
- **Đo lường:** hệ thống chưa ghi nhận lý do thoát của khách hàng và tỷ lệ chuyển đổi theo từng bộ lọc.

Trong ba nhóm, **Đo lường là nguyên nhân gốc rễ nhất**, vì thiếu dữ liệu đo lường thì không thể xác định chính xác mức độ đóng góp của hai nhóm còn lại, khiến mọi cải tiến đều mang tính phỏng đoán.

Bổ sung tham khảo (không thay thế kỹ thuật chính thức), phân tích theo **Power-Interest Grid** xếp nhóm "Quản lý chặt chẽ" (quyền lực cao – quan tâm cao) gồm: Khách hàng cuối, Đội Sản phẩm Du lịch – Đi lại, và Đội Kỹ thuật nền tảng.

### 4.1.3. Phân tích định lượng

**a) Thời gian**

Thời gian chu kỳ được tính theo quy tắc: các bước tuần tự cộng dồn, các bước có rẽ nhánh lấy trung bình có trọng số theo xác suất nhánh.

- Thời gian chu kỳ: **T_ck ≈ 107,2 giây/phiên**
- Thời gian chờ: **T_chờ ≈ 4,42 giây** (chờ truy vấn nhà cung ứng + sửa dữ liệu nhập sai + làm mới phiên hết hạn)
- Thời gian xử lý: **T_xl = 107,2 − 4,42 ≈ 102,8 giây**
- **Hiệu suất thời gian = T_xl/T_ck = 102,8/107,2 ≈ 95,9%**

Kết luận: nút thắt **không** nằm ở tốc độ hệ thống (chỉ khoảng 4,4 giây độ trễ trên toàn bộ chu kỳ) mà ở **thời gian thao tác của khách hàng** — chiếm 90,5/107,2 ≈ **84,4%** thời gian chu kỳ — và ở **tỷ lệ chuyển đổi thấp (38%)**. Do đó ưu tiên cải tiến nên đặt vào việc rút ngắn thao tác người dùng, không phải tối ưu hạ tầng.

**b) Chất lượng**

*Bảng 4.3. Chỉ số chất lượng quy trình Tìm kiếm – đặt vé*

| # | Chỉ số | Hiện tại | Mục tiêu | Biện pháp cải thiện |
|---|---|---|---|---|
| 1 | Tỷ lệ phiên trả về kết quả | 96% | ≥99% | Gợi ý ngày/sân bay lân cận khi không có kết quả trực tiếp |
| 2 | Tỷ lệ chuyển đổi (phiên → chọn được chuyến) | 38% | ≥50% | Sắp xếp mặc định theo hành vi, giảm số bước lọc |
| 3 | Thời gian phản hồi trung bình | 3,5 giây | ≤2,0 giây | Tăng tỷ lệ phục vụ từ bộ đệm, truy vấn song song |
| 4 | Thời gian phản hồi p95 | 6,2 giây | ≤4,0 giây | Đặt ngưỡng timeout riêng cho từng nhà cung ứng |
| 5 | Tỷ lệ phục vụ từ bộ đệm (cache-hit) | 40% | ≥65% | Tinh chỉnh chính sách hết hạn bộ đệm theo tuyến và khung giờ |
| 6 | Tỷ lệ lệch giá hiển thị so với giá thanh toán | 3,5% | ≤1,0% | Đồng bộ giá theo sự kiện thay vì theo chu kỳ định sẵn |
| 7 | Tỷ lệ phiên giữ chỗ hết hạn phải làm lại | 8% | ≤3% | Kéo dài thời hạn giữ chỗ, làm mới phiên ngầm |
| 8 | Điểm hài lòng khách hàng (CSAT, thang 5) | 4,0 | ≥4,5 | Cải thiện đồng bộ 7 chỉ số trên |

Nếu quy ước mỗi chỉ số đạt mục tiêu tính 1 điểm, quy trình hiện đạt **0/8 chỉ số ở mức mục tiêu**. Điều này cho thấy dư địa cải thiện trải đều trên nhiều mặt chứ không tập trung vào một điểm nghẽn duy nhất — phù hợp với kết luận từ sơ đồ xương cá rằng thiếu hệ thống đo lường là nguyên nhân gốc.

**c) Chi phí**

Quy trình này chạy **tự động hoàn toàn** ở phần hệ thống: các bước xử lý do "Ứng dụng MoMo", "Nền tảng Core" và "Hãng bay/GDS" đảm nhiệm, không có nhân sự MoMo thao tác trực tiếp trong luồng chính. Vì vậy, áp dụng công thức chi phí nhân sự = thời gian × đơn giá lương cho kết quả **≈ 0 đồng/phiên**. Con số này đúng về mặt công thức nhưng không phản ánh bản chất kinh tế của một quy trình đã tự động hóa.

Nhóm bổ sung mô hình **chi phí hạ tầng và truy vấn** làm chỉ số kinh tế chính, phù hợp hơn với bản chất quy trình:

**C = chi phí hạ tầng (6 đ) + chi phí vận hành/ghi log (4 đ) + 0,60 × chi phí truy vấn song song (24 đ) = 24,4 đồng/phiên**

trong đó hệ số 0,60 phản ánh việc 40% số phiên được phục vụ từ bộ đệm nên không phát sinh chi phí truy vấn tới nhà cung ứng.

Ở quy mô 100.000 phiên/ngày: **≈ 2,44 triệu đồng/ngày**, tương đương **≈ 890 triệu đồng/năm**. Nếu nâng tỷ lệ phục vụ từ bộ đệm từ 40% lên 65% (mục tiêu ở Bảng 4.3), hệ số truy vấn giảm từ 0,60 xuống 0,35, chi phí mỗi phiên còn 18,4 đồng — **giảm 24,6%, tiết kiệm khoảng 219 triệu đồng/năm**.

---

## 4.2. Hỗ trợ khách hàng và tiếp nhận phản hồi

### 4.2.1. Phân tích quy trình

Quy trình phục vụ khách hàng gặp sự cố giao dịch (treo/lỗi) hoặc có khiếu nại trong quá trình đặt vé. Giá trị mang lại: khôi phục đúng trạng thái vé hoặc hoàn tiền kịp thời, duy trì niềm tin của khách hàng vào nền tảng. Kết quả có thể đạt được: lỗi được khắc phục nội bộ; vé được cập nhật lại sau xác minh với hãng bay; hoàn tiền do mất chỗ thực sự; khiếu nại được xử lý ngay hoặc sau xác minh; hoặc khiếu nại leo thang lên Bộ phận Tài chính/Pháp chế.

### 4.2.2. Phân tích định tính

**a) Phân tích giá trị gia tăng — Quy trình con 1 (Tra soát giao dịch lỗi/treo)**

*Bảng 4.4. Phân loại giá trị gia tăng — Tra soát giao dịch lỗi/treo*

| Hoạt động | Người thực hiện | Loại giá trị | Mô tả | Khắc phục |
|---|---|---|---|---|
| Ghi nhận ticket tra soát, đánh dấu giao dịch | Đội Vận hành SP Du lịch | BVA | Bước hành chính bắt buộc để kiểm soát xử lý trùng lặp | Tự động tạo ticket khi hệ thống phát hiện bất thường, không cần nhân sự khởi tạo thủ công |
| Kiểm tra log hệ thống nội bộ | Đội Kỹ thuật | VA | Xác định trực tiếp nguyên nhân, quyết định hướng xử lý | Xây dựng dashboard log tự động phân loại lỗi thường gặp |
| Khắc phục và kích hoạt lại luồng xuất vé | Đội Kỹ thuật | VA | Giải quyết trực tiếp vấn đề của khách hàng | Tự động hóa thử lại cho các lỗi timeout đã có mẫu xử lý |
| Liên hệ đối chiếu với hãng bay | Đội Vận hành SP Du lịch | BVA | Cần thiết để xác minh trạng thái thực tế, khách hàng không thấy | Kênh API tra cứu real-time thay vì liên hệ thủ công |
| Phản hồi trạng thái đặt chỗ thực tế | Hãng bay/Đối tác | BVA | Bước xác nhận bắt buộc từ bên ngoài | Thỏa thuận SLA phản hồi tối đa với từng hãng bay |
| Cập nhật lại vé cho khách | Đội Vận hành SP Du lịch | VA | Khôi phục đúng quyền lợi khách hàng | Tự động đồng bộ vé ngay khi có xác nhận từ hãng |
| Khởi tạo hoàn tiền | Đội Vận hành SP Du lịch | VA | Đảm bảo quyền lợi tài chính khi mất chỗ thực sự | Tự động hóa hoàn tiền ngay khi xác định đủ điều kiện |
| Thông báo kết quả và đóng ticket | Đội Vận hành SP Du lịch | VA | Hoàn tất vòng đời xử lý, thông báo cho khách hàng | Gửi thông báo đa kênh (app/SMS/email) đồng thời |

**b) Phân tích giá trị gia tăng — Quy trình con 2 (Xử lý khiếu nại khách hàng)**

*Bảng 4.5. Phân loại giá trị gia tăng — Xử lý khiếu nại khách hàng*

| Hoạt động | Người thực hiện | Loại giá trị | Mô tả | Khắc phục |
|---|---|---|---|---|
| Tiếp nhận, phân loại và tạo ticket | CSKH | BVA | Bước phân luồng bắt buộc | Chatbot phân loại sơ bộ trước khi chuyển nhân sự |
| Xử lý trực tiếp và phản hồi khách | CSKH | VA | Giải quyết ngay theo kịch bản chuẩn | Mở rộng danh mục kịch bản xử lý nhanh |
| Liên hệ xác minh với hãng bay/đối tác | Đội Vận hành SP Du lịch | BVA | Cần thiết cho khiếu nại phức tạp, khách hàng không thấy | Ưu tiên kênh xác minh tự động (API) |
| Đề xuất và thực hiện phương án xử lý | Đội Vận hành SP Du lịch | VA | Mang lại quyền lợi thực tế cho khách hàng có căn cứ | Chuẩn hóa khung phương án theo từng loại khiếu nại |
| Soạn phản hồi từ chối | Đội Vận hành SP Du lịch | NVA | Chỉ phát sinh khi khiếu nại không có căn cứ, không tạo giá trị mới | Mẫu phản hồi chuẩn kèm giải thích rõ ràng, giảm thời gian soạn thảo |
| Xem xét theo quy định bảo vệ người tiêu dùng | Bộ phận Tài chính/Pháp chế | VA | Bảo vệ quyền lợi khách hàng ở mức cao nhất khi leo thang | Quy trình leo thang có SLA rõ ràng |
| Đóng ticket và khảo sát hài lòng | CSKH | BVA | Hoàn tất vòng đời, đo lường chất lượng dịch vụ | Khảo sát tự động ngay sau khi đóng ticket |

**c) Phân tích lãng phí (Move/Hold/Overdo)**

Cả hai quy trình con đều xuất hiện đủ ba nhóm lãng phí:

- **Hold** — chờ hãng bay/đối tác phản hồi xác minh. Đây là **điểm nghẽn chính** và nằm ngoài tầm kiểm soát trực tiếp của MoMo.
- **Move** — trao đổi thông tin ticket thủ công giữa CSKH, Vận hành và Kỹ thuật qua email/điện thoại, dễ sai lệch và thất lạc ngữ cảnh.
- **Overdo** — áp dụng quy trình xác minh/chẩn đoán đầy đủ cho cả những trường hợp lặp lại đã có tiền lệ xử lý rõ ràng.

Khắc phục chung: hệ thống case-management dùng chung theo thời gian thực; kênh API xác minh tự động với hãng bay; và cơ sở tri thức (knowledge base) cho các lỗi/khiếu nại thường gặp.

**d) Phân tích các bên liên quan**

Kỹ thuật chính thức được chọn là **biểu đồ Pareto**, trình bày ở mục 4.2.3 (phân loại 9 nhóm vấn đề hậu mãi theo tần suất).

Bổ sung tham khảo theo **Power-Interest Grid**: nhóm "Quản lý chặt chẽ, phối hợp thường xuyên" gồm Ban điều hành mảng Du lịch – Đi lại và Đội Vận hành Sản phẩm Du lịch; nhóm "Giữ hài lòng" gồm Bộ phận Tài chính/Pháp chế và cơ quan quản lý nhà nước; nhóm "Thông tin thường xuyên" gồm CSKH, khách hàng cuối và hãng bay/đối tác.

### 4.2.3. Phân tích định lượng

*Bảng 4.6. Chỉ số định lượng hai quy trình con hậu mãi*

| Chỉ số | Quy trình 1 (Tra soát) | Quy trình 2 (Khiếu nại) |
|---|---|---|
| Thời gian chu kỳ (T_ck) | ≈ 5,8 giờ | ≈ 4,23 giờ |
| Hiệu suất thời gian | ≈ 69,0% | ≈ 43,3% |
| Chi phí xử lý 1 ca | ≈ 301.000 đồng | ≈ 123.500 đồng |
| Chất lượng | 55% lỗi nội bộ khắc phục ngay; 27% phải hoàn tiền; 80% xong trong SLA 8 giờ | 60% xử lý ngay theo kịch bản; 55% có căn cứ hợp lệ; 5,4% leo thang; CSAT ≈ 4,1/5 |

Công thức thời gian áp dụng đúng quy tắc: các bước tuần tự cộng dồn, nhánh XOR lấy trung bình có trọng số theo xác suất. Ví dụ với Quy trình 2:

**T_ck = 0,3 + 0,6×0,5 + 0,4×[1 + 6 + 0,55×1 + 0,45×(0,5 + 0,3×4)] + 0,3 ≈ 4,23 giờ**

Hiệu suất thời gian thấp hơn hẳn ở Quy trình 2 (43,3% so với 69,0%) xác nhận rằng **thời gian chờ hãng bay/đối tác phản hồi (nhóm Hold) là điểm nghẽn nghiêm trọng nhất của toàn mảng hậu mãi**.

**Phân tích Pareto.** Trên 590 ticket/khiếu nại minh họa trong một quý, 9 nhóm vấn đề được xếp theo tần suất giảm dần. Bốn nhóm đầu — trừ tiền chưa xuất vé (31,5%), chậm hoàn tiền (21,0%), sai lệch thông tin (16,6%) và không nhận được vé điện tử (10,3%) — cộng lại chiếm **79,4%** tổng số vụ việc. Kết quả này phù hợp với nguyên tắc 80/20: tập trung xử lý bốn nhóm nguyên nhân đầu sẽ giải quyết được gần bốn phần năm khối lượng công việc hậu mãi, đúng với hướng ưu tiên cải tiến đã đề xuất ở mục 4.2.2.

---

## 4.3. Quản trị giá, khuyến mãi và chính sách hiển thị giá

### 4.3.1. Phân tích quy trình

Quy trình mang lại giá trị cho cả khách hàng cuối (giá minh bạch, khuyến mãi hấp dẫn) và nội bộ MoMo (kiểm soát rủi ro tài chính/pháp lý trước khi công bố giá). Kết quả có thể đạt được: chính sách giá/KM được phê duyệt và công bố thành công; hoặc bị hủy/từ chối do không đạt thẩm định rủi ro hoặc hồ sơ điều kiện không đầy đủ.

### 4.3.2. Phân tích định tính

**a) Phân tích giá trị gia tăng**

Quy trình gồm 23 hoạt động, phân loại thành **4 VA, 14 BVA và 5 NVA**. Cả 5 hoạt động NVA đều là các bước làm lại (rework): yêu cầu bổ sung dữ liệu, trả lại chuẩn hóa, điều chỉnh mục tiêu chiến dịch, bổ sung hồ sơ pháp lý, và sửa cấu hình lỗi.

*Bảng 4.7. Phân loại giá trị gia tăng quy trình Quản trị giá*

| Hoạt động | Người thực hiện | Loại | Mô tả | Khắc phục |
|---|---|---|---|---|
| Gửi / Tiếp nhận / Kiểm tra dữ liệu giá gốc | Hãng bay–NCC / Bộ phận Giá | BVA | Đầu vào bắt buộc, chưa tạo giá trị trực tiếp cho khách | Chuẩn hóa định dạng dữ liệu đầu vào bắt buộc từ hãng bay |
| Yêu cầu bổ sung dữ liệu (nếu thiếu) | Bộ phận Giá | NVA | Phát sinh do dữ liệu đầu vào không đạt chuẩn ngay từ đầu | Cổng thông tin cho hãng bay tự kiểm tra hợp lệ trước khi gửi |
| Chuẩn hóa giá/thuế/phí và kiểm tra | Bộ phận Giá | BVA | Đảm bảo dữ liệu đồng nhất trước khi dùng | Rule Engine tự động chuẩn hóa theo công thức thuế chuẩn |
| Trả lại điều chỉnh chuẩn hóa (nếu sai) | Bộ phận Giá | NVA | Làm lại do sai công thức tính | Kiểm tra chéo (Maker-Checker) trước khi chuyển tiếp |
| Phân tích tệp KH và mục tiêu chiến dịch | Marketing | BVA | Chuẩn bị cơ sở cho quyết định KM, khách hàng chưa thấy | Hệ thống CRM/BI hỗ trợ phân tích tự động |
| Xây dựng chính sách giá/KM | Marketing | VA | Tạo ra ưu đãi cụ thể mang lại giá trị cho khách | Thư viện mẫu cơ chế KM đã duyệt sẵn |
| Thiết kế cơ chế KM và điều kiện | Marketing | VA | Hoàn thiện sản phẩm ưu đãi cuối cùng | Template hồ sơ điều kiện chuẩn hóa |
| Điều chỉnh đối tượng/mục tiêu (nếu không phù hợp) | Marketing | NVA | Làm lại do đánh giá sai tệp khách hàng ban đầu | Kiểm tra độ phù hợp bằng dữ liệu hành vi trước khi thiết kế |
| Thẩm định tài chính và kiểm tra hồ sơ | Tài chính/Pháp chế | BVA | Kiểm soát rủi ro, khách hàng không thấy trực tiếp | Checklist pháp lý chuẩn để Marketing tự rà trước |
| Yêu cầu bổ sung hồ sơ (nếu thiếu) | Tài chính/Pháp chế | NVA | Làm lại do hồ sơ Marketing gửi chưa đủ | Template hồ sơ điều kiện đã duyệt sẵn |
| Cấu hình thuật toán giá và hiển thị | Kỹ thuật | VA | Đưa chính sách vào vận hành thực tế | Unit test tự động trước khi lên môi trường thật |
| Ghi nhận / lưu trữ dữ liệu | App MoMo | BVA | Bước kỹ thuật nền tảng | Tự động hóa hoàn toàn, không cần can thiệp thủ công |
| Kiểm tra hiển thị (UAT) | Kỹ thuật / App | BVA | Đảm bảo chất lượng trước khi ra mắt | Kiểm thử tự động quét giao diện |
| Yêu cầu chỉnh sửa cấu hình (nếu lỗi) | Kỹ thuật | NVA | Làm lại do lỗi cấu hình/hiển thị | Unit test và kiểm thử tự động |
| Công bố giá/KM chính thức | Kỹ thuật | VA | Đưa giá trị đến tay người dùng cuối | Bước cuối, đã tối ưu |
| Hiển thị thành công đến người dùng | App MoMo | VA | Hoàn tất giá trị cốt lõi của quy trình | Giám sát tự động, cảnh báo sớm nếu lỗi hiển thị |

**b) Phân tích lãng phí (Move/Hold/Overdo)**

*Bảng 4.8. Nhận diện lãng phí quy trình Quản trị giá*

| Nhóm | Liệt kê | Mô tả | Khắc phục |
|---|---|---|---|
| **Move** | Hồ sơ giá/KM luân chuyển qua 5 khâu thủ công: Hãng bay → Bộ phận Giá → Marketing → Tài chính/Pháp chế → Kỹ thuật | Mỗi lần bàn giao đều qua email/file rời rạc, dễ thất lạc hoặc sai phiên bản, không có hệ thống theo dõi trạng thái tập trung | Nền tảng quản lý luồng phê duyệt (BPM Software) dùng chung, hiển thị trạng thái theo thời gian thực cho mọi bên |
| **Hold** | Chờ hãng bay gửi lại dữ liệu bổ sung; chờ Marketing sửa cơ chế KM khi bị từ chối; chờ Kỹ thuật rà soát khi kiểm thử lỗi | Tăng đáng kể thời gian chu kỳ, có thể bỏ lỡ thời điểm vàng (time-to-market) của chiến dịch | SLA phản hồi nội bộ và với đối tác rõ ràng; cảnh báo tự động khi ticket quá hạn |
| **Overdo** | Chuẩn hóa thuế/phí thủ công lặp lại cho từng hãng bay; soạn lại hồ sơ điều kiện KM từ đầu dù cấu trúc tương tự | Tốn thời gian nhân sự cho tác vụ lặp, tăng nguy cơ sai sót con người | ETL tự động chuẩn hóa cấu trúc giá; thư viện template cho các loại hình KM chuẩn |
| **Overdo** | Cấu hình sai tham số dẫn đến phải sửa lại; hồ sơ pháp lý thiếu chặt chẽ bị bác | Lãng phí toàn bộ nỗ lực các bước trước, đe dọa doanh thu và uy tín nếu lọt ra môi trường thật | Maker-Checker bắt buộc; kiểm thử tự động rà soát giao diện trước nghiệm thu |

**c) Phân tích các bên liên quan**

Sáu bên liên quan chính: **Khách hàng** (mong giá minh bạch, mã KM dễ hiểu — rủi ro rời bỏ nếu giá bị "độn" lúc thanh toán); **Hãng bay/NCC** (mong chính sách giá được tuân thủ đúng — rủi ro tranh chấp nếu bán sai giá gốc); **Bộ phận Giá** (áp lực xử lý khối lượng dữ liệu lớn, dễ sai sót thủ công); **Marketing** (mong phê duyệt nhanh — hay xung đột với Pháp chế); **Tài chính/Pháp chế** (kiểm soát ngân sách và pháp lý — dễ trở thành điểm nghẽn); **Kỹ thuật/Growth** (mong yêu cầu rõ ràng — rủi ro lỗi ẩn khi kết hợp nhiều chính sách).

**Biểu đồ Pareto** trên 85 điểm ghi nhận vấn đề:

*Bảng 4.9. Phân tích Pareto các vấn đề quy trình Quản trị giá*

| Nhóm vấn đề | Tỷ trọng | Lũy kế |
|---|---|---|
| Hồ sơ pháp lý/điều kiện KM không chặt chẽ | 29,41% | 29,41% |
| Dữ liệu đầu vào thiếu sót | 23,53% | 52,94% |
| Lỗi cấu hình kỹ thuật | 17,65% | 70,59% |
| Mâu thuẫn cơ chế khuyến mãi | 17,65% | 88,24% |
| Sai chuẩn hóa cấu trúc giá | 11,76% | 100,00% |

Áp dụng nguyên tắc 80/20: ba nhóm đầu (lũy kế 70,59%) là ưu tiên cải tiến hàng đầu.

### 4.3.3. Phân tích định lượng

**a) Thời gian**

Thời gian theo luồng thuận lợi (Happy Path) = **940 phút (≈ 15,6 giờ)**.

Với các nhánh phải làm lại, thời gian chu kỳ tuân theo công thức vòng lặp **CT = T/(1−r)**, trong đó T là thời gian thực hiện một lượt và r là xác suất phải làm lại. Từ đó, **thời gian trễ tăng thêm do làm lại** của mỗi nhánh là:

**T_trễ = CT − T = T/(1−r) − T = T × r/(1−r)**

*Bảng 4.10. Thời gian trễ do làm lại theo từng nhánh*

| Nhánh làm lại | r (xác suất) | T (phút) | Cách tính cũ (r×T) | Cách tính đúng: T × r/(1−r) |
|---|---|---|---|---|
| Bổ sung dữ liệu Hãng bay | 20% | 60 | 12,0 | **15,00** |
| Sai chuẩn hóa | 10% | 45 | 4,5 | **5,00** |
| Sai mục tiêu Marketing | 15% | 120 | 18,0 | **21,18** |
| Thiếu hồ sơ pháp lý | 25% | 90 | 22,5 | **30,00** |
| Lỗi cấu hình phải sửa | 15% | 90 | 13,5 | **15,88** |
| **Tổng thời gian trễ** | | | 70,5 | **≈ 87,06** |

Cách tính cũ (chỉ nhân xác suất với thời gian) bỏ sót khả năng một nhánh phải làm lại nhiều hơn một lần; công thức vòng lặp khắc phục điều này.

- Thời gian chu kỳ trung bình = 940 + 87,06 ≈ **1.027,06 phút (≈ 17,1 giờ)**
- Thời gian tạo giá trị (VA) = **465 phút**
- **Hiệu suất chu kỳ quy trình PCE = 465/1.027,06 × 100% ≈ 45,28%**

Nghĩa là hơn một nửa thời gian của quy trình bị tiêu tốn cho kiểm duyệt, chuẩn hóa và chờ đợi.

**b) Chất lượng**

Tỷ lệ chất lượng xuyên suốt quy trình (Rolled Throughput Yield):

**RTY = 80% × 90% × 85% × 75% × 85% ≈ 39,01%**

Chỉ khoảng 39% số chiến dịch được thiết lập hoàn hảo ngay từ lần đầu, không phải quay lại bất kỳ khâu nào. Hướng khắc phục theo thứ tự tác động: nâng chất lượng đầu vào (80% → 95%) bằng kiểm tra hợp lệ tự động; nâng chất lượng hồ sơ pháp lý (75% → 95%) bằng checklist bắt buộc; nâng chất lượng cấu hình (85% → 98%) bằng unit test tự động.

**c) Chi phí**

Khác với quy trình ở mục 4.1, quy trình này có nhân sự thao tác trực tiếp ở hầu hết các bước, nên mô hình chi phí = thời gian × đơn giá lương là phù hợp.

- Chi phí nhân công theo Happy Path ≈ **1.413.600 đồng/chiến dịch**
- Chi phí cho các hoạt động tạo giá trị (VA) = Marketing (300 phút × 1.440 đ/phút) + Kỹ thuật (160 phút × 2.000 đ/phút) = 432.000 + 320.000 = **752.000 đồng**
- **Hiệu suất chi phí = 752.000/1.413.600 × 100% ≈ 53,2%**

Gần một nửa chi phí nhân sự được chi cho các hoạt động kiểm tra, rà soát và đối chiếu — chưa tính chi phí cơ hội do thời gian trễ 87 phút mỗi chiến dịch.

---

# Chương 5: KẾT LUẬN

## 5.1. Kết quả đạt được

Đồ án đã xây dựng sơ đồ kiến trúc quy trình nghiệp vụ mảng đặt vé máy bay trên MoMo theo ba nhóm Quản lý – Cốt lõi – Hỗ trợ với tổng cộng 10 quy trình. Trong đó, 6 quy trình đại diện được mô hình hóa chi tiết bằng BPMN 2.0:

- **Quản lý:** Quản trị giá – khuyến mãi và chính sách hiển thị giá; Quản lý hạng vé máy bay.
- **Cốt lõi:** Tìm kiếm – lựa chọn hành trình – thanh toán và xác nhận đặt vé; Đổi chuyến bay.
- **Hỗ trợ:** Hỗ trợ khách hàng và tiếp nhận phản hồi; Tự động hóa xuất hóa đơn điện tử (VAT).

Ba trong số sáu quy trình trên tiếp tục được phân tích sâu theo hai lăng kính định tính và định lượng: Tìm kiếm – đặt vé, Hỗ trợ khách hàng, và Quản trị giá.

Kết quả phân tích cho thấy một số mẫu hình chung, lặp lại xuyên suốt nhiều quy trình khác nhau của mảng đặt vé máy bay:

- **Giá trị gia tăng tập trung ở khâu ra quyết định của khách hàng và khâu xử lý dữ liệu**, trong khi phần lớn hoạt động không tạo giá trị (NVA) đều là các bước sửa lỗi hoặc làm lại, có thể loại bỏ bằng thiết kế lại quy trình hoặc bổ sung kiểm soát chất lượng đầu vào. Ví dụ, quy trình Tìm kiếm – đặt vé ghi nhận 5 hoạt động VA, 8 hoạt động BVA và 3 hoạt động NVA, trong đó cả 3 NVA đều thuộc dạng sửa lỗi; quy trình Quản trị giá có 5 hoạt động NVA thì cả 5 đều là bước làm lại.
- **Lãng phí chủ yếu thuộc hai nhóm Hold và Overdo.** Nhóm Hold — thời gian chờ phản hồi hoặc xác minh từ hãng bay và đối tác bên ngoài — xuất hiện lặp lại ở cả quy trình hậu mãi (chờ xác minh giao dịch lỗi) lẫn quy trình quản trị đối tác (chờ đối tác phản hồi kế hoạch khắc phục). Đây là dạng lãng phí nằm ngoài tầm kiểm soát trực tiếp của MoMo. Ngược lại, nhóm Overdo — áp dụng quy trình kiểm soát đầy đủ cho cả những trường hợp đã có tiền lệ xử lý — hoàn toàn có thể cải thiện bằng nội lực.
- **Hiệu suất thời gian chênh lệch lớn giữa các quy trình tùy theo mức độ lệ thuộc bên ngoài.** Quy trình Tìm kiếm – đặt vé (chủ yếu xử lý nội bộ, gọi API song song) đạt hiệu suất thời gian khoảng 95,9%; trong khi các quy trình có bước chờ đối tác phản hồi chỉ đạt khoảng 43–69%. Điều này cho thấy nút thắt lớn nhất của hệ thống không nằm ở năng lực xử lý nội bộ của MoMo mà ở tốc độ phối hợp với các đối tác bên ngoài.
- **Nguyên nhân gốc rễ được xác định qua phân tích Pareto và sơ đồ xương cá** đều quy về một số nhóm lặp lại: thiếu chuẩn hóa và tự động hóa trong trao đổi dữ liệu với đối tác; thiếu SLA nội bộ rõ ràng; và hạn chế trong hệ thống đo lường, giám sát vận hành theo thời gian thực.

## 5.2. Hạn chế của đồ án

- Do không tiếp cận được dữ liệu vận hành nội bộ và không có điều kiện phỏng vấn trực tiếp nhân sự của M_Service, **toàn bộ số liệu định lượng trong báo cáo là số liệu minh họa/giả định của nhóm**, được xây dựng dựa trên bằng chứng gián tiếp (trải nghiệm sử dụng ứng dụng thực tế, tài liệu hướng dẫn công khai của MoMo, quy định của Ngân hàng Nhà nước, và đối chiếu thông lệ ngành thương mại điện tử/OTA) thay vì số liệu vận hành chính thức. Các bộ câu hỏi ở Chương 3 vì vậy là công cụ khảo sát đã thiết kế nhưng chưa được triển khai thực tế.
- Mô hình BPMN phản ánh cách nhóm hiểu quy trình dựa trên bằng chứng công khai, có thể khác biệt so với thiết kế thực tế bên trong hệ thống của MoMo — đặc biệt ở các bước kỹ thuật nội bộ như cơ chế bộ đệm dữ liệu giá, cách điều phối truy vấn nhà cung ứng, và logic xử lý ngoại lệ chi tiết.
- Một số tham số nghiệp vụ trong mô hình là giả định do nhóm đặt ra vì doanh nghiệp không công bố công khai — cụ thể là mốc thời hạn 72 giờ để yêu cầu xuất hóa đơn VAT, việc sử dụng một hệ thống hóa đơn điện tử của đối tác thứ ba, và giới hạn 2 lần thử lại khi tích hợp API hạng vé. Những tham số này đã được ghi chú rõ tại nơi sử dụng và cần được xác nhận lại nếu triển khai thực tế.
- Phạm vi phân tích định lượng chỉ bao phủ 3 trong 10 quy trình đã liệt kê; 7 quy trình còn lại mới dừng ở mức mô tả và (với 3 quy trình) mô hình hóa BPMN.

## 5.3. Hướng phát triển

- Nếu có điều kiện tiếp cận phỏng vấn trực tiếp các đội ngũ vận hành liên quan (CSKH, Vận hành Sản phẩm Du lịch, Bộ phận Quản lý Giá, Tài chính/Pháp chế), nhóm có thể triển khai các bộ câu hỏi đã thiết kế ở Chương 3 để hiệu chỉnh lại số liệu định lượng và mô hình BPMN cho sát thực tế vận hành hơn, đồng thời xác thực các giả định đã đặt ra.
- Mở rộng phạm vi mô hình hóa và phân tích sâu sang các quy trình còn lại — đặc biệt là Quản trị danh mục hãng bay và đối tác nhà cung ứng, Mua thêm dịch vụ sau đặt chỗ, và Quản lý vé đã mua — để có bức tranh đầy đủ về toàn bộ mảng đặt vé máy bay.
- Xây dựng mô hình "To-Be" cho các quy trình đã phân tích, lượng hóa mức cải thiện dự kiến của từng đề xuất (ví dụ: tác động của việc nâng tỷ lệ phục vụ từ bộ đệm lên 65% tới chi phí truy vấn, hay tác động của Maker-Checker tới chỉ số RTY).
- Ưu tiên triển khai các đề xuất cải tiến có chi phí thấp và nằm hoàn toàn trong tầm kiểm soát nội bộ của MoMo trước (bổ sung hệ thống đo lường hành vi người dùng, chuẩn hóa checklist và SLA nội bộ), sau đó mới đến các cải tiến phụ thuộc sự phối hợp của hãng bay/đối tác bên ngoài — vì đây là nhóm lãng phí (Hold) khó kiểm soát trực tiếp nhất theo phát hiện xuyên suốt đồ án.

---

# TÀI LIỆU THAM KHẢO

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

**Báo chí và trang tin thứ ba**

14. Tinh tế. *Dùng thử tính năng "Du lịch – Đi lại" trên Ví MoMo.* https://tinhte.vn/thread/dung-thu-tinh-nang-du-lich-di-lai-tren-vi-momo.3235308/
15. Người Đô Thị. *MoMo ra mắt tính năng "Du lịch - Đi lại" giúp việc mua vé máy bay, vé tàu, xe khách cực dễ.* https://nguoidothi.net.vn/momo-ra-mat-tinh-nang-du-lich-di-lai-giup-viec-mua-ve-may-bay-ve-tau-xe-khach-cuc-de-26496.html
16. Điện Máy Chợ Lớn. *Hướng dẫn cách đặt vé máy bay Vietnam Airlines bằng MoMo.* https://dienmaycholon.com/kinh-nghiem-mua-sam/huong-dan-cach-dat-ve-may-bay-vietnam-airlines-bang-momo-don-gian-de-thuc-hien
17. Thế Giới Di Động. *Cách đặt mua vé máy bay Vietnam Airlines thông qua MoMo cực kỳ tiện lợi.* https://www.thegioididong.com/game-app/cach-dat-mua-ve-may-bay-vietnam-airlines-thong-qua-momo-cuc-ky-tien-loi-1259463
18. Thanh Niên. *MoMo thêm tính năng mua vé tàu xe tết, trả tiền sau.* https://thanhnien.vn/momo-them-tinh-nang-mua-ve-tau-xe-tet-tra-tien-sau-1851414853.htm

**Văn bản pháp luật**

19. Ngân hàng Nhà nước Việt Nam. *Thông tư số 17/2024/TT-NHNN quy định việc mở và sử dụng tài khoản thanh toán tại tổ chức cung ứng dịch vụ thanh toán.*
20. Ngân hàng Nhà nước Việt Nam. *Thông tư số 23/2019/TT-NHNN sửa đổi, bổ sung một số điều của Thông tư số 39/2014/TT-NHNN hướng dẫn về dịch vụ trung gian thanh toán.*

**Tài liệu học thuật và khung lý thuyết**

21. Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of Business Process Management* (2nd ed.). Springer.
22. Object Management Group (OMG). (2013). *Business Process Model and Notation (BPMN), Version 2.0.2.*
23. Ishikawa, K. (1985). *Guide to Quality Control.* Asian Productivity Organization.
24. CellPhoneS. *Tìm hiểu hệ thống quy trình nghiệp vụ của công ty CellphoneS* (tài liệu tham khảo mẫu của giảng viên).

---

# DANH MỤC TỪ VIẾT TẮT

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
| KM | — | Khuyến mãi — chương trình ưu đãi/giảm giá |
| KPI | Key Performance Indicator | Chỉ số hiệu năng chính |
| KYB | Know Your Business | Xác minh thông tin pháp lý/năng lực tổ chức đối tác |
| MST | — | Mã số thuế |
| NCC | — | Nhà cung cấp |
| NHNN | — | Ngân hàng Nhà nước Việt Nam |
| NVA | Non-Value Adding | Hoạt động không tạo giá trị |
| OTA | Online Travel Agency | Đại lý du lịch trực tuyến |
| PCE | Process Cycle Efficiency | Hiệu suất chu kỳ quy trình (tỷ lệ thời gian tạo giá trị) |
| PNR | Passenger Name Record | Mã hồ sơ đặt chỗ hành khách |
| RTY | Rolled Throughput Yield | Tỷ lệ chất lượng xuyên suốt quy trình (không lỗi từ đầu đến cuối) |
| SLA | Service Level Agreement | Thỏa thuận mức cam kết dịch vụ |
| T&C | Terms & Conditions | Điều khoản và điều kiện áp dụng |
| UAT | User Acceptance Testing | Kiểm thử nghiệm thu người dùng |
| VA | Value Adding | Hoạt động tạo giá trị trực tiếp cho khách hàng |
| VAT | Value Added Tax | Thuế giá trị gia tăng |

---

# BẢNG PHÂN CÔNG CÔNG VIỆC NHÓM

| STT | MSSV | Họ và tên | Vai trò | Nhiệm vụ và đóng góp cụ thể |
|---|---|---|---|---|
| 1 | 25410175 | Đinh Xuân Bảo | Nhóm trưởng | Quản lý tiến độ đồ án, tổng hợp và biên tập báo cáo chính, rà soát toàn diện; xây dựng 5 sơ đồ BPMN gốc (Quản trị giá, Quản lý hạng vé, Tìm kiếm vé, Mua thêm dịch vụ, Xuất hóa đơn) |
| 2 | 25410167 | Vũ Thị Nhân Ái | Thành viên | Thu thập tài liệu quy định pháp lý (Thông tư NHNN về ví điện tử và trung gian thanh toán), rà soát thuật ngữ chuyên ngành và chính sách thuế VAT trong thương mại điện tử |
| 3 | 25410168 | Phạm Ngọc Bảo An | Thành viên | Thiết kế khung câu hỏi phỏng vấn chuẩn 2×2, xây dựng khung phân tích giá trị gia tăng (VA/BVA/NVA), nghiên cứu lịch sử hình thành và phát triển của MoMo |
| 4 | 25410191 | Hồ Nguyễn Bảo Duy | Thành viên | Khảo sát thực tế tính năng đặt vé trên ứng dụng MoMo, thu thập bằng chứng giao diện từng bước, ghi nhận luồng thanh toán và biên bản kiểm thử |
| 5 | 25410195 | Nguyễn Huỳnh Mỹ Duyên | Thành viên | Rà soát cấu trúc báo cáo theo mẫu chuẩn của trường, kiểm tra tính đồng bộ của danh mục từ viết tắt, định dạng bảng biểu và hình vẽ |
| 6 | 25410206 | Nguyễn Đắc Hiển | Thành viên | Xây dựng báo cáo chuyên sâu mảng Tìm kiếm và Thanh toán vé, thiết kế mô hình BPMN nhóm quy trình cốt lõi, tính toán định lượng thời gian chu kỳ và chi phí vận hành |
| 7 | 25410223 | Lê Quốc Hưng | Thành viên | Phân tích và mô hình hóa quy trình Đổi chuyến bay, mô tả chi tiết chính sách phí đổi, cấu trúc phí chênh lệch và cơ chế tái phát hành vé (Re-issue) |
| 8 | 25410237 | Nguyễn Mậu An Khương | Thành viên | Xây dựng báo cáo Hỗ trợ khách hàng và Tra soát giao dịch lỗi, quy trình Quản trị danh mục đối tác nhà cung ứng, phân tích biểu đồ Pareto (80/20) và kiến trúc tổng thể 10 quy trình |
