def grouped_data_func(data: list[tuple[int|str]]) -> dict[int, dict[int, list[dict[str, str]]]]:
    grouped_data = {}
    for item in data:
        vol_num, file_num = item[0], item[1]
        if vol_num not in grouped_data:
            grouped_data[vol_num] = {}
        if file_num not in grouped_data[vol_num]:
            grouped_data[vol_num][file_num] = []
        grouped_data[vol_num][file_num].append({
            "file_name": item[2], "task_title": item[3], "appearing_detail_name": item[4]
            })
    return grouped_data