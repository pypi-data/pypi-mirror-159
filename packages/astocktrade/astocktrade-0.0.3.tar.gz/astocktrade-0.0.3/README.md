import astocktradever1.getdata as ag
 ag.get_tradeday(...)
 ag.getdatafrombaostock(...)

  getdata：
    get_tradeday:
      def get_tradeday(start_str,end_str):
      sample: list = get_tradeday('2022-07-01','2022-07-11') #获取20220701至20220711之间所有股票交易日并存入 list 中

    getdatafrombaostock:
      def getdatafrombaostock(stnamelist,stday,edday,fq,otpath,add_or_rpl): 
      sample: getdatafrombaostock('D\\namelist.csv','2022-07-01','2022-07-11','5','D\\store\\,'new') #获取 D\\namelist.csv 中所有股票20220701至20220711间5分钟k线信息,存入 D\\store\\，为新添
                   getdatafrombaostock('D\\namelist.csv','2022-07-01','2022-07-11','5','D\\store\\,'add') #获取 D\\namelist.csv 中所有股票20220701至20220711间5分钟k线信息,存入 D\\store\\，为追加
                   注： fq位置为k线频率 d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写
                           namelist.csv文件包含股票名称的列名应为 ts_code 股票名称形如 sh.xxxxxx 或 sz.xxxxxx 小写字母
                           保存文件名称为对应股票名称 如：sh.600000 保存为 sh.600000.csv
    
    get_alldatebar:
       def get_alldatebar(st,ed,otpath):
       sample:get_alldatebar('2022-07-01','2022-07-11','D\\store\\) #获取20220701至20220711之间每一日大盘全部信息，分日存入D\\store\\
    
    get_tick:
       def get_tick(stock_code) :
       sample: list = get_tick('600000') #获取sh.600000股票实时信息，存入list
       注：list[i]信息包括但不限于 #{i=
                                              # 0 名称
                                              # 1 今开
                                              # 2 昨收
                                              # 3 此时价格
                                              # 4 最高
                                              # 5 最低
                                              # 30 年月天
                                              # 31 时分秒
                                              # ......
                                              # }


​       





