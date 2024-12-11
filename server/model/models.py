from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, DateTime, text
from sqlalchemy.dialects.mysql import SMALLINT, DECIMAL, BIGINT, INTEGER, TINYINT, VARCHAR, TEXT, CHAR

db = SQLAlchemy()


class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]

        return fields


class OmindApp(db.Model, EntityBase):
    __tablename__ = 'omind_app'

    id = Column(INTEGER(10), primary_key=True)
    app_type = Column(INTEGER(10), nullable=True, server_default=db.text("'0'"), comment='0 openAPI 1 奥升小程序')
    app_name = Column(VARCHAR(64), nullable=True, server_default=text("'智充'"), comment='应用名')
    app_key = Column(VARCHAR(32), nullable=True, server_default=text("'uuid8172947266'"), comment='应用key')
    secret = Column(VARCHAR(64), nullable=True, server_default=text("'9ksgg26688hsy5'"), comment='应用密钥')
    valid_time = Column(BIGINT(20), nullable=True, server_default=text("'253402271999'"), comment='有效期')
    state = Column(TINYINT(4), nullable=True, server_default=text("'0'"), comment='启用标记0未启用 1启用')
    create_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"))


class OmindBill(db.Model, EntityBase):
    __tablename__ = 'omind_bill'
    __table_args__ = {'comment': '充电订单信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='自增id')
    station_id = Column(VARCHAR(20), nullable=True, index=True, server_default=text("'11122221111'"),
                        comment='充电站id(运营商自定义的唯一编码)')
    base_operator_id = Column(VARCHAR(10), nullable=True, server_default=text("'1qwasa1122'"),
                              comment='基础平台运营商id(组织机构代码)')
    start_charge_seq = Column(VARCHAR(32), nullable=True, index=True, server_default=text("'asferwe32343532'"),
                              comment='格式"运营商ID+唯一编号",27字符')
    connector_id = Column(VARCHAR(26), nullable=True, index=True, server_default=text("'1wed12qws'"),
                          comment='充电设备接口编码(充电设备接口编码，同一运营商内唯一)')
    start_charge_seq_stat = Column(TINYINT(3), nullable=True, server_default=text("'1'"),
                                   comment='充电订单状态:1、启动中;2、充电中;3、停止中;4、已结束;5、未知;8、异常订单;20、已处理异常订单')
    user_id = Column(BIGINT(20), nullable=True, server_default=text("'0'"), comment='充电者用户id')
    start_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), index=True,  comment='开始充电时间(格式"yyyy-MM-dd HH:mm:ss")')
    end_time = Column(DateTime, index=True, comment='结束充电时间(格式"yyyy-MM-dd HH:mm:ss")')
    total_power = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"),
                         comment='累计充电量(单位:度,小数点后2位)')
    total_elec_money = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"),
                              comment='总电费(单位:元,小数点后2位)')
    total_service_money = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"),
                                 comment='总服务费(单位:元,小数点后2位)')
    total_money = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"),
                         comment='累计总金额(单位:元,小数点后2位)')
    real_pay_money = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"),
                            comment='实际支付总金额(单位:元,小数点后2位)')
    stop_reason = Column(INTEGER(10), nullable=True, server_default=text("'0'"),
                         comment='充电结束原因:0、用户手动停止充电;1、客户归属地运营商平台停止充电;2、BMS停止充电;3、充电机设备故障;4、连接器断开;5-99、自定义')
    stop_fail_reason = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                              comment='停止失败原因:0、无;1、此设备不存在;2、此设备离线;3、设备已停止充电;4~99、自定义')
    sum_period = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='时段数N，范围：0～32')
    charge_detail = Column(TEXT, comment='交易信息 json')
    car_vin = Column(VARCHAR(18), nullable=True, server_default=text("'kk87786612334'"), comment='车辆识别码')
    plate_no = Column(VARCHAR(10), nullable=True, server_default=text("''"), comment='车牌号')
    succ_stat = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='成功标识:0、成功;1、失败;')
    soc = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"), comment='电池剩余电量(默认:0)')
    pay_state = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='是否支付:0、未支付;1、已支付;')
    remark = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='备注')
    price_info = Column(TEXT, comment='价格信息 json')
    pay_plat = Column(VARCHAR(32), nullable=True, server_default=text("''"), comment='充电平台')
    transaction_id = Column(VARCHAR(30), nullable=True, server_default=text("''"), comment='支付交易号(如微信)')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, index=True, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')
    currentA = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"),
                      comment='A相电流(单位:A,默认:0 含直流(输出))')
    voltageA = Column(DECIMAL(6, 2), server_default=text("'0.00'"), comment='A相电压(单位:V,默认:0 含直流(输出))')
    charge_type = Column(TINYINT(1), nullable=True, server_default=text("'1'"), comment='充电类型 1、充满;2、按金额充电')
    charge_money = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"), comment='用户预计充电金额')


