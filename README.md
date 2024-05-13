# MTS Assistant для людей с ОВЗ (Backend Submodule)

## О проекте

MTS Assistant для людей с ОВЗ — это инновационный проект, созданный для облегчения доступа к технологиям и улучшения качества жизни людей с ограниченными возможностями. Разработанный в рамках хакатона True Tech Hack, этот проект использует современные технологии для голосового управления и анализа данных, предоставляя удобный и безопасный интерфейс для взаимодействия.

## Как запустить

Для успешного развертывания и запуска MTS Assistant выполните следующие шаги:

1. **Установка зависимостей**:
   - Запустите `poetry install` для установки всех необходимых зависимостей проекта.

2. **Настройка конфигураций**:
   - Добавьте файл конфигурации `.env` в директорию `configs/` для корректной работы всех модулей.

3. **Локальный запуск**:
   - Используйте команду `make local` для локального запуска всех сервисов проекта.

4. **Миграции базы данных**:
   - Выполните `make migrate-up name=head` для применения последних миграций к базе данных.

5. **Запуск приложения**:
   - Используйте команду `make up` для запуска всех компонентов системы.

6. **Загрузка моделей машинного обучения**:
   - Скачайте необходимые модели в директорию `ml/models/` для работы модуля распознавания речи.

## Дополнительная информация

**Используемые технологии и их преимущества**:

- **Whisper для распознавания речи**: обеспечивает высокую точность преобразования речи в текст, что делает интерфейс доступным для пользователей с различными ограничениями.
- **Saiga Mistral для принятия решений**: адаптирует ответы системы к индивидуальным потребностям пользователя, улучшая персонализацию взаимодействия.
- **Toxic Classifier для распознавания токсичных запросов**: повышает безопасность общения, фильтруя нежелательные и вредоносные сообщения.
- **FastAPI для бэкенда и React для фронтенда**: обеспечивают высокую производительность, масштабируемость и отзывчивость пользовательского интерфейса.
- **CI/CD**: автоматизирует процессы тестирования и развертывания, сокращая время на доработки и обновления.
- **Git submodules**: упрощают управление зависимостями и модулями, позволяя легко интегрировать и обновлять компоненты проекта.

## О Команде

Наша команда — это группа специалистов в области разработки программного обеспечения, дизайна, анализа данных и искусственного интеллекта. Мы стремимся использовать наш опыт и знания для создания решений, которые делают мир более доступным и дружелюбным для всех, независимо от их физических ограничений.
