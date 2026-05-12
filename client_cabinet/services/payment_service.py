def get_payments_data():

    payments = [
        {
            "payment_number": "PAY-2026-0001",
            "payment_date": "18.07.2026",
            "posting_date": "18.07.2026",
            "received_amount": 50000,
            "allocated_amount": 42000,
            "unallocated_amount": 8000,
            "status": "Частково рознесено",
            "payer": "ТОВ Приклад",
            "iban": "UA123456789012345678901234567",
            "payment_purpose": "Оплата за електричну енергію згідно рахунків",
            "bank_document_url": "#",
            "linked_invoices": [
                {
                    "invoice_number": "АВ-2026-071",
                    "invoice_date": "01.07.2026",
                    "invoice_type": "Аванс",
                    "invoice_amount": 18000,
                    "allocated_amount": 12000,
                    "pdf_url": "#",
                },
                {
                    "invoice_number": "ФАКТ-2026-061",
                    "invoice_date": "30.06.2026",
                    "invoice_type": "За фактичне споживання",
                    "invoice_amount": 42300,
                    "allocated_amount": 30000,
                    "pdf_url": "#",
                },
            ],
            "history": [
                {"date": "18.07.2026 10:15", "event": "Платіж імпортовано з банку", "user": "Система"},
                {"date": "18.07.2026 10:20", "event": "Платіж частково рознесено", "user": "SAP"},
            ],
        },
        {
            "payment_number": "PAY-2026-0002",
            "payment_date": "22.07.2026",
            "posting_date": "22.07.2026",
            "received_amount": 15000,
            "allocated_amount": 15000,
            "unallocated_amount": 0,
            "status": "Рознесено",
            "payer": "ТОВ Приклад",
            "iban": "UA123456789012345678901234567",
            "payment_purpose": "Оплата за рахунком АВ-2026-072",
            "bank_document_url": "#",
            "linked_invoices": [
                {
                    "invoice_number": "АВ-2026-072",
                    "invoice_date": "10.07.2026",
                    "invoice_type": "Аванс",
                    "invoice_amount": 12000,
                    "allocated_amount": 15000,
                    "pdf_url": "#",
                },
            ],
            "history": [
                {"date": "22.07.2026 09:00", "event": "Платіж імпортовано з банку", "user": "Система"},
                {"date": "22.07.2026 09:03", "event": "Платіж повністю рознесено", "user": "SAP"},
            ],
        },
    ]

    received_total = 78000
    total_invoiced = sum(
        inv["invoice_amount"]
        for p in payments
        for inv in p["linked_invoices"]
    )

    return {
        "summary": {
            "received_total": received_total,
            "allocated_total": 69000,
            "unallocated_total": 9000,
            "payments_count": len(payments),
            "accounting_balance": received_total - total_invoiced,
        },
        "payments": payments,
    }