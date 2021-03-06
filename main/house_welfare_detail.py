from flask import Blueprint
from flask import Flask, request, jsonify
import pandas as pd
import json

blue_house_welfare_detail = Blueprint("house_welfare_detail", __name__, url_prefix='/house_welfare_detail')

@blue_house_welfare_detail.route("/")
def house_welfare__detail_home():
    return "house_welfare_detail"
# ----- moving_in_qual_ranking --------------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/moving_in_qual_ranking", methods=['GET', 'POST'])
def show_moving_in_qual_ranking():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '영구임대주택':
        moving_data = pd.read_csv("./data/house_welfare/permanent_lease/Selection_Ranking.csv")
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격 및 선정순위" + "\n\n"
                            + '♤ ' + str(moving_data.iloc[0]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[0]['qualification']) + '\n\n'
                            + str(moving_data.iloc[0]['note'])+ '\n\n\t\t'
                            + '♤ ' + str(moving_data.iloc[1]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[1]['qualification']) + '\n\n'
                            + str(moving_data.iloc[1]['note'])+ '\n\n\t\t'
                            + '♤ ' + str(moving_data.iloc[2]['rank']) + ' :' + '\n\n\t\t' + str(moving_data.iloc[2]['qualification']) + '\n\n'     }})
        res['template']['outputs'].append({"basicCard": {"title": "영구임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                                                         "thumbnail": {"imageUrl": ""},
                                                         "buttons": [{
                                                                      "label": "링크연결",
                                                                      "action": "webLink",
                                                                      "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH103"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                                                     "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                                                     "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block",
                                                     "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                                                     "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
        
# -------------------------------------------------------------------------------------------------------------------------------------------

# ------ apply_step -------------------------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/apply_step", methods=['GET', 'POST'])
def show_apply_step():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '통합공공임대주택':
        step_data = pd.read_csv("./data/house_welfare/total_public/total_public_app_process.csv")
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 통합공공임대주택 신청절차" + "\n\n"
                            + "1. " + str(step_data.iloc[0]['절 차']) + ' :' + '\n\t\t' + str(step_data.iloc[0]['describe']) + '\n\n'
                            + "2. " + str(step_data.iloc[1]['절 차']) + ' :' + '\n\t\t' + str(step_data.iloc[1]['describe']) + '\n\n'
                            + "3. " + str(step_data.iloc[2]['절 차']) + ' :' + '\n\t\t' + str(step_data.iloc[2]['describe']) + '\n\n'
                            + "4. " + str(step_data.iloc[3]['절 차']) + ' :' + '\n\t\t' + str(step_data.iloc[3]['describe']) + '\n\n'
                            + "5. " + str(step_data.iloc[4]['절 차']) + ' :' + '\n\t\t' + str(step_data.iloc[4]['describe'])}})
        res['template']['outputs'].append({"basicCard": {"title": "통합공공임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                                                         "thumbnail": {"imageUrl": ""},
                                                         "buttons": [{
                                                                      "label": "링크연결",
                                                                      "action": "webLink",
                                                                      "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH112"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "628b1ed4055a574d7df534ff", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법","action": "block",
                "blockId": "628b2f71055a574d7df5383d", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
        
    elif welfare_type == '영구임대주택':
        step_data = pd.read_csv("./data/house_welfare/permanent_lease/apply_step.csv")
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 영구임대주택 신청절차" + "\n\n"
                            + "1. " + str(step_data.iloc[0]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[0]['describe']) + '\n\n'
                            + "2. " + str(step_data.iloc[1]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[1]['describe']) + '\n\n'
                            + "3. " + str(step_data.iloc[2]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[2]['describe']) + '\n\n'
                            + "4. " + str(step_data.iloc[3]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[3]['describe']) + '\n\n'
                            + "5. " + str(step_data.iloc[4]['step']) + ' :' + '\n\t\t' + str(step_data.iloc[4]['describe'])}})
        res['template']['outputs'].append({"basicCard": {"title": "영구임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                                                         "thumbnail": {"imageUrl": ""},
                                                         "buttons": [{
                                                                      "label": "링크연결",
                                                                      "action": "webLink",
                                                                      "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH103"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                                                     "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주·선정순위", "action": "block",
                                                     "blockId": "628b412f299dbd02ee7a6666", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block",
                                                     "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                                                     "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
        
# -------------------------------------------------------------------------------------------------------------------------------------

# ----- general_supply_selection -------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/general_supply_selection", methods=['GET', 'POST'])
def show_general_supply_selection():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '통합공공임대주택':
        general_data = pd.read_csv("./data/house_welfare/total_public/total_public_general_supply_select.csv")
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 일반공급 입주자격 및 입주자 선정방법" + "\n\n"
                            + '♤ ' + str(general_data.iloc[0]['class']) + ' : 추첨' + '\n\n\t\t' + str(general_data.iloc[0]['qualification']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[1]['class']) + ' : 추첨' + '\n\n\t\t' + str(general_data.iloc[1]['qualification']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[2]['class']) + ' : 추첨' + '\n\n\t\t' + str(general_data.iloc[2]['qualification']) + '\n\n\n'
                            + '♤ ' + str(general_data.iloc[3]['class']) + ' : 추첨' + '\n\n\t\t' + str(general_data.iloc[3]['qualification'])}})
        res['template']['outputs'].append({"basicCard": {"title": "통합공공임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                                                         "thumbnail": {"imageUrl": ""},
                                                         "buttons": [{
                                                                      "label": "링크연결",
                                                                      "action": "webLink",
                                                                      "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH112"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                "blockId": "628b1ed4055a574d7df534ff", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
        
# ----------------------------------------------------------------------------------------------------------------------------------

# ----- income_asset_how -----------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/income_asset_how", methods=['GET', 'POST'])
def show_income_asset_how():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '통합공공임대주택':
        income_data = pd.read_csv("./data/house_welfare/total_public/total_public_members_median_income.csv")
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 통합공공임대주택 소득 · 자산 산정방법" + "\n\n"
                            + '♤ ' + str(income_data.iloc[0]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[0]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[1]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[1]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[2]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[2]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[3]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[3]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[4]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[4]['how']) + '\n\n\n'
                            + '♤ ' + str(income_data.iloc[5]['class']) + ' :' + '\n\n\t\t' + str(income_data.iloc[5]['how'])}})
        res['template']['outputs'].append({"basicCard": {"title": "통합공공임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                          "thumbnail": {"imageUrl": ""},
                          "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH112"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block",
                "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법", "action": "block",
                "blockId": "628b2f71055a574d7df5383d", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------

# ----- moving_in_qual -----------------------------------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/moving_in_qual", methods=['GET', 'POST'])
def show_moving_in_qual():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": []
        }}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '통합공공임대주택':
        qual = pd.read_csv("./data/house_welfare/total_public/total_public_Tenant_Qual.csv")
    
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격" + "\n\n" 
                            + "입주자모집공고일 현재 무주택세대구성원으로서 아래의 소득 및 자산보유 기준에 해당하는 공급신청자격자" + "\n\n"
                            + '- ' + "입주자모집공고일 현재 무주택세대구성원으로서 아래의 소득 및 자산보유기준을 충족하는 자"}})
        res['template']['outputs'].append({"simpleText": {"text": "■ 무주택세대구성원" + "\n\n" 
                            + '♤ ' + str(qual.iloc[1]['세대 구성원']) + ' :' + '\n\n\t\t' + str(qual.iloc[1]['설명']) + '\n\n\n'
                            + '♤ ' + str(qual.iloc[2]['세대 구성원']) + ' :'  + '\n\n\t\t' + str(qual.iloc[2]['설명']) + '\n\n\n'
                            + '♤ ' + str(qual.iloc[3]['세대 구성원']) + ' :'  + '\n\n\t\t' + str(qual.iloc[3]['설명'])}})
        res['template']['outputs'].append({"basicCard": {"title": "통합공공임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                        "label": "링크연결",
                                        "action": "webLink",
                                        "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH112"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block",
                                                     "blockId": "628b1ed4055a574d7df534ff", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법", "action": "block",
                                                     "blockId": "628b2f71055a574d7df5383d", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                                                     "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block",
                                                     "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                                                     "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
                                          
    elif welfare_type == '영구임대주택':
        qual = pd.read_csv("./data/house_welfare/permanent_lease/homeless_household_note.csv")
        
        res['template']['outputs'].append({"simpleText": {"text": "■ 입주자격" + "\n\n" 
                            + "입주자모집공고일 현재 무주택세대구성원으로서 아래에 해당하는 공급신청자격자" + "\n\n"
                            + '- ' + "입주자모집공고일 현재 무주택세대구성원으로서 아래의 소득 및 자산보유기준을 충족하는 자"}})
        res['template']['outputs'].append({"simpleText": {"text": "■ 무주택세대구성원" + "\n\n" 
                            + '♤ ' + str(qual.iloc[1]['세대 구성원']) + ' :' + '\n\n\t\t' + str(qual.iloc[1]['설명']) + '\n\n\n'
                            + '♤ ' + str(qual.iloc[2]['세대 구성원']) + ' :'  + '\n\n\t\t' + str(qual.iloc[2]['설명']) + '\n\n\n'
                            + '♤ ' + str(qual.iloc[3]['세대 구성원']) + ' :'  + '\n\n\t\t' + str(qual.iloc[3]['설명'])}})
        res['template']['outputs'].append({"basicCard": {"title": "영구임대주택 링크", "description": "자세한 사항은 링크 연결로...",
                            "thumbnail": {"imageUrl": ""},
                            "buttons": [{
                                          "label": "링크연결",
                                          "action": "webLink",
                                          "webLinkUrl": "https://www.myhome.go.kr/hws/portal/cont/selectContRentalView.do#guide=RH103"}]}})
        
        tmp_quickReplies_set['quickReplies'].append({"label": "입주·선정순위", "action": "block",
                                                     "blockId": "628b412f299dbd02ee7a6666", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block",
                                                     "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block",
                                                     "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block",
                                                     "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
#----------------------------------------------------------------------------------------------------------------------

# ----- welfare selection ----------------------------------------------------------------------------------------------
@blue_house_welfare_detail.route("/selection", methods=['GET', 'POST'])
def blue_house_welfare_detail_selection():
    body = request.get_json()
    
    welfare_type = body['action']['clientExtra']['welfare_type']
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": welfare_type + '\n\n' + "원하시는 상세정보를 선택해주세요."
                }
            }
        ]
    }
}
    
    tmp_quickReplies_set = {"quickReplies": []}
    
    if welfare_type == '통합공공임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "소득·자산 산정방법", "action": "block", 
                                                     "blockId": "628b1ed4055a574d7df534ff", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "일반 입주·선정방법", "action": "block", 
                                                     "blockId": "628b2f71055a574d7df5383d", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "62873757ee5923754330c0b2"})
        
        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
    
    elif welfare_type == '영구임대주택':
        tmp_quickReplies_set['quickReplies'].append({"label": "입주자격", "action": "block", 
                                                     "blockId": "628b0241bacfd86a3725d282", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "입주·선정순위", "action": "block", 
                                                     "blockId": "628b412f299dbd02ee7a6666", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "신청절차", "action": "block", 
                                                     "blockId": "628b38eb055a574d7df53a46", "extra": {"welfare_type" : welfare_type}})
        tmp_quickReplies_set['quickReplies'].append({"label": "주택복지", "action": "block", 
                                                     "blockId": "62859d5e33d26f492e9e84ed"})
        tmp_quickReplies_set['quickReplies'].append({"label": "메인메뉴", "action": "block", 
                                                     "blockId": "62873757ee5923754330c0b2"})

        res['template'].update(tmp_quickReplies_set)
        
        return jsonify(res)
    
    else :
        return "error!"
    # ---------------------------------------------------------------------------------------------------------------------------------------