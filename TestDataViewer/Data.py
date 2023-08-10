import pandas as pd

class Data_sorting:

    def __init__(self, product, device, lpcode):
        product_filter = product
        device_filter = device
        lpcode_filter = lpcode
        raw_data = pd.read_excel("./2021_메리츠TM_데이터라벨링.xlsx", sheet_name='raw', skiprows=1)

        self.set_data = raw_data.loc[(raw_data['보종'] == product_filter)
                                     & (raw_data['기기'] == device_filter) & (raw_data['LP유형'] == lpcode_filter)]

    # 폰트
    def font_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['폰트'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['폰트'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['폰트'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['폰트'] == i)])
                          * 100, 1)) + "%")
        font_result = pd.DataFrame({'폰트': slot, 'Win': win_count, '승률': win_rate})
        return font_result.sort_values(by=["Win"], ascending=False)

    # 폰트 컬러
    def font_color_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['폰트컬러'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['폰트컬러'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['폰트컬러'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['폰트컬러'] == i)])
                          * 100, 1)) + "%")
        font_color_result = pd.DataFrame({'폰트컬러': slot, 'Win': win_count, '승률': win_rate})
        return font_color_result.sort_values(by=["Win"], ascending=False)
    # 배경 컬러
    def background_color_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['배경컬러'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['배경컬러'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['배경컬러'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['배경컬러'] == i)])
                          * 100, 1)) + "%")
        background_color_result = pd.DataFrame({'배경컬러': slot, 'Win': win_count, '승률': win_rate})
        return background_color_result.sort_values(by=["Win"], ascending=False)
    #포인트 컬러
    def point_color_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['포인트컬러'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['포인트컬러'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['포인트컬러'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['포인트컬러'] == i)])
                          * 100, 1)) + "%")
        point_color_result = pd.DataFrame({'포인트컬러': slot, 'Win': win_count, '승률': win_rate})
        return point_color_result.sort_values(by=["Win"], ascending=False)
    # 이미지
    def image_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['이미지'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['이미지'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['이미지'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['이미지'] == i)])
                    * 100, 1)) + "%")
        image_result = pd.DataFrame({'이미지': slot, 'Win': win_count, '승률': win_rate})
        return image_result.sort_values(by=["Win"], ascending=False)
    # 레이아웃
    def layout_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['레이아웃'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['레이아웃'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['레이아웃'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['레이아웃'] == i)])
                    * 100, 1)) + "%")
        layout_result = pd.DataFrame({'레이아웃': slot, 'Win': win_count, '승률': win_rate})
        return layout_result.sort_values(by=["Win"], ascending=False)
    # 아이템
    def item_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['아이템'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['아이템'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['아이템'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['아이템'] == i)])
                    * 100, 1)) + "%")
        item_result = pd.DataFrame({'아이템': slot, 'Win': win_count, '승률': win_rate})
        return item_result.sort_values(by=["Win"], ascending=False)
    # 화법
    def expression_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['화법'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['화법'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(len(list.loc[(list['화법'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['화법'] == i)])
                    * 100, 1)) + "%")
        expression_result = pd.DataFrame({'화법': slot, 'Win': win_count, '승률': win_rate})
        return expression_result.sort_values(by=["Win"], ascending=False)
    # 담보
    def content_list(self):
        list = self.set_data
        slot = []
        win_count = []
        win_rate = []
        for i in list['담보'].unique():
            slot.append(i)
            win_count.append(len(list.loc[(list['담보'] == i) & (list['결과'] == 'WIN')]))
            win_rate.append(
                str(round(
                    len(list.loc[(list['담보'] == i) & (list['결과'] == 'WIN')]) / len(list.loc[(list['담보'] == i)])
                    * 100, 1)) + "%")
        content_result = pd.DataFrame({'담보': slot, 'Win': win_count, '승률': win_rate})
        return content_result.sort_values(by=["Win"], ascending=False)

    # LP코드 불러오기
    def lp_list(self):
        list = self.set_data.loc[(self.set_data['결과'] == 'WIN')]
        lp_result = pd.DataFrame({'LP 목록': list['코드값'].value_counts().index})
        return lp_result

    # LP 태그값 불러오기
    def lp_tag(self, code):
        list = self.set_data.loc[(self.set_data['코드값'] == code) & (self.set_data['결과'] == 'WIN')]
        tag_result = pd.DataFrame({'내용': list.T.index, '태그값': list.T.iloc[:, 0]})
        return tag_result

"""
    # 이전 계산 방식, 현재 미사용
    def content_list(self):
        list = self.set_data.loc[(self.set_data['결과'] == 'WIN')]
        content_result = pd.DataFrame({'담보': list['담보'].value_counts().index, 'Win 횟수': list['담보'].value_counts().values})
        return content_result
"""