class OmindConnector(db.Model, EntityBase):
    __tablename__ = 'omind_connector'
    __table_args__ = {'comment': '充电设备接口信息表'}

    id = Column(INTEGER(10), primary_key=True, comment='自增id')
    station_id = Column(VARCHAR(20), nullable=True, index=True, server_default=text("''"),
                        comment='充电站id(运营商自定义的唯一编码)')
    operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                         comment='基础运营商id(组织机构代码)')
    user_operator_id = Column(VARCHAR(10), nullable=True, server_default=text("''"),
                              comment='用户平台运营商id(组织机构代码)')
    base_operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                              comment='基础运营商id(组织机构代码)')
    equipment_id = Column(VARCHAR(23), nullable=True, index=True, server_default=text("''"),
                          comment='设备编码(设备唯一编码，对同一运营商，保证唯一)')
    connector_id = Column(VARCHAR(26), nullable=True, index=True, server_default=text("''"),
                          comment='充电设备接口编码(充电设备接口编码，同一运营商内唯一)')
    connector_name = Column(VARCHAR(30), nullable=True, server_default=text("''"), comment='充电设备接口名称')
    connector_type = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                            comment='接口类型:1、家用插座(2);2、交流接口插座(模式3，B);3、交流接口插头(带枪线，3，C);4、直流接口枪头(带，4);5、无线充电座;6、其他')
    voltage_upper_limits = Column(SMALLINT(5), nullable=True, server_default=text("'0'"),
                                  comment='额定电压上限(单位:V)')
    voltage_lower_limits = Column(SMALLINT(5), nullable=True, server_default=text("'0'"),
                                  comment='额定电压下限(单位:V)')
    current_value = Column(SMALLINT(5), nullable=True, comment='额定电流(单位:A)')
    power = Column(DECIMAL(6, 2), nullable=True, server_default=text("'0.00'"), comment='额定功率(单位:kW)')
    park_no = Column(VARCHAR(10), nullable=True, server_default=text("''"), comment='车位号(停车场车位编号)')
    national_standard = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='国家标准:1、2011;2、2015')
    status = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                    comment='充电设备接口状态:0、离网;1、空闲;2、占用(未充电);3、占用(充电中);4、占用(预约锁定);255、故障')
    park_status = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                         comment='车位状态:0:未知;10:空闲;50:已上锁')
    lock_status = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                         comment='地锁状态:0:未知;10:已解锁;50:已上锁')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindEquipment(db.Model, EntityBase):
    __tablename__ = 'omind_equipment'
    __table_args__ = {'comment': '充电设备信息表'}

    id = Column(INTEGER(10), primary_key=True, comment='自增id')
    station_id = Column(VARCHAR(20), nullable=True, index=True, server_default=text("''"),
                        comment='充电站id(运营商自定义的唯一编码)')
    operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                         comment='运营商id(组织机构代码)')
    user_operator_id = Column(VARCHAR(10), nullable=True, server_default=text("''"),
                              comment='用户平台运营商id(组织机构代码)')
    base_operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                              comment='基础运营商id(组织机构代码)')
    equipment_id = Column(VARCHAR(23), nullable=True, index=True, server_default=text("''"),
                          comment='设备编码(设备唯一编码，对同一运营商，保证唯一)')
    equipment_name = Column(VARCHAR(30), nullable=True, server_default=text("''"), comment='充电设备名称')
    manufacturer_id = Column(VARCHAR(9), nullable=True, index=True, server_default=text("''"),
                             comment='设备生产商组织机构代码')
    manufacturer_name = Column(VARCHAR(30), nullable=True, server_default=text("''"), comment='设备生产商名称')
    equipment_model = Column(VARCHAR(20), nullable=True, server_default=text("''"),
                             comment='设备型号(由设备生产商定义的设备型号)')
    production_date = Column(VARCHAR(10), nullable=True, server_default=text("''"), comment='设备生产日期(YYYY-MM-DD)')
    equipment_type = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                            comment='设备类型:1、直流设备;2、交流设备;3、交直流一体设备;4、无线设备;5、其他')
    equipment_lng = Column(DECIMAL(6, 6), nullable=True, server_default=text("'0.000000'"),
                           comment='站点经度(GCJ-02坐标系,保留小数点后6位)')
    equipment_lat = Column(DECIMAL(6, 6), nullable=True, server_default=text("'0.000000'"),
                           comment='站点纬度(GCJ-02坐标系,保留小数点后6位)')
    power = Column(DECIMAL(6, 1), nullable=True, server_default=text("'0.0'"),
                   comment='充电设备总功率(单位:kW,保留小数点后1位)')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindFeedback(db.Model, EntityBase):
    __tablename__ = 'omind_feedback'
    __table_args__ = {'comment': '用户反馈表'}

    id = Column(BIGINT(20), primary_key=True, comment='主键ID')
    user_id = Column(BIGINT(20), nullable=True, index=True, server_default=text("'0'"), comment='用户ID')
    connector_id = Column(VARCHAR(26), nullable=True, server_default=text("''"), comment='桩ID')
    feedback_type = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                           comment='反馈类型:1、充电站;2、充电桩;3、充电枪;50、其他')
    feedback_content = Column(VARCHAR(256), nullable=True, server_default=text("''"), comment='反馈内容')
    imgs = Column(TEXT, comment='图片')
    reply_content = Column(VARCHAR(256), nullable=True, server_default=text("''"), comment='回复内容')
    reply_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='是否回复:0、未回复;1、已回复')
    remark = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='备注')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindOperator(db.Model, EntityBase):
    __tablename__ = 'omind_operator'
    __table_args__ = {'comment': '基础设施运营商信息表'}

    id = Column(INTEGER(10), primary_key=True, comment='自增id')
    operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                         comment='运营商id(组织机构代码)')
    operator_name = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='运营商名称')
    operator_tel1 = Column(VARCHAR(32), nullable=True, server_default=text("''"), comment='运营商客服电话1')
    operator_tel2 = Column(VARCHAR(32), nullable=True, server_default=text("''"), comment='运营商客服电话2')
    operator_reg_address = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='运营商注册地址')
    operator_note = Column(VARCHAR(255), nullable=True, server_default=text("''"), comment='备注信息')
    user_operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                              comment='客户归属运营商id(组织机构代码)')
    operator_secret = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='运营商密钥')
    data_secret = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='消息密钥')
    data_secret_iv = Column(CHAR(16), nullable=True, server_default=text("''"), comment='消息密钥初始化向量')
    sig_secret = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='签名密钥')
    base_operator_secret = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='基础运营商密钥')
    base_data_secret = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='基础消息密钥')
    base_data_secret_iv = Column(CHAR(16), nullable=True, server_default=text("''"), comment='基础消息密钥初始化向量')
    base_sig_secret = Column(VARCHAR(64), nullable=True, server_default=text("''"), comment='基础签名密钥')
    api_url = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='接口地址')
    plat_type = Column(TINYINT(3), nullable=True, server_default=text("'1'"), comment='平台类型:1、OMIND')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindPrice(db.Model, EntityBase):
    __tablename__ = 'omind_price'
    __table_args__ = {'comment': '充电价格表'}

    id = Column(BIGINT(20), primary_key=True, comment='自增id')
    station_id = Column(VARCHAR(20), nullable=True, server_default=text("''"), comment='充电站ID')
    price_code = Column(BIGINT(20), nullable=True, server_default=text("'0'"), comment='价格模版ID，0为默认价格')
    start_time = Column(DateTime, nullable=True, comment='时段起始时间点 6位 HHmmss')
    price_type = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='价格类型:0、尖;1、峰;2、平;3、谷;')
    elec_price = Column(DECIMAL(10, 4), nullable=True, server_default=text("'0.0000'"), comment='电价:XXXX.XXXX')
    service_price = Column(DECIMAL(10, 4), nullable=True, server_default=text("'0.0000'"),
                           comment='服务费单价:XXXX.XXXX')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    remark = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='备注')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindStation(db.Model, EntityBase):
    __tablename__ = 'omind_station'
    __table_args__ = {'comment': '充电站信息表'}

    id = Column(INTEGER(10), primary_key=True, comment='自增id')
    station_id = Column(VARCHAR(20), nullable=True, index=True, server_default=text("''"),
                        comment='充电站id(运营商自定义的唯一编码)')
    operator_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                         comment='运营商id(组织机构代码)')
    user_operator_id = Column(VARCHAR(10), nullable=True, server_default=text("''"),
                              comment='用户平台运营商id(组织机构代码)')
    base_operator_id = Column(VARCHAR(10), nullable=True, server_default=text("''"),
                              comment='基础运营商id(组织机构代码)')
    equipment_owner_id = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"),
                                comment='设备所属商id(组织机构代码)')
    station_name = Column(VARCHAR(50), nullable=True, server_default=text("''"), comment='充电站名称')
    country_code = Column(VARCHAR(2), nullable=True, server_default=text("''"), comment='充电站国家代码,比如CN')
    area_code = Column(VARCHAR(20), nullable=True, index=True, server_default=text("''"), comment='充电站省市辖区编码')
    address = Column(VARCHAR(50), nullable=True, server_default=text("''"), comment='详细地址')
    station_tel = Column(VARCHAR(30), nullable=True, server_default=text("''"),
                         comment='站点电话(能够联系场站工作人员进行协助的联系电话)')
    service_tel = Column(VARCHAR(30), nullable=True, server_default=text("''"),
                         comment='服务电话(平台服务电话，例如400的电话)')
    station_type = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                          comment='站点类型:1、公共;50、个人;100、公交(专用);101、环卫(专用);102、物流(专用);103、出租车(专用);255、其他')
    station_status = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                            comment='站点状态:0、未知;1、建设中;5、关闭下线;6、维护中;50、正常使用')
    park_nums = Column(INTEGER(10), nullable=True, server_default=text("'0'"),
                       comment='车位数量(可停放进行充电的车位总数，默认：0 未知)')
    station_lng = Column(DECIMAL(10, 6), nullable=True, server_default=text("'0.000000'"),
                         comment='站点经度(GCJ-02坐标系,保留小数点后6位)')
    station_lat = Column(DECIMAL(10, 6), nullable=True, server_default=text("'0.000000'"),
                         comment='站点纬度(GCJ-02坐标系,保留小数点后6位)')
    site_guide = Column(VARCHAR(100), nullable=True, server_default=text("''"),
                        comment='站点引导:描述性文字，用于引导车主找到充电车位')
    construction = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                          comment='建设场所类型:1、居民区;2、公共机构;3、企事业单位;4、写字楼;5、工业园区;6、交通枢纽;7、大型文体设施;8、城市绿地;9、大型建筑配建停车场;10、路边停车位;11、城际高速服务区;255、其他')
    pictures = Column(TEXT, comment='站点照片(充电设备照片、充电车位照片、停车场入口照片)JSON串')
    match_cars = Column(VARCHAR(100), nullable=True, server_default=text("''"),
                        comment='使用车型描述(描述该站点接受的车大小以及类型，如大巴、物流车、私家乘用车、出租车等)')
    park_info = Column(VARCHAR(100), nullable=True, server_default=text("''"),
                       comment='车位楼层及数量描述(车位楼层以及数量信息)')
    busine_hours = Column(VARCHAR(100), nullable=True, server_default=text("''"), comment='营业时间描述')
    electricity_fee = Column(VARCHAR(256), nullable=True, server_default=text("''"), comment='充电电费描述')
    service_fee = Column(VARCHAR(256), nullable=True, server_default=text("''"), comment='服务费描述')
    park_fee = Column(VARCHAR(100), nullable=True, server_default=text("''"), comment='停车费描述')
    payment = Column(VARCHAR(20), nullable=True, server_default=text("''"),
                     comment='支付方式::刷卡、线上、现金。其中电子钱包类卡为刷卡，身份鉴权卡、微信/支付宝、APP为线上')
    support_order = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                           comment='是否支持预约(充电设备是否需要提前预约后才能使用。0为不支持预约;1为支持预约。不填默认为0)')
    plat_type = Column(TINYINT(3), nullable=True, comment='平台类型')
    remark = Column(VARCHAR(100), nullable=True, server_default=text("''"), comment='备注信息')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindStationImage(db.Model, EntityBase):
    __tablename__ = 'omind_station_images'
    __table_args__ = {'comment': '充电站图片表'}

    id = Column(INTEGER(10), primary_key=True, comment='自增id')
    station_id = Column(VARCHAR(20), nullable=True, server_default=text("''"),
                        comment='充电站id(运营商自定义的唯一编码)')
    image_type = Column(TINYINT(1), nullable=True, server_default=text("'1'"),
                        comment='图片类型:1、充电站照片;2、充电桩照片;3、充电车位照片;4、停车场入口照片')
    image_url = Column(VARCHAR(255), nullable=True, server_default=text("''"), comment='站点图片')
    image_name = Column(VARCHAR(32), nullable=True, server_default=text("''"), comment='图片名称')
    show_seq = Column(INTEGER(10), server_default=text("'0'"), comment='显示顺序')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindUser(db.Model, EntityBase):
    __tablename__ = 'omind_user'
    __table_args__ = {'comment': '用户表'}

    uid = Column(BIGINT(20), primary_key=True, comment='自增id')
    phone_code = Column(VARCHAR(10), nullable=True, server_default=text("+86"), comment='国家区号码')
    mobile = Column(VARCHAR(11), nullable=False, index=True, server_default=text("''"), comment='用户手机号')
    nick_name = Column(VARCHAR(80), nullable=True, server_default=text("'koko'"), comment='用户昵称')
    wechat_name = Column(VARCHAR(255), nullable=True, server_default=text("'kokoko'"), comment='微信昵称')
    password = Column(VARCHAR(20), nullable=False, server_default=text("123456"),
                      comment='当且仅当该移动应用已获得该用户的 userinfo 授权时，才会出现该字段')
    openid_wx = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='小程序openID')
    unionid_ali = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='ali统一id')
    openid_ali = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='支付宝用户唯一标识')
    credit_pay_wx = Column(INTEGER(11), nullable=True, server_default=text("'0'"), comment='微信信用分授权-后支付')
    credit_pay_ali = Column(INTEGER(11), nullable=True, server_default=text("'0'"), comment='阿里信用分授权-后支付')
    sex = Column(TINYINT(1), nullable=True, server_default=text("'0'"), comment='0、未知;1、男;2、女')
    country = Column(VARCHAR(100), nullable=True, server_default=text("'中国'"), comment='国家')
    province = Column(VARCHAR(64), nullable=True, server_default=text("'广东'"), comment='省')
    city = Column(VARCHAR(64), nullable=True, server_default=text("'珠海'"), comment='城市')
    birthday = Column(BIGINT(20), nullable=True, server_default=text("'0'"), comment='生日')
    avatar = Column(VARCHAR(255), nullable=True, server_default=text("''"), comment='头像地址')
    platform = Column(INTEGER(10), nullable=True, server_default=text("'0'"),
                      comment='注册来源的平台:关联平台id(0未知)')
    disable_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='是否禁用用户:0、启用;1、禁用')
    register_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='注册时间')
    last_visit_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='最近一次访问时间')
    last_visit_ip = Column(VARCHAR(32), nullable=True, server_default=text("''"), comment='最近一次访问ip')
    last_visit_area = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='最近一次访问ip对应区域')
    org_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                      comment='用户是否从属组织机构:0、不从属;1、从属')
    remark = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='备注')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')


