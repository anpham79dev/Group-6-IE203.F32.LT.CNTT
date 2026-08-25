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
