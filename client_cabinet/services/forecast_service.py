def get_current_correction_data():
    return {
        "period": "Червень 2026",

        "rules": {
            "group_a_deadline": "D-3 до 16:00",
            "group_a_limit": "10%",
            "group_b_deadline": "D-2 до 15:00",
            "group_b_limit": "8%",
            "available_period": "05.06 — 30.06",
        },

        "group_a": [
            {
                "tko": "АЗК Львів 1",
                "eic": "62Z000000000001A",
                "osr": "Львівобленерго",
                "current": 5420,
                "new": 5500,
                "deviation": "+1.47%",
                "status": "Готово",
                "status_class": "success",
            },
            {
                "tko": "АЗК Львів 2",
                "eic": "62Z000000000002A",
                "osr": "Львівобленерго",
                "current": 4800,
                "new": 4950,
                "deviation": "+3.13%",
                "status": "Частково",
                "status_class": "warning",
            },
            {
                "tko": "АЗК Тернопіль 1",
                "eic": "62Z000000000003A",
                "osr": "Тернопільобленерго",
                "current": 6100,
                "new": 6950,
                "deviation": "+13.93%",
                "status": "Перевищення",
                "status_class": "danger",
            },
            {
                "tko": "АЗК Львів 3",
                "eic": "62Z000000000004A",
                "osr": "Львівобленерго",
                "current": 3300,
                "new": 3310,
                "deviation": "+0.30%",
                "status": "Готово",
                "status_class": "success",
            },
            {
                "tko": "АЗК Тернопіль 2",
                "eic": "62Z000000000005A",
                "osr": "Тернопільобленерго",
                "current": 7200,
                "new": 7000,
                "deviation": "-2.78%",
                "status": "Готово",
                "status_class": "success",
            },
            {
                "tko": "АЗК Львів 4",
                "eic": "62Z000000000006A",
                "osr": "Львівобленерго",
                "current": 5100,
                "new": 5150,
                "deviation": "+0.98%",
                "status": "Частково",
                "status_class": "warning",
            },
            {
                "tko": "АЗК Івано-Франківськ 1",
                "eic": "62Z000000000007A",
                "osr": "Прикарпаттяобленерго",
                "current": 8200,
                "new": 8400,
                "deviation": "+2.44%",
                "status": "Готово",
                "status_class": "success",
            },
            {
                "tko": "АЗК Рівне 1",
                "eic": "62Z000000000008A",
                "osr": "Рівнеобленерго",
                "current": 4600,
                "new": 5200,
                "deviation": "+13.04%",
                "status": "Перевищення",
                "status_class": "danger",
            },
            {
                "tko": "АЗК Луцьк 1",
                "eic": "62Z000000000009A",
                "osr": "Волиньобленерго",
                "current": 3900,
                "new": 3950,
                "deviation": "+1.28%",
                "status": "Готово",
                "status_class": "success",
            },
            {
                "tko": "АЗК Чернівці 1",
                "eic": "62Z000000000010A",
                "osr": "Чернівціобленерго",
                "current": 5700,
                "new": 5600,
                "deviation": "-1.75%",
                "status": "Готово",
                "status_class": "success",
            },
        ],

        "group_b": [
            {
                "tko": "АЗК Київ 1",
                "eic": "62Z000000000001B",
                "osr": "ДТЕК Київські електромережі",
                "plan": 5600,
                "consumed": 2300,
                "available": 3300,
                "new": 5400,
                "deviation": "-3.57%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Київ 2",
                "eic": "62Z000000000002B",
                "osr": "ДТЕК Київські електромережі",
                "plan": 4200,
                "consumed": 3900,
                "available": 300,
                "new": 3800,
                "deviation": "-9.52%",
                "status": "Менше вже спожитого",
                "status_class": "danger",
            },
            {
                "tko": "АЗК Київ 3",
                "eic": "62Z000000000003B",
                "osr": "ДТЕК Київські електромережі",
                "plan": 7100,
                "consumed": 2000,
                "available": 5100,
                "new": 7000,
                "deviation": "-1.41%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Львів 5",
                "eic": "62Z000000000004B",
                "osr": "Львівобленерго",
                "plan": 3900,
                "consumed": 1200,
                "available": 2700,
                "new": 4000,
                "deviation": "+2.56%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Одеса 1",
                "eic": "62Z000000000005B",
                "osr": "ДТЕК Одеські електромережі",
                "plan": 6400,
                "consumed": 2800,
                "available": 3600,
                "new": 6600,
                "deviation": "+3.13%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Одеса 2",
                "eic": "62Z000000000006B",
                "osr": "ДТЕК Одеські електромережі",
                "plan": 5000,
                "consumed": 4700,
                "available": 300,
                "new": 4550,
                "deviation": "-9.00%",
                "status": "Менше вже спожитого",
                "status_class": "danger",
            },
            {
                "tko": "АЗК Харків 1",
                "eic": "62Z000000000007B",
                "osr": "Харківобленерго",
                "plan": 7800,
                "consumed": 3100,
                "available": 4700,
                "new": 7900,
                "deviation": "+1.28%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Дніпро 1",
                "eic": "62Z000000000008B",
                "osr": "ДТЕК Дніпровські електромережі",
                "plan": 6900,
                "consumed": 2400,
                "available": 4500,
                "new": 7200,
                "deviation": "+4.35%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Полтава 1",
                "eic": "62Z000000000009B",
                "osr": "Полтаваобленерго",
                "plan": 3500,
                "consumed": 900,
                "available": 2600,
                "new": 3700,
                "deviation": "+5.71%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Вінниця 1",
                "eic": "62Z000000000010B",
                "osr": "Вінницяобленерго",
                "plan": 4400,
                "consumed": 4100,
                "available": 300,
                "new": 4000,
                "deviation": "-9.09%",
                "status": "Менше вже спожитого",
                "status_class": "danger",
            },
        ],
    }