class OmindUserCar(db.Model, EntityBase):
    __tablename__ = 'omind_user_car'
    __table_args__ = {'comment': '用户的车辆'}

    id = Column(BIGINT(20), primary_key=True, comment='车辆ID')
    user_id = Column(BIGINT(20), nullable=True, index=True, server_default=text("'0'"), comment='用户ID')
    plate_no = Column(VARCHAR(10), nullable=True, index=True, server_default=text("''"), comment='车牌号')
    car_vin = Column(VARCHAR(18), nullable=True, index=True, server_default=text("'7143k2934ns'"), comment='车辆vin码')
    engine_no = Column(VARCHAR(32), nullable=True, server_default=text("'yk184619333880'"), comment='发动机号码')
    vehicle_type = Column(VARCHAR(32), nullable=True, server_default=text("'轿车'"), comment='车辆类型')
    car_model = Column(VARCHAR(64), nullable=True, server_default=text("'hongqi'"), comment='品牌型号')
    owner = Column(VARCHAR(64), nullable=True, server_default=text("'dake'"), comment='车辆所有人')
    address = Column(VARCHAR(64), nullable=True, server_default=text("'广东省珠海市'"), comment='住址')
    use_character = Column(VARCHAR(8), nullable=True, server_default=text("'非运营'"), comment='使用性质:运营、非运营')
    register_date = Column(Date, comment='注册日期(格式"yyyy-MM-dd")')
    issue_date = Column(Date, comment='发证日期(格式"yyyy-MM-dd")')
    license_imgs = Column(TEXT, comment='行驶证图片json串')
    check_state = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                         comment='审核状态:0、待审核;1、审核通过;2、审核不通过;3、不需审核')
    auth_state = Column(TINYINT(3), nullable=True, server_default=text("'0'"),
                        comment='认证状态:0、不认证;1、待认证;2、认证通过;3、认证不通过')
    remark = Column(VARCHAR(128), nullable=True, server_default=text("''"), comment='备注')
    del_flag = Column(TINYINT(3), nullable=True, server_default=text("'0'"), comment='数据状态:0、正常;1、删除')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    tenant_id = Column(VARCHAR(20), server_default=text("'000000'"), comment='租户编号')
