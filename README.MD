## Symptom Checker for COVID-19

This is a rule-based approach for SC

Flow system:
<img src="asset/Triage flow for covid_vn.png"/>

### Usage
```
from src.app import Application
app = Application()
app.run('screening')

Bạn tên gì:nguễn văn a  
Giới tính của bạn:female
Tuổi của bạn:77
Bạn có đồng ý với các điều khoảng sau đây khôngg
1. ... 
2. ... 
3. ... (y/n)y
Bạn có cảm thấy mình bị bệnh như cảm hoặc cúm không? (y/n)y
Bạn có cảm thấy khó thở hoặc đau khi ấn vào ngực không? (y/n)n
Bạn có cảm thấy khó thở hơn bình thường không? (y/n)n
Bạn có hay chóng mặt hoặc đau đầu dẫn đến thường xuyên ngất xỉu không? (y/n)n
Bạn có buồn nôn/nôn mửa/tiêu chảy không? (y/n)n
Trong 24 giờ qua bạn có sốt không? (y/n)y
Nhiệt độ hiện tại của bạn có cao hơn mức bình thường không? (y/n/idk)n
Bạn có ho không? (y/n)y
Bạn có một trong những triệu chứng dưới đây không:
Liên tục ớn lạnh,
Mất vị giác hoặc khứu giác,
Viêm họng,
Chảy/Sổ mũi,
Đau nhức cơ,
Mệt mỏi, khó chịu, buồn nôn, tiêu chảy (y/n)n
Bạn có đang trong thời kỳ mang thai không hoặc bạn vừa sinh trong vòng 2 tuần trở lại? (y/n)n
yellow
Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi
```