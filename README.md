Demo:

![Spectral by HTML5 UP - 個人 - Microsoft_ Edge 2024-07-14 22-52-52](https://github.com/user-attachments/assets/1464e965-f93e-45d5-926c-81bc275f8ecf)


(1) CSRF，寫在 JS 裡，並且 Script 要寫在 HTML 中才會正確接收 CSRF

![image](https://github.com/user-attachments/assets/92c40e23-3343-4a6e-9928-ff43ad48bb53)


(2) 為了將上傳的檔案儲存在 static/media 中，必須在 setting 中設定環境變數。

![image](https://github.com/user-attachments/assets/f8fcd8cf-d223-4eef-a296-fcade8740aa4)


(3) 在 View.py 中呼叫欲使用的 model ( 在這是 styleTrans.py )，並且將風格轉換後的圖片儲存在 static/media/transfered 底下。

![image](https://github.com/user-attachments/assets/e2d18b43-d2b0-4fb2-8458-fa14c5191dac)


(4) model.py 中，定義上傳的資料形式，並且定義上傳的路徑為何 ( 在此是將圖片儲存於 static/media/uploads )。form.py 中，定義的是圖片在後台儲存的形式。

![image](https://github.com/user-attachments/assets/c4840ded-9e8d-4d2f-a049-2d18076393aa)


model from https://github.com/nazianafis/Neural-Style-Transfer/tree/main

有關 model 的解說可參考： https://medium.com/geekculture/a-lightweight-pytorch-implementation-of-neural-style-transfer-86603e5eb551
