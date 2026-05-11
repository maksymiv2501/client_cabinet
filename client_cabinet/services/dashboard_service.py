def get_dashboard_data():
    return {
        "payment_calendar": [
            {
                "kind": "advance",
                "period": "Липень 2026",
                "invoice_number": "АВ-2026-071",
                "invoice_type": "Авансовий",
                "due_date": "05.07.2026",
                "amount": 18000,
                "status": "До оплати",
                "days_left": 18,
            },
            {
                "kind": "advance",
                "period": "Липень 2026",
                "invoice_number": "АВ-2026-072",
                "invoice_type": "Авансовий",
                "due_date": "15.07.2026",
                "amount": 12000,
                "status": "До оплати",
                "days_left": 28,
            },
            {
                "kind": "actual",
                "period": "Червень 2026",
                "invoice_number": "ФАКТ-2026-061",
                "invoice_type": "За фактичне споживання",
                "due_date": "20.06.2026",
                "amount": 42300,
                "status": "Частково оплачено",
                "days_left": -2,
                "actual_details": {
                    "actual_amount": 42300,
                    "advance_invoices": [
                        {
                            "invoice_number": "АВ-2026-061",
                            "amount": 12000,
                            "paid": 12000,
                            "status": "Оплачено",
                        },
                        {
                            "invoice_number": "АВ-2026-062",
                            "amount": 15000,
                            "paid": 15000,
                            "status": "Оплачено",
                        },
                        {
                            "invoice_number": "АВ-2026-063",
                            "amount": 10000,
                            "paid": 10000,
                            "status": "Оплачено",
                        },
                    ],
                    "advance_paid_total": 37000,
                    "opening_balance": -12500,
                    "result": -7200,
                    "result_text": "Переплата переноситься на майбутні періоди",
                },
            },
        ],

        "action_cards": {
            "documents": {
                "count": 2,
                "title": "Документи до підпису",
                "description": "Очікують підписання додатки до договору",
                "button": "Перейти до документів",
            },
            "forecast": {
                "month": "Липень 2026",
                "deadline": "15.06.2026",
                "status": "Не подано",
                "description": "Потрібно подати прогноз споживання",
                "button": "Подати прогноз",
            },
            "feedback": {
                "count": 1,
                "title": "Нова відповідь",
                "description": "Є відповідь на звернення FB-2026-0003",
                "button": "Переглянути звернення",
            },
        },
    }