def get_next_month_plan_data():
    return {
        "period": "Липень 2026",
        "rules": {
            "monthly_deadline": "15.06.2026",
            "group_a_limit": "10%",
            "group_b_limit": "8%",
        },
        "group_a": [
            {
                "tko": "АЗК Львів 1",
                "eic": "62Z000000000001A",
                "osr": "Львівобленерго",
                "year_plan": 8500,
                "hourly_sum": 8420,
                "deviation": "-0.94%",
                "status": "Погодинка заповнена",
                "status_class": "success",
            },
            {
                "tko": "АЗК Тернопіль 1",
                "eic": "62Z000000000003A",
                "osr": "Тернопільобленерго",
                "year_plan": 7600,
                "hourly_sum": 8400,
                "deviation": "+10.53%",
                "status": "Перевищення",
                "status_class": "danger",
            },
        ],
        "group_b": [
            {
                "tko": "АЗК Київ 1",
                "eic": "62Z000000000001B",
                "osr": "ДТЕК Київські електромережі",
                "year_plan": 5600,
                "new_plan": 5700,
                "deviation": "+1.79%",
                "status": "В нормі",
                "status_class": "success",
            },
            {
                "tko": "АЗК Одеса 1",
                "eic": "62Z000000000005B",
                "osr": "ДТЕК Одеські електромережі",
                "year_plan": 6400,
                "new_plan": 7300,
                "deviation": "+14.06%",
                "status": "Перевищення",
                "status_class": "danger",
            },
        ],
    }


def get_next_year_plan_data():

    months = [
        "Січ", "Лют", "Бер", "Кві",
        "Тра", "Чер", "Лип", "Сер",
        "Вер", "Жов", "Лис", "Гру",
    ]

    tko_list = [
        ("АЗК Львів 1", "62Z000000000001A", "Львівобленерго", "A"),
        ("АЗК Львів 2", "62Z000000000002A", "Львівобленерго", "A"),
        ("АЗК Тернопіль 1", "62Z000000000003A", "Тернопільобленерго", "A"),
        ("АЗК Київ 1", "62Z000000000001B", "ДТЕК Київські електромережі", "B"),
        ("АЗК Київ 2", "62Z000000000002B", "ДТЕК Київські електромережі", "B"),
        ("АЗК Одеса 1", "62Z000000000005B", "ДТЕК Одеські електромережі", "B"),
        ("АЗК Харків 1", "62Z000000000007B", "Харківобленерго", "B"),
        ("АЗК Дніпро 1", "62Z000000000008B", "ДТЕК Дніпровські електромережі", "B"),
        ("АЗК Рівне 1", "62Z000000000008A", "Рівнеобленерго", "A"),
        ("АЗК Чернівці 1", "62Z000000000010A", "Чернівціобленерго", "A"),
    ]

    items = []

    for index, item in enumerate(tko_list):

        base = 3200 + index * 420

        monthly_values = []
        total = 0

        for month_index, month in enumerate(months):

            value = base + month_index * 120
            total += value

            monthly_values.append({
                "month": month,
                "value": value,
            })

        items.append({
            "tko": item[0],
            "eic": item[1],
            "osr": item[2],
            "group": item[3],
            "months": monthly_values,
            "total": total,
            "status": "Заповнено" if index % 4 != 0 else "Потребує перевірки",
            "status_class": "success" if index % 4 != 0 else "warning",
        })

    return {
        "year": 2027,
        "months": months,
        "rules": {
            "yearly_deadline": "21.11.2026",
            "reminder": "за 7 днів",
        },
        "items": items,
    }