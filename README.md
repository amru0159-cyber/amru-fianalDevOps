# Local AI DevOps Project

โปรเจกต์ระบบ AI Chatbot ที่ทำงานบนเครื่องคอมพิวเตอร์ โดยใช้ Docker, Ollama, Open WebUI และ Python

## Objectives
- ติดตั้งและใช้งาน AI ภายในเครื่อง
- สร้างระบบ Chatbot ผ่านเว็บไซต์
- ทดสอบ AI สองโมเดลด้วย Python
- จัดการโปรเจกต์ด้วย Git และ GitHub

## Technologies
- Docker และ Docker Compose
- Ollama
- Open WebUI
- Python 3
- Git และ GitHub

## AI Models
1. GLM4: glm4:9b-chat-q2_K
2. Qwen3: qwen3:4b

## Project Structure
- Model1-GLM/main.py : Python สำหรับ GLM
- Model2-QWEN/main.py : Python สำหรับ Qwen3
- docker-compose.yml : ตั้งค่า Docker
- result.md : บันทึกผลการทดลอง

## How to Run
1. เปิด Ollama และ Docker Desktop
2. เริ่มระบบด้วย docker compose up -d
3. เปิด http://localhost:3000
4. ทดสอบ Python ด้วยคำสั่ง:

   python3 Model1-GLM/main.py

   python3 Model2-QWEN/main.py

## Results
สามารถติดตั้งและเรียกใช้ GLM4 และ Qwen3 ผ่าน Ollama ได้ และทดสอบการเชื่อมต่อผ่าน Python สำเร็จ
