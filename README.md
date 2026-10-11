# feature-adoption-tracker
трекинг адоптации продуктовых фич. Adoption rate, RFM по фичам, кластеризация пользователей по паттернам использования.
# feature-adoption-tracker

Трекинг адоптации продуктовых фич.

## Возможности
- Запись событий использования фич
- Adoption rate по каждой фиче
- Детектор низкого adoption
- Кластеризация пользователей по паттернам
- Streamlit-дашборд

## Быстрый старт
cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Пример
curl -X POST http://localhost:8000/api/events \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"feature":"AI Search"}'

curl http://localhost:8000/api/adoption
curl http://localhost:8000/api/adoption/low

## Тесты
pytest tests/ -v

## Лицензия
MIT
