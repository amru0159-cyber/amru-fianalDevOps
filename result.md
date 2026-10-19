# ผลการทดลอง Local AI DevOps

## 1. การติดตั้ง
ติดตั้ง Docker, Ollama และ Open WebUI เพื่อสร้างระบบ AI Chatbot ภายในเครื่อง

## 2. โมเดลที่ใช้
- GLM4 9B รุ่นบีบอัด q2_K
- Qwen3 4B

## 3. ผลการทดสอบ
- Ollama สามารถเรียกใช้งานโมเดลได้
- Qwen3 สามารถตอบคำถามภาษาไทยผ่าน Python ได้
- GLM4 สามารถตอบคำถามภาษาไทยผ่าน Python ได้
- สามารถใช้งานระบบ Chatbot ผ่าน Open WebUI บน localhost

## 4. ปัญหาและการแก้ไข
- โมเดล GLM4 รุ่น 1B และ 2B ไม่มีใน Ollama จึงเลือกใช้ GLM4 9B รุ่นบีบอัด
- ไฟล์ Python ว่าง ทำให้โปรแกรมไม่แสดงผล จึงเพิ่มโค้ดเชื่อมต่อ Ollama API
- ตั้งค่า GitHub Remote ให้ตรงกับ Repository ที่ต้องการ

## 5. สรุป
โปรเจกต์สามารถใช้งาน AI ภายในเครื่องโดยใช้ Ollama, Docker, Open WebUI และ Python ได้สำเร็จ
