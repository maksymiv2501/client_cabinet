def get_feedback_data():
    return {
        "summary": {
            "total": 12,
            "open": 4,
            "waiting_for_client": 1,
            "new_answers": 2,
            "sla_success_percent": 94,
        },

        "topics": [
            {
                "code": "billing",
                "name": "Розрахунки за спожиту електричну енергію, тарифи та пільги",
                "sla_days": 15,
                "manager": "Олена Мельник",
                "template": (
                    "Опишіть номер рахунку, період, суму, суть невідповідності "
                    "та додайте документи, якщо вони є."
                ),
            },
            {
                "code": "contract_owner_change",
                "name": "Переоформлення договору при зміні власника",
                "sla_days": 30,
                "manager": "Марія Бойко",
                "template": (
                    "Вкажіть номер договору, поточного власника, нового власника "
                    "та перелік документів, які додаються."
                ),
            },
            {
                "code": "new_objects",
                "name": "Додавання нових об'єктів споживача",
                "sla_days": 20,
                "manager": "Андрій Коваль",
                "template": (
                    "Вкажіть EIC-код, адресу об'єкта, ОСР, планову дату підключення "
                    "та контактну особу."
                ),
            },
            {
                "code": "requisites_change",
                "name": "Зміна реквізитів поточних договорів",
                "sla_days": 15,
                "manager": "Марія Бойко",
                "template": (
                    "Вкажіть номер договору, які саме реквізити потрібно змінити, "
                    "нові реквізити та додайте підтверджуючі документи."
                ),
            },
            {
                "code": "contract_values",
                "name": "Договірні величини, коригування та перевищення",
                "sla_days": 20,
                "manager": "Андрій Коваль",
                "template": (
                    "Опишіть період, договірні величини, очікуване коригування "
                    "та причину звернення."
                ),
            },
            {
                "code": "time_tariff",
                "name": "Перехід на тариф, диференційований за періодами часу",
                "sla_days": 20,
                "manager": "Андрій Коваль",
                "template": (
                    "Вкажіть договір, ТКО, бажану дату переходу та очікуваний режим споживання."
                ),
            },
            {
                "code": "staff_complaint",
                "name": "Скарги на роботу персоналу Компанії",
                "sla_days": 15,
                "manager": "Служба контролю якості",
                "template": (
                    "Опишіть ситуацію, дату, контактну особу та бажаний результат розгляду."
                ),
            },
            {
                "code": "restore_supply",
                "name": "Відновлення енергопостачання після відключення",
                "sla_days": 10,
                "manager": "Андрій Коваль",
                "template": (
                    "Вкажіть договір, об'єкт, причину відключення, дату оплати заборгованості "
                    "та додайте підтвердження оплати."
                ),
            },
            {
                "code": "consumption_data",
                "name": "Надання даних про споживання електричної енергії",
                "sla_days": 10,
                "manager": "Андрій Коваль",
                "template": (
                    "Вкажіть період, договір, ТКО та формат даних, який потрібно надати."
                ),
            },
            {
                "code": "invoice_check",
                "name": "Перевірка правильності рахунку на оплату",
                "sla_days": 15,
                "manager": "Олена Мельник",
                "template": (
                    "Вкажіть номер рахунку, період, суму, що викликає питання, "
                    "та коротко опишіть очікуване уточнення."
                ),
            },
            {
                "code": "other",
                "name": "Інше",
                "sla_days": 15,
                "manager": "Контакт-центр",
                "template": "Опишіть суть звернення максимально детально.",
            },
        ],

        "tickets": [
            {
                "id": "FB-2026-0003",
                "created_at": "09.05.2026 09:20",
                "topic_code": "invoice_check",
                "topic": "Перевірка правильності рахунку на оплату",
                "subject": "Перевірка рахунку ФАКТ-2026-061",
                "status": "waiting_for_client",
                "status_text": "Очікує дані від клієнта",
                "priority": "normal",
                "author": "Василь Максимів",
                "assignee": "Олена Мельник",
                "department": "Фінансовий відділ",
                "channel": "Кабінет клієнта",
                "source_system": "Luxtrade",
                "sla_days": 15,
                "sla_left": "SLA на паузі",
                "sla_state": "paused",
                "last_activity": "09.05.2026 14:10",
                "has_new_answer": True,
                "client_action_required": True,
                "short_text": "Просимо перевірити суму фактичного рахунку за червень 2026.",
                "attachments": [
                    {"name": "invoice_FACT-2026-061.pdf", "size": "420 KB"},
                ],
                "messages": [
                    {
                        "author": "Василь Максимів",
                        "role": "Клієнт",
                        "time": "09.05.2026 09:20",
                        "text": "Просимо перевірити суму фактичного рахунку за червень 2026. Є питання щодо врахування авансів.",
                        "attachments": [
                            {"name": "invoice_FACT-2026-061.pdf", "size": "420 KB"},
                        ],
                    },
                    {
                        "author": "Олена Мельник",
                        "role": "ОККО-КОНТРАКТ",
                        "time": "09.05.2026 14:10",
                        "text": "Для перевірки просимо надати акт ОСР або деталізацію обсягів за червень. SLA призупинено до отримання даних.",
                        "attachments": [],
                    },
                ],
            },
            {
                "id": "FB-2026-0002",
                "created_at": "07.05.2026 11:45",
                "topic_code": "new_objects",
                "topic": "Додавання нових об'єктів споживача",
                "subject": "Додавання нового ТКО у Львові",
                "status": "in_progress",
                "status_text": "В роботі",
                "priority": "normal",
                "author": "Василь Максимів",
                "assignee": "Андрій Коваль",
                "department": "Технічний відділ",
                "channel": "Кабінет клієнта",
                "source_system": "Luxtrade",
                "sla_days": 20,
                "sla_left": "12 днів",
                "sla_state": "active",
                "last_activity": "08.05.2026 10:30",
                "has_new_answer": False,
                "client_action_required": False,
                "short_text": "Потрібно додати нову точку комерційного обліку до договору.",
                "attachments": [
                    {"name": "new_tko_application.xlsx", "size": "86 KB"},
                    {"name": "ownership_document.pdf", "size": "1.2 MB"},
                ],
                "messages": [
                    {
                        "author": "Василь Максимів",
                        "role": "Клієнт",
                        "time": "07.05.2026 11:45",
                        "text": "Просимо додати нове ТКО за адресою м. Львів, вул. Енергетична, 10.",
                        "attachments": [
                            {"name": "new_tko_application.xlsx", "size": "86 KB"},
                            {"name": "ownership_document.pdf", "size": "1.2 MB"},
                        ],
                    },
                    {
                        "author": "Андрій Коваль",
                        "role": "ОККО-КОНТРАКТ",
                        "time": "08.05.2026 10:30",
                        "text": "Звернення прийнято в роботу. Дані передано на перевірку.",
                        "attachments": [],
                    },
                ],
            },
            {
                "id": "FB-2026-0001",
                "created_at": "02.05.2026 16:05",
                "topic_code": "requisites_change",
                "topic": "Зміна реквізитів поточних договорів",
                "subject": "Оновлення email для рахунків",
                "status": "answered",
                "status_text": "Відповідь надано",
                "priority": "normal",
                "author": "Василь Максимів",
                "assignee": "Марія Бойко",
                "department": "Юридичний відділ",
                "channel": "Кабінет клієнта",
                "source_system": "Luxtrade",
                "sla_days": 15,
                "sla_left": "Виконано в SLA",
                "sla_state": "done",
                "last_activity": "03.05.2026 12:15",
                "has_new_answer": True,
                "client_action_required": False,
                "short_text": "Потрібно змінити email для отримання рахунків.",
                "attachments": [],
                "messages": [
                    {
                        "author": "Василь Максимів",
                        "role": "Клієнт",
                        "time": "02.05.2026 16:05",
                        "text": "Просимо змінити email для отримання рахунків на billing.client@company.ua.",
                        "attachments": [],
                    },
                    {
                        "author": "Марія Бойко",
                        "role": "ОККО-КОНТРАКТ",
                        "time": "03.05.2026 12:15",
                        "text": "Email оновлено. Наступні рахунки будуть надсилатися на billing.client@company.ua.",
                        "attachments": [
                            {"name": "confirmation.pdf", "size": "210 KB"},
                        ],
                    },
                ],
            },
        ],
    }