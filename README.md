# 🧑‍💻 Freelancer API (FastAPI)

Bu API FastAPI yordamida yozilgan bo‘lib, freelancerlar bilan ishlash uchun CRUD (Create, Read, Update, Delete) funksiyalarni ta'minlaydi.

## 🔧 Texnologiyalar
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## 📌 Funksiyalar
- Freelancer qo‘shish / ko‘rish / tahrirlash / o‘chirish
- Status yangilash (`available`, `busy`, `on_leave`)
- Skill bo‘yicha qidirish

## ✅ Validatsiya
- Telefon raqami `+998` bilan boshlanishi shart
- `skills` bo‘sh bo‘lmasligi kerak
- `status` faqat belgilangan qiymatlar bo‘lishi mumkin
- `joined_at` avtomatik to‘ldiriladi

## ▶️ Ishga tushirish
```bash
uvicorn main:app --reload