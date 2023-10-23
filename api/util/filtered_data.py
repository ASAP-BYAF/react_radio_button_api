def filtered_data_func(data: dict[int, dict[int, list[dict[str, str]]]],
                       filter_list: list[str]
                       ) -> dict[int, dict[int, list[dict[str, str]]]]:
    filtered_data = {}
    for i_k, i_v in data.items():
        for j_k, j_v in i_v.items():
            print(j_v)
            task_list = [k_v['task_title'] for k_v in j_v]
            print(task_list)
            print(i_k, j_k)
            result = all(item in task_list for item in filter_list)

            if result:
                if i_k not in filtered_data:
                    filtered_data[i_k] = {}
                if j_k not in filtered_data[i_k]:
                    filtered_data[i_k][j_k] = j_v
    return filtered_data