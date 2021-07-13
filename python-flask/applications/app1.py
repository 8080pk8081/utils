from flask import Blueprint, request, current_app

# 定义新蓝图-env 需要加入到configs/setting.py中
from modules.module import host_os, target_host, snap, implement_host
from utils.db_utils import db

env = Blueprint('env', __name__, url_prefix="/env")


# 宿主机相关API
# 查
@env.route('/hostOS/all', methods=['POST'])
def get_hostOS_all():
    """
    宿主机全量查询，倒序
    @return:  query set
    """
    dict1 = {"status": '1'}
    host_os_data = host_os.query.order_by(host_os.update_date.desc()).all()    # 倒序全量
    host_os_data = [x.to_json() for x in host_os_data]
    host_os_data = [dict(x, **dict1) for x in host_os_data]      # 加载ping ip 的状态，将状态加到字典中一并返回，合并字典。
    return {"success": True, "hostos_data": host_os_data}