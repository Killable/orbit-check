from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.runtime.client_request import ClientRequest
from office365.runtime.utilities.request_options import RequestOptions
from office365.runtime.http.http_method import HttpMethod
from office365.runtime.utilities.uri_builder import UriBuilder
from office365.sharepoint.client_context import ClientContext

# Office 365 租户相关信息
site_url = "<site_url>"
username = "<username>"
password = "<password>"

# 创建身份验证上下文
ctx_auth = AuthenticationContext(url=site_url)
if ctx_auth.acquire_token_for_user(username=username, password=password):
    # 创建客户端上下文
    ctx = ClientContext(site_url, ctx_auth)

    # 获取Excel文档
    excel_file_url = "<excel_file_url>"
    excel_file = ctx.web.get_file_by_server_relative_url(excel_file_url).get().execute_query()

    # 打开工作簿
    workbook = excel_file.get_workbook(ctx)
    ctx.load(workbook)
    ctx.execute_query()

    # 获取第一个工作表
    worksheet = workbook.worksheets.get_by_index(0)
    ctx.load(worksheet)
    ctx.execute_query()

    # 在A1单元格中写入数据
    cell_address = "A1"
    cell = worksheet.get_range(cell_address)
    cell.values = "Hello, Office 365!"
    cell.update()
    ctx.execute_query()

    print("数据已写入A1单元格。")

else:
    print("身份验证失败。")
