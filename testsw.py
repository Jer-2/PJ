from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3

class MySwitch(app_manager.RyuApp):
    OFP_VERSIONS =[ofproto_v1_3.OFP_VERSION]

    def __init__(self, *_args, **_kwargs):
        super(MySwitch).__init__(*_args, **_kwargs)
        
@set_ev_cls(ofp_event.EventOFPSSwitchFeatures,CONFIG_DISPATCHER)
def switch_features_handler(self,ev):
    self.logger.info("-----------add default flow -----------")      #宣告self logger.info為紀錄訊息
    dp=ev.msg.datapath                           #儲存openflow交換器的ryu.controller.Datapath的實體
    ofp=dp.ofprotos                              #解析openflow訊息函式庫
    parser=dp.ofporto_parser
    match=parser.OFPMatch()                         #新增一個Match，封包達成條件就能match
    actions = [parser.OFPActionOutput(ofp.OFPP_CONTROLLER,ofp.OFPCML_NO_BUFFER)]        #宣告actions為parser用OFPActionOutput class  #原為OFPP_CONTROLLER(轉送到Controller的Packet-in訊息)，可嘗試改為OFPP_ALL（轉送到除了來源以外的所有port）
                                                                                        #OFPCML_NO_BUFFER則為無緩衝對所有指定的點發送訊息
    inst =[parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS,actions)]
                                                                                            #Instruction是指當封包滿足Match後執行的動作，把action以OFPnstructionActions包裝起來
    mod=parser.OFPFlowMod(datapath=dp,priortiy=0,match=match,instrutions=inst)
                                                                            #FlowMod Function可以讓我們對Switch寫入由我們定義的Flow Entry
                         #更改flowtable區
    dp.send_msg(mod)
                                                                        #將定義好的FlowEntry送給Switch 
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg=ev.msg
        dp=msg.datapath
        parser= dp.ofproto_parser
                                                         #繼承上面的宣告
        self.logger.info("-----------add flood flow-----------")
        match=parser.OFPMatch()
                                                     #新增一個Match，封包達成條件就能match
        actions=[parser.OFPActionOutput(ofp.OFPP_FLOOD)]
        inst=[parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS,actions)]
        mod=parser.OFPFlowMod(datapath=dp,priority=2048,match=match,instructions=inst)
        dp.send_msg(mod)

