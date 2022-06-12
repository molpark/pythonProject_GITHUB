###**重要
'''
只用table_data = engine.execute(sql_cmd) 的好处是,这个返回值是一个对象,后续的代码不管这个结果有没有值都可以进行下去
----
rows = table_data.fetchall() 这种能直接print出结果
,并且用 if not rows 能判断select语句是否有结果.如果没有结果代表为空,后续代码会有报错的可能
这种适合必须要判断是否含有数据的情况
'''
def load_file():
    if os.path.exists(file_name):
        os.remove(file_name)
    sql_cmd = '''
			select 
				 *
			from db_ads.ads_starbuck_novacustomizedv1_sftp
			where dt='2022-03-19'  
			--dt = cast(current_date as varchar)
				'''
    #fatchall的方法
    try:
        table_data = engine.execute(sql_cmd)
        rows = table_data.fetchall()
        #print(rows)
        if not rows:
            print('无数据')
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write('')
        else:
            dafule_data = '下单日期;宝尊订单号-OMS;App订单号-OMS;SKU;数量;杯子类型;客制化信息;字号;备注'
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write(dafule_data + '\n')
            for result in rows:
                result_date = str(result[0]) + ";" + str(result[1]) + ";" + str(result[2]) + ";" + str(result[3]) \
                              + ";" + str(result[4]) + ";" + str(result[5]) + ";" + str(result[6]) \
                              + ";" + str(result[7]) + ";" + str(result[8]) + ";" + str(result[9]) + ";"
                with open(file_name, 'a', encoding="utf-8") as f:
                    f.write(result_date + '\n')
    except Exception as e:
        print('无表或sql报错')
    #exec后对象的处理方法
    ##就是可以参考以下的方法




#jdsz_compete_core_index_local.py   单层字典解法
for result in table_data:
    # 公共字段解析
    data_line = str(result[0]) + "\x1f" + str(result[1]) + "\x1f" + str(result[2]) + "\x1f" + str(result[3]) + "\x1f" \
                + str(result[4]) + "\x1f" + str(result[5]) + "\x1f" + str(result[8]) + "\x1f"

    remark_id = "\x1f" + str(result[9]) + "\x1f" + str(result[7])

    data = json.loads(result[6])
    # print(data)
    main_data = []
    for i in row:
        main_data.append(str(data.get(i, '')))
    # print(main_data)
    list_data = '\x1f'.join(main_data)
    result_date = data_line + list_data + remark_id
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(result_date + '\n')



#双层解法 外面列表套着里面字典
#jdsz_pre_goods_detail_local.py
#碰到有结构不一致tag不一致.但是dws 不分表给的字段也全.那也可以用这种
    for result in table_data:
        # 公共字段解析
        # print(result)
        data_line = str(result[0]) + "\x1f" + str(result[1]) + "\x1f" + str(result[2]) + "\x1f" + str(
            result[3]) + "\x1f" \
                    + str(result[4]) + "\x1f" + str(result[5]) + "\x1f" + str(result[8]) + "\x1f"

        remark_id = "\x1f" + str(result[9]) + "\x1f" + str(result[7])
        data = json.loads(result[6])
        #print(data)
        for it in data:
            main_data = []
            for i in row:
                main_data.append(str(it.get(i, '')))
            # print(main_data)
            list_data = '\x1f'.join(main_data)
            # print(list_data)
            result_date = data_line + list_data + remark_id
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write(result_date + '\n')

#####ppzh_key_comparison_local.py
####此钟为字典里面多层字典,并需要将第一层的key 取出,第二层循环取value
    for result in table_data:
        # 公共字段解析
        data_line = str(result[0]) + "\x1f" + str(result[1]) + "\x1f" + str(result[2]) + "\x1f" + str(
            result[3]) + "\x1f" \
                    + str(result[4]) + "\x1f" + str(result[5]) + "\x1f" + str(result[8]) + "\x1f"
        remark_id = "\x1f" + str(result[9]) + "\x1f" + str(result[7])

        data = json.loads(result[6])
        main_data = []
        #print(data)
        for i in row_top:
            main_data.append(str(i))
            for it in row:
                main_data.append(str(data.get(i,'').get(it,'')).replace(',',''))
            list_data = '\x1f'.join(main_data)
            result_date = data_line + list_data + remark_id
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write(result_date + '\n')
            main_data=[]


#ctmp_shop_customerservice_workload_local.py 列表中套着两个
#ctmp_shop_customerservice_workload where modulename = '赤兔名品_客服绩效_专项分析_工作量分析'

for result in table_data:
    # 公共字段解析
    # print(result)
    data_line = str(result[0]) + "\x1f" + str(result[1]) + "\x1f" + str(result[2]) + "\x1f" + str(
        result[3]) + "\x1f" \
                + str(result[4]) + "\x1f" + str(result[5]) + "\x1f" + str(result[8]) + "\x1f"

    remark_id = "\x1f" + str(result[9]) + "\x1f" + str(result[7])
    data = json.loads(result[6])
    # print(data)
    main_data = []
    for i in row_top:
        data_li = data.get(i, '')
        # print(data_li)
        if i == 'value_list':
            for it in data_li:
                # print(it)
                for ia in row:
                    main_data.append(str(it.get(ia, '')))
                alist = i + '\x1f'
                list_data = '\x1f'.join(main_data)
                list_data = alist + list_data
                result_data = data_line + list_data + remark_id
                with open(file_name, 'a', encoding="utf-8") as f:
                    f.write(result_data + '\n')
                # 清空列表供循环使用
                # print(main_data)
                main_data = []
        else:
            for ii in row:
                main_data.append(str(data_li.get(ii, '')))
            alist = i + '\x1f'
            list_data = '\x1f'.join(main_data)
            list_data = alist + list_data
            result_data = data_line + list_data + remark_id
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write(result_data + '\n')
            # 清空列表供循环使用
            # print(main_data)
            main_data = []

#sbb3_rpa_mofang 少见 该逻辑无法复现,src 底层已更改
#ylmf_statement_collect_data where modulename = '引力魔方_报表_汇总数据'
for result in table_data:
    # print(result)
    # 公共字段解析

    data_line = str(result[0]) + "\t" + str(result[1]) + "\t" + str(result[2]) + "\t" + str(result[3]) + "\t" \
                + str(result[4]) + "\t" + str(result[5]) + "\t"

    remark_id = "\t" + str(result[9]) + "\t" + str(result[7])
    data = json.loads(result[6])
    # print(data)
    main_data = []
    # 拆行一条变多条
    for level1 in row1:
        for level2 in row2:
            for level3 in row3:
                level3_data = data.get(level1).get(level2).get(level3)
                level3_data_keys = dict(level3_data).keys()
                for level4 in level3_data_keys:
                    for level5 in row5:
                        alist = level1 + '\t' + level2 + '\t' + level3 + '\t' + level4 + '\t'
                        main_data.append(str(data.get(level1).get(level2).get(level3).get(level4).get(level5)))
                    list_data = '\t'.join(main_data)
                    list_data = alist + list_data.replace('None', '').replace(',', '')
                    result_data = data_line + list_data + remark_id
                    with open(file_name, 'a', encoding="utf-8") as f:
                        f.write(result_data + '\n')
                    # 清空列表供循环使用
                    main_data = []