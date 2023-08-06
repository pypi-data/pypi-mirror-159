import numbers

from python_sdk_client.libs.client_cfg import InsightServiceCfg


def handle(anotherfunc, input_str, tenant_type: str, x_api_key: str, org_id: str, batch_size: numbers = 300, **kwargs):
    response = []
    if input_str is None:
        temp_resp = anotherfunc(tenant_type, x_api_key, org_id=org_id, **kwargs)
        if temp_resp is None or 'records' not in temp_resp or temp_resp['records'] is None:
            return response

        response = response + temp_resp['records']
        if temp_resp['totalPages'] is not None:
            total_pages = int(temp_resp['totalPages'])
            if temp_resp['currentPageItems'] > 0:
                total_pages = int(min(total_pages, InsightServiceCfg.MAX_SIZE / temp_resp['currentPageItems']))
            for i in range(1, total_pages, 1):
                temp_resp = anotherfunc(tenant_type, x_api_key, org_id=org_id, page=i, **kwargs)
                response = response + temp_resp['records']
        return response

    if input_str is not None:
        input_list = input_str.split(", ")
        for i in range(0, len(input_list), batch_size):
            current_batch = input_list[i:i + batch_size]
            current_batch_str = ','.join(current_batch)
            temp_resp = anotherfunc(tenant_type, x_api_key, org_id=org_id, ids=current_batch_str, **kwargs)
            if temp_resp is not None and 'records' in temp_resp and temp_resp['records'] is not None:
                response = response + temp_resp['records']
        return